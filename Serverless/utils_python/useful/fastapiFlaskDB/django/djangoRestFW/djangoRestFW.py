
# https://www.django-rest-framework.org/tutorial/quickstart/
# https://www.youtube.com/watch?v=cJveiktaOSQ

# pip install djangorestframework
# pip install markdown       # Markdown support for the browsable API.
# pip install django-filter  # Filtering support

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

# python manage.py runserver
# http://127.0.0.1:8000/

# bash: curl -u admin -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
# Enter host password for user 'admin':
# {
#     "count": 1,
#     "next": null,
#     "previous": null,
#     "results": [
#         {
#             "url": "http://127.0.0.1:8000/users/1/",
#             "username": "admin",
#             "email": "admin@example.com",
#             "groups": []
#         }
#     ]
# }

# settings.py
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
# ]
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }
# urlpatterns = [
#     ...
#     path('api-auth/', include('rest_framework.urls'))
# ]

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




# from django.urls import path, include
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]