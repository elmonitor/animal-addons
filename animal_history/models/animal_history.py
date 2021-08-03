# Copyright (C) 2021 elmonitor.net
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models, api

class AnimalHistory(models.Model):
    _name = "animal.history"
    _description = "Historia Clínica"
    _order = "date"
    animal_id = fields.Many2one("animal", string="Mascota", required = True)
    anamnesis = fields.Text(string="Anamnesis", required=True)
    partner_id = fields.Many2one("res.partner", string="Veterinario", required=True)
    temperature = fields.Float(string="Temperatura")
    heart_frec = fields.Integer(string="Frecuencia Cardiaca")
    breath_frec = fields.Integer(string="Frecuencia Respiratoria")
    mucous = fields.Char(string="Mucosas")
    dehydration = fields.Float(string="Deshidratación (%)")
    weight = fields.Float(string="Peso (Kg.)")
    attitude = fields.Char(string="Actitud")
    condition = fields.Selection([('1','1. Muy mal'),('2','2. Mal'),('3','3. Regular'),('4','4. Bien'),('5','5. Optimo')], string="Condición Corporal")
    affected = fields.Text(string="Sistemas afectados")
    tests = fields.Text(string="Exámenes complementarios")
    dif_diagnosis = fields.Text(string="Diagnóstico diferencial")
    def_diagnosis = fields.Text(string="Diagnóstico definitivo")
    initial_treatment = fields.Text(string="Tratamiento inicial")
    date = fields.Datetime(string="Fecha de consulta", required=True)
    next_date = fields.Datetime(string="Próxima Fecha de consulta")
