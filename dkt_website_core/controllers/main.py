from odoo import http
from odoo.http import request
from datetime import datetime, time
from pytz import UTC

class WebsiteVisitor(http.Controller):
    @http.route('/website/visitor/stats', type='json', auth="public", website=True)
    def get_visitor_stats(self):
        Website = request.env['website']
        website = Website.get_current_website()
        Visitor = request.env['website.visitor']
        
        # Total pengunjung
        total_visitors = Visitor.search_count([('website_id', '=', website.id)])
        
        # Pengunjung hari ini
        today_start = datetime.combine(datetime.now(), time.min)
        today_visitors = Visitor.search_count([
            ('website_id', '=', website.id),
            ('create_date', '>=', today_start.strftime('%Y-%m-%d %H:%M:%S'))
        ])
        
        # Pengunjung online
        online_visitors = Visitor.search_count([
            ('website_id', '=', website.id),
            ('last_connection_datetime', '>=', datetime.now(UTC).strftime('%Y-%m-%d %H:%M:%S'))
        ])
        
        return {
            'total': total_visitors,
            'today': today_visitors,
            'online': online_visitors
        } 

class WebsiteNews(http.Controller):
    @http.route(['/news', '/news/page/<int:page>'], type='http', auth='public', website=True)
    def news_list(self, page=1, **kwargs):
        News = request.env['website.news'].sudo()
        domain = [('website_published', '=', True)]
        
        # Search
        search = kwargs.get('search')
        if search:
            domain += [('name', 'ilike', search)]
            
        # Category filter
        category_id = kwargs.get('category_id')
        if category_id:
            domain += [('category_id', '=', int(category_id))]
            
        # Pagination
        per_page = 9
        total = News.search_count(domain)
        pager = request.website.pager(
            url='/news',
            total=total,
            page=page,
            step=per_page,
            url_args=kwargs
        )
        
        # Get news
        news_items = News.search(domain, limit=per_page, offset=pager['offset'], order='date_published desc')
        
        # Get categories for filter
        categories = request.env['website.news.category'].sudo().search([])
        
        values = {
            'news_items': news_items,
            'pager': pager,
            'categories': categories,
            'search': search,
            'current_category': category_id and request.env['website.news.category'].sudo().browse(int(category_id)) or False
        }
        return request.render('dkt_website_core.news_list_template', values)
        
    @http.route(['/news/<string:slug>'], type='http', auth='public', website=True)
    def news_detail(self, slug, **kwargs):
        news = request.env['website.news'].sudo().search([('slug', '=', slug), ('website_published', '=', True)], limit=1)
        if not news:
            return request.not_found()
            
        # Increment view count
        news.increase_view_count()
        
        # Get categories
        categories = request.env['website.news.category'].sudo().search([])
        
        # Get recent news
        recent_news = request.env['website.news'].sudo().search([
            ('website_published', '=', True),
        ], limit=5, order='date_published desc')
        
        values = {
            'news': news,
            'categories': categories,
            'recent_news': recent_news
        }
        return request.render('dkt_website_core.news_detail_template', values)

class NewsSnippet(http.Controller):
    @http.route('/news-data', auth="public", type="json", methods=['POST'])
    def news_list_snippet(self, **kwargs):
        # Ambil data berita dari model `website.news`
        news_list = request.env['website.news'].sudo().search(
            [('website_published', '=', True)],
            limit=10,
            order='date_published desc'
        )

        # Format data menjadi list of dictionaries
        news_data = [{
            'name': news.name,
            'thumbnail': news.thumbnail,
            'category': news.category_id.name,
            'teaser': news.teaser,
            'date_published': news.date_published.strftime('%d/%m/%Y') if news.date_published else '',  # Format tanggal
            'view_count': news.view_count,
            'slug': news.slug
        } for news in news_list]

        return news_data
class ServicesSnippet(http.Controller):
    @http.route('/services-data', auth="public", type="json", methods=['POST'])
    def services_list_snippet(self, **kwargs):
        # Ambil data government.service dari model `website.news`
        services_list = request.env['government.service'].sudo().search(
            [('is_active', '=', True)],
            order='sequence desc'
        )
        # Format data menjadi list of dictionaries
        services_data = [{
            'id': service.id,
            'name': service.name,
            'icon': service.icon,
            'description': service.description,
            'url': service.url,
            'name': service.name,
            'icon': service.icon,
            'description': service.description,
            'url': service.url,
            'service_type': service.service_type
        } for service in services_list]

        return services_data

class HeadlineSnippet(http.Controller):

    @http.route('/headline-data', auth="public", type="json", methods=['POST'])
    def headline_snippet(self, **kwargs):
        # Ambil data berita dari model `website.news`
        headline_list = request.env['website.headline'].sudo().search(
            [('is_published', '=', True)],
            order='create_date desc',
            limit=1
        )
        # Format data menjadi list of dictionaries
        headline_data = [{
            'id': headline.id,
            'name': headline.name,
            'headline_image': headline.headline_image,
            'description': headline.description,
        } for headline in headline_list]

        return headline_data