# api/resources.py

from tastypie.resources import ModelResource
from api.models import Credit

class CreditResource(MOdelResource):
    class Meta:
        queryset = Credit.objects.all()
        resource_name = 'credit'
