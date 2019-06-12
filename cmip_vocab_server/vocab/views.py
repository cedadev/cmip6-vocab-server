from cmip_vocab_server.vocab.models import Collection, Concept, Vocab
from cmip_vocab_server.vocab.serializers import CollectionsSerializer, \
    ConceptSerializer, VocabSerializer, VocabDetailSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class VocabViewSet(viewsets.ViewSet):
    """
    API endpoint that allows vocabs to be viewed.
    """

    def list(self, request):
        """
        Get the list of vocabs.
        """
        queryset = Vocab.objects.all()
        serializer = VocabSerializer(queryset, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Get the details for an individual vocab
        """
        queryset = Vocab.objects.all()
        vocab = get_object_or_404(queryset, pk=pk)
        serializer = VocabDetailSerializer(vocab, context={'request': request})
        return Response(serializer.data)


class CollectionViewSet(viewsets.ViewSet):
    """
    API endpoint that allows collections to be viewed.
    """

    def list(self, request, vocab):
        """
        Get the list of collections.
        """
        # What we really want is the vocab, which contains a list of
        # collections
        return redirect("/vocabs/" + vocab)

    def retrieve(self, request, vocab, pk=None):
        """
        Get the details for an individual collection
        """
        pk = "{}/{}".format(vocab, pk)
        queryset = Collection.objects.all()
        collection = get_object_or_404(queryset, pk=pk)
        serializer = CollectionsSerializer(
            collection, context={'request': request})
        return Response(serializer.data)


class ConceptViewSet(viewsets.ViewSet):
    """
    API endpoint that allows concepts to be viewed.
    """

    def list(self, request, vocab, collection):
        """
        Get the list of concepts.
        """
        # What we really want is the collection, which contains a list of
        # concepts
        return redirect("/collections/{}/{}".format(vocab, collection))

    def retrieve(self, request, vocab, collection, pk=None):
        """
        Get the details for an individual collection
        """
        pk = "{}/{}/{}".format(vocab, collection, pk)
        queryset = Concept.objects.all()
        concept = get_object_or_404(queryset, pk=pk)
        serializer = ConceptSerializer(concept, context={'request': request})
        return Response(serializer.data)
