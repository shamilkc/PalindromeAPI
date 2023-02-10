
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    #creating user with a username and password
    if User.objects.filter(username=request.data['username']).exists():
        return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password']
    )
    token = Token.objects.create(user=user)
    return Response({"message": "User created successfully", "token": token.key}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, pk):
    #updating user
    user = User.objects.get(pk=pk)
    user.username = request.data.get('username', user.username)
    user.set_password(request.data.get('password', user.password))
    user.save()
    return Response({"message": "User updated successfully"})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    #deleting user
    User.objects.get(pk=pk).delete()
    return Response({"message": "User deleted successfully"})

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    #login a user and returning the token
    username = request.data['username']
    password = request.data['password']
    
    user = authenticate(username=username, password=password)
    print(user)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


