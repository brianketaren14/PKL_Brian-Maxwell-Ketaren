from odoo import models, fields

class GovernmentService(models.Model):
    _name = 'government.service'
    _description = 'Government Service'
    _order = 'sequence'

    name = fields.Char('Nama Layanan', required=True)
    sequence = fields.Integer('Urutan', default=10)
    icon = fields.Binary('Ikon', required=True)
    description = fields.Html('Deskripsi')
    url = fields.Char('URL Layanan')
    service_type = fields.Selection([
        ('internal', 'Layanan Internal'),
        ('external', 'Layanan Eksternal')
    ], string='Tipe Layanan', default='internal')
    is_active = fields.Boolean('Aktif', default=True) 