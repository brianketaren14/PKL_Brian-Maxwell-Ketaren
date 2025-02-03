/** @odoo-module **/

import { registry } from '@web/core/registry';
import publicWidget from '@web/legacy/js/public/public_widget';

const KaroMap = publicWidget.Widget.extend({
    selector: '.karo-map',
    
    start: function () {
        return this._super.apply(this, arguments).then(() => {
            this._initMap();
        });
    },
    
    _initMap: function () {
        if (!this.el) return;

        const map = L.map(this.el).setView([3.1067, 98.2643], 13);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        // Tambahkan marker untuk kantor Pemkab Karo
        L.marker([3.1067, 98.2643])
            .addTo(map)
            .bindPopup('Kantor Bupati Karo')
            .openPopup();
    },
});

registry.category('public_widgets').add('KaroMap', KaroMap);

export default KaroMap; 