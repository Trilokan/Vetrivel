# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolSubject(models.Model):
    _name = "school.subject"

    name = fields.Char(string="Section", required=True)
    subject_uid = fields.Char(string="Code", required=True)
    description = fields.Text(string="Description")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = "[{0}] {1}".format(record.subject_uid, record.name)
            result.append((record.id, name))
        return result

