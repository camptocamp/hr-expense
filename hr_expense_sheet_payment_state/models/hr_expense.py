# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    def _get_account_move_line_values(self):
        result = super()._get_account_move_line_values()
        for expense, values in result.items():
            values[-1].update({'exclude_from_invoice_tab': True})
        return result


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    payment_state = fields.Selection([
        ("not_paid", "Not Paid"),
        ("in_payment", "In Payment"),
        ("paid", "Paid"),
        ("partial", "Partially Paid"),
        ("reversed", "Reversed"),
        ("invoicing_legacy", "Invoicing App Legacy"),
    ], string="Payment Status", store=True, readonly=True, copy=False, tracking=True, compute="_compute_payment_state")

    @api.depends('account_move_id.payment_state')
    def _compute_payment_state(self):
        for sheet in self:
            sheet.payment_state = sheet.account_move_id.payment_state or 'not_paid'
