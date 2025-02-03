/** @odoo-module **/

import { jsonrpc } from "@web/core/network/rpc_service";
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.DKTservices = publicWidget.Widget.extend({
    selector: '.services_snippet',

    /**
     * @override
     */
    async start() {
        console.log('test')
        let servicesRow = this.el.querySelector('.services-row');
        if (servicesRow) {
            try {
                // Panggil endpoint RPC untuk mendapatkan data berita
                const data = await jsonrpc('/services-data', {});
                let html = '';

                data.forEach(service => {
                    // Buat tampilan service
                    html += `<div class="card service-card-snippet service-card h-100">
                        <div class="card-body d-flex flex-column position-relative text-center">
                            <div class="service-icon mb-3">
                                <img class="img-fluid rounded" style="max-height: 120px; object-fit: cover;" src="/web/image/government.service/${service.id}/icon">
                            </div>
                            <h5 class="card-title">${service.name}</h5>
                            <p class="card-text flex-grow-1">${service.description}</p>
                            <div class="mt-auto">
                                <a class="btn btn-primary" href="${service.url}">
                                    Akses Layanan
                                </a>
                            </div>
                        </div>
                    </div>`;
                });
                servicesRow.innerHTML = html;
            } catch (error) {
                console.error('Error fetching services data:', error);
            }
        }
    }
});

export default publicWidget.registry.DKTservices;
