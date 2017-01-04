# -*- coding: utf-8 -*-
from openerp import models,fields,api
class TodoTask(models.Model):
    _inherit = 'todo.task' #attribute to inherit apps
	user_id = fields.Many2one('res.users', 'Responsible')  #field for who made the task
    date_deadline = fields.Date('Deadline') #deadline of task
    name = fields.Char(help = "what needs to be done?")  #help when hovered around description field