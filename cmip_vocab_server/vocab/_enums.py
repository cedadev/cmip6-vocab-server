from enum import Enum


class CV_Type(Enum):
    ACTIVITY_ID = 'activity_id'
    EXPERIMENT_ID = 'experiment_id'
    GRID_LABEL = 'grid_label'
    INSTITUTION_ID = 'institution_id'
    SOURCE_ID = 'source_id'
    TABLE_ID = 'table_id'
    VARIABLE_ID = 'variable_id'


class CV_Description(Enum):
    ACTIVITY_ID = 'Activity identifier'
    EXPERIMENT_ID = 'Short experiment identifier'
    GRID_LABEL = 'Grid identifier'
    INSTITUTION_ID = 'Insitition identifier'
    SOURCE_ID = 'Model identifier'
    TABLE_ID = 'Table identifier'
    VARIABLE_ID = 'Short variable name'
