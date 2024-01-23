odoo.define('product_media_urls.product_media_script', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var QWeb = core.qweb;

    publicWidget.registry.ProductMediaDisplay = publicWidget.Widget.extend({
        selector: '.oe_website_sale',
        events: {
            'click .product_media_image': '_onClickProductMediaImage',
        },

        /**
         * Handles the click event on product media images.
         *
         * @private
         * @param {Event} ev
         */
        _onClickProductMediaImage: function (ev) {
            ev.preventDefault();
            var $target = $(ev.currentTarget);
            var imageUrl = $target.data('image-url');
            var mediaUrl = $target.data('media-url');

            if (imageUrl) {
                this._displayImage(imageUrl);
            } else if (mediaUrl) {
                this._displayMedia(mediaUrl);
            }
        },

        /**
         * Displays the image in a modal or a designated area.
         *
         * @param {string} imageUrl
         */
        _displayImage: function (imageUrl) {
            // Implementation to display the image.
            var $imageModal = $(QWeb.render('product_media_template', {
                src: imageUrl
            }));
            $imageModal.modal('show');
        },

        /**
         * Displays the media in a modal or a designated area.
         *
         * @param {string} mediaUrl
         */
        _displayMedia: function (mediaUrl) {
            // Implementation to display the media.
            var $mediaModal = $(QWeb.render('product_media_template', {
                src: mediaUrl
            }));
            $mediaModal.modal('show');
        },
    });
});