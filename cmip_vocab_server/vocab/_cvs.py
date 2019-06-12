import json
from os import path

from cmip_vocab_server.settings import CV_DIR
from cmip_vocab_server.vocab._enums import CV_Type


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
    cv = cv_json[cv_type.value]
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
        cv[key] = cv_json[key][definition_label]

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
        cv[key] = ''

    return cv


if __name__ == '__main__':
    print(get_cv(CV_Type.ACTIVITY_ID))

    for cv in CV_Type:
        if cv == CV_Type.VARIABLE_ID:
            # currently we do not have a json file for variables
            continue
        print(cv.value)
        print(get_cv(cv))

    try:
        print(get_cv('junk'))
    except ValueError:
        pass
