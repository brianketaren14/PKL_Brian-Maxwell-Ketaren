from odoo import models, fields, api
from datetime import datetime
import re
import unicodedata

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[-\s]+', '-', text).strip('-')

class News(models.Model):
    _name = 'website.news'
    _description = 'Website News'
    _inherit = ['website.published.mixin', 'mail.thread', 'mail.activity.mixin']
    _order = 'date_published desc'

    name = fields.Char('Judul', required=True, tracking=True)
    slug = fields.Char('URL Slug', compute='_compute_slug', store=True)
    thumbnail = fields.Binary('Thumbnail', required=True)
    thumbnail_filename = fields.Char('Nama File Thumbnail')
    teaser = fields.Text('Teaser', required=True, help='Ringkasan singkat berita yang akan ditampilkan di halaman depan', tracking=True)
    content = fields.Html('Konten', required=True, sanitize=True, tracking=True)
    date_published = fields.Datetime('Tanggal Publikasi', default=fields.Datetime.now, tracking=True)
    author_id = fields.Many2one('res.users', 'Penulis', default=lambda self: self.env.user, tracking=True)
    category_id = fields.Many2one('website.news.category', 'Kategori', tracking=True, ondelete='restrict')
    view_count = fields.Integer('Jumlah Dilihat', default=0)
    is_featured = fields.Boolean('Berita Unggulan', default=False, tracking=True)
    website_published = fields.Boolean('Dipublikasikan', copy=False, tracking=True, default=False)
    
    @api.depends('name')
    def _compute_slug(self):
        for record in self:
            if record.name:
                record.slug = slugify(record.name)
    
    def _compute_website_url(self):
        for record in self:
            record.website_url = f'/news/{record.slug}'
            
    def increase_view_count(self):
        self.write({'view_count': self.view_count + 1})

    def toggle_published(self):
        self.ensure_one()
        self.website_published = not self.website_published
        return True

    def toggle_featured(self):
        self.ensure_one()
        self.is_featured = not self.is_featured
        return True

class NewsCategory(models.Model):
    _name = 'website.news.category'
    _description = 'News Category'
    _inherit = ['mail.thread']
    
    name = fields.Char('Nama Kategori', required=True, tracking=True)
    description = fields.Text('Deskripsi', tracking=True)
    news_ids = fields.One2many('website.news', 'category_id', string='Berita')
    news_count = fields.Integer('Jumlah Berita', compute='_compute_news_count')
    
    @api.depends('news_ids')
    def _compute_news_count(self):
        for record in self:
            record.news_count = len(record.news_ids) 