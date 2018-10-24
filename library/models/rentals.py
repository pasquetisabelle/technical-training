# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import date,datetime

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'
    _order = "rental_date desc,return_date desc"

    customer_id = fields.Many2one(
        'res.partner',
        'Customer',
        domain=[('customer','=',True), ],
        required=True,
    )
    book_id = fields.Many2one(
        'product.product',
        'Book',
        domain=[('book','=',True)],
        required=True,
    )
    rental_date =  fields.Date(string='Rental date', required=True, default=lambda self: fields.Date.today())
    return_date =  fields.Date(string='Return date', required=True)
    

            
    @api.multi
    def action_return_book(self):
        self.ensure_one()
        
        get_param = self.env['ir.config_parameter'].sudo().get_param
        amount = float(get_param('library.amount_rental')) or 1
        
        self.return_date = date.today()
        
        nbr_day = (self.return_date - self.rental_date).days + 1
        for rental in self:
            price_vals = {
                'date_payment': date.today(),
                'amount': amount*nbr_day,
                'customer_id':rental.customer_id.id,
                }
            price = self.env['library.payment'].create(price_vals)
            
            
            
            return {"type":"ir.actions.act_window",
                "name":'library.payment',    
                "view_mode":"form",
                "view_type":"form",
                "res_model":"library.payment", 
                "res_id" : price.id,
                "target":"new",    
                }
        
        
    @api.multi
    def action_lost_book(self):
        self.ensure_one()   
        
        get_param = self.env['ir.config_parameter'].sudo().get_param
        fine = float(get_param('library.fine')) or 10.0
        for rental in self:
            price_vals = {
                'date_payment': date.today(),
                'amount': fine,
                'customer_id':rental.customer_id.id,
                }
            price = self.env['library.payment'].create(price_vals)
            
            
            
            return {"type":"ir.actions.act_window",
                "name":'library.payment',    
                "view_mode":"form",
                "view_type":"form",
                "res_model":"library.payment", 
                "res_id" : price.id,
                "target":"new",    
                }