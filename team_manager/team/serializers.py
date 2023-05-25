from rest_framework import serializers
from .models import User, Place, Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PlaceUserSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ['id', 'name', 'description', 'updated', 'level']

    def get_level(self, place_instance):
        data = Experience.objects.filter(place=place_instance).last()
        return data.level


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1


class UserDetailedSerializer(serializers.ModelSerializer):
    places = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'mobile', 'mail',
                  'position', 'hire_date', 'leave_date', 'updated', 'places']
        depth = 1

    def get_places(self, user_instance):
        data = Place.objects.filter(user=user_instance)
        return [PlaceUserSerializer(place).data for place in data]
