# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"),
                 ("stock_moved", "Stock Moved"),
                 ("cancel", "Cancel")]
TRANSACT_TYPE = [("in", "IN"), ("out", "OUT")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class MaterialTransact(models.Model):
    _name = "material.transact"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    order_id = fields.Many2one(comodel_name="arc.order", string="Order")
    person_id = fields.Many2one(comodel_name="arc.person", string="Person")
    transact_by = fields.Many2one(comodel_name="arc.person", string="Transact By")
    transact_on = fields.Date(string="Transact On")
    transact_type = fields.Selection(selection=TRANSACT_TYPE, string="Transaction Type", required=True)
    transact_detail = fields.One2many(comodel_name="transact.detail", inverse_name="material_id")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    writter = fields.Text(string="Writter", track_visibility="always")

    @api.multi
    def trigger_cancel(self):
        transact_by = self.env.user.person_id.id
        writter = "Material In cancel by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "cancel",
                    "writter": writter,
                    "transact_by": transact_by,
                    "transact_on": CURRENT_DATE})

    def generate_back_order(self):
        recs = self.transact_detail
        transact_detail = []
        for rec in recs:
            total_quantity = rec.previous_quantity + rec.quantity
            if total_quantity < rec.order_quantity:
                transact_detail.append((0, 0, {"order_ref": rec.order_ref,
                                               "product_id": rec.product_id.id,
                                               "description": rec.description,
                                               "order_quantity": rec.order_quantity,
                                               "previous_quantity": total_quantity}))

        if transact_detail:
            material_transact = {"person_id": self.person_id.id,
                                 "order_id": self.order_id.id,
                                 "transact_type": self.transact_type,
                                 "detail": transact_detail}

            self.env["material.transact"].create(material_transact)

    def generate_move(self, recs):
        config = self.env["store.config"].search([("company_id", "=", self.env.user.company_id.id)])
        transact = config.get_material_transact(self.transact_type)

        for rec in recs:
            result = {"source_id": transact["source_id"],
                      "destination_id": transact["destination_id"],
                      "reference": rec.name,
                      "product_id": rec.product_id.id,
                      "description": rec.description,
                      "quantity": rec.quantity,
                      "progress": "moved"}

            self.env["arc.move"].create(result)

    @api.multi
    def trigger_stock_moved(self):
        transact_by = self.env.user.person_id.id
        recs = self.env["transact.detail"].search([("material_id", "=", self.id), ("quantity", ">", 0)])

        if not recs:
            raise exceptions.ValidationError("Error! No Products found")

        self.generate_move(recs)
        self.generate_back_order()

        writter = "Material In by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "stock_moved",
                    "writter": writter,
                    "transact_by": transact_by,
                    "transact_on": CURRENT_DATE})

    @api.multi
    def trigger_generate_invoice(self):
        recs = self.transact_detail
        invoice_detail = []
        for rec in recs:
            order_detail_id = self.env["order.detail"].search([("order_id", "=", self.order_id.id),
                                                               ("name", "=", rec.order_ref)])

            if not order_detail_id:
                raise exceptions.ValidationError("Error! Order Details Not Found")

            invoice_detail.append((0, 0, {"order_ref": rec.order_ref,
                                          "material_ref": rec.name,
                                          "product_id": order_detail_id.product_id.id,
                                          "description": order_detail_id.description,
                                          "unit_price": order_detail_id.unit_price,
                                          "discount": order_detail_id.discount,
                                          "tax_id": order_detail_id.tax_id.id,
                                          "pf": order_detail_id.pf,
                                          "quantity": rec.quantity,}))

        if invoice_detail:
            invoice = {"person_id": self.person_id.id,
                       "order_id": self.order_id.id,
                       "invoice_type": self.order_id.order_type,
                       "invoice_detail": invoice_detail,
                       "expected_delivery": self.order_id.expected_delivery,
                       "freight": self.order_id.freight,
                       "payment": self.order_id.payment,
                       "insurance": self.order_id.insurance,
                       "certificate": self.order_id.certificate,
                       "warranty": self.order_id.warranty}

            self.env["arc.invoice"].create(invoice)

    @api.model
    def create(self, vals):
        sequence = "{0}{1}".format(self._name, vals["transact_type"])
        vals["name"] = self.env["ir.sequence"].next_by_code(sequence)
        return super(MaterialTransact, self).create(vals)


class MaterialTransactDetail(models.Model):
    _name = "transact.detail"

    name = fields.Char(string="Name", readonly=True)
    order_ref = fields.Char(string="Reference", readonly=True)
    product_id = fields.Many2one(comodel_name="arc.product", string="Item", required=True)
    description = fields.Text(string="Description")
    uom_id = fields.Many2one(comodel_name="product.uom", string="UOM", related="product_id.uom_id")
    order_quantity = fields.Float(string="Order Quantity", default=0, required=True)
    previous_quantity = fields.Float(string="Previous Received Qty", default=0, required=True)
    quantity = fields.Float(string="Quantity", default=0, required=True)
    material_id = fields.Many2one(comodel_name="material.transact", string="Material In")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", related="material_id.progress")

    @api.constrains("order_quantity", "quantity", "previous_quantity")
    def check_transact_quantity(self):
        if (self.quantity + self.previous_quantity) > self.order_quantity:
            raise exceptions.ValidationError("Error! In quantity more than order")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(MaterialTransactDetail, self).create(vals)
