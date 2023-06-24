# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Expense(models.Model):
    _name = 'expense.money'
    _description = ''

    name = fields.Char(string='Name', required=True)
    expense = fields.Float(string='Amount', required=True)
    expense_id = fields.Many2one('money.flow')
