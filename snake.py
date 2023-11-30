import pygame

class Snake:
    speed = 1
    width = 20
    height = 20
    direction = 'right'
    frames = 10

    # x and y of each snake part
    parts = [[], [], []]

    def __init__(self, screen):
        self.reset(screen)

    def draw(self, screen, moving):
        self.frames -= 1

        for i, part in enumerate(self.parts):
            pygame.draw.rect(screen, 'white', pygame.Rect(part[0], part[1], self.width, self.height))

            if moving and self.frames == 0:
                if i == (len(self.parts) - 1):
                    if self.direction == 'right':
                        part[0] += self.width
                    elif self.direction == 'left':
                        part[0] -= self.width
                    elif self.direction == 'up':
                     part[1] -= self.height
                    elif self.direction == 'down':
                        part[1] += self.height
                else:
                    part[0] = self.parts[i + 1][0]
                    part[1] = self.parts[i + 1][1]
            
        if self.frames == 0:
            self.frames = 10

    def changeDirection(self, direction):
        head = self.parts[-1]
        firstSnakePart = self.parts[-2]

        match direction:
            case 'right':
                if firstSnakePart[0] == head[0] + 20 and firstSnakePart[1] == head[1]:
                    return
            case 'left':
                if firstSnakePart[0] == head[0] - 20 and firstSnakePart[1] == head[1]:
                    return
            case 'up':
                if firstSnakePart[0] == head[0] and firstSnakePart[1] == head[1] - 20:
                    return
            case 'down':
                if firstSnakePart[0] == head[0] and firstSnakePart[1] == head[1] + 20:
                    return

        self.direction = direction

    def isSnakeColidingScreen(self, screenWidth, screenHeight):
        head = self.parts[-1]

        if  head[0] >= screenWidth or head[0] < 0 or head[1] >= screenHeight or head[1] < 0:
           return True
        return False


    def isSnakeColidingItself(self):
        head = self.parts[len(self.parts) - 1]
        body = self.parts[0:-1]
        
        for part in body:
            if part[0] == head[0] and part[1] == head[1]:
                return True
            
        return False

    def addSnakePart(self):
        lastPartPosition = self.parts[0]

        self.parts.insert(0, [lastPartPosition[0], lastPartPosition[1]])

    def reset(self, screen):
        self.speed = 1
        self.width = 20
        self.height = 20
        self.direction = 'right'
        self.frames = 10

        # x and y of each snake part
        self.parts = [[], [], []]
        for i in range(3):
            self.parts[i] = [self.width * (i + 1), 20]


