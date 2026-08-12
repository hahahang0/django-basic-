from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Post

@receiver(pre_save,sender=Post)
def normalize_post_title(sender,instance,**kwargs):
    instance.title = instance.title.strip()

@receiver(post_save,sender=Post)
def post_create(sender,instance,created,**kwargs):
    if created:
        print(
            f"New Post Created: {instance.title}"
        )