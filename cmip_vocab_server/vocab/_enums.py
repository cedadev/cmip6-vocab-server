from enum import Enum


class CV_Type(Enum):
    ACTIVITY_ID = "activity_id"
    EXPERIMENT_ID = "experiment_id"
    GRID_LABEL = "grid_label"
    FREQUENCY = "frequency"
    INSTITUTION_ID = "institution_id"
    MIP_ERA = "mip_era"
    NOMINAL_RESOLUTION = "nominal_resolution"
    SOURCE_ID = "source_id"
    REALM = "realm"
    SOURCE_TYPE = "source_type"
    SUB_EXPERIMENT_ID = "sub_experiment_id"
    TABLE_ID = "table_id"
    VARIABLE_ID = "variable_id"


class CV_Description(Enum):
    ACTIVITY_ID = "Activity identifier"
    EXPERIMENT_ID = "Short experiment identifier"
    FREQUENCY = "Frequency"
    GRID_LABEL = "Grid identifier"
    INSTITUTION_ID = "Institution identifier"
    MIP_ERA = "MIP Era"
    NOMINAL_RESOLUTION = "Nominal resolution"
    REALM = "Realm"
    SOURCE_ID = "Model identifier"
    SOURCE_TYPE = "Source type"
    SUB_EXPERIMENT_ID = "Sub experiment identifier"
    TABLE_ID = "Table identifier"
    VARIABLE_ID = "Short variable name"
