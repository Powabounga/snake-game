import pygame

class Apple:
    snake = None
    width = 20
    height = 20
    color = 'green'
    x = None
    y = None

    def __init__(self, x, y, snake):
        self.x = x
        self.y = y
        self.snake = snake

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def removeAppleIfEaten(self):
        head = self.snake.parts[len(self.snake.parts) - 1]
        if head[0] == self.x and head[1] == self.y:
            self.snake.addSnakePart()
            return None
        return self
        
