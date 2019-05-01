# -*- coding: utf-8 -*-

from odoo import models, fields, api

PROGRESS_INFO = [("draft", "Draft"),
                 ("confirmed", "Confirmed"),
                 ("done", "Done"),
                 ("cancel", "Cancel")]


class QuestionPaper(models.Model):
    _name = "question.paper"

    date = ""