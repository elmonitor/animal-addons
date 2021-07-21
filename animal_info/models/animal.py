# Copyright (C) 2021 elmonitor.net
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models

class Animal(models.Model):
    _inherit = "animal"
    microchip =  = fields.Char(string="Micro Chip")
    esterilized = fields.Boolean(string="Esterilizado")
    
