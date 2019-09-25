import json
from os import path

from cmip_vocab_server.settings import CV_DIR
from cmip_vocab_server.vocab._enums import CV_Type
from dreqPy import dreq


def get_cv(cv_type):
    """
    Get a json representation of the CV.

    @param cv_type(CV_Type): the CV of interest

    @return a json object containing details of the CV
    """

    if not isinstance(cv_type, CV_Type):
        raise ValueError('Invalid CV_Type: {}'.format(cv_type))

    file_name = 'CMIP6_{}.json'.format(cv_type.value)
    cv_file = path.join(CV_DIR, file_name)

    # do something special for 'variable'
    if cv_type == CV_Type.VARIABLE_ID:
        cv = _parse_variable()
        return cv

    with open(cv_file) as json_data:
        cv_json = json.load(json_data)

    if cv_type in [CV_Type.ACTIVITY_ID, CV_Type.INSTITUTION_ID,
                   CV_Type.GRID_LABEL]:
        cv = _parse_kv(cv_json, cv_type)

    if cv_type == CV_Type.EXPERIMENT_ID:
        cv = _parse_experiment(cv_json, cv_type, 'experiment')

    if cv_type == CV_Type.SOURCE_ID:
        cv = _parse_experiment(cv_json, cv_type, 'label_extended')

    if cv_type == CV_Type.TABLE_ID:
        cv = _parse_table(cv_json, cv_type)

    return cv


def _parse_kv(cv_json, cv_type):
    """
    Extract key, values from a json file.

    @param cv_json: a json representation of the cv
    @param cv_type(CV_Type): the CV of interest

    @return: a dict of pref_label, description
    """
    cv_json = cv_json[cv_type.value]
    cv = {}
    for key in cv_json:
        cv[key] = {'prefLabel': cv_json[key],
                   'definition': ''}
    return cv


def _parse_experiment(cv_json, cv_type, definition_label):
    """
    Extract key, values from an 'experiment' json file.

    @param cv_json: a json representation of the cv
    @param cv_type(CV_Type): the CV of interest
    @param definition_label(str): the label od the description field

    @return: a dict of pref_label, description
    """
    cv_json = cv_json[cv_type.value]
    cv = {}
    for key in cv_json:
        cv[key] = {'prefLabel': cv_json[key][definition_label],
                   'definition': ''}

    return cv


def _parse_table(cv_json, cv_type):
    """
    Extract key, values from a 'table' json file.

    @param cv_json: a json representation of the cv
    @param cv_type(CV_Type): the CV of interest

    @return: a dict of pref_label, description
    """
    cv_json = cv_json[cv_type.value]
    cv = {}
    for key in cv_json:
        cv[key] = {'prefLabel': '',
                   'definition': ''}

    return cv


def _parse_variable():
    """
    Extract titles and descriptions for the variables.

    @return: a dict of pref_label, description
    """
    # load the data
    dq = dreq.loadDreq()

    # get a list of the variables
    variables = dq.coll['var'].items

    cv = {}
    for v in variables:
        cv[v.label] = {'prefLabel': v.title,
                       'definition': v.description}

    return cv


if __name__ == '__main__':
    print(get_cv(CV_Type.ACTIVITY_ID))

    for cv in CV_Type:
        print(cv.value)
        print(get_cv(cv))

    try:
        print(get_cv('junk'))
    except ValueError:
        pass
