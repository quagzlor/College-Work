import pygame  # to make the game
import random  # to randomise ball movement

from pygame.transform import scale

FPS = 60 #Frame rate

#Window Dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

#Paddle Dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_BUFFER = 5 #Distance from screen edge

#Obstruction Dimensions
OBSTRUCT_WIDTH = 4
OBSTRUCT_HEIGHT = 30

#Ball Dimensions
BALL_WIDTH = 10
BALL_HEIGHT = 10

#Speed of paddle and ball
PADDLE_SPEED = 2

BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#Colour codes
WHITE = (255,255,255)
BLACK = (0,0,0)

#Initialise Screen
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

def drawBall(ballxPos,ballyPos): #Draws the Ball
    ball = pygame.Rect(ballxPos,ballyPos,BALL_WIDTH,BALL_HEIGHT)
    pygame.draw.rect(screen,WHITE,ball)

def drawUserPaddle(paddle1yPos): #Paddle to be controlled by us or ML AI
    UserPaddle = pygame.Rect(PADDLE_BUFFER,paddle1yPos,PADDLE_WIDTH,PADDLE_HEIGHT)
    pygame.draw.rect(screen,WHITE,UserPaddle)

def drawAIPaddle(paddle2yPos): #Paddle to be controlled by simple logic AI
    AIPaddle = pygame.Rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH,paddle2yPos,PADDLE_WIDTH,PADDLE_HEIGHT)
    pygame.draw.rect(screen,WHITE,AIPaddle)

def drawObstruct(): #Obstruction
    Obstruct = pygame.Rect(WINDOW_WIDTH/2 - OBSTRUCT_WIDTH, WINDOW_HEIGHT/2 - OBSTRUCT_HEIGHT/2,OBSTRUCT_WIDTH, OBSTRUCT_HEIGHT)
    pygame.draw.rect(screen,WHITE,Obstruct)


def updateBall(HIDDEN_SCORE, paddle1yPos,paddle2yPos,ballxPos,ballyPos,ballXDirection,ballYDirection): #Update ball movement
    #Update x and y movement
    ballxPos = ballxPos + ballXDirection * BALL_X_SPEED
    ballyPos = ballyPos + ballYDirection * BALL_Y_SPEED

    score = 0

    #Checks if ball hit the user paddle
    if (ballxPos <= PADDLE_BUFFER + PADDLE_WIDTH and 
        ballyPos + BALL_HEIGHT >= paddle1yPos and
        ballyPos - BALL_HEIGHT <= paddle1yPos + PADDLE_HEIGHT):
        ballXDirection = 1 #Direction change
        score = HIDDEN_SCORE
        HIDDEN_SCORE = HIDDEN_SCORE - 0.01
    elif(ballxPos <= 0): #Went past the paddle
        ballXDirection = 1
        score = -1
        return [HIDDEN_SCORE,score,paddle1yPos,paddle2yPos,ballxPos,ballyPos,ballXDirection,ballYDirection]

    #Check if it hits AI paddle
    if (ballxPos >= WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH and 
        ballyPos + BALL_HEIGHT >= paddle2yPos and
        ballyPos - BALL_HEIGHT <= paddle2yPos + PADDLE_HEIGHT):
        ballXDirection = -1 #Direction change
        HIDDEN_SCORE = HIDDEN_SCORE + 0.01
    elif(ballxPos >= WINDOW_WIDTH - BALL_WIDTH): #Went past the paddle
        ballXDirection = -1
        score = 2
        HIDDEN_SCORE = 1
        return [HIDDEN_SCORE,score,paddle1yPos,paddle2yPos,ballxPos,ballyPos,ballXDirection,ballYDirection]

    """
    #Check if it hits the obstruction
    if (ballxPos >= WINDOW_WIDTH/2 - OBSTRUCT_WIDTH/2 and 
        ballyPos + BALL_HEIGHT >= WINDOW_HEIGHT/2 + OBSTRUCT_HEIGHT and
        ballyPos - BALL_HEIGHT <= WINDOW_HEIGHT/2 + OBSTRUCT_HEIGHT):
        ballXDirection = -1 #Direction change
    elif(ballxPos <= WINDOW_WIDTH/2 + OBSTRUCT_WIDTH/2 and 
        ballyPos + BALL_HEIGHT >= WINDOW_HEIGHT/2 + OBSTRUCT_HEIGHT and
        ballyPos - BALL_HEIGHT <= WINDOW_HEIGHT/2 + OBSTRUCT_HEIGHT):
        ballXDirection = 1 #Direction change
    """
    if (ballyPos <= 0): #Hits the top of the screen
        ballyPos = 0
        ballYDirection = 1
    elif (ballyPos >= WINDOW_HEIGHT - BALL_HEIGHT): #Hits the bottom of the screen
        ballyPos = WINDOW_HEIGHT - BALL_HEIGHT
        ballYDirection = -1

    return [HIDDEN_SCORE, score,paddle1yPos,paddle2yPos,ballxPos,ballyPos,ballXDirection,ballYDirection]

def UpdatePaddle1(action, paddle1yPos): #Updates user paddle positon. Controlled by us or AI
    #Move up
    if (action[1] == 1):
        paddle1yPos = paddle1yPos - PADDLE_SPEED
    #Move down
    if (action[2] == 1):
        paddle1yPos = paddle1yPos + PADDLE_SPEED

    if (paddle1yPos < 0): #Keep it on screen
        paddle1yPos = 0
    if (paddle1yPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle1yPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    
    return paddle1yPos

def UpdatePaddle2(paddle2yPos, ballyPos,HIDDEN_SCORE): #Updates AI paddle position. Controlled by the location of the ball.
    AI_PADDLE_SPEED = PADDLE_SPEED*(random.randint(8,11)/10)
    #Move paddle up the screen if ball is in upper half of paddle
    if (paddle2yPos + PADDLE_HEIGHT / 2 < ballyPos + BALL_HEIGHT / 2):
        paddle2yPos = paddle2yPos + AI_PADDLE_SPEED
    #Vice-versa
    if (paddle2yPos + PADDLE_HEIGHT / 2 > ballyPos + BALL_HEIGHT /2 ):
        paddle2yPos = paddle2yPos - AI_PADDLE_SPEED

    if (paddle2yPos < 0): #Keep it on screen
        paddle2yPos = 0
    if (paddle2yPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle2yPos = WINDOW_HEIGHT - PADDLE_HEIGHT

    return paddle2yPos

#The game itself
class Pong:
    def __init__(self):
        #Random number for initial direction
        num = random.randint(0,9)

        self.tally = 0 #Score

        #Initial paddle positions
        self.paddle1yPos = WINDOW_HEIGHT/2 - PADDLE_HEIGHT/2
        self.paddle2yPos = WINDOW_HEIGHT/2 - PADDLE_HEIGHT/2

        #Ball direction
        self.ballxDirection = 1
        self.ballyDirection = 1

        #Starting point
        self.ballxPos = WINDOW_WIDTH/2 - BALL_WIDTH/2

        #Randomly decide ball movement
        if(0 < num < 3):
            self.ballxDirection = 1
            self.ballyDirection = 1
        if (3 <= num < 5):
            self.ballxDirection = -1
            self.ballyDirection = 1
        if (5 <= num < 8):
            self.ballxDirection = 1
            self.ballyDirection = -1
        if (8 <= num < 10):
            self.ballxDirection = -1
            self.ballyDirection = -1

        num = random.randint(0,9)

        self.ballyPos = num * (WINDOW_HEIGHT - BALL_HEIGHT) / 9

        #Scaling
        self.scaled_surface = pygame.Surface((84, 84), depth=32)

    def getPresentFrame(self):

        #Calls the event queue for each frame
        pygame.event.pump()

        screen.fill(BLACK) #Black background

        #Draw paddles and obstruction
        drawAIPaddle(self.paddle2yPos)
        drawUserPaddle(self.paddle1yPos)
        #drawObstruct()

        #Draw ball
        drawBall(self.ballxPos,self.ballyPos)

        #Update the window
        pygame.display.flip()

        #Copies pixels from the game to a 3D array, for use in ML
        pygame.transform.scale(pygame.display.get_surface(),(84,84),self.scaled_surface)
        image_data = pygame.surfarray.array2d(self.scaled_surface)

        return image_data

    def getNextFrame(self,action):
        pygame.event.pump()
        score = 0
        screen.fill(BLACK)
        HIDDEN_SCORE = 0 #Discourages repeated use of same actions
        drawObstruct()

        #Update Paddles
        self.paddle1yPos = UpdatePaddle1(action, self.paddle1yPos)
        drawUserPaddle(self.paddle1yPos)

        self.paddle2yPos = UpdatePaddle2(self.paddle2yPos, self.ballyPos,HIDDEN_SCORE)
        drawAIPaddle(self.paddle2yPos)

        #Update variables by changing ball position
        [HIDDEN_SCORE,score,self.paddle1yPos,self.paddle2yPos,self.ballxPos,self.ballyPos,self.ballxDirection,self.ballyDirection] = updateBall(HIDDEN_SCORE,self.paddle1yPos,self.paddle2yPos,self.ballxPos,self.ballyPos,self.ballxDirection,self.ballyDirection)
        
        drawBall(self.ballxPos,self.ballyPos)

        #Get surface data
        pygame.transform.scale(pygame.display.get_surface(), (84, 84), self.scaled_surface)
        image_data = pygame.surfarray.array2d(self.scaled_surface)

        pygame.display.flip()

        self.tally = self.tally + score

        return [score,image_data]

