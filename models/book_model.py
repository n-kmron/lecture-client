# book_model.py
# noinspection PyUnresolvedReferences
from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)
class Book(models.Model):
    _name = 'esi.book'

    name = fields.Char('Titre', help="Name of the book ?", unique=True)
    description = fields.Text('Description', help="Resume of the book ?")

    cover_image = fields.Binary(help="Book Cover")


    date_created = fields.Date('Date de publication', help="Date of publication ?")

    pages = fields.Integer('Nombres de pages',help="Number of pages ?")

    authors = fields.Many2many(
        comodel_name='res.partner',
        string='Authors',
    )

    @api.constrains('date_created')
    def _check_date(self):
        for book in self:
            if book.date_created > fields.Date.today():
                raise models.ValidationError('The date of publication must be less than today')

    @api.constrains('pages')
    def _check_pages_size(self):
        for book in self:
            if book.pages <= 0:
                raise models.ValidationError('The number of pages must be greater than 0')
