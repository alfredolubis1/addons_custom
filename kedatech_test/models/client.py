from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.misc import profile

class Client(models.Model):
    _name = "client.client"
    
    name = fields.Char('Name')
    email = fields.Char('Email')
    user_id = fields.Many2one('res.users', 'Client')