# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

INVOICE_TYPE = [("sales", "Sales"),
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


class Invoice(models.Model):
    _name = "arc.invoice"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", readonly=True)
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person", required=True)
    address = fields.Text(string="Address")
    item_ids = fields.One2many(comodel_name="invoice.item", inverse_name="invoice_id")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    invoice_type = fields.Selection(selection=PROGRESS_INFO, string="Invoice Type")

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

    # # Purchase
    # po_id = fields.Many2one(comodel_name="", string="")
    dpo_id = fields.Many2one(comodel_name="direct.purchase", string="Purchase Order")
    # purchase_quote_id = fields.Many2one(comodel_name="", string="")
    #
    # # Sale
    # so_id = ""
    # sale_quote_id = ""
    #
    # # Inventory
    # inventory_id = ""

    expected_delivery = fields.Char(string='Expected Delivery')
    freight = fields.Char(string='Freight')
    payment = fields.Char(string='Payment')
    insurance = fields.Char(string='Insurance')
    certificate = fields.Char(string='Certificate')
    warranty = fields.Char(string='Warranty')

    #
    # # Accounting
    # journal_items = ""

    @api.multi
    def trigger_confirm(self):
        self.trigger_update_total()
        writter = "Invoice confirmed by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        data = {"progress": "confirmed", "writter": writter}

        self.write(data)

    @api.multi
    def trigger_cancel(self):
        self.trigger_update_total()
        writter = "Invoice cancelled by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        data = {"progress": "cancel", "writter": writter}

        self.write(data)

    @api.multi
    def trigger_approve(self):
        self.trigger_update_total()
        self.generate_journal_entry()
        writter = "Invoice approved by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        data = {"progress": "approved", "writter": writter}

        self.write(data)

    @api.multi
    def trigger_update_total(self):
        recs = self.item_ids

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

    @api.multi
    def generate_journal_entry(self):

        data = {"date": self.date,
                "journal_type_id": self.get_journal_type_id(),
                "reference": self.name,
                "progress": "posted",
                "item_ids": self.get_journal_items()}

        self.env["arc.journal"].create(data)

    @api.multi
    def get_journal_items(self):
        recs = self.item_ids

        data = {"date": self.date,
                "invoice_id": self.id,
                "journal_type_id": self.get_journal_type_id(),
                "person_id": self.person_id.id}

        line_detail = []
        for rec in recs:
            item = {}
            item.update(data)
            amount = self.get_credit_debit(rec.after_discount)
            description = "{0} \n {1} \n {2}".format(rec.product_id.product_uid,
                                                     rec.product_id.name,
                                                     rec.product_id.description)
            item["description"] = description
            item["credit"] = amount["credit"]
            item["debit"] = amount["debit"]
            line_detail.append((0, 0, item))

        # CGST
        amount = self.get_credit_debit(self.cgst)
        item = {"description": "CGST",
                "credit": amount["credit"],
                "debit": amount["debit"]}
        item.update(data)
        line_detail.append((0, 0, item))

        # SGST
        amount = self.get_credit_debit(self.sgst)
        item = {"description": "SGST",
                "credit": amount["credit"],
                "debit": amount["debit"]}
        item.update(data)
        line_detail.append((0, 0, item))

        # IGST
        amount = self.get_credit_debit(self.igst)
        item = {"description": "SGST",
                "credit": amount["credit"],
                "debit": amount["debit"]}
        item.update(data)
        line_detail.append((0, 0, item))

        # Round-Off
        amount = self.get_credit_debit(self.round_off)
        item = {"description": "SGST",
                "credit": amount["credit"],
                "debit": amount["debit"]}
        item.update(data)
        line_detail.append((0, 0, item))

        # Packing & Forwarding
        amount = self.get_credit_debit(self.pf)
        item = {"description": "Packing and forwarding",
                "credit": amount["credit"],
                "debit": amount["debit"]}
        item.update(data)
        line_detail.append((0, 0, item))

        # Total
        amount = self.get_credit_debit(self.grand_amount)
        description = "Credit for the {0} {1}".format(self.person_id.person_uid,
                                                      self.person_id.name)
        item = {"description": description,
                "credit": amount["debit"],
                "debit": amount["credit"]}
        item.update(data)
        line_detail.append((0, 0, item))

        return line_detail

    def get_journal_type_id(self):
        if self.invoice_type == "sales":
            journal_type_id = self.env["journal.type"].search([("name", "=", "Sales")])
        elif self.invoice_type == "purchase":
            journal_type_id = self.env["journal.type"].search([("name", "=", "Purchase")])
        elif self.invoice_type == "sales_return":
            journal_type_id = self.env["journal.type"].search([("name", "=", "Sales Return")])
        elif self.invoice_type == "purchase_return":
            journal_type_id = self.env["journal.type"].search([("name", "=", "Purchase Return")])

        if not journal_type_id:
            raise exceptions.ValidationError("Error! Journal Is not set")

        return journal_type_id.id

    def get_credit_debit(self, amount):
        credit = debit = 0
        if self.invoice_type in ["sales", "purchase_return"]:
            credit = amount
        elif self.invoice_type in ["purchase", "sales_return"]:
            debit = amount

        return {"credit": credit, "debit": debit}

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        vals["writter"] = "Invoice created by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        return super(Invoice, self).create(vals)
