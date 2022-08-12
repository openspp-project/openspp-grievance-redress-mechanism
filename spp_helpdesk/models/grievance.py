# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class OpenSPPGrievance(models.Model):
    _inherit = "helpdesk.ticket"

    cycle_id = fields.Many2one("g2p.cycle", "Cycle")
    group_id = fields.Many2one("res.partner", "Group", domain=[("is_group", "=", True)])
    group_readonly_id = fields.Many2one("res.partner", "Group", related="group_id")
    partner_readonly_id = fields.Many2one(
        "res.partner", "Registrant", related="partner_id"
    )
    program_id = fields.Many2one("g2p.program", "Program")
    program_readonly_id = fields.Many2one(
        "g2p.program", "Program", related="program_id"
    )
    cycle_readonly_id = fields.Many2one("g2p.cycle", "Cycle", related="cycle_id")
    is_group = fields.Boolean("Group", related="partner_id.is_group")

    @api.onchange("partner_id")
    def _get_groups(self):
        groups = self.env["g2p.group.membership"].search(
            [
                ("individual", "=", self.partner_id.id),
            ]
        )
        vals = []
        if groups:
            for line in groups:
                vals.append(line.group.id)
        res = {}
        res["domain"] = {"group_id": [("id", "in", vals)]}

        return res

    @api.onchange("partner_id", "group_id")
    def _get_programs(self):
        programs = self.env["g2p.program_membership"].search(
            [
                ("partner_id", "in", [self.partner_id.id, self.group_id.id]),
            ]
        )
        vals = []
        if programs:
            for line in programs:
                vals.append(line.program_id.id)
        res = {}
        res["domain"] = {"program_id": [("id", "in", vals)]}

        return res

    @api.onchange("program_id")
    def _get_cycle(self):
        cycle = self.env["g2p.cycle.membership"].search(
            [
                ("partner_id", "=", self.partner_id.id),
            ]
        )
        vals = []
        if cycle:
            for line in cycle:
                if line.cycle_id.program_id.id == self.program_id.id:
                    vals.append(line.cycle_id.id)
        res = {}
        res["domain"] = {"cycle_id": [("id", "in", vals)]}
        return res
