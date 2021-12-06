from django.contrib.auth.models import User, Group
from rest_framework import serializers
from jobmanagers.models import Company,Job,Category,Location,Tech

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class CompanySerializers(serializers.Serializer):
#     company_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     company_email = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     linkedin_url = serializers.CharField(required=True, allow_blank=False, max_length=100)

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields= '__all__'

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields= '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= '__all__'

class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields= '__all__'

class TechSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tech
        fields= '__all__'