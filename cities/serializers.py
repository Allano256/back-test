from rest_framework import serializers
from .models import City, NewCity


class Cityserializer(serializers.ModelSerializer):
    # user=serializers.ReadOnlyField(source='user.username')
    # is_user= serializers.SerializerMethodField()
   

    def get_is_owner(self, obj):
        request=self.context['request']
        return request.user == obj.user


    class Meta:
        model= City
        fields =[
            'id','city_name','country','emoji', 'date','notes','lat','lng'
        ]


class NewCitySerializer(serializers.ModelSerializer):
    def get_is_owner(self, obj):
        request=self.context['request']
        return request.user== obj.user
    

    class Meta:
        model = NewCity
        fields = [
            'id','user', 'city_name','date', 'notes','lat','lng'
        ]





