/** @odoo-module **/

import { registry } from '@web/core/registry';

const publicWidget = registry.category('public_widgets');

publicWidget.add('VisitorCounter', {
    selector: '.visitor-stats',
    
    start() {
        this._updateStats();
        setInterval(() => this._updateStats(), 5 * 60 * 1000);
        return Promise.resolve();
    },

    _updateStats() {
        this.rpc('/website/visitor/stats').then(stats => {
            if (this.el) {
                this.el.querySelector('.total-visitors').textContent = stats.total || 0;
                this.el.querySelector('.today-visitors').textContent = stats.today || 0;
                this.el.querySelector('.online-visitors').textContent = stats.online || 0;
            }
        });
    },
}); 