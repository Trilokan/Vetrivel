# -*- coding: utf-8 -*-

from odoo import models, fields, api


class JournalType(models.Model):
    _name = "journal.type"

    name = fields.Char(string="Name")
    journal_uid = fields.Char(string="Code")

    _sql_constraints = [("journal_uid", "unique(journal_uid)", "Journal Type must be unique")]

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = "[{0}] {1}".format(record.journal_uid, record.name)
            result.append((record.id, name))
        return result
