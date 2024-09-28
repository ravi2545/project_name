from django.db import models
import requests

# Create your models here.

class JIRAField(models.Model):
    name = models.CharField(blank=True, null=True)
    field_id = models.CharField(max_length=100, primary_key=True)
    schema_json = models.CharField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    field_key = models.CharField(blank=True, null=True)
    stable_id = models.CharField(max_length=255, blank=True, null=True)
    is_locked = models.BooleanField(default=False)
    searcherKey = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    

class GetsiteFields(models.Model):
    site_name = models.CharField()

    def __str__(self):
        return self.site_name


class CheckStatistics(models.Model):
    model_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()