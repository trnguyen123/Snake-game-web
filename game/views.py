from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .game_logic import SnakeGame
from django.http import JsonResponse
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def game_view(request):
    if 'game' not in request.session:
        request.session['game'] = SnakeGame()

    game = request.session['game']

    if request.method == 'POST':
        data = json.loads(request.body)
        direction = data.get('direction')
        if direction:
            game.change_direction(direction)
        game.update()

    return JsonResponse(game.get_state())
