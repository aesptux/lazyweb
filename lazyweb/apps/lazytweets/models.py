from django.db import models


class Tweet(models.Model):
    tid = models.BigIntegerField()
    username = models.CharField(max_length=60)
    created_at = models.CharField(max_length=25)
    content = models.CharField(max_length=140)
    url = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username
