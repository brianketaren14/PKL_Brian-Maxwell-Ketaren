/** @odoo-module **/

import { registry } from '@web/core/registry';
import { patch } from '@web/core/utils/patch';
import publicWidget from '@web/legacy/js/public/public_widget';
import KaroMap from "./leaflet_map";
import VisitorCounter from "./visitor_counter";

// Pastikan kategori public_widgets sudah ada
const publicWidgets = registry.category('public_widgets');

// Daftarkan widget jika belum terdaftar
if (!publicWidgets.contains('KaroMap')) {
    publicWidgets.add('KaroMap', KaroMap);
}

if (!publicWidgets.contains('VisitorCounter')) {
    publicWidgets.add('VisitorCounter', VisitorCounter);
} 