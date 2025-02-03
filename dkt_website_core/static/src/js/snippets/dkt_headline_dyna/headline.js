/** @odoo-module **/

import { jsonrpc } from "@web/core/network/rpc_service";
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.DKTheadline = publicWidget.Widget.extend({
    selector: '.headline_snippet',

    /**
     * @override
     */
    async start() {
        let headlineRow = this.el.querySelector('#headline_row');
        if (headlineRow) {
            try {
                // Panggil endpoint RPC untuk mendapatkan data berita
                const data = await jsonrpc('/headline-data', {});
                let html = '';

                data.forEach(headline => {
                    // Buat tampilan berita
                    html += `
                    <div class="website-headline-background" style="background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.3)), url('/web/image/website.headline/${headline.id}/headline_image')">
                        <div class="row position-relative h-100 w-100 text-light" >
                            <div class="col position-absolute top-0 start-50 translate-middle-x text-center w-80 mt-3">
                                <h2>${headline.name}</h2
                                <p>${headline.description}</p>
                                <a href="#" class="btn btn-primary mt-3">Berita Selengkapnya</a>
                            </div>
                        </div>
                    </div>
                    `;
                });
                headlineRow.innerHTML = html;
            } catch (error) {
                console.error('Error fetching news data:', error);
            }
        }
    }
});

export default publicWidget.registry.DKTheadline;
