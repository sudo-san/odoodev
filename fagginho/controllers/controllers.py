# -*- coding: utf-8 -*-
from odoo import http

# class Fagginho(http.Controller):
#     @http.route('/fagginho/fagginho/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fagginho/fagginho/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fagginho.listing', {
#             'root': '/fagginho/fagginho',
#             'objects': http.request.env['fagginho.fagginho'].search([]),
#         })

#     @http.route('/fagginho/fagginho/objects/<model("fagginho.fagginho"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fagginho.object', {
#             'object': obj
#         })