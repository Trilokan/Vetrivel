# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("cancel", "Cancel")]
APPROVE_PROGRESS_INFO = [("draft", "Draft"), ("approved", "Approved"), ("cancel", "Cancel")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class PurchaseIndent(models.Model):
    _name = "purchase.indent"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", required=True, default=CURRENT_DATE)
    name = fields.Char(string="Name", readonly=True)
    department_id = fields.Many2one(comodel_name="hr.department", string="Department", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    indent_detail = fields.One2many(comodel_name="purchase.indent.detail", inverse_name="indent_id")
    requested_by = fields.Many2one(comodel_name="arc.person", string="Requested By", readonly=True)
    cancel_by = fields.Many2one(comodel_name="arc.person", string="Cancel By", readonly=True)
    writter = fields.Char(string="Writter", track_visibility="always")

    @api.multi
    def trigger_confirm(self):
        requested_by = self.env.user.person_id.id
        writter = "Purchase Indent Confirmed by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"progress": "confirmed", "writter": writter, "requested_by": requested_by})

    @api.multi
    def trigger_cancel(self):
        cancel_by = self.env.user.person_id.id
        writter = "Purchase Indent cancel by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"progress": "cancel", "writter": writter, "cancel_by": cancel_by})

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(PurchaseIndent, self).create(vals)


class PurchaseIndentDetail(models.Model):
    _name = "purchase.indent.detail"

    name = fields.Char(string="Name", readonly=True)
    product_id = fields.Many2one(comodel_name="arc.product", string="Item", required=True)
    description = fields.Text(string="Item Description")
    uom_id = fields.Many2one(comodel_name="product.uom", string="UOM", related="product_id.uom_id")
    indent_quantity = fields.Float(string="Indent Quantity", default=0, required=True)
    approved_quantity = fields.Float(string="Approved Quantity", default=0, required=True)
    indent_id = fields.Many2one(comodel_name="purchase.indent", string="Purchase Indent")
    indent_progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", related="indent_id.progress")
    approve_progress = fields.Selection(selection=APPROVE_PROGRESS_INFO, string="Progress")

    @api.constrains("approved_quantity")
    def check_indent_quantity(self):
        if self.approved_quantity > self.indent_quantity:
            raise exceptions.ValidationError("Error! Approved quantity more than requested")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(PurchaseIndentDetail, self).create(vals)
