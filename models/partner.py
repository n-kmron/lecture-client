from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    is_author = fields.Boolean(string='Author', default=False)

    book_ids = fields.Many2many('esi.book', string='Books', readonly=True)
