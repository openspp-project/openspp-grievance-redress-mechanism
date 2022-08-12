# Part of Newlogic OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class OpenSPPGrievanceRegistrant(models.Model):
    _inherit = "res.partner"

    def open_ticket_form(self):
        return {
            "name": "Create Ticket",
            "view_mode": "form",
            "res_model": "helpdesk.ticket",
            "view_id": self.env.ref("helpdesk_mgmt.ticket_view_form").id,
            "type": "ir.actions.act_window",
            "target": "current",
            "context": {"default_partner_id": self.id},
        }

    ticket_ids = fields.One2many("helpdesk.ticket", "partner_id", "Tickets")
