from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PlayingHistory
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
@csrf_exempt
def save_playing_history(request):
    if request.method == "POST":
        data = json.loads(request.body)  # Lấy dữ liệu từ frontend
        difficulty = data.get("difficulty")
        score = data.get("score")

        # Lưu vào database
        history = PlayingHistory.objects.create(difficulty=difficulty, score=score)

        return JsonResponse({"message": "Lịch sử chơi đã được lưu!", "id": history.id}, status=201)

    return JsonResponse({"error": "Phương thức không được hỗ trợ!"}, status=405)

def get_playing_history(request):
    if request.method == "GET":
        # Sắp xếp lịch sử chơi theo thứ tự thời gian tăng dần
        history = PlayingHistory.objects.all().order_by('played_at')
        data = [
            {
                "difficulty": h.difficulty,
                "score": h.score,
                "played_at": h.played_at.strftime("%Y-%m-%d %H:%M:%S")
            }
            for h in history
        ]
        return JsonResponse(data, safe=False)

    return JsonResponse({"error": "Phương thức không được hỗ trợ!"}, status=405)

