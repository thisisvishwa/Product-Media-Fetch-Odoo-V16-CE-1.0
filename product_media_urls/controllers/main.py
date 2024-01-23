from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Binary

class ProductMediaController(http.Controller):

    @http.route('/product_media/fetch', type='http', auth="public", website=True)
    def fetch_product_media(self, product_id, **kw):
        ProductTemplate = request.env['product.template']
        product = ProductTemplate.sudo().browse(int(product_id))

        if not product.exists():
            return request.not_found()

        response = {
            'image_url': product.external_image_url,
            'media_url': product.external_media_url,
        }

        return request.make_response(
            headers={'Content-Type': 'application/json'},
            data=json.dumps(response)
        )

    @http.route(['/product_media/image/<int:product_id>'], type='http', auth="public", website=True)
    def product_image(self, product_id, **kw):
        ProductTemplate = request.env['product.template']
        product = ProductTemplate.sudo().browse(int(product_id))

        if not product.exists() or not product.external_image_url:
            return request.not_found()

        return Binary().content_from_url(url=product.external_image_url)

    @http.route(['/product_media/media/<int:product_id>'], type='http', auth="public", website=True)
    def product_media(self, product_id, **kw):
        ProductTemplate = request.env['product.template']
        product = ProductTemplate.sudo().browse(int(product_id))

        if not product.exists() or not product.external_media_url:
            return request.not_found()

        return Binary().content_from_url(url=product.external_media_url)