import os
import json
from django.apps import AppConfig
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from courses.models import Course
from config.settings import BASE_DIR


@receiver(post_save, sender=Course)
def product_saved(sender, instance, created, **kwargs):
    if created:
        print(f'{instance.title} created!')
        print(kwargs)
    else:
        print('Product updated!')


@receiver(pre_delete, sender=Course)
def product_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'courses/delete_course/', f'course{instance.id}.json')

    courses_data = {
        'id': instance.id,
        'title': instance.title,
        'description': instance.description,

    }

    with open(file_path, mode='w') as file_json:
        json.dump(courses_data, file_json, indent=3)

    print(f'{instance.title} is deleted')