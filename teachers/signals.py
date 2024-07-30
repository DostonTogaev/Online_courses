import os
import json
from django.apps import AppConfig
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from teachers.models import Teacher
from config.settings import BASE_DIR


@receiver(post_save, sender=Teacher)
def product_saved(sender, instance, created, **kwargs):
    if created:
        print(f'{instance.name} created!')
        print(kwargs)
    else:
        print('Product updated!')


@receiver(pre_delete, sender=Teacher)
def product_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'teachers/delete_teacher/', f'teacher{instance.id}.json')

    teachers_data = {
        'id': instance.id,
        'name': instance.name,
        'description': instance.description,
        'level': instance.level,

    }

    with open(file_path, mode='w') as file_json:
        json.dump(teachers_data, file_json, indent=4)

    print(f'{instance.name} is deleted')
