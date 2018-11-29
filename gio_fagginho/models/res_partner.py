# -*- coding: utf-8 -*-
# Copyright: giordano.ch AG
# Autor: Benjamin Taccone
# Version: 1.0 - 28.11.2018

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    phone2 = fields.Char('Telefon 2')
    website2 = fields.Char('Webseite 2')
    oldposition = fields.Char('Alte Stelle')