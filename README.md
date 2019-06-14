# cmip6-vocab-server

This is a Django application to serve up the CMIP6 vocabulary as SKOS in a
json-ld representation.

## Installation

It is recommended that you create a python virtual environment to install the
code in.

```
cd /usr/local
python -m venv cmip-vocab-server
source /usr/local/cmip-vocab-server/bin/activate
pip install -U pip
pip install https://github.com/cedadev/cmip6-vocab-server/archive/master.zip
```

In order to populate the applications database a copy of the CMIP6 CV json
files are needed. These should be downloaded from
https://github.com/WCRP-CMIP/CMIP6_CVs/archive/master.zip

Once the application has been installed then generate a `local_sttings.py` file
from `local_sttings.py.ini` and update the contents as required.

Create the database tables
```
python manage.py migrate vocab
python manage.py migrate
```

Populate the database with data from the CMIP6 CV json files
```
python manage.py populate_db
```

Run the server
```
python manage.py runserver
```

## Usage

The application initially gets it content from the CMIP6 json CV files. The
extracted data are stored in a database and then served up via an API. The
content is returned from the application as a SKOS representation in a json-ld
format.

There is a vocabulary that consists of SKOS collections, with each collection
representing a controlled vocabulary. Each collection contains a list of SKOS
concepts, with each concept representing a term in a vocabulary.

Example curls

Show the collections in the vocabulary

```
$ curl http://vocab-test.ceda.ac.uk/vocabs/CMIP6/
{
    "@id": "http://vocab-test.ceda.ac.uk/vocabs/CMIP6/",
    "@type": [
        "http://www.w3.org/2004/02/skos/core#Collection"
    ],
    "http://www.w3.org/2004/02/skos/core#prefLabel": "CMIP6",
    "http://www.w3.org/2004/02/skos/core#definition": "Coupled Model Intercomparison Project Phase 6",
    "http://www.w3.org/2004/02/skos/core#member": [
        {
            "@id": "http://vocab-test.ceda.ac.uk/collections/CMIP6/activity_id/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/collections/CMIP6/experiment_id/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/collections/CMIP6/grid_label/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/collections/CMIP6/institution_id/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/collections/CMIP6/source_id/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/collections/CMIP6/table_id/"
        }
    ]
}
```

As seen above this includes a label and description of the vocab and a list of
collections in the vocab.

Show the concepts in a collection (edited) 

```
$ curl http://vocab-test.ceda.ac.uk/collections/CMIP6/activity_id/
{
    "@id": "http://vocab-test.ceda.ac.uk/collections/CMIP6/activity_id/",
    "@type": [
        "http://www.w3.org/2004/02/skos/core#Collection"
    ],
    "http://www.w3.org/2004/02/skos/core#prefLabel": "activity_id",
    "http://www.w3.org/2004/02/skos/core#definition": "Activity identifier",
    "http://www.w3.org/2004/02/skos/core#member": [
        {
            "@id": "http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/AerChemMIP/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/C4MIP/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/CDRMIP/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/CFMIP/"
        },
        {
            "@id": "http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/CMIP/"
        }, ...
```

Show the concepts in a collection

```
$ curl http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/CORDEX/
{
    "@id": "http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/CORDEX/",
    "@type": [
        "http://www.w3.org/2004/02/skos/core#Concept"
    ],
    "http://www.w3.org/2004/02/skos/core#prefLabel": "CORDEX",
    "http://www.w3.org/2004/02/skos/core#definition": "Coordinated Regional Climate Downscaling Experiment"
}
```

As seen above this includes a label and description of the concept.
For use in a faceted search.  It would be possible to call 
http://vocab-test.ceda.ac.uk/vocabs/CMIP6/ to get a list of values to use as
facets and then by calling the id of each facet in turn i.e.
http://vocab-test.ceda.ac.uk/collections/CMIP6/activity_id/, you could get the
possible values for a facet.

## Content Negotiation

The service will return the data as either `application/ld_json` or
`text/html`, the default is `application/ld_json`.

Content type can be requested via the `Accept` header

```
Accept: application/ld+json
```

or file extension (jsonld or api)

```
http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/CORDEX.jsonld
```

or request parameter (jsonld or api)

```
http://vocab-test.ceda.ac.uk/concepts/CMIP6/activity_id/CORDEX/?format=jsonld
```

Additionally the returned json-ld can be formatted using `indent` in the
`Accept` header

```
Accept: application/ld+json;indent=4
```

## Web Browser

As the application is written using the django rest framework a web interface
is automatically provided.
