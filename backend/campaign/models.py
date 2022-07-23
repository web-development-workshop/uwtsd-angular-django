from django.db import models

# Create your models here.


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    campaign_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
