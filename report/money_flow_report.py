# -*- coding: utf-8 -*-

from odoo import fields, models, tools, api

class MoneyFlowReport(models.Model):
    """ """

    _name = 'money.flow.report'
    _auto = False
    _description = ''
    _rec_name = 'date'
    _order = 'date desc'

    date = fields.Datetime('Issue Date', readonly=True)
    name = fields.Char(string='Name', readonly=True)
    money_type = fields.Selection(string='Type', selection=[('cash', 'Cash'), ('credit_card', 'Credit Card')], readonly=True)
    currency_id = fields.Many2one('res.currency', string='Currency', readonly=True)
    amount = fields.Float(string='Amount', digits=(16,0), readonly=True)

    def _select(self):
        return """
            SELECT
                mf.id,
                mf.issue_date as date,
                mf.name,
                mf.money_type,
                mf.amount,
                mf.currency_id
        """

    def _from(self):
        return """
            FROM money_flow as mf
        """

    def _where(self):
        return """"""

    def _group_by(self):
        return """
            GROUP BY
                mf.id,
                mf.issue_date,
                mf.money_type,
                mf.name,
                mf.amount,
                mf.currency_id
        """

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                %s
                %s
                %s
                %s
            )
        """ % (self._table, self._select(), self._from(), self._where(), self._group_by()))