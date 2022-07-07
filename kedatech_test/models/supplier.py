from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Supplier(models.Model):
    _name = "supplier.supplier"
    
    name = fields.Char('Name', required="1")
    email = fields.Char('Email')
    user_id = fields.Many2one('res.users', 'User')