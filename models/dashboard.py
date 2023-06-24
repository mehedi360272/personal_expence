# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Dashboard(models.Model):
    _name = 'dashboard.money'
    _description = ''

    money_flow_ids = fields.Many2one('money.flow', required='True')
    cash = fields.Many2one('money.flow', required='True')
    expenses = fields.Float(related="money_flow_ids.amount", string="Total Expense")
    available_balances = fields.Integer(related="money_flow_ids.available_balance", string="Available Balance")
    total_incomes = fields.Integer(related="money_flow_ids.total_income", string="Total Income")
