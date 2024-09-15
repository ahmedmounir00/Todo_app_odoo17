from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Todo(models.Model):
    _name = "todo.management"
    _inherit = ['mail.thread']
    _description = "New Task"
    _rec_name = "task_name"

    task_name = fields.Char(string="Task Name" , required=True , tracking=True)
    description = fields.Char(string="Description" , tracking=True)
    due_date = fields.Date(string="Due Date" , required=True , tracking=True)
    status = fields.Selection([
        ('new','New'),
        ('in progress','In Progress'),
        ('completed','Completed'),
    ],string='Status' , default="new" , tracking=True)
    assign_to = fields.Many2one('res.partner' , string="Assign To")

    _sql_constraints = [
        ('unique_name', 'unique(task_name)', 'This name is exist.')
    ]


