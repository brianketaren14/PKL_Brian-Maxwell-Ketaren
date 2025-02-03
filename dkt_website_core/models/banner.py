from odoo import models, fields

class WebsiteBanner(models.Model):
    _name = 'website.banner'
    _description = 'Website Banner'
    _order = 'sequence'

    name = fields.Char('Judul', required=True)
    sequence = fields.Integer('Urutan', default=10)
    image = fields.Binary('Gambar', required=True)
    description = fields.Html('Deskripsi')
    url = fields.Char('URL')
    active = fields.Boolean('Aktif', default=True) 