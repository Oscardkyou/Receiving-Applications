from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=Profile)
def add_to_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name='Пользователь')
        instance.user.groups.add(group)
