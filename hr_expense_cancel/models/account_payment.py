from odoo import models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def action_draft_cancel(self):
        for payment in self:
            payment.action_draft()
            payment.action_cancel()
