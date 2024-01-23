from odoo import models, fields, api
from odoo.exceptions import UserError
import requests

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    external_image_url = fields.Char(string='External Image URL')
    external_media_url = fields.Char(string='External Media URL')

    def fetch_external_media(self):
        for record in self:
            if record.external_image_url:
                try:
                    response = requests.get(record.external_image_url)
                    if response.status_code == 200:
                        record.image_1920 = response.content
                    else:
                        record.message_post(
                            body="Failed to fetch image from URL: %s" % record.external_image_url,
                            subtype="mail.mt_comment"
                        )
                except Exception as e:
                    record.message_post(
                        body="Error fetching image from URL: %s (Error: %s)" % (record.external_image_url, str(e)),
                        subtype="mail.mt_comment"
                    )
            if record.external_media_url:
                # Implement fetching additional media if required
                pass

    @api.model
    def create(self, vals):
        record = super(ProductTemplate, self).create(vals)
        if 'external_image_url' in vals or 'external_media_url' in vals:
            record.fetch_external_media()
        return record

    def write(self, vals):
        result = super(ProductTemplate, self).write(vals)
        if 'external_image_url' in vals or 'external_media_url' in vals:
            self.fetch_external_media()
        return result

    @api.model
    def _cron_fetch_external_media(self):
        products = self.search([('external_image_url', '!=', False)])
        for product in products:
            product.fetch_external_media()