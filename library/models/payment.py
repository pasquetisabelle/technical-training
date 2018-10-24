# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Payment(models.Model):
    _name = 'library.payment'
    _description = 'Book payment'
    
    date_payment = fields.Date(string='Date paiement')
    amount = fields.Float(string='Amount')
    customer_id = fields.Many2one('res.partner', 'Customer', domain=[('customer','=',True), ], required=True)
    
    