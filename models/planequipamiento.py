# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Planequipamiento(models.Model):
	_name = "planequipamiento"
	_inherit = ['image.mixin']
	name = fields.Char(string="Plan")
