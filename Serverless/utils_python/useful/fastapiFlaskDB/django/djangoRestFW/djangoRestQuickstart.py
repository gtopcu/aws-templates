
# https://www.django-rest-framework.org/tutorial/quickstart/
# https://www.youtube.com/watch?v=cJveiktaOSQ

# Create the project directory
# mkdir tutorial
# cd tutorial

# # Create a virtual environment to isolate our package dependencies locally
# python3 -m venv env
# source env/bin/activate  # On Windows use `env\Scripts\activate`

# # Install Django and Django REST framework into the virtual environment
# pip install django
# pip install djangorestframework

# # Set up a new project with a single application
# django-admin startproject tutorial .  # Note the trailing '.' character
# cd tutorial
# django-admin startapp quickstart
# cd ..


# Serializers
# from django.contrib.auth.models import Group, User
# from rest_framework import serializers

# class ItemSerializer(serializers.ModelSerializer): # HyperlinkedModelSerializer
#     class Meta:
#         model = User
#         fields = "__all__"
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


# Views
# from django.contrib.auth.models import Group, User
# from rest_framework import permissions, viewsets

# from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

# URLs
# from django.urls import include, path
# from rest_framework import routers

# from tutorial.quickstart import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


# from django.urls import path
# from . import views

# url_patterns = [
#     # path('', views.api_root)
#     path('', views.get_data),
#     path('add/', views.add_item)
# ]