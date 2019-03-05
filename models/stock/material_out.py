# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"),
                 ("dispatched", "Dispatched"),
                 ("cancel", "Cancel")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class MaterialOut(models.Model):
    _name = "material.out"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", readonly=True)
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    person_id = fields.Many2one(comodel_name="arc.person", string="Person")
    # po_id = fields.Many2one(comodel_name="arc.person", string="Purchase Order")
    dpo_id = fields.Many2one(comodel_name="direct.purchase", string="Purchase Order")
    so_id = fields.Many2one(comodel_name="sale.order", string="Sale Order")
    out_detail = fields.One2many(comodel_name="material.out.detail", inverse_name="material_id")
    dispatched_by = fields.Many2one(comodel_name="arc.person", string="Dispatched By", readonly=True)
    writter = fields.Char(string="Writter", track_visibility="always")

    @api.multi
    def trigger_cancel(self):
        writter = "Material Out cancel by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "cancel", "writter": writter})

    def generate_back_order(self):
        recs = self.out_detail
        out_detail = []
        for rec in recs:
            out_quantity = rec.previous_out_quantity + rec.out_quantity
            if out_quantity < rec.order_quantity:
                out_detail.append((0, 0, {"reference": rec.name,
                                          "ref_id": rec.id,
                                          "product_id": rec.product_id.id,
                                          "description": rec.description,
                                          "order_quantity": rec.order_quantity,
                                          "previous_out_quantity": out_quantity}))

        if out_detail:
            material_out = {"person_id": self.person_id.id,
                            "dpo_id": self.dpo_id.id,
                            "so_id": self.so_id.id,
                            "out_detail": out_detail}

            self.env["material.out"].create(material_out)

    def generate_move(self, recs):
        config = self.env["store.config"].search([("company_id", "=", self.env.user.company_id.id)])

        source_id = config.store_id.id
        destination_id = config.purchase_id.id

        for rec in recs:
            result = {"source_id": source_id,
                      "destination_id": destination_id,
                      "reference": rec.name,
                      "product_id": rec.product_id.id,
                      "description": rec.description,
                      "quantity": rec.out_quantity,
                      "progress": "moved"}

            self.env["arc.move"].create(result)

    @api.multi
    def trigger_in(self):
        received_by = self.env.user.person_id.id
        recs = self.env["material.out.detail"].search([("material_id", "=", self.id), ("out_quantity", ">", 0)])

        if not recs:
            raise exceptions.ValidationError("Error! No Products found")

        self.generate_move(recs)
        self.generate_back_order()

        writter = "Material Out by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "dispatched", "writter": writter, "dispatched_by": received_by})

    @api.multi
    def trigger_generate_invoice(self):
        recs = self.out_detail
        detail = []
        for rec in recs:
            detail.append((0, 0, {"product_id": rec.product_id.id,
                                  "ref_id": rec.ref_id.id,
                                  "description": rec.description,
                                  "unit_price": rec.ref_id.unit_price,
                                  "quantity": rec.out_quantity,
                                  "discount": rec.ref_id.discount,
                                  "tax_id": rec.ref_id.tax_id.id,
                                  "pf": rec.ref_id.pf}))

        if detail:
            invoice = {"person_id": self.person_id.id,
                       "dpo_id": self.dpo_id.id,
                       "so_id": self.so_id.id,
                       "invoice_type": self.get_invoice_type(),
                       "item_ids": detail}

            terms = self.get_terms_and_condition()
            invoice.update(terms)

            self.env["arc.invoice"].create(invoice)

    def get_terms_and_condition(self):
        if self.dpo_id:
            obj = self.dpo_id.id
        elif self.so_id:
            obj = self.so_id.id

        invoice = {"expected_delivery": obj.expected_delivery,
                   "freight": obj.freight,
                   "payment": obj.payment,
                   "insurance": obj.insurance,
                   "certificate": obj.certificate,
                   "warranty": obj.warranty}

        return invoice

    def get_invoice_type(self):
        order_type = None
        if self.dpo_id:
            order_type = self.dpo_id.order_type

        if not order_type:
            raise exceptions.ValidationError("Error! Oder Type Not Found")

        return order_type

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(MaterialOut, self).create(vals)


class MaterialOutDetail(models.Model):
    _name = "material.out.detail"

    name = fields.Char(string="Name", readonly=True)
    reference = fields.Char(string="Reference", readonly=True)
    ref_id = fields.Many2one(comodel_name="direct.purchase.item")
    product_id = fields.Many2one(comodel_name="arc.product", string="Item", required=True)
    description = fields.Text(string="Description")
    uom_id = fields.Many2one(comodel_name="product.uom", string="UOM", related="product_id.uom_id")
    order_quantity = fields.Float(string="Order Quantity", default=0, required=True)
    previous_out_quantity = fields.Float(string="Previous Dispatched Qty", default=0, required=True)
    out_quantity = fields.Float(string="Quantity", default=0, required=True)
    material_id = fields.Many2one(comodel_name="material.out", string="Material In")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", related="material_id.progress")

    @api.constrains("order_quantity", "out_quantity", "previous_out_quantity")
    def check_issue_quantity(self):
        if (self.out_quantity + self.previous_out_quantity) > self.order_quantity:
            raise exceptions.ValidationError("Error! In quantity more than order")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(MaterialOutDetail, self).create(vals)
