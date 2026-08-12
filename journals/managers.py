# from fcntl import F_SEAL_SEAL
from django.db import models 

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            is_published=True
        )

    def unpublished(self):
        return self.filter(
            is_published = False
        )
    def recent(self):
        return self.order_by(
            "-created_at"
        )
    def by_author(self,user):
        return self.filter(
            author = user
        )

    def search(self, query):

        return self.filter(
            models.Q(
                title__icontains=query
            )
            |
            models.Q(
                content__icontains=query
            )
        )