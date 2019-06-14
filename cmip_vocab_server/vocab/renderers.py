from rest_framework import renderers


class JsonLDRenderer(renderers.JSONRenderer):
    media_type = 'application/ld+json'
    format = 'jsonld'

    def __init__(self):
            super().__init__()
