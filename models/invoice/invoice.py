# -*- coding: utf-8 -*-

from odoo import models, fields


class Invoice(models.Model):
    _name = "arc.invoice"

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")
    person_id = fields.Many2one(comodel_name="arc.person", string="Person")
    address = fields.Text(string="Address")
    item_ids = ""
    progress = ""
    invoice_type = ""

    # Calculation
    sub_total_amount = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    others = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    round_off = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    grand_amount = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    cgst = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    sgst = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    igst = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    taxable_amount = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)
    un_taxable_amount = fields.Float(string="Sub Total", required=True, readonly=True, default=0.0)

    # Purchase
    po_id = fields.Many2one(comodel_name="", string="")
    dpo_id = fields.Many2one(comodel_name="", string="")
    purchase_quote_id = fields.Many2one(comodel_name="", string="")

    # Sale
    so_id = ""
    sale_quote_id = ""

    # Inventory
    inventory_id = ""

    # Terms & Condition
    payment_term = ""
    delivery_term = ""
    term_1 = ""
    term_2 = ""
    term_3 = ""

    # Accounting
    journal_items = ""
