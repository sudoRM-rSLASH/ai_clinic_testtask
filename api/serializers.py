from rest_framework import serializers
from api.models import Teams, People


class TeamSerializer(serializers.ModelSerializer):
    teammate = serializers.StringRelatedField(many=True)

    class Meta:
        model = Teams
        fields = ("id", "name", "teammate")


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ("id", "first_name", "last_name", "email", "team")
