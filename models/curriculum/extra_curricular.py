# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExtraCurricular(models.Model):
    _name = "extra.curricular"

    name = ""
    curricular_detail = ""

