from cmip_vocab_server.vocab._helper import get_server_url
from rest_framework import serializers

SKOS = "http://www.w3.org/2004/02/skos/core#"


class VocabSerializer(serializers.BaseSerializer):
    """
    Serialise a list of vocab objects to json-ld.
    """

    def to_representation(self, objs):
        server_uri = get_server_url(self.context['request'])
        vocabs = []
        for obj in objs:
            vocab = {}
            vocab["@id"] = "{}/vocabs/{}".format(server_uri, obj.pk)
            vocab["@type"] = ["{}Collection".format(SKOS)]
            vocab["{}prefLabel".format(SKOS)] = obj.prefLabel
            vocab["{}definition".format(SKOS)] = obj.definition
            vocabs.append(vocab)

        return vocabs


class VocabDetailSerializer(serializers.BaseSerializer):
    """
    Serialise a vocabs object to json-ld.
    """

    def to_representation(self, obj):
        server_uri = get_server_url(self.context['request'])
        collections = []
        for collection in obj.collections.all():
            collections.append({"@id": "{}/collections/{}".format(
                server_uri, collection.pk)})
        vocab = {}
        vocab["@id"] = "{}/vocabs/{}".format(server_uri, obj.pk)
        vocab["@type"] = ["{}Collection".format(SKOS)]
        vocab["{}prefLabel".format(SKOS)] = obj.prefLabel
        vocab["{}definition".format(SKOS)] = obj.definition
        vocab["{}member".format(SKOS)] = collections

        return vocab


class CollectionsSerializer(serializers.BaseSerializer):
    """
    Serialise a collections object to json-ld, include details of associated
    concepts.
    """

    def to_representation(self, obj):
        server_uri = get_server_url(self.context['request'])
        members = []
        for member in obj.members.all():
            members.append({"@id": "{}/concepts/{}".format(
                server_uri, member.pk)})
        collection = {}
        collection["@id"] = "{}/collections/{}".format(server_uri, obj.pk)
        collection["@type"] = ["{}Collection".format(SKOS)]
        collection["{}prefLabel".format(SKOS)] = obj.prefLabel
        collection["{}definition".format(SKOS)] = obj.definition
        collection["{}member".format(SKOS)] = members

        return collection


class ConceptSerializer(serializers.BaseSerializer):
    """
    Serialise a concepts object to json-ld.
    """

    def to_representation(self, obj):
        server_uri = get_server_url(self.context['request'])
        concept = {}
        concept["@id"] = "{}/concepts/{}".format(server_uri, obj.pk)
        concept["@type"] = ["{}Concept".format(SKOS)]
        concept["{}prefLabel".format(SKOS)] = obj.prefLabel
        concept["{}definition".format(SKOS)] = obj.definition

        return concept
