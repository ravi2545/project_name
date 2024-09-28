from rest_framework import serializers
from .models import JIRAField, GetsiteFields

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = JIRAField
        fields = ['field_id', 'name', 'schema_json', 'description', 'field_key', 'stable_id', 'is_locked', 'searcherKey']

    name = serializers.CharField(allow_blank=True, required=False)
    schema_json = serializers.CharField(allow_blank=True, required=False)
    description = serializers.CharField(allow_blank=True, required=False)
    field_key = serializers.CharField(allow_blank=True, required=False)
    stable_id = serializers.CharField(allow_blank=True, required=False)
    searcherKey = serializers.CharField(allow_blank=True, required=False)


class SiteFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetsiteFields
        fields = ['site_name']
