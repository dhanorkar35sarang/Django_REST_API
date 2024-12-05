from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username'] 

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()  
    users = serializers.SerializerMethodField()  
    created_by = serializers.StringRelatedField()  

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']


    def get_users(self, obj):
        
        return [{"id": user.id, "name": user.username} for user in obj.users.all()]
