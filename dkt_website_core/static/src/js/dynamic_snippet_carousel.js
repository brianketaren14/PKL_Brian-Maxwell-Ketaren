/** @odoo-module **/

import { registry } from '@web/core/registry';
import { SnippetCarousel } from '@website/snippets/s_dynamic_snippet/options';
import { DynamicSnippetCarousel } from '@website/snippets/s_dynamic_snippet_carousel/options';

const publicWidget = registry.category('public_widgets');

publicWidget.add('dktDynamicSnippetCarousel', SnippetCarousel.extend({
    selector: '.s_carousel_dyna_news',

    /**
     * @override
     */
    init: function () {
        this._super.apply(this, arguments);
        this.template_key = 'dkt_website_core.dkt_carousel_dyna_template';
        this.controller_url = '/dkt_website_core/dynamic_snippet_news';
    },

    /**
     * @override
     */
    _getSearchDomain: function () {
        const filterBy = this.$target.get(0).dataset.filterOpt || 'latest';
        const numberOfRecords = parseInt(this.$target.get(0).dataset.numberOfRecords) || 3;
        const numberOfColumns = parseInt(this.$target.get(0).dataset.numberOfColumns) || 3;
        
        return {
            filter: filterBy,
            limit: numberOfRecords,
            columns: numberOfColumns
        };
    },
}));

export default publicWidget.registry.dktDynamicSnippetCarousel; 