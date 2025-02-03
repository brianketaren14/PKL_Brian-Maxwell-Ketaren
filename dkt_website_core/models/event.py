from odoo import models, fields, api

class Event(models.Model):
    _inherit = 'event.event'

    # Tambahan fields untuk event
    subtitle = fields.Text('Sub Judul', translate=True)
    location_address = fields.Text('Alamat Lokasi')
    contact_person = fields.Char('Kontak Person')
    contact_phone = fields.Char('No. Telepon')
    contact_email = fields.Char('Email')
    is_featured = fields.Boolean('Featured Event', default=False)
    
    # Kategori event (misal: seminar, workshop, dll)
    category_id = fields.Many2one('event.category', string='Kategori Event')
    
    # Tambahan gambar untuk galeri
    gallery_ids = fields.Many2many('ir.attachment', string='Galeri Foto')
    
    # Dokumen terkait (misal: jadwal acara, brosur, dll)
    document_ids = fields.Many2many('ir.attachment', 'event_document_rel', 
                                  'event_id', 'attachment_id', string='Dokumen') 