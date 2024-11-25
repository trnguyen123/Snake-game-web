import random

GRID_SIZE = 20  # Kích thước lưới
WIDTH, HEIGHT = 600, 400  # Kích thước màn chơi


class SnakeGame:
    def __init__(self):
        self.snake = [[100, 50], [90, 50], [80, 50]]  # Vị trí rắn
        self.food = self.spawn_food()  # Vị trí thức ăn
        self.direction = 'RIGHT'  # Hướng ban đầu
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        return [
            random.randrange(1, WIDTH // GRID_SIZE) * GRID_SIZE,
            random.randrange(1, HEIGHT // GRID_SIZE) * GRID_SIZE,
        ]

    def change_direction(self, new_direction):
        if new_direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            self.direction = new_direction

    def update(self):
        if self.game_over:
            return

        head = self.snake[0][:]
        if self.direction == 'UP':
            head[1] -= GRID_SIZE
        elif self.direction == 'DOWN':
            head[1] += GRID_SIZE
        elif self.direction == 'LEFT':
            head[0] -= GRID_SIZE
        elif self.direction == 'RIGHT':
            head[0] += GRID_SIZE

        # Kiểm tra va chạm
        if head in self.snake or head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
            self.game_over = True
            return

        self.snake.insert(0, head)
        if head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def get_state(self):
        return {
            "snake": self.snake,
            "food": self.food,
            "score": self.score,
            "game_over": self.game_over,
        }
    
    
