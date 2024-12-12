from rest_framework import serializers
from .models import  NewCity

class NewCitySerializer(serializers.ModelSerializer):
    """
    This is the serializer for the data recieved on the backend from the front end.
    """
    def get_is_owner(self, obj):
        request=self.context['request']
        return request.user== obj.user
    

    class Meta:
        model = NewCity
        fields = [
            'id','user', 'city_name','date', 'notes','lat','lng'
        ]





