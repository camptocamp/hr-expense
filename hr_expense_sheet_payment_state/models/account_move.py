# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def is_invoice(self, include_receipts=False):
        self.ensure_one()
        if self.line_ids.expense_id:
            return True
        return super().is_invoice(include_receipts)
