# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
    _name = "arc.account"

    name = fields.Char(string="Name")
    account_uid = fields.Char(string="Code")
    journal_id = fields.Many2one(comodel_name="journal.type", string="Journal Type")
    credit = fields.Float(string="Credit")
    debit = fields.Float(string="Debit")
    allow_reconcile = fields.Boolean(string="Allow Reconcile")

    _sql_constraints = [("account_uid", "unique(account_uid)", "Account must be unique")]