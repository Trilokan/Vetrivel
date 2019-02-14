# -*- coding: utf-8 -*-

from odoo import models, fields


class JournalType(models.Model):
    _name = "journal.type"

    name = fields.Char(string="Name")
    journal_uid = fields.Char(string="Code")

    _sql_constraints = [("journal_uid", "unique(journal_uid)", "Journal Type must be unique")]
