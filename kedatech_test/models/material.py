from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = "material.material"
    
    name = fields.Char('Material Name')
    material_code = fields.Char('Material Code')
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string="Material Type")
    material_price = fields.Float('Material Price')
    supplier_id = fields.Many2one('supplier.supplier', 'Supplier')
    
    @api.constrains('material_price')
    def _check_price(self):
        for rec in self:
            if rec.material_price < 100.0:
                raise ValidationError(_("Harga Material tidak boleh kurang dari 100"))
    
    