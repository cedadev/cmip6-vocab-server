from django.apps import AppConfig


class VocabConfig(AppConfig):
    name = 'cmip_vocab_server.vocab'

    def ready(self):
        from cmip_vocab_server.vocab._helper import init_concepts
        init_concepts()
