# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    authors_ids = fields.Many2many('library.partner', string="Authors")
    edition_date =  fields.Date(string='Edition date',)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')
    
    
class BookCopy(models.Model):
    _name = 'library.book_copy'
    _description = 'Book Copy'
    _inherits = {'library.book' : 'book_id'}
    
    book_id = fields.Many2one('library.book')
    ref_interne = fields.Char(string='Reference')
    
    _sql_constraints = [("uniq_id","unique(ref_interne)","A reference already exists with this book. It must be unique !"),]
    
    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        default = default or {}
        default['ref_interne'] = self.ref_interne + "/copy"
        
        return super(BookCopy, self).copy(default)

    
