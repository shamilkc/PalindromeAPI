from django.shortcuts import render

# Create your views here.


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['GET'])
@permission_classes([AllowAny])
def base(request):
    routes = [
            {"user/":{
                        "signup/":"creates user",
                        "login/":"login user",
                        "update/<id>/":"updates user",
                        "delete/<id>/":"deletes user",
                        
                        
                        }
            },


            {"game/":{
                        "start/":"creates a game and returns game ID",
                        "update/<id>/":"takes a character from user and updates in the board",
                        "board/<id>/":"dislplay the board",
                        "list/":"diaplay all game ID it the database",
                        }
            },

            ]
    return Response({"routes":routes})
