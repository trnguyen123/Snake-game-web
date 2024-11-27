from django.db import models

class PlayingHistory(models.Model):
    difficulty = models.CharField(max_length=50)  # Lưu mức độ chơi (Dễ, Trung bình, Khó)
    score = models.IntegerField()                # Lưu điểm số của người chơi
    played_at = models.DateTimeField(auto_now_add=True)  # Lưu thời gian chơi

    def __str__(self):
        return f"{self.difficulty} - {self.score} điểm"
