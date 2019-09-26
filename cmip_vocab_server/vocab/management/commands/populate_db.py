from cmip_vocab_server.vocab._cvs import get_cv
from cmip_vocab_server.vocab._enums import CV_Description, CV_Type
from cmip_vocab_server.vocab.models import Collection, Concept, Vocab
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def _load_data(self):
        """
        Populate the database from the json files.
        """
        vocab_id = "CMIP6"
        vocab = Vocab(
            id=vocab_id,
            prefLabel="CMIP6",
            definition="Coupled Model Intercomparison Project Phase 6",
        )
        vocab.save()

        for cv_type in CV_Type:
            definition = get_cv_description(cv_type)
            collection_id = "{}/{}".format(vocab_id, cv_type.value)
            collection = Collection(
                id=collection_id, prefLabel=cv_type.value, definition=definition
            )
            collection.save()

            cv = get_cv(cv_type)
            for key in cv:
                concept_id = "{}/{}".format(collection_id, key)
                concept = Concept(
                    id=concept_id,
                    notation=cv[key]["notation"],
                    prefLabel=cv[key]["pref_label"],
                    definition=cv[key]["definition"],
                )
                concept.save()
                collection.members.add(concept)

            vocab.collections.add(collection)

    def handle(self, *args, **options):
        self._load_data()


def get_cv_description(cv_type):
    """
    Get the description of a CV.

    @param cv_type(CV_Type): the CV of interest

    @return a str containing the description of a CV
    """

    if cv_type == CV_Type.ACTIVITY_ID:
        return CV_Description.ACTIVITY_ID.value

    if cv_type == CV_Type.CF_STANDARD_NAME:
        return CV_Description.CF_STANDARD_NAME.value

    if cv_type == CV_Type.DATA_NODE:
        return CV_Description.DATA_NODE.value

    if cv_type == CV_Type.EXPERIMENT_ID:
        return CV_Description.EXPERIMENT_ID.value

    if cv_type == CV_Type.FREQUENCY:
        return CV_Description.FREQUENCY.value

    if cv_type == CV_Type.GRID_LABEL:
        return CV_Description.GRID_LABEL.value

    if cv_type == CV_Type.INSTITUTION_ID:
        return CV_Description.INSTITUTION_ID.value

    if cv_type == CV_Type.MIP_ERA:
        return CV_Description.MIP_ERA.value

    if cv_type == CV_Type.MODEL_COHORT:
        return CV_Description.MODEL_COHORT.value

    if cv_type == CV_Type.NOMINAL_RESOLUTION:
        return CV_Description.NOMINAL_RESOLUTION.value

    if cv_type == CV_Type.PRODUCT:
        return CV_Description.PRODUCT.value

    if cv_type == CV_Type.REALM:
        return CV_Description.REALM.value

    if cv_type == CV_Type.SOURCE_ID:
        return CV_Description.SOURCE_ID.value

    if cv_type == CV_Type.SOURCE_TYPE:
        return CV_Description.SOURCE_TYPE.value

    if cv_type == CV_Type.SUB_EXPERIMENT_ID:
        return CV_Description.SUB_EXPERIMENT_ID.value

    if cv_type == CV_Type.TABLE_ID:
        return CV_Description.TABLE_ID.value

    if cv_type == CV_Type.VARIABLE_ID:
        return CV_Description.VARIABLE_ID.value

    if cv_type == CV_Type.VARIANT_LABEL:
        return CV_Description.VARIANT_LABEL.value

    return ""
