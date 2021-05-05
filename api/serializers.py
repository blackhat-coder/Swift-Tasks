from rest_framework import serializers
from tapp.models import TodoModel

class todoserializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('id', 'title', 'body')