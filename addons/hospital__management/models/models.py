# -*- coding: utf-8 -*-

from odoo import models, fields, api
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patients'
    name = fields.Char(string="Title", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
            ('male','Male'),
           ('female', 'Female'),
        ], required =True, default='male'
    )
    note = fields.Text(string='Description')


# class hospital__management(models.Model):
#     _name = 'hospital__management.hospital__management'
#     _description = 'hospital__management.hospital__management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
