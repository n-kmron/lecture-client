# noinspection PyUnresolvedReferences
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    book_ids = fields.Many2many('esi.book', string='Composés des livres')
