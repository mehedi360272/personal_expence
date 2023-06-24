# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta

class MoneyFlow(models.Model):
    _name = 'money.flow'
    _description = ''
    _order = 'issue_date desc'

    _rec_name = 'month', 'money_type'
    def _default_currency_id(self):
        return self.env.user.company_id.currency_id

    name = fields.Char(string='Name', required=True)
    image = fields.Image()
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self._default_currency_id())
    # amount = fields.Float(string='Amount', digits=(16, 0), required=True)
    description = fields.Text(string='Description')
    money_type = fields.Selection(
        string='Money Type',
        selection=[('cash', 'Cash'), ('credit_card', 'Credit Card')], required=True, default='cash')
    issue_date = fields.Datetime(string='Issue date', default=fields.Datetime.now, required=True)
    month = fields.Selection([
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ], string='Month')
    user_id = fields.Many2one('res.users', 'Paid By')
    attachments = fields.Many2many('ir.attachment', string='add file')
    income_ids = fields.One2many('income.money', 'income_id')
    expense_ids = fields.One2many('expense.money', 'expense_id')

    total_income = fields.Integer(compute="_total_income", string="Total Income")
    amount = fields.Float(compute="_total_expense", string='Total Expense', digits=(16, 0), required=True)
    available_balance = fields.Integer(compute="_available_balance", string="Total Available Balance")

    @api.depends('income_ids.income')
    def _total_income(self):
        for record in self:
            record.total_income = sum(record.income_ids.mapped('income'))

    @api.depends('expense_ids.expense')
    def _total_expense(self):
        for record in self:
            record.amount = sum(record.expense_ids.mapped('expense'))

    @api.depends('total_income', 'amount')
    def _available_balance(self):
        for record in self:
            record.available_balance = record.total_income - record.amount

    @api.model
    def create(self, vals):
        if self.env["money.flow"].search([("month", "=", vals['month'])]):
            raise ValidationError(_("You have already been allocated."))
        return super(MoneyFlow, self).create(vals)

