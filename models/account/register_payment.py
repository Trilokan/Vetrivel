# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions, _
from datetime import datetime, timedelta


PAYMENT_TYPE = [("to_pay", "To Pay"), ("to_receive", "To Receive")]
PAYMENT_MODE = [("cash", "Cash"), ("bank", "Bank")]
PROGRESS_INFO = [("un_posted", "Un Posted"), ("posted", "Posted")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Register Payment
class RegisterPayment(models.Model):
    _name = "register.payment"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", required=True, default=CURRENT_DATE)
    name = fields.Char(string="Name", readonly=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person", required=True)
    invoice_id = fields.Many2one(comodel_name="arc.invoice", string="Invoice")
    note_id = fields.Many2one(comodel_name="journal.item", string="Note")
    display = fields.Html(string="Display")
    amount = fields.Float(string="Amount")
    payment_type = fields.Selection(selection=PAYMENT_TYPE, string="Payment Type")
    payment_mode = fields.Selection(selection=PAYMENT_MODE, string="Payment Mode")
    is_credit_note = fields.Boolean(string="Credit Note")
    is_debit_note = fields.Boolean(string="Debit Note")
    is_payment = fields.Boolean(string="Payment")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")

    @api.onchange('is_credit_note')
    def onchange_is_credit_note(self):
        if self.is_credit_note:
            self.is_debit_note = False
            self.is_payment = False

    @api.onchange('is_debit_note')
    def onchange_is_debit_note(self):
        if self.is_debit_note:
            self.is_credit_note = False
            self.is_payment = False

    @api.onchange('is_payment')
    def onchange_is_debit_note(self):
        if self.is_payment:
            self.is_credit_note = False
            self.is_debit_note = False

    def trigger_register(self):
        if self.invoice_id:
            if self.is_payment:
                pass
            elif self.is_credit_note:
                pass
            elif self.is_debit_note:
                pass
        else:
            if self.is_payment:
                self.generate_credit_debit_note()

    def check_invoice_payment_amount(self):
        recs = self.env["journal.item"].search([("invoice_id", "=", self.invoice_id.id)])

        credit = debit = 0
        for rec in recs:
            credit = credit + rec.credit
            debit = debit + rec.debit

        if self.payment_type == "to_pay":
            credit = credit + self.amount
        elif self.payment_type == "to_receive":
            debit = debit + self.amount

        if self.invoice_id.invoice_type in ["sales", "purchase_return"]:
            if credit > debit:
                raise exceptions.ValidationError("P")
        elif self.invoice_id.invoice_type in ["purchase", "sales_return"]:
            if debit > credit:
                raise exceptions.ValidationError("P")

    def check_invoice_payment_note(self):
        recs = self.env["journal.item"].search([("invoice_id", "=", self.invoice_id.id)])
        credit = self.note_id.credit
        debit = self.note_id.debit

        for rec in recs:
            credit = credit + rec.credit
            debit = debit + rec.debit

        if self.invoice_id.invoice_type in ["sales", "purchase_return"]:
            if credit < debit:
                # Split Noted Id

                raise exceptions.ValidationError("P")
        elif self.invoice_id.invoice_type in ["purchase", "sales_return"]:
            if debit < credit:
                # Split Noted Id
                raise exceptions.ValidationError("P")

    def generate_payment_reconcile(self):
        self.check_invoice_payment_amount()
        entry_id = self.generate_credit_debit_note()
        config = self.env["account.config"].search([("company_id", "=", self.env.user.company_id.id)])

        item = self.env["journal.item"].search([("account_id", "=", config.bank_id.id), ("journal_id", "=", entry_id.id)])
        item.write({"invoice_id": self.invoice_id.id})

    def generate_credit_note_reconcile(self):
        pass

    def generate_debit_note_reconcile(self):
        pass

    def generate_credit_debit_note(self):
        config = self.env["account.config"].search([("company_id", "=", self.env.user.company_id.id)])

        data = {"date": self.date,
                "journal_type_id": self.get_journal_type_id(),
                "person_id": self.person_id.id}

        line_detail = []

        # Person To Bank
        amount = self.get_credit_debit(self.amount)
        item = {"account_id": self.person_id.get_account_id(self.payment_type),
                "description": "Payment",
                "credit": amount["credit"],
                "debit": amount["debit"]}
        item.update(data)
        line_detail.append((0, 0, item))

        # Bank To Company
        item = {"account_id": config.bank_id.id,
                "description": "Payment",
                "credit": amount["debit"],
                "debit": amount["credit"]}
        item.update(data)
        line_detail.append((0, 0, item))

        # Journal Entry
        data = {"date": self.date,
                "journal_type_id": self.get_journal_type_id(),
                "reference": self.name,
                "progress": "posted",
                "item_ids": line_detail}

        journal_id = self.env["arc.journal"].create(data)

        return journal_id

    def get_credit_debit(self, amount):
        credit = debit = 0
        if self.payment_type == "to_pay":
            credit = amount
        elif self.payment_type == "to_receive":
            debit = amount

        return {"credit": credit, "debit": debit}

    def get_journal_type_id(self):
        journal_type_id = False

        if self.payment_type == "to_pay":
            journal_type_id = self.env["journal.type"].search([("name", "=", "Payment")])
        elif self.payment_type == "to_receive":
            journal_type_id = self.env["journal.type"].search([("name", "=", "Receive")])

        if not journal_type_id:
            raise exceptions.ValidationError("Error! Journal Is not set")

        return journal_type_id.id

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(RegisterPayment, self).create(vals)
