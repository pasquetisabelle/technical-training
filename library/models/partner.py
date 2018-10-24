# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Partner(models.Model):
    _inherit = 'res.partner'

    author =  fields.Boolean('is an Author', default=False)
    publisher =  fields.Boolean('is a Publisher', default=False)
    rental_ids = fields.One2many(
        'library.rental',
        'customer_id',
        string='Rentals')
    book_ids = fields.Many2many(
        comodel_name="product.product",
        string="Books",
        domain=[('book','=',True), ],
    )
    nationality_id = fields.Many2one(
        'res.country',
        'Nationality',
    )
    birthdate =  fields.Date('Birthdate',)

    payment_count = fields.Float(string="Payment Count", compute="_countpayment")
    payment_ids = fields.One2many('library.payment','customer_id', string="Payment")

    def _countpayment(self):
        
        for customer in self:
            customer.payment_count = len(customer.payment_ids)
            
    def action_payment(self):
        return {"type":"ir.actions.act_window",
                "name":'library.payment',    
                "view_mode":"tree,form",
                "res_model":"library.payment", 
                "domain" : [('customer_id','=',self.id)]   
                }