from odoo import models, fields
import geoip2.database

class WebsiteVisitor(models.Model):
    _inherit = 'website.visitor'

    country_id = fields.Many2one('res.country', string='Negara')
    region = fields.Char('Daerah')

    def _update_visitor_location(self, ip_address):
        reader = geoip2.database.Reader('path/to/GeoLite2-City.mmdb')
        try:
            response = reader.city(ip_address)
            self.write({
                'country_id': self.env['res.country'].search([('code', '=', response.country.iso_code)]).id,
                'region': response.city.name
            })
        except:
            pass
        finally:
            reader.close() 