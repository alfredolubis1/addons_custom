from addons_custom.kedatech_test.models.material import Material
from odoo.tests import common

class TestPriceRule(common.TransactionCase):
    
    
    def test_price_rule(self):
        """Price cannot be less than 100.00"""
        try:
            print("Try Create material.material object with material price less than 100")
            test_price = self.env['material.material'].create({
                'name': 'Patung',
                'supplier_id': 1,
                'material_type': 'fabric',
                'material_price': 90,
                'material_code': 'M-004'
            })
        except:
            print("System Refuse to create material.material object if material price less than 100")
            test_price = self.env['material.material'].create({
                'name': 'Patung',
                'supplier_id': 1,
                'material_type': 'fabric',
                'material_price': 100,
                'material_code': 'M-004'
            })
        self.assertGreaterEqual(test_price.material_price, 100, "Create Material Object with price more than 100")
        print("Test Was Successful")
        
        
    def test_update_material(self):
        """Create 1 material object with name 'Sweater'"""
        test_material_obj = self.env['material.material'].create({
            'name': 'Sweater',
            'supplier_id': 1,
            'material_type': 'cotton',
            'material_price': 100000,
            'material_code': 'M-009',
        })
        self.assertEqual(test_material_obj.name, 'Sweater', msg="Create Success")
        print('Running')
        print("Success Create 1 Test material obj = ", test_material_obj.name)
        print("Updating Test material obj name to 'Jacket'")
        test_material_obj.update({
            'name': 'Jacket'
        })
        self.assertEqual(test_material_obj.name, 'Jacket', msg="Update Success")
        print("Success Update Test Material obj name = ", test_material_obj.name)
        
    
    def test_unlink_material(self):
        """Create 1 material object with name 'Sweater'"""
        test_material_obj = self.env['material.material'].create({
            'name': 'Sweater',
            'supplier_id': 1,
            'material_type': 'cotton',
            'material_price': 100000,
            'material_code': 'M-009',
        })
        self.assertEqual(test_material_obj.name, 'Sweater', msg="Create Success")
        print('Running')
        print("Success Create 1 Test material obj = ", test_material_obj)
        print("Updating Test material obj name to 'Jacket'")
        obj_id = test_material_obj.id
        print("obj id = ", test_material_obj.id)
        test_material_obj.unlink()
        prove_unlink = self.env['material.material'].search([('id', '=', obj_id)])
        self.assertEqual(prove_unlink.id, False, msg="Success Remove")
        