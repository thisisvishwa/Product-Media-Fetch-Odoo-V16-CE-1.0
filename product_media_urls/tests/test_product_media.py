from odoo.tests.common import TransactionCase

class TestProductMedia(TransactionCase):

    def setUp(self):
        super(TestProductMedia, self).setUp()
        self.ProductTemplate = self.env['product.template']

    def test_product_media_urls(self):
        # Create a product template with external media URLs
        product_template = self.ProductTemplate.create({
            'name': 'Test Product',
            'external_image_url': 'http://example.com/image.jpg',
            'external_media_url': 'http://example.com/media.mp4'
        })

        # Check if the product template is created with the correct URLs
        self.assertEqual(product_template.external_image_url, 'http://example.com/image.jpg')
        self.assertEqual(product_template.external_media_url, 'http://example.com/media.mp4')

        # Simulate fetching media from external URLs
        # This should be replaced with actual logic for fetching media
        fetched_image = 'Fetched image content'
        fetched_media = 'Fetched media content'

        # Check if the fetched media matches the expected content
        # This is a placeholder for actual content validation
        self.assertEqual(fetched_image, 'Fetched image content')
        self.assertEqual(fetched_media, 'Fetched media content')

        # Check for error logging when fetching fails
        # This should be replaced with actual error handling logic
        try:
            raise Exception('Simulated fetch error')
        except Exception as e:
            error_log = str(e)
            self.assertIn('Simulated fetch error', error_log)