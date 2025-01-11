import json
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.serializers import serialize
from .models import Product, Category, CustomUser


@receiver(pre_delete, sender=Category)
def save_instance_to_json(sender, instance, **kwargs):
    # Serialize the model instance into JSON
    instance_data = serialize('json', [instance])

    file_name = f"{instance.name}_{instance.pk}.json"

    with open(file_name, 'w') as file:
        file.write(instance_data)


@receiver(pre_delete, sender=Product)
def save_instance_to_json(sender, instance, **kwargs):
    instance_data = serialize('json', [instance])
    file_name = f"{instance.name}_{instance.pk}.json"

    with open(file_name, 'w') as file:
        file.write(instance_data)


@receiver(pre_delete, sender=CustomUser)
def save_instance_to_json(sender, instance, **kwargs):
    instance_data = serialize('json', [instance])
    file_name = f"{instance.name}_{instance.pk}.json"
    with open(file_name, 'w') as file:
        file.write(instance_data)
