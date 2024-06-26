from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Teams, People
from .serializers import TeamSerializer, PersonSerializer


# Set of views for Teams
class TeamAPIView(APIView):
    # Creating Team
    # Requires name in form-data
    def post(self, request, *args, **kwargs):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get 1 or All Teams
    # Requires query param: ?pk={team_id} to get 1 team
    def get(self, request, *args, **kwargs):
        if pk := request.GET.get("pk"):
            team = TeamSerializer(get_object_or_404(Teams, pk=pk))
            return Response(team.data, status=status.HTTP_200_OK)
        teams = Teams.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Change Team
    # Requires name in form-data, query param: ?pk={team_id}
    def put(self, request, *args, **kwargs):
        if pk := request.GET.get("pk"):
            team = get_object_or_404(Teams, pk=pk)
            serializer = TeamSerializer(team, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data=[{"Message": "Team ID not received"}],
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Delete Team
    # Requires query param: pk={team_id}
    def delete(self, request, *args, **kwargs):
        if pk := request.GET.get("pk"):
            team = get_object_or_404(Teams, pk=pk)
            team.delete()
            return Response(
                data=[{"Message": f"Team ID {pk} deleted"}], status=status.HTTP_200_OK
            )
        return Response(
            data=[{"Message": "Team ID not received"}],
            status=status.HTTP_400_BAD_REQUEST,
        )


# Set of views for People
class PeopleApiView(APIView):
    # Creating Person
    # Requires first_name, last_name, email, team (only ID) in form-data
    def post(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get 1 or All People
    # Requires query param: ?pk={person_id} to get 1 person
    def get(self, request, *args, **kwargs):
        if pk := request.GET.get("pk"):
            person = PersonSerializer(get_object_or_404(People, pk=pk))
            return Response(person.data, status=status.HTTP_200_OK)
        people = People.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Change Person
    # Requires first_name or/and last_name or/and email and/or team (only ID) in form-data, query param: ?pk={person_id}
    def put(self, request, *args, **kwargs):
        if pk := request.GET.get("pk"):
            person = get_object_or_404(People, pk=pk)
            serializer = PersonSerializer(person, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data=[{"Message": "Person ID not received"}],
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Delete Person
    # Requires query param: pk={person_id}
    def delete(self, request, *args, **kwargs):
        if pk := request.GET.get("pk"):
            person = get_object_or_404(People, pk=pk)
            person.delete()
            return Response(
                data=[{"Message": f"Person ID {pk} deleted"}], status=status.HTTP_200_OK
            )
        return Response(
            data=[{"Message": "Person ID not received"}],
            status=status.HTTP_400_BAD_REQUEST,
        )
