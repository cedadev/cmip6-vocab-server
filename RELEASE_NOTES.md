# Release Notes for cmip6-vocab-server

## 25/09/19

skos:notation has been added
The value used for skos:prefLabel is now uesd for skos:notation
The value used for skos:definition is now uesd for skos:prefLabel


## 09/08/19

Update Django version to 2.2.4
Add dreqPy dependency
Add CMIP6 'variables' to the vocab

To add the variables to the database run

```
python manage.py populate_db
```
