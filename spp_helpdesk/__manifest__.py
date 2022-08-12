# Part of Newlogic OpenSPP. See LICENSE file for full copyright and licensing details.


{
    "name": "OpenSPP Helpdesk System",
    "category": "OpenSPP",
    "version": "15.0.0.0.1",
    "sequence": 3,
    "author": "Newlogic",
    "website": "https://newlogic.com/",
    "license": "AGPL-3",
    "depends": ["base", "helpdesk_mgmt", "g2p_registry_base", "g2p_programs"],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/custom_helpdesk_view.xml",
        "views/custom_registrant_view.xml",
        "views/custom_beneficiary_view.xml",
        "views/custom_cycle_membership_view.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
