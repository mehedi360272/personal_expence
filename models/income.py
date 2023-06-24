# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Income(models.Model):
    _name = 'income.money'
    _description = ''

    name = fields.Char(string='Income Source', required=True)
    income = fields.Float(string='Income', required=True)
    income_id = fields.Many2one('money.flow')
