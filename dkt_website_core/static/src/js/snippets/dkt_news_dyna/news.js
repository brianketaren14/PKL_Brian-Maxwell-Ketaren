/** @odoo-module **/

import { jsonrpc } from "@web/core/network/rpc_service";
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.DKTnews = publicWidget.Widget.extend({
    selector: '.news_snippet',

    /**
     * @override
     */
    async start() {
        let newsRow = this.el.querySelector('.news-row');
        if (newsRow) {
            try {
                // Panggil endpoint RPC untuk mendapatkan data berita
                const data = await jsonrpc('/news-data', {});
                let html = '';

                data.forEach(news => {
                    // Pastikan tanggal memiliki format yang benar
                    const datePublished = news.date_published ? news.date_published : 'Tidak tersedia';

                    // Pastikan view count tidak undefined atau null
                    const viewCount = news.view_count !== undefined ? news.view_count : 0;

                    // Pastikan thumbnail memiliki URL yang valid
                    const thumbnailSrc = news.thumbnail ? `data:image/png;base64,${news.thumbnail}` : '/path/to/default/image.png';

                    // Buat tampilan berita
                    html +=`
                                <div class="card news-card-snippet h-100">
                                    <img class="card-img-top" alt="${news.name}" src="${thumbnailSrc}" style="height:200px;">
                                    <div class="card-body position-relative">
                                        ${news.category ? `<span class="badge bg-primary mb-2">${news.category}</span>` : ''}
                                        <h5 class="card-title" style="height:3em;">
                                            ${news.name}
                                        </h5>

                                        <p class="card-text" style="overflow-y: auto; height:100px">
                                            ${news.teaser}
                                        </p>
                                        <div>
                                            <div class="text-muted mb-3">
                                                <small>
                                                    <i class="fa fa-calendar me-1"></i>
                                                    ${datePublished}
                                                    <i class="fa fa-eye ms-2 me-1"></i>
                                                    ${viewCount} kali dilihat
                                                </small>
                                            </div>
                                            <a class="btn btn-primary" href="/news/${news.slug}">
                                                Baca Selengkapnya
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>`;
                });
                newsRow.innerHTML = html;
            } catch (error) {
                console.error('Error fetching news data:', error);
            }
        }
    }
});

export default publicWidget.registry.DKTnews;
