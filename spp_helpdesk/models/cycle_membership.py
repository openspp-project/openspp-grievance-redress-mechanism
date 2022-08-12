# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
from odoo import models


class OpenSPPCycleMembership(models.Model):
    _inherit = "g2p.cycle.membership"

    def open_ticket_form(self):
        return {
            "name": "Create Ticket",
            "view_mode": "form",
            "res_model": "helpdesk.ticket",
            "view_id": self.env.ref("helpdesk_mgmt.ticket_view_form").id,
            "type": "ir.actions.act_window",
            "target": "current",
            "context": {
                "default_partner_id": self.partner_id.id,
                "default_program_id": self.cycle_id.program_id.id,
                "default_cycle_id": self.cycle_id.id,
            },
        }
