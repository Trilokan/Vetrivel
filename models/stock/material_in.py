# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"),
                 ("received", "Received"),
                 ("cancel", "Cancel")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class MaterialIn(models.Model):
    _name = "material.in"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", readonly=True)
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    person_id = fields.Many2one(comodel_name="arc.person", string="Person")
    # po_id = fields.Many2one(comodel_name="arc.person", string="Purchase Order")
    dpo_id = fields.Many2one(comodel_name="direct.purchase", string="Purchase Order")
    in_detail = fields.One2many(comodel_name="material.in.detail", inverse_name="material_id")
    received_by = fields.Many2one(comodel_name="arc.person", string="Received By", readonly=True)
    writter = fields.Char(string="Writter", track_visibility="always")

    @api.multi
    def trigger_cancel(self):
        writter = "Material In cancel by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "cancel", "writter": writter})

    def generate_back_order(self):
        recs = self.in_detail
        in_detail = []
        for rec in recs:
            in_quantity = rec.previous_in_quantity + rec.in_quantity
            if in_quantity < rec.order_quantity:
                in_detail.append((0, 0, {"reference": rec.name,
                                         "ref_id": rec.id,
                                         "product_id": rec.product_id.id,
                                         "description": rec.description,
                                         "order_quantity": rec.order_quantity,
                                         "previous_in_quantity": in_quantity}))

        if in_detail:
            material_in = {"person_id": self.person_id.id,
                           "dpo_id": self.dpo_id.id,
                           "in_detail": in_detail}

            self.env["material.in"].create(material_in)

    def generate_move(self, recs):
        config = self.env["store.config"].search([("company_id", "=", self.env.user.company_id.id)])

        source_id = config.purchase_id.id
        destination_id = config.store_id.id

        for rec in recs:
            result = {"source_id": source_id,
                      "destination_id": destination_id,
                      "reference": rec.name,
                      "product_id": rec.product_id.id,
                      "description": rec.description,
                      "quantity": rec.in_quantity,
                      "progress": "moved"}

            self.env["arc.move"].create(result)

    @api.multi
    def trigger_in(self):
        received_by = self.env.user.person_id.id
        recs = self.env["material.in.detail"].search([("material_id", "=", self.id), ("in_quantity", ">", 0)])

        if not recs:
            raise exceptions.ValidationError("Error! No Products found")

        self.generate_move(recs)
        self.generate_back_order()

        writter = "Material In by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "received", "writter": writter, "received_by": received_by})

    @api.multi
    def trigger_generate_invoice(self):
        recs = self.in_detail
        detail = []
        for rec in recs:
            detail.append((0, 0, {"product_id": rec.product_id.id,
                                  "ref_id": rec.ref_id.id,
                                  "description": rec.description,
                                  "unit_price": rec.ref_id.unit_price,
                                  "quantity": rec.in_quantity,
                                  "discount": rec.ref_id.discount,
                                  "tax_id": rec.ref_id.tax_id.id,
                                  "pf": rec.ref_id.pf}))

        if detail:
            invoice = {"person_id": self.person_id.id,
                       "dpo_id": self.dpo_id.id,
                       "expected_delivery": self.dpo_id.expected_delivery,
                       "freight": self.dpo_id.freight,
                       "payment": self.dpo_id.payment,
                       "insurance": self.dpo_id.insurance,
                       "certificate": self.dpo_id.certificate,
                       "warranty": self.dpo_id.warranty,
                       "item_ids": detail}

            self.env["arc.invoice"].create(invoice)

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(MaterialIn, self).create(vals)


class MaterialInDetail(models.Model):
    _name = "material.in.detail"

    name = fields.Char(string="Name", readonly=True)
    reference = fields.Char(string="Reference", readonly=True)
    ref_id = fields.Many2one(comodel_name="direct.purchase.item")
    product_id = fields.Many2one(comodel_name="arc.product", string="Item", required=True)
    description = fields.Text(string="Description")
    uom_id = fields.Many2one(comodel_name="product.uom", string="UOM", related="product_id.uom_id")
    order_quantity = fields.Float(string="Order Quantity", default=0, required=True)
    previous_in_quantity = fields.Float(string="Previous Received Qty", default=0, required=True)
    in_quantity = fields.Float(string="Quantity", default=0, required=True)
    material_id = fields.Many2one(comodel_name="material.in", string="Material In")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", related="material_id.progress")

    @api.constrains("order_quantity", "in_quantity", "previous_in_quantity")
    def check_issue_quantity(self):
        if (self.in_quantity + self.previous_in_quantity) > self.order_quantity:
            raise exceptions.ValidationError("Error! In quantity more than order")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(MaterialInDetail, self).create(vals)
