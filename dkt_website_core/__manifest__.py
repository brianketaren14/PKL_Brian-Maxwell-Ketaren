{
    'name': 'Website Pemkab Karo',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'summary': 'Website Resmi Pemerintah Kabupaten Karo',
    'description': """
Website Resmi Pemerintah Kabupaten Karo dengan fitur:
- Halaman Depan Responsif dengan Tampilan Modern
- Banner Dinamis & Informatif
- Kalender Event dengan Carousel
- Berita Terkini (3 Kolom dengan Thumbnail)
- Layanan Pemerintahan Terintegrasi
- Peta Wilayah dengan Leaflet Map
- Statistik Pengunjung berdasarkan Wilayah
- Menu Jumbotron Dinamis
    """,
    'author': 'PT. Dota Kero Teknologi',
    'website': 'https://www.dotakaro.com',
    'depends': [
        'base',
        'website',
        'website_event',
        'website_blog',
        'contacts',
        'base_geolocalize',
        'web',
        'portal',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        
        # Backend Views
        'views/banner_views.xml',
        'views/service_views.xml',
        'views/news_views.xml',
        'views/headline_views.xml',
        'views/event/event_views.xml',
        'views/menu_views.xml',

        # Frontend Templates - Assets
        'views/templates/assets.xml',
        
        # Frontend Templates - Layout
        'views/templates/layout/layout.xml',
        
        # Frontend Templates - Components
        'views/templates/components/banner_carousel.xml',
        'views/templates/components/services.xml',
        'views/templates/components/event_section.xml',
        'views/templates/components/news_section.xml',
        'views/templates/components/visitor_stats.xml',
        'views/templates/components/map.xml',
        
        # Frontend Templates - Pages
        'views/templates/pages/home.xml',
        'views/templates/pages/news.xml',
        'views/templates/pages/event/detail.xml',

        # frontend snippets
        'views/snippets/news-snippet.xml',
        'views/snippets/services-snippet.xml',
        'views/snippets/headline-snippet.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # SCSS Components
            '/dkt_website_core/static/src/scss/**/*.scss',
            
            # JavaScript Components
            '/dkt_website_core/static/src/js/leaflet_map.js',
            '/dkt_website_core/static/src/js/visitor_counter.js',
            '/dkt_website_core/static/src/js/snippets/card-slider/card-slider.js',
            '/dkt_website_core/static/src/js/snippets/dkt_news_dyna/news.js',
            '/dkt_website_core/static/src/js/snippets/dkt_news_dyna/news_snippet_slider.js',
            '/dkt_website_core/static/src/js/snippets/dkt_services_dyna/services.js',
            '/dkt_website_core/static/src/js/snippets/dkt_services_dyna/services_snippet_slider.js',
            '/dkt_website_core/static/src/js/snippets/dkt_headline_dyna/headline.js',
        ],
        'web.assets_common': [
            # External Libraries
            'https://unpkg.com/leaflet@1.7.1/dist/leaflet.css',
            'https://unpkg.com/leaflet@1.7.1/dist/leaflet.js',
        ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
    'config': {
        'geoip_enabled': False,
    },
} 