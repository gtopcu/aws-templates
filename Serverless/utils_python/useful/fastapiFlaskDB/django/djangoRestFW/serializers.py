
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.Serializer): # ModelSerializer, HyperlinkedModelSerializer
    class Meta:
        model = Item
        fields = "__all__"
#       fields = ('id', 'name', 'price', 'description', 'image')
#       fields = ['url', 'username', 'email', 'groups']

