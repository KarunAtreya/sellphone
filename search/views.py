
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_CONTAINS,
    LOOKUP_QUERY_EXCLUDE,
    FUNCTIONAL_SUGGESTER_COMPLETION_MATCH,
    FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
    FUNCTIONAL_SUGGESTER_PHRASE_MATCH,
    FUNCTIONAL_SUGGESTER_PHRASE_MATCH,
    FUNCTIONAL_SUGGESTER_TERM_MATCH,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    CompoundSearchFilterBackend,
    MultiMatchSearchFilterBackend,
    FunctionalSuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .documents import PhoneDocument
from .serializers import PhoneDocumentSerializer


class PhoneDocumentView(BaseDocumentViewSet):

    document = PhoneDocument
    serializer_class = PhoneDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
        MultiMatchSearchFilterBackend,
        FunctionalSuggesterFilterBackend,
    ]

    search_fields = (
        'user',
        'brand',
        'model',
        'price',
    )

    multi_match_search_fields = {
        'user': {'boost': 4},
        'brand': {'boost': 4}, 
        'model' : {'boost': 4}, 
        'price':None}

    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'user': {
            'field': 'user.username',
            'fuzziness': 'auto',
            'multi_match_options':'best_fields',


        },
        'brand': {
            'field':'brand',
            'lookups':[
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_CONTAINS,
            ],
            'fuzziness': 'auto',
        },
        'model': {
            'field':'model',
            'lookups':[
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
            ],
            'fuzziness': 'AUTO',
            'multi_match_options':'best_fields',
        },
        'price': {
            'field': 'price',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ]
        },
    }

    ordering = ('_score', 'id', 'price',)
    ordering_fields = {
        'id': 'id',
        'price': 'price',
    }


    functional_suggester_fields = {
         'name_suggest': {
             'field': 'user.username.suggest',
             'suggesters': [
                 FUNCTIONAL_SUGGESTER_COMPLETION_MATCH,
                 FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
             ],
         },
         'brand_suggest': {
             'field': 'brand.suggest',
             'suggesters': [
                 FUNCTIONAL_SUGGESTER_COMPLETION_MATCH,
                 FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
             ],
         },
     }