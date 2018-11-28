# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Partner(models.Model):

    _inherit = 'res.partner'

        telefon2 = fields.Char('Telefon 2')
        website2 = fields.Char('Webseite 2')
        altestelle = fields.Char('Alte Stelle')
