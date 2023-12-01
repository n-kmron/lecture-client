# book_model.py
# noinspection PyUnresolvedReferences
from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'esi.book'

    name = fields.Char('Titre', help="Name of the book ?", unique=True)
    description = fields.Html('Description', help="Resume of the book ?")

    cover_image = fields.Binary(help="Book Cover")
    date_created = fields.Date('Date de publication', help="Date of publication ?")
    pages = fields.Integer('Nombres de pages', help="Number of pages ?")

    authors = fields.Many2many(
        comodel_name='res.partner',
        string='Authors',
    )

    liked_by_users = fields.Many2many('res.users', string='Liked By')
    likes_count = fields.Integer(compute='_compute_likes_count', string='Likes')

    @api.depends('liked_by_users')
    def _compute_likes_count(self):
        for record in self:
            record.likes_count = len(record.liked_by_users)

    # Méthode pour gérer le like/unlike
    def toggle_like_book(self):
        self.ensure_one()
        if self.env.user in self.liked_by_users:
            # Si l'utilisateur actuel a déjà aimé le livre, on le retire de la liste des "likes"
            # [(3, ID)] est utilisé pour supprimer la relation existante avec cet utilisateur
            self.liked_by_users = [(3, self.env.user.id)]
        else:
            # Si l'utilisateur actuel n'a pas encore aimé le livre, on l'ajoute à la liste des "likes"
            # [(4, ID)] est utilisé pour ajouter une relation avec cet utilisateur
            self.liked_by_users = [(4, self.env.user.id)]

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
