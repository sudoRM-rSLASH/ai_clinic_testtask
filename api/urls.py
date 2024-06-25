from django.urls import path, include
from .views import (
    TeamAPIView,
    PeopleApiView,
)

urlpatterns = [
    # Urls for Teams
    path('api/teams/', TeamAPIView.as_view(), name='post'),
    path('api/teams/', TeamAPIView.as_view(), name='get'),
    path('api/teams/', TeamAPIView.as_view(), name='put'),
    path('api/teams/', TeamAPIView.as_view(), name='delete'),

    # Urls for People
    path('api/people/', PeopleApiView.as_view(), name='post'),
    path('api/people/', PeopleApiView.as_view(), name='get'),
    path('api/people/', PeopleApiView.as_view(), name='put'),
    path('api/people/', PeopleApiView.as_view(), name='delete'),
]
