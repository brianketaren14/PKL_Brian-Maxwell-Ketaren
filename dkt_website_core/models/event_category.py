from odoo import models, fields

class EventCategory(models.Model):
    _name = 'event.category'
    _description = 'Kategori Event'
    _order = 'sequence, name'

    name = fields.Char('Nama Kategori', required=True, translate=True)
    sequence = fields.Integer('Urutan', default=10)
    description = fields.Text('Deskripsi', translate=True)
    active = fields.Boolean('Active', default=True)
    color = fields.Integer('Warna')
    icon = fields.Binary('Icon') 