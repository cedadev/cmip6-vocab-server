from cmip_vocab_server.vocab._cvs import get_cv
from cmip_vocab_server.vocab._enums import CV_Description, CV_Type
from cmip_vocab_server.vocab.models import Collection, Concept, Vocab


def get_cv_description(cv_type):
    """
    Get the description of a CV.

    @param cv_type(CV_Type): the CV of interest

    @return a str containing the description of a CV
    """

    if cv_type == CV_Type.ACTIVITY_ID:
        return CV_Description.ACTIVITY_ID.value

    if cv_type == CV_Type.EXPERIMENT_ID:
        return CV_Description.EXPERIMENT_ID.value

    if cv_type == CV_Type.GRID_LABEL:
        return CV_Description.GRID_LABEL.value

    if cv_type == CV_Type.INSTITUTION_ID:
        return CV_Description.INSTITUTION_ID.value

    if cv_type == CV_Type.SOURCE_ID:
        return CV_Description.SOURCE_ID.value

    if cv_type == CV_Type.TABLE_ID:
        return CV_Description.TABLE_ID.value

    if cv_type == CV_Type.VARIABLE_ID:
        return CV_Description.VARIABLE_ID.value

    return ''


def get_server_url(request):
    """
    Get the server URL from the request object.

    @param request

    @return a str containing the server URL
    """
    server = '{}://{}'.format(request.scheme, request.get_host())
    return server


def init_concepts():
    """
    If the database is empty them populate it for the json files.
    """
    queryset = Concept.objects.all()
    if len(queryset) > 0:
        return

    vocab_id = 'CMIP6'
    vocab = Vocab(id=vocab_id, prefLabel='CMIP6',
                  definition='Coupled Model Intercomparison Project Phase 6')
    vocab.save()

    for cv_type in CV_Type:
        definition = get_cv_description(cv_type)
        collection_id = "{}/{}".format(vocab_id, cv_type.value)
        collection = Collection(
            id=collection_id, prefLabel=cv_type.value, definition=definition)
        collection.save()

        cv = get_cv(cv_type)
        for label in cv:
            concept_id = "{}/{}".format(collection_id, label)
            concept = Concept(
                id=concept_id, prefLabel=label, definition=cv[label])
            concept.save()
            collection.members.add(concept)

        vocab.collections.add(collection)
