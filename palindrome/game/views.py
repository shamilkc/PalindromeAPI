from django.shortcuts import render



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from.models import Game
from random import randint




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_game(request):
    #Initializing empty string and returning game ID
    game = Game.objects.create(board="")
    return Response({"game_id": game.id})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_board(request,pk):
    # Returning string in a game board from the server
    game = Game.objects.get(id=pk)
    return Response({"board": game.board})
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_board(request,pk):
    # logic for updating the string and adding one more random number
    
    game = Game.objects.get(id=pk)
    board = game.board + request.data["char"]# Appends character from the data to the board
    game.save()
    if len(board) != 5:
        game.board = board + str(randint(0, 9))# generates random number Append to boarduntil length reachs 5
        game.save()
        return Response({"board": game.board})
    else:
        
        is_palindrome = board == board[::-1]# checks palindrome
        if is_palindrome:
            return Response({"is_palindrome": True,"board": board})
        else:
            return Response({"is_palindrome": False,"board": board})
    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list(request):
    # List all game IDs created in the system
        games = Game.objects.all()
        game_ids = [game.id for game in games]
        return Response({"game_ids": game_ids})
    





        