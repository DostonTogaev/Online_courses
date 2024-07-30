import os
import json
from django.apps import AppConfig
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from blog.models import Blog
from config.settings import BASE_DIR


@receiver(post_save, sender=Blog)
def product_saved(sender, instance, created, **kwargs):
    if created:
        print(f'{instance.title} created!')
        print(kwargs)
    else:
        print('Product updated!')


@receiver(pre_delete, sender=Blog)
def product_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'blog/delete_blog/', f'blog{instance.id}.json')

    product_data = {
        'id': instance.id,
        'title': instance.title,
        'Body': instance.Body,

    }

    with open(file_path, mode='w') as file_json:
        json.dump(product_data, file_json, indent=4)

    print(f'{instance.title} is deleted')