# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class ResConfigSetting(models.TransientModel):
     _inherit = 'res.config.settings'
        
     amount_rental = fields.Float(string='Amount')
     fine = fields.Float(string='Fine')
        
        
        
     @api.model
     def get_values(self):
        res = super(ResConfigSetting, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res.update(amount_rental=float(get_param('library.amount_rental')) ,
                   fine=float(get_param('library.fine')) )
        return res
    
     @api.model
     def set_values(self):
        super(ResConfigSetting, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param ('library.amount_rental', self.amount_rental)
        set_param ('library.fine', self.fine)
  