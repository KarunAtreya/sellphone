
from .models import *
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import (
    Document,
    fields,
    Index
)

PHONE_INDEX = Index('phone')

PHONE_INDEX.settings(
    number_of_shards = 1,
    number_of_replicas = 1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball",],
    char_filter=["html_strip",]
)

@PHONE_INDEX.doc_type
class PhoneDocument(Document):
    id = fields.IntegerField(attr='id')

    user = fields.ObjectField(
        attr = 'user_indexing',
        properties = {
            'id': fields.IntegerField(),
            'username': fields.TextField(
                analyzer=html_strip,
                fields ={
                    'raw': fields.TextField(analyzer='keyword', multi=True),
                    'suggest': fields.CompletionField(multi=True),
                }
            ),
        }
    )

    image1 = fields.FileField()

    brand = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword',),
            'suggest': fields.CompletionField(),
        },
        multi=True
    )

    model = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', multi=True),
            'suggest': fields.CompletionField(multi=True),
        },
        multi=True
    )

    price = fields.FloatField()

    class Django(object):
        model = Phone

    




