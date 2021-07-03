# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models

class Animal(models.Model):
    _inherit = "animal"
    medicine_list_id = fields.One2many(
        "medicine_list", string="Lista de medicamentos", index=True
    )
