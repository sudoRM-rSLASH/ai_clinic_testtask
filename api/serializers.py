from rest_framework import serializers
from api.models import Teams, People


class TeamSerializer(serializers.ModelSerializer):
    teammate = serializers.StringRelatedField(many=True)

    class Meta:
        model = Teams
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
