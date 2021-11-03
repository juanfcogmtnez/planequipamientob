# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Project(models.Model):
	_inherit = 'project.project'
	descripcion =fields.Char(string='Extension de módulo proyecto')
