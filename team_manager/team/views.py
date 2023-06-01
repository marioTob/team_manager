from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Place, Experience
from .serializers import (UserSerializer, UserDetailedSerializer,
                          PlaceSerializer, ExperienceSerializer)


'''Errors:'''
no_user_err = 'no User with this id'
no_place_err = 'no Place with this id'


def safe_get(model_class, default=None, **kargs):
    try:
        item = model_class.objects.get(**kargs)
        return item
    except ObjectDoesNotExist:
        return default


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserDetailedSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user(request, id):
    user = safe_get(User, id=id)
    if not user:
        return Response({'error': no_user_err}, status.HTTP_400_BAD_REQUEST)
    serializer = UserDetailedSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    user_data = request.data
    serializer = UserSerializer(data=user_data)
    if not serializer.is_valid():
        error = {'error': serializer.errors}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateUser(request, id):
    update_data = request.data
    user = safe_get(User, id=id)
    if not user:
        error = {'errors': no_user_err}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(user, data=update_data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, id):
    user = safe_get(User, id=id)
    if not user:
        return Response({'error': no_user_err}, status.HTTP_400_BAD_REQUEST)
    user.delete()
    return Response(f'User {id} deleted')


@api_view(['GET'])
def places(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def place(request, id):
    place = safe_get(Place, id=id)
    if not place:
        return Response({'error': no_place_err}, status.HTTP_400_BAD_REQUEST)
    serializer = PlaceSerializer(place, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addPlace(request):
    place_data = request.data
    serializer = PlaceSerializer(data=place_data)
    if not serializer.is_valid():
        error = {'error': serializer.errors}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updatePlace(request, id):
    update_data = request.data
    place = safe_get(Place, id=id)
    if not place:
        error = {'errors': no_place_err}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer = PlaceSerializer(place, data=update_data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePlace(request, id):
    place = safe_get(Place, id=id)
    if not place:
        return Response({'error': no_place_err}, status.HTTP_400_BAD_REQUEST)
    place.delete()
    return Response(f'Place {id} deleted')


@api_view(['POST'])
def addExperience(request):
    experiance_data = request.data
    serializer = ExperienceSerializer(data=experiance_data)
    if not serializer.is_valid():
        error = {'error': serializer.errors}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateExperience(request):
    update_data = request.data
    experience = safe_get(
        Experience, None, user=update_data['user'], place=update_data['place'])
    if not experience:
        error = {'errors': 'no Experience with this parameters'}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer = ExperienceSerializer(experience, data=update_data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
