from rest_framework import serializers
from .models import NewCity


class NewCitySerializer(serializers.ModelSerializer):
    """
    New City Serializer.
    """

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.user

    class Meta:
        model = NewCity
        fields = ["id", "user", "city_name", "date", "notes", "lat", "lng"]

        date = serializers.DateField(format="%Y-%m-%d")
