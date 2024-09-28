from rest_framework import viewsets, status
from .models import JIRAField
from .serializers import FieldSerializer, SiteFieldSerializer
from rest_framework.response import Response
import requests
from .fields import Fields
import json

class JIRAViewSet(viewsets.ModelViewSet):
    queryset = JIRAField.objects.all()
    serializer_class = FieldSerializer


class ExternalApiViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for interacting with an external API using requests.
    """

    def list(self, request):
        # This will handle GET requests to list data from the external API
        url = "laptopsstore"
        fields_data = Fields(url)
        response = fields_data.get_fields()
        
        try:
            if response.status_code == 200:
                data = response.json()
            return Response(data, status=status.HTTP_200_OK)

        except requests.exceptions.HTTPError as http_err:
            return Response({"error": f"HTTP error occurred: {http_err}"}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as err:
            return Response({"error": f"Error occurred: {err}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class MyModelViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for handling POST requests.
    """
    def create(self, request):
        # This will handle POST requests for creating a new instance
        get_name = request.data
        url = get_name.get('site_name', '')
        try:
            fields_data = Fields(url)
            response = fields_data.get_fields()
            serializer = SiteFieldSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            if response:
                field_data = response
                if field_data:
                    self.get_data(field_data)

                return Response(True, status=status.HTTP_201_CREATED)
            else:
                return Response(False, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.HTTPError as http_err:
            return Response({"error": f"HTTP error occurred: {http_err}"}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as err:
            return Response({"error": f"Error occurred: {err}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_data(self, field_data):
        for fields in field_data:
            queryset = JIRAField.objects.filter(field_id=fields.get('id', '')).exists()
            if not queryset:
                f_data = {
                    'name': fields.get('name', ''),
                    'field_id': fields.get('id', ''),
                    'schema_json': str(fields.get('schema', {})),
                    'description': fields.get('description', ''),
                    'field_key': fields.get('key', ''),
                    'stable_id': fields.get('stableId', ''),
                    'is_locked': fields.get('isLocked', False),
                    'searcherKey': fields.get('searcherKey', '')
                }
                
                serializer = FieldSerializer(data=f_data)
                if serializer.is_valid():
                    serializer.save()
                    print(fields.get('id', ''))
                else:
                    print(serializer.errors)
            else:
                continue