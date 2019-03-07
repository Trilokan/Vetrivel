# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

ORDER_TYPE = [("sales", "Sales"),
              ("purchase", "Purchase"),
              ("sales_return", "Sales Return"),
              ("purchase_return", "Purchase Return")]
PROGRESS_INFO = [("draft", "Draft"),
                 ("confirmed", "Confirmed"),
                 ("approved", "Approved"),
                 ("cancel", "Cancel")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class Order(models.Model):
    _name = "arc.order"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", readonly=True)
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person", required=True)
    address = fields.Text(string="Address")
    order_detail = fields.One2many(comodel_name="order.detail", inverse_name="order_id")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    order_type = fields.Selection(selection=ORDER_TYPE, string="Order Type", required=True)

    # Calculation
    sub_total_amount = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    others = fields.Float(string="Others", required=True, readonly=True, default=0.0)
    round_off = fields.Float(string="Rounding-Off", required=True, readonly=True, default=0.0)
    grand_amount = fields.Float(string="Grand Total", required=True, readonly=True, default=0.0)
    cgst = fields.Float(string="CGST", required=True, readonly=True, default=0.0)
    sgst = fields.Float(string="SGST", required=True, readonly=True, default=0.0)
    igst = fields.Float(string="IGST", required=True, readonly=True, default=0.0)
    tax_amount = fields.Float(string="Tax Amount", required=True, readonly=True, default=0.0)
    un_tax_amount = fields.Float(string="Un-Tax Amount", required=True, readonly=True, default=0.0)
    discount_amount = fields.Float(string="Discount Amount", required=True, readonly=True, default=0.0)
    pf = fields.Float(string="PF Amount", required=True, readonly=True, default=0.0)

    expected_delivery = fields.Char(string='Expected Delivery')
    freight = fields.Char(string='Freight')
    payment = fields.Char(string='Payment')
    insurance = fields.Char(string='Insurance')
    certificate = fields.Char(string='Certificate')
    warranty = fields.Char(string='Warranty')

    @api.multi
    def trigger_confirm(self):
        self.trigger_update_total()
        writter = "Order confirmed by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        data = {"progress": "confirmed", "writter": writter}

        self.write(data)

    @api.multi
    def trigger_cancel(self):
        self.trigger_update_total()
        writter = "Order cancelled by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        data = {"progress": "cancel", "writter": writter}

        self.write(data)

    @api.multi
    def trigger_approve(self):
        recs = self.env["order.detail"].search([("order_id", "=", self.id), ("quantity", ">", 0)])

        if not recs:
            raise exceptions.ValidationError("Error! No Products found")

        self.generate_material_transact(recs)
        writter = "Order approved by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        data = {"progress": "approved", "writter": writter}

        self.write(data)

    def generate_material_transact(self, recs):
        transact_detail = []
        for rec in recs:
            transact_detail.append((0, 0, {"order_ref": rec.name,
                                           "product_id": rec.product_id.id,
                                           "description": rec.description,
                                           "order_quantity": rec.quantity}))

        if transact_detail:
            transact = {"order_id": self.id,
                        "person_id": self.person_id.id,
                        "transact_type": self.get_material_transact_type(),
                        "transact_detail": transact_detail}

            self.env["material.transact"].create(transact)

    def get_material_transact_type(self):
        transact_type = None
        if self.order_type in ["purchase", "sales_return"]:
            transact_type = "in"
        elif self.order_type in ["sales", "purchase_return"]:
            transact_type = "out"

        if not transact_type:
            raise exceptions.ValidationError("Error! Transaction Type Not Found")

        return transact_type

    @api.multi
    def trigger_update_total(self):
        recs = self.order_detail

        sub_total_amount = cgst = sgst = igst = tax_amount = pf = discount_amount = 0
        for rec in recs:
            rec.update_total()
            cgst = cgst + rec.cgst
            sgst = sgst + rec.sgst
            igst = igst + rec.igst
            sub_total_amount = sub_total_amount + rec.total
            tax_amount = tax_amount + rec.tax_amount
            discount_amount = discount_amount + rec.discount_amount
            pf = pf + rec.pf

        total = sub_total_amount + self.others
        self.grand_amount = round(total)
        self.round_off = round(total) - total
        self.cgst = cgst
        self.sgst = sgst
        self.igst = igst
        self.sub_total_amount = sub_total_amount
        self.tax_amount = tax_amount
        self.un_tax_amount = self.others
        self.pf = pf
        self.discount_amount = discount_amount

    @api.model
    def create(self, vals):
        sequence = "{0}_{1}".format(self._name, vals["order_type"])
        vals["name"] = self.env["ir.sequence"].next_by_code(sequence)
        vals["writter"] = "Order created by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        return super(Order, self).create(vals)
