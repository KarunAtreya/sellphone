from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry

@receiver(post_save)
def update_document(sender, **kwargs):
    """Update document on added/changed records.

    Update Phone document index if related fields have been updated
    in the database.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'api':
        if model_name == 'phone':
            instances = instance.api.all()
            for _instance in instances:
                registry.update(_instance)

        if model_name == 'user':
            instances = instance.api.all()
            for _instance in instances:
                registry.update(_instance)


@receiver(post_delete)
def delete_document(sender, **kwargs):
    """Update document on deleted records.

    Updates Phone document from index if related fields
    have been removed from database.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'api':
        if model_name == 'phone':
            instances = instance.api.all()
            for _instance in instances:
                registry.update(_instance)

        if model_name == 'user':
            instances = instance.api.all()
            for _instance in instances:
                registry.update(_instance)
