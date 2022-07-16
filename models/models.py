from odoo import models,fields, api

class Todo(models.Model):
    _name ="md.todo"

    name = fields.Char("Nombre")
    status = fields.Selection(selection=[("borrador","Borrador"),("hecho","Hecho")])
