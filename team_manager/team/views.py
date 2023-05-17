from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, PlaceSerializer
from .models import User, Place


def safe_get(model_class, default=None, **kargs):
    try:
        item = model_class.objects.get(**kargs)
        return item
    except ObjectDoesNotExist:
        return default


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user(request, id):
    user = safe_get(User, id=id)
    if not user:
        return Response({'error': 'no User with this id'}, status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if not serializer.is_valid():
        error = {'error': serializer.errors}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateUser(request, id):
    data = request.data
    user = safe_get(User, id=id)
    if not user:
        error = {'errors': 'no User with this id'}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, id):
    user = safe_get(User, id=id)
    if not user:
        return Response({'error': 'no User with this id'}, status.HTTP_400_BAD_REQUEST)
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
        return Response({'error': 'no Place with this id'}, status.HTTP_400_BAD_REQUEST)
    serializer = PlaceSerializer(place, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addPlace(request):
    data = request.data
    serializer = PlaceSerializer(data=data)
    if not serializer.is_valid():
        error = {'error': serializer.errors}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updatePlace(request, id):
    data = request.data
    place = safe_get(Place, id=id)
    if not place:
        error = {'errors': 'no Place with this id'}
        return Response(error, status.HTTP_400_BAD_REQUEST)
    serializer = PlaceSerializer(place, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePlace(request, id):
    place = safe_get(Place, id=id)
    if not place:
        return Response({'error': 'no Place with this id'}, status.HTTP_400_BAD_REQUEST)
    place.delete()
    return Response(f'Place {id} deleted')


