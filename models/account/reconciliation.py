# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reconciliation(models.Model):
    _name = "arc.reconcile"

    name = fields.Char(string="Name")
    full_reconcile_ids = fields.One2many(comodel_name="journal.item", inverse_name="full_reconcile_id")
    part_reconcile_ids = fields.One2many(comodel_name="journal.item", inverse_name="part_reconcile_id")

    def check_reconcile(self):
        recs = self.full_reconcile_ids + self.part_reconcile_ids
        credit = 0
        debit = 0
        for rec in recs:
            credit = credit + rec.credit
            debit = debit + rec.debit

        if credit == debit:
            for rec in recs:
                rec.full_reconcile_id = self.id
                rec.part_reconcile_id = False

        else:
            for rec in recs:
                rec.full_reconcile_id = False
                rec.part_reconcile_id = self.id
