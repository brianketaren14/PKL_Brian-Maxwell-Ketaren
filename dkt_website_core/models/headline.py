from odoo import models, fields

class Headline(models.Model):
    _name = 'website.headline'
    _description = 'Website Headline'

    name = fields.Char(string='Judul Headline', required=True)
    headline_image = fields.Binary(string='Gambar Headline', required=True)
    description = fields.Text(required=True)
    is_published = fields.Boolean(string='Published', required=True)

