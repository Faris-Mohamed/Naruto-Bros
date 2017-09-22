#Faris M's Computer Science Side Project #1 (Naruto Bro's)
#Special Thanks to Samuel Gamelin for his help.


#--------------------Modules--------------------#
import random           #Get the random module (for generating random numbers)
import pygame           #Get the pygame module (Used for event loops)
from pygame import *    #Get the shortcuts from pygame (Ex., draw.Rect(...) instead of pygame.draw.Rect(...))


#------------Pygame initialization (Starts pygame)------------#

init() #Initialize all imported pygame modules

clock = time.Clock()    #Creates a clock (Clocks are used to track and control the framerate of a game)

#--------------------Display Aesthetics--------------------#
display.set_caption("Naruto Bro's") #Sets the caption of the display to Naruto Bro's
icon = image.load("HiddenLeafLogo.png")    #Loads the icon of the display

#--------------------Display Information--------------------#

width_of_display,height_of_display = 800,600      #Creating the resolution of my game.
SCREEN = display.set_mode((width_of_display,height_of_display)) #It creates an instance of the pygame.Surface class with given dimensions, and returns that (Essentially a screen that images can be printed onto, filled with colours, and have text printed onto it.

#--------------------Colours--------------------#

black = (0,0,0)                #An arrangement of many variables all assigned with an RGB code, used as colours for generation of blocks, fonts, etc.
white = (255,255,255)
green = (0,255,0)
bright_green = (0,200,0)
orange = (255,140,0)
olive = (128,128,0)
cyan = (0,255,255)
blue = (0,0,255)
coolblue = (53,115,255)
teal = (0,128,128)
silver = (192,192,192)
gray = (128,128,128)
maroon = (128,0,0)
khaki = (240,230,140)
purple = (128,0,128)
yellow = (255,255,0)
bright_yellow = (200,200,0)
navy = (0,0,128)
magenta = (255,0,255)
red = (255,0,0)
bright_red = (200,0,0)


#--------------------Images--------------------#

#Logo
Logo = image.load("JapLogoNaruto.png")

#Players
NarutoImageTemp = image.load("NarutoImage.png")
Naruto = transform.scale(NarutoImageTemp, (75, 75))
NarutoImageLeft= transform.flip(Naruto,True,False)
NarutoImageRight= transform.flip(Naruto,False,False)

SasukeImageTemp = image.load("SasukeImage.png")
Sasuke = transform.scale(SasukeImageTemp, (75, 75))
SasukeLeft=transform.flip(Sasuke,True,False)
SasukeRight=transform.flip(Sasuke,False,False)

#RasenShiruken/Chidori
RasenShirukenImageTemp = image.load("rasenShiruken.png")
RasenShirukenUP = transform.scale(RasenShirukenImageTemp, (23,23))
RasenShirukenDOWN = transform.flip(RasenShirukenUP, True, True)
RasenShirukenLEFT = transform.flip(RasenShirukenUP,True,True)
RasenShirukenRIGHT = transform.rotate(RasenShirukenUP, 270)

ChidoriImageTemp = image.load("Chidori.png")
ChidoriRIGHT = transform.scale(ChidoriImageTemp, (23,23))
ChidoriLEFT= transform.flip(ChidoriRIGHT,True,False)
ChidoriUP =  transform.rotate(ChidoriRIGHT,90)
ChidoriDOWN = ChidoriLEFT= transform.rotate(ChidoriRIGHT,270)

#Backgrounds
introBackground = image.load("introBackground.jpg")
helpScreenBackground = image.load("helpScreenBackground.jpg")
gameBackground = image.load("gameBackground.png")
gameBackground2 = image.load("gameBackground2Final.png")
gameBackground3 = image.load("gameBackground3Final.png")
gameBackground4 = image.load("gameBackground4Final.png")
gameBackground5 = image.load("gameBackground5Final.png")
pauseBackground = image.load("pauseBackground.jpg")
pauseBackground2 = image.load("pauseBackground.jpg")
pauseBackground3= image.load("pauseBackground.jpg")
pauseBackground4 = image.load("pauseBackground.jpg")
pauseBackground5= image.load("pauseBackground.jpg")

#Music note and "no" sign
mutelogo = image.load("mutelogo.png")
not_permitted = image.load("not_permitted.png")

#--------------------Music and Sound Effects--------------------#

mainmenu_music = mixer.Sound("mainmenu_music.wav")  #Load Music
gamemusic = mixer.music.load("gamemusic.wav")
gameOver_music = mixer.Sound("aftercrash.wav")

crash_sound = mixer.Sound("crashsound.wav")         #Load Sound Effects
rasenShirukenSound = mixer.Sound("RasenShiruken.wav")
sasukeChidoriSound= mixer.Sound("SasukeChidori.wav")
blockhit_sound = mixer.Sound("blockhit.wav")
blockhit_sound2 = mixer.Sound("blockhit2.wav")
blockhit_sound3 = mixer.Sound("blockhit3.wav")
blockhit_sound4 = mixer.Sound("blockhit4.wav")
blockhit_sound5 = mixer.Sound("blockhit5.wav")
buttonclick_sound = mixer.Sound("buttonpress.wav")
buttonclick_sound2 = mixer.Sound("buttonpress2.wav")
buttonclick_sound3 = mixer.Sound("buttonpress3.wav")
buttonclick_sound4 = mixer.Sound("buttonpress4.wav")
buttonclick_sound5 = mixer.Sound("buttonpress5.wav")

#--------------------Variables, Constants, and Lists--------------------#

generated = False       #Flag to check if a block was generated
attackShot = False          #Flag to check if a attack was shot
mainmenumusicON = False         #Flag to check if the main menu music is on
mute = False                #Flag to check if mute is toggled


DOWN = 0            #Constants used to determine the type of blocks and attacks
UP = 1
RIGHT = 2
LEFT = 3

FPS = 60   #Constant used for frame per seconds

blockList = []       #All the blocks, attacks, sounds, colours, and backgrounds maintained in lists used for muting, backgrounds, block generation and collisions
attackList = []
blockhit_soundlist = [blockhit_sound, blockhit_sound2, blockhit_sound3, blockhit_sound4, blockhit_sound5]
buttonclick_soundlist = [buttonclick_sound, buttonclick_sound2, buttonclick_sound3, buttonclick_sound4, buttonclick_sound5]
allSoundsAndMusicList = [mainmenu_music, gameOver_music, crash_sound, rasenShirukenSound, blockhit_sound, blockhit_sound2, blockhit_sound3, blockhit_sound4, blockhit_sound5, buttonclick_sound, buttonclick_sound2, buttonclick_sound3, buttonclick_sound4, buttonclick_sound5]
gameBackgroundList = [gameBackground, gameBackground2, gameBackground3, gameBackground4, gameBackground5]
pauseBackgroundList = [pauseBackground,pauseBackground2,pauseBackground3,pauseBackground4,pauseBackground5]
listOfBlockColours = [white,red,bright_red,orange,coolblue,cyan,blue,yellow,bright_yellow,green,bright_green,magenta,silver,gray,maroon,olive,purple,teal,navy,khaki]

#--------------------Classes--------------------#

class Player:                               #A class for the player

    def __init__(self, x, y, w, h):         #Special function that is used to initialize the players' attributes (i.e. give them starting values)

        self.x = x          #x position
        self.y = y          #y position
        self.width = w      #width
        self.height = h     #height
        self.spdX = 0     #x spd
        self.spdY = 0     #y spd

    c=random.randint(0,1)

    if c==0:

        def draw(self):                                 #Function that draws/prints the player on the screen
                SCREEN.blit(Naruto, (self.x, self.y))  #Prints the player (an image) onto the screen at given coordinates

        def handleMovementAndKeys(self):  # Function that handles key input and movement from the player

            global paused  # Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
            global mute
            global attackShot
            global attacksFired
            global player
            global Naruto

            for event in pygame.event.get():  # Retrieves all events currently in the queue in the form of a loop

                if event.type == QUIT:  # If the player wants to quit;
                    quit()  # Quit from the game

                elif event.type == KEYDOWN:  # If a key gets pressed down;

                    if event.key == K_p:  # If it is the p key;
                        paused = True  # Set the pause flag to true
                        pause()  # Call the pause function

                    elif event.key == K_LEFT:  # Or else and if it is the Left key;
                        Naruto=NarutoImageLeft
                        if minimum_x:  # If the player reached the left part of the screen;
                            self.spdX = 0  # Stop the player along the X axis
                        else:  # If the player is not at the border of the left part of the screen;
                            self.spdX = -5  # Add -5 to the players' x spd


                    elif event.key == K_RIGHT:  # Or else and if it is the Right key;
                        Naruto=NarutoImageRight
                        if maximum_x:  # If the player reached the right part of the screen;
                            self.spdX = 0  # Stop the player along the X axis
                        else:  # If the player is not at the border of the right part of the screen;
                            self.spdX = 5  # Add 5 to the players' x spd

                    elif event.key == K_DOWN:  # Or else and if it is the Down key;
                        if MAX_Y:  # If the player reached the bottom part of the screen;
                            self.spdY = 0  # Stop the player along the Y axis
                        else:  # If the player is not at the border of the bottom part of the screen;
                            self.spdY = 5  # Add 5 to the players' y spd

                    elif event.key == K_UP:  # Or else and if it is the Down key;
                        if MIN_Y:  # If the player reached the top part of the screen;
                            self.spdY = 0  # Stop the player along the Y axis
                        else:  # If the player is not at the border of the top part of the screen;
                            self.spdY = -5  # Add -5 to the players' y spd

                    elif event.key == K_a:  # Or else and if it is the a key;
                        if not attackShot:  # If attackShot is False;
                            attackList.append(attack(player.x + 5, player.y + 5, 15, 15, -5, RasenShirukenLEFT,LEFT))  # Add a attack going to the left
                            rasenShirukenSound.play()  # Play the gunshot sound
                            attackShot = True  # Flag attackShot as True
                            attacksFired += 1  # Add 1 to the attacksFired count

                    elif event.key == K_d:  # Or else and if it is the d key;
                        if not attackShot:  # If attackShot is False;
                            attackList.append(attack(player.x + 5, player.y + 5, 15, 15, 5, RasenShirukenRIGHT,RIGHT))  # Add a attack going to the right
                            rasenShirukenSound.play()  # Play the gunshot sound
                            attackShot = True  # Flag attackShot as True
                            attacksFired += 1  # Add 1 to the attacksFired count

                    elif event.key == K_s:  # Or else and if it is the s key;
                        if not attackShot:  # If attackShot is False;
                            attackList.append(attack(player.x + 5, player.y + 5, 15,15, 5, RasenShirukenDOWN,DOWN))  # Add a attack going to down
                            rasenShirukenSound.play()  # Play the gunshot sound
                            attackShot = True  # Flag attackShot as True
                            attacksFired += 1  # Add 1 to the attacksFired count

                    elif event.key == K_w:  # Or else and if it is the w key;
                        if not attackShot:  # If attackShot is False;
                            attackList.append(attack(player.x + 5, player.y + 5, 15, 15, -5, RasenShirukenUP,UP))  # Add a attack going to up
                            rasenShirukenSound.play()  # Play the gunshot sound
                            attackShot = True  # Flag attackShot as True
                            attacksFired += 1  # Add 1 to the attacksFired count

                    elif event.key == K_m:  # Or else and if it is the m key;
                        if mute:  # If mute is flagged (sounds and music are muted);
                            mute = False  # Set mute to false
                        else:  # If mute is not flagged (sounds and music are not muted);
                            mute = True  # Set mute to true
                elif event.type == KEYUP:  # If a key gets released;
                    if event.key == K_DOWN or event.key == K_UP:  # If it is either the down or up keys;
                        self.spdY = 0  # Set the Y spd to 0
                    elif event.key == K_LEFT or event.key == K_RIGHT:  # Or else and if it is either the left or right keys;
                        self.spdX = 0  # Set the Y spd to 0

            self.x += self.spdX   #Add the X spd to the players' x position
            self.y += self.spdY   #Add the Y spd to the players' y position


    else:

        def handleMovementAndKeys(self):  # Function that handles key input and movement from the player

            global paused  # Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
            global mute
            global attackShot
            global attacksFired
            global player
            global Sasuke

            for event in pygame.event.get():  # Retrieves all events currently in the queue in the form of a loop

                if event.type == QUIT:  # If the player wants to quit;
                    quit()  # Quit from the game

                elif event.type == KEYDOWN:  # If a key gets pressed down;

                    if event.key == K_p:  # If it is the p key;
                        paused = True  # Set the pause flag to true
                        pause()  # Call the pause function

                    elif event.key == K_LEFT:  # Or else and if it is the Left key;
                        Sasuke=SasukeLeft
                        if minimum_x:  # If the player reached the left part of the screen;
                            self.spdX = 0  # Stop the player along the X axis
                        else:  # If the player is not at the border of the left part of the screen;
                            self.spdX = -5  # Add -5 to the players' x spd


                    elif event.key == K_RIGHT:  # Or else and if it is the Right key;
                        Sasuke = SasukeRight
                        if maximum_x:  # If the player reached the right part of the screen;
                            self.spdX = 0  # Stop the player along the X axis
                        else:  # If the player is not at the border of the right part of the screen;
                            self.spdX = 5  # Add 5 to the players' x spd



                    elif event.key == K_DOWN:  # Or else and if it is the Down key;
                        if MAX_Y:  # If the player reached the bottom part of the screen;
                            self.spdY = 0  # Stop the player along the Y axis
                        else:  # If the player is not at the border of the bottom part of the screen;
                            self.spdY = 5  # Add 5 to the players' y spd

                    elif event.key == K_UP:  # Or else and if it is the Down key;
                        if MIN_Y:  # If the player reached the top part of the screen;
                            self.spdY = 0  # Stop the player along the Y axis
                        else:  # If the player is not at the border of the top part of the screen;
                            self.spdY = -5  # Add -5 to the players' y spd

                    elif event.key == K_a:  # Or else and if it is the a key;
                        if not attackShot:  # If attackShot is False;
                            attackList.append(attack(player.x + 5, player.y + 5, 15, 15, -5, ChidoriLEFT,LEFT))  # Add a attack going to the left
                            sasukeChidoriSound.play()  # Play the gunshot sound
                            attackShot = True  # Flag attackShot as True
                            attacksFired += 1  # Add 1 to the attacksFired count

                    elif event.key == K_d:  # Or else and if it is the d key;
                        if not attackShot:  # If attackShot is False;
                            attackList.append(attack(player.x + 5, player.y + 5, 15, 15, 5, ChidoriRIGHT,RIGHT))  # Add a attack going to the right
                            sasukeChidoriSound.play()  # Play the gunshot sound
                            attackShot = True  # Flag attackShot as True
                            attacksFired += 1  # Add 1 to the attacksFired count

                    elif event.key == K_s:  # Or else and if it is the s key;
                        if not attackShot:  # If attackShot is False;
                            attackList.append(attack(player.x + 5, player.y + 5, 15, 15, 5, ChidoriDOWN,DOWN))  # Add a attack going to down
                            sasukeChidoriSound.play()  # Play the gunshot sound
                            attackShot = True  # Flag attackShot as True
                            attacksFired += 1  # Add 1 to the attacksFired count

                    elif event.key == K_w:  # Or else and if it is the w key;
                        if not attackShot:  # If attackShot is False;
                            attackList.append(attack(player.x + 5, player.y + 5, 15, 15, -5, ChidoriUP,UP))  # Add a attack going to up
                            sasukeChidoriSound.play()  # Play the gunshot sound
                            attackShot = True  # Flag attackShot as True
                            attacksFired += 1  # Add 1 to the attacksFired count

                    elif event.key == K_m:  # Or else and if it is the m key;
                        if mute:  # If mute is flagged (sounds and music are muted);
                            mute = False  # Set mute to false
                        else:  # If mute is not flagged (sounds and music are not muted);
                            mute = True  # Set mute to true

                elif event.type == KEYUP:  # If a key gets released;
                    if event.key == K_DOWN or event.key == K_UP:  # If it is either the down or up keys;
                        self.spdY = 0  # Set the Y spd to 0
                    elif event.key == K_LEFT or event.key == K_RIGHT:  # Or else and if it is either the left or right keys;
                        self.spdX = 0  # Set the Y spd to 0

            self.x += self.spdX   #Add the X spd to the players' x position
            self.y += self.spdY   #Add the Y spd to the players' y position


        def draw(self):                                 #Function that draws/prints the player on the screen
            SCREEN.blit(Sasuke, (self.x, self.y))  # Prints the player (an image) onto the screen at given coordinates


    def checkBorders(self):                 #Function that stops the player from going over the screen border

        global minimum_x #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
        global maximum_x
        global MIN_Y
        global MAX_Y

        minimum_x = False   #Reset all the border flags
        maximum_x = False
        MIN_Y = False
        MAX_Y = False

        if self.x > width_of_display - self.width - 5.3:       #If the user reaches the right part of the display;
            self.spdX = 0                                     #Stop the player along the X axis
            maximum_x = True                                        #Flag maximum_x

        if self.x < 5.3:                                    #If the user reaches the left part of the display;
            self.spdX = 0                                     #Stop the player along the X axis
            minimum_x = True                                        #Flag minimum_x

        if self.y > height_of_display - self.height - 5.3:     #If the user reaches the bottom part of the display;
            self.spdY = 0                                     #Stop the player along the Y axis
            MAX_Y = True                                        #Flag MAX_Y

        if self.y < 5.3:                                    #If the user reaches the top part of the display;
            self.spdY = 0                                     #Stop the player along the Y axis
            MIN_Y = True                                        #Flag MIN_Y

    def handleCollisions(self):             #Function that handles collisions between the player and the blocks

        global blockList #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope

        for block in blockList:     #For each block in the blocklist;

            if block.x <= self.x + self.width and block.x + block.width >= self.x and block.y <= self.y + self.width and block.y + block.height >= self.y:
                crash()     #Check if the players' coordinates and the blocks'

    def checkLevel(self):

        global score #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
        global level
        global leveladded
        global changingSurface
        global gamechange
        global player
        global blockList
        global attackList
        global attackShot
        global message

        if score == 500:        #If the player reaches a score of 500;
            win()                   #Call the win function

        if score > 99 and score%100 == 0 and not leveladded:        #If the score is over 99, divisible by 100 and a level is not being currently added;
            level += 1                  #Add 1 to the level
            leveladded = True           #Flag that a level was added
            message = False             #Flag that a message needs to be displayed on the screen

            changingSurface.blit(gameBackgroundList[level-1], (0,0))    #Set the background to a specific picture within the gameBackgroundList (according to the level)
            changingSurface.set_alpha(0)                                #Set the transparency of the background to 0
            gamechange = 0                                              #Reset the transparency variable to 0
            Largefont = font.SysFont("helvetica", 80)                                     #Set up a variable called LargeFont used for large text to be displayed
            TextSurf, TextRect = renderText('Level ' + str(level), Largefont, white)   #Use the renderText function to render the text to be displayed
            TextRect.center = ((width_of_display/2), (height_of_display/2))                   #Set the center of the text rectangle as the center of the screen
            changingSurface.blit(TextSurf, TextRect)                                    #Print the message on the screen

            player.x = width_of_display/2            #Reset the players' x and y coordinatesto the center of the screen
            player.y = height_of_display/2
            player.spdX = 0                       #Set the players' X and Y spds to 0 (essentially stop the player)
            player.spdY = 0
            blockList = []                          #Reset the blockList
            blockList.append(Block(random.randrange(0,width_of_display), -600, 20 + level * 5, 20 + level * 5, level+3, random.choice(listOfBlockColours), DOWN)) #Add a block to the blockList that is going down
            attackList = []         #Reset the attackList
            attackShot = False      #Flag that a attack is not shot

        if score > 100 and score%100 != 0:      #If the score is greater than 100 and the score is not divisble by 100;
            leveladded = False                      #Reset the leveladded flag
            if not message:                         #If a message is displayed on the screen;
                changingSurface.blit(gameBackgroundList[level-1], (0,0))    #Reset the background to a specific picture within the gameBackgroundList (according to the level)
                changingSurface.set_alpha(0)                                #Set the transparency of the background to 0
                gamechange = 0                                              #Reset the transparency variable to 0
                message = True                                              #Reset the message flag to say the the message is done being displayed

#------------------------------------------------------------------------------#

class Block:                            #A class for the blocks

    def __init__(self, x, y, w, h, s, c, st):         #Special function that is used to initialize the blocks' attributes (i.e. give them starting values)

        self.x = x                #x position
        self.y = y                #y position
        self.width = w            #width
        self.height = h           #height
        self.spd = s            #spd
        self.colour = c           #colour
        self.sort = st            #sort/type

    def draw(self):                                 #Function that draws/prints the player on the screen

        draw.rect(SCREEN, self.colour, [self.x, self.y, self.width, self.height]) #Draws the block (a coloured square) onto the screen at given coordinates

    def handleMovement(self):       #Function that handles movement of the blocks

        global score #Globals (allows) the variable to be changed globally, across the game in between functions, instead of locally inside functions as a scope

        if self.sort == 0:                                  #If the block type is 0 (Block going down);
            self.y += self.spd                                #Add the blocks' spd to its y coordinate
            if self.y > height_of_display:                             #If the block goes past the bottom part of the screen;
                self.y = self.height * - 1                              #Reset the blocks' y position right above the top of the screen
                self.x = random.randrange(0,width_of_display-self.width)              #Reset the players' x position to a random value between 0 and the width of the screen minus its width
                self.colour = random.choice(listOfBlockColours)
                score += 1                                              #Add 1 to the score

        elif self.sort == 1:                                #Or else and if the block type is 1 (Block going up);
            if score >= 15:                                     #If the score is greater than or equal to 15;
                self.y += self.spd                                #Add the blocks' spd to its y coordinate
                if self.y < 0 - self.height:                             #If the block goes past the top part of the screen;
                    self.y = height_of_display + self.height                   #Reset the blocks' y position right under the bottom of the screen
                    self.x = random.randrange(0,width_of_display-self.width)              #Reset the players' x position to a random value between 0 and the width of the screen minus its width
                    self.colour = random.choice(listOfBlockColours)
                    score += 1                                              #Add 1 to the score

        elif self.sort == 2:                                #Or else and if the block type is 2 (Block going to the right);
            if score >= 30:                                     #If the score is greater than or equal to 30;
                self.x += self.spd                                #Add the blocks' spd to its x coordinate
                if self.x > width_of_display:                             #If the block goes past the right part of the screen;
                    self.x = self.height * -1                               #Reset the blocks' x position right behind the left part of the screen
                    self.y = random.randrange(0,height_of_display-self.height)             #Reset the players' y position to a random value between 0 and the height of the screen minus its height
                    self.colour = random.choice(listOfBlockColours)
                    score += 1                                              #Add 1 to the score

        elif self.sort == 3:                                #Or else and if the block type is 3 (Block going to the left);
            if score >= 45:                                     #If the score is greater than or equal to 45;
                self.x += self.spd                                #Add the blocks' spd to its x coordinate
                if self.x < 0 - self.width:                            #If the block goes past the left part of the screen;
                    self.x = width_of_display + self.width                     #Reset the blocks' x position right behind the right part of the screen
                    self.y = random.randrange(0,height_of_display-self.height)             #Reset the players' y position to a random value between 0 and the height of the screen minus its height
                    self.colour = random.choice(listOfBlockColours)
                    score += 1                                              #Add 1 to the score

    def generate():       #Function that handles the generation of blocks

        global blockList #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
        global generated
        global score
        global level

        if score > 45 and score%15 == 0 and not generated:      #If the score is greater than 45,is divisble by 15, and a block was not generated;

            randomsort = random.randint(0,3)                #Get a random number between 0 and 3 (including 0 and 3)

            if randomsort == 0:       #If the random number is 0;
                blockList.append(Block(random.randrange(0,800-20 + level * 5), random.randrange(0,300) * -1, 20 + level * 5, 20 + level * 5, level+3, random.choice(listOfBlockColours), DOWN)) #Add a block to the blockList that is going down
                generated = True        #Flag that a block was generated

            elif randomsort == 1:      #Or else and if the random number is 1;
                blockList.append(Block(random.randrange(0,width_of_display-(20 + level * 5)), random.randrange(height_of_display, height_of_display + 300), 20 + level * 5, 20 + level * 5, level*-1-3, random.choice(listOfBlockColours), UP)) #Add a block to the blockList that is going up
                generated = True        #Flag that a block was generated

            elif randomsort == 2:      #Or else and if the random number is 2;
                blockList.append(Block(random.randrange(30,300) * -1, random.randrange(0,height_of_display-(20 + level * 5)), 20 + level * 5, 20 + level * 5, level+3, random.choice(listOfBlockColours), RIGHT)) #Add a block to the blockList that is going right
                generated = True        #Flag that a block was generated

            elif randomsort == 3:      #Or else and if the random number is 3;
                blockList.append(Block(random.randrange(width_of_display, width_of_display + 300), random.randrange(0,height_of_display-(20 + level * 5)), 20 + level * 5, 20 + level * 5, level*-1-3, random.choice(listOfBlockColours), LEFT)) #Add a block to the blockList that is going left
                generated = True        #Flag that a block was generated

        elif score > 45 and score%15 != 0:  #Or else and if the score is greater than 45 and the score is divisble by 15;
            generated = False        #Reset the generated flag

#------------------------------------------------------------------------------#

class attack:                            #A class for the attack

    def __init__(self, x, y, w, h, s, img, st):         #Special function that is used to initialize the blocks' attributes (i.e. give them starting values)

        self.x = x              #x position
        self.y = y              #y position
        self.width = w          #width
        self.height = h         #height
        self.spd = s          #spd
        self.image = img        #image
        self.sort = st          #sort/type

    def draw(self):                                 #Function that draws/prints the player on the screen

        SCREEN.blit(self.image, (self.x, self.y))         #Prints the player (an image) onto the screen at given coordinates

    def handleMovement(self):       #Function that handles movement of the attack

        if self.sort == 0:            #If the attack type is 0 (attack going down);
            self.y += self.spd           #Add the attacks' spd to its y coordinate

        elif self.sort == 1:          #Or else and if the attack type is 1 (attack going up);
            self.y += self.spd           #Add the attacks' spd to its y coordinate

        elif self.sort == 2:          #Or else and if the attack type is 2 (attack going right);
            self.x += self.spd           #Add the attacks' spd to its x coordinate

        elif self.sort == 3:          #Or else and if the attack type is 3 (attack going left);
            self.x += self.spd           #Add the attacks' spd to its x coordinate

    def handleCollisions(self):             #Function that handles collisions between the attack and the blocks

        global score #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
        global attackList
        global blockList
        global attackShot
        global attacksHit

        for block in blockList:     #For each block in the blocklist;

            for attack in range(len(attackList)): #For each attack in the range of attackList;

                if block.x <= self.x + self.width and block.x + block.width >= self.x and block.y <= self.y + self.height and block.y + block.height >= self.y:
                                            #If the attack collides with the block;
                    attackShot = False          #Reset the attackShot flag
                    del attackList[attack]      #Delete the attack from the list

                    score += 1                  #Add 1 to the score
                    attacksHit += 1             #Add 1 to the attacksHit variable (variable that keeps track of how many attacks hit blocks

                    if block.sort == 0:                             #If the block type is 0 (Block going down);
                        random.choice(blockhit_soundlist).play()        #Play a random block hit sound effect
                        block.x = random.randrange(0, width_of_display-self.width)    #Reset the players' x position to a random value between 0 and the width of the screen minus its width
                        block.y = self.height * - 1                     #Reset the blocks' y position right above the top of the screen
                        block.colour = random.choice(listOfBlockColours)

                    elif block.sort == 1:                           #Or else and if the block type is 1 (Block going up);
                        random.choice(blockhit_soundlist).play()        #Play a random block hit sound effect
                        block.x = random.randrange(0, width_of_display-self.width)    #Reset the players' x position to a random value between 0 and the width of the screen minus its width
                        block.y = height_of_display + self.height          #Reset the blocks' y position right under the bottom of the screen
                        block.colour = random.choice(listOfBlockColours)

                    elif block.sort == 2:                           #Or else and if the block type is 2 (Block going to the right);
                        random.choice(blockhit_soundlist).play()        #Play a random block hit sound effect
                        block.y = random.randrange(0, height_of_display-self.height)   #Reset the blocks' y position to a random value between 0 and the height of the screen minus its height
                        block.x = self.width * -1                       #Reset the blocks' x position right behind the left part of the screen
                        block.colour = random.choice(listOfBlockColours)

                    elif block.sort == 3:                           #Or else and if the block type is 3 (Block going to the left);
                        random.choice(blockhit_soundlist).play()        #Play a random block hit sound effect
                        block.y = random.randrange(0, height_of_display-self.height)   #Reset the players' y position to a random value between 0 and the height of the screen minus its height
                        block.x = width_of_display + self.width            #Reset the blocks' x position right behind the right part of the screen
                        block.colour = random.choice(listOfBlockColours)

                elif self.x > width_of_display:    #Or else and if the attack goes past the bottom part of the screen;
                    del attackList[attack]          #Delete the attack from the list
                    attackShot = False              #Reset the attackShot flag

                elif self.x < 0:                #Or else and if the attack goes past the top part of the screen;
                    del attackList[attack]          #Delete the attack from the list
                    attackShot = False              #Reset the attackShot flag

                elif self.y > height_of_display:   #Or else and if the attack goes past the right part of the screen;
                    del attackList[attack]          #Delete the attack from the list
                    attackShot = False              #Reset the attackShot flag

                elif self.y < 0:                #Or else and if the attack goes past the left part of the screen;
                    del attackList[attack]          #Delete the attack from the list
                    attackShot = False              #Reset the attackShot flag





#----------------------------------Functions-----------------------------------#

def info():    #A function to diaplay basic information on the screen while the player is playing the game

    InfoFont = font.SysFont("helvetica", 25)            #Setup an font to use to display the information

    SCREEN.blit(mutelogo, (width_of_display-35, 5))       #Print the music note in the top-right corner of the screen

    if mute:                                            #Checks if mute is flagged;

        SCREEN.blit(not_permitted, (width_of_display-32, 5))          #If it is print the "no" sign on top of the music note in the top-right corner of the screen

    scoretext = InfoFont.render('Score: ' + str(score), True, white)#Render all the different information such as score, how to pause, how to mute, level, and time survivied
    pausetext = InfoFont.render('Pause: P', True, white)
    musictext = InfoFont.render('Music/Sounds: M', True, white)
    leveltext = InfoFont.render('Level: ' + str(level), True, white)
    timetext = InfoFont.render('Time Survived: ' + str("%.0f"%time), True, white)

    SCREEN.blit(scoretext, (5,0))           #Prints all (except time survived) information under the top border of the screen
    SCREEN.blit(pausetext, (125,0))
    SCREEN.blit(musictext, (225,0))
    SCREEN.blit(leveltext, (415,0))

    if time < 9.5:                #This checks to see the length of the text of time survived and automatically adjusts to adapt perfectly in the bottom right corner of the screen
        SCREEN.blit(timetext, (650,height_of_display-25))
    elif time < 99.5:
        SCREEN.blit(timetext, (640,height_of_display-25))
    elif time < 999.5:
        SCREEN.blit(timetext, (630,height_of_display-25))

def renderText(text, font, colour):    #A function that takes in 3 parameters; text, font, and colour, then renders the text and returns the Surface and the Surfaces' rectangle

    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def button(message, x, y, w, h, ac, ic, action):   #Function that creates buttons

    mouse = pygame.mouse.get_pos()          #Gets the position of the mouse as a tuple
    click = pygame.mouse.get_pressed()      #Checks if any buttons on the mouse are pressed as a tuple

    if x + w + 25 > mouse[0] > x - 25 and y + h > mouse[1] > y:  #If the mouse hovers over the button a rectangle and two circles at each end of that rectangle are drawn with an 'active colour'

        draw.rect(SCREEN, ac, (x, y, w, h))
        draw.circle(SCREEN, ac, (x+5,y+25), 25)
        draw.circle(SCREEN, ac, (x+100,y+25), 25)

        if click[0] == 1:          #If the 'left button on the mouse' is clicked while the mouse is over the button, a sound effect plays and the action (function) is called
            random.choice(buttonclick_soundlist).play()
            action()

    else:                     #When the mouse is not over the button a rectangle and two circles at each end of that rectangle are drawn with an 'inactive colour'
        draw.rect(SCREEN, ic, (x, y, w, h))
        draw.circle(SCREEN, ic, (x+5,y+25), 25)
        draw.circle(SCREEN, ic, (x+100,y+25), 25)

    buttonFont = font.SysFont("helvetica", 20)                      #Setup a font
    TextSurf, TextRect = renderText(message, buttonFont, black)    #Render text, get its surface and rectangle through the renderText function
    TextRect.center = ((x+(w/2)), (y+(h/2)))                        #Set the center of the Texts' rectangle as the center of the button
    SCREEN.blit(TextSurf, TextRect)                                 #Print the text at the center of the button

def unpause():

    global paused         #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
    global gamechange

    mixer.music.unpause()       #Unpause the game music

    paused = False          #Reset the pause flag
    gamechange = 0          #Reset the transparency variable
    mouse.set_visible(0)    #Make the mouse invisible

def pause():

    global player         #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
    global allSoundsAndMusicList
    global mute

    mixer.music.pause()     #Pauses the game music

    mouse.set_visible(1)    #Makes the mouse visible

    changingSurface = Surface((width_of_display,height_of_display))   #Creates a surface
    changingSurface.blit(pauseBackgroundList[level-1], (0,0))   #Prints a picture from the pauseBackgroundList that corresponds with the level on that screen
    changingSurface.set_alpha(0)                                #Makes it completely transparent
    change = 0                                                  #Variable that will be used to change the transparency of the background

    while paused:                               #While pause is True;

        if change < 255:        #If the transparency variable is less than 255 (Note that when change is equal to 255 the background is completely opaque, and no changes occur whatsoever);
            change += 4         #Add 4 to the transparency variable
        changingSurface.set_alpha(change)        #The backgrounds' transparency is changed with the new transparency value
        SCREEN.blit(changingSurface,(0,0))       #The background is printed onto the screen

        SCREEN.blit(mutelogo, (width_of_display-35, 5))       #Print the music note in the top-right corner of the screen

        if mute:                                            #Checks if mute is flagged;

            SCREEN.blit(not_permitted, (width_of_display-32, 5))          #If it is print the "no" sign on top of the music note in the top-right corner of the screen

        for event in pygame.event.get(): #Retrieves all events currently in the queue in the form of a loop
            if event.type == QUIT: #If the player wants to quit;
                quit()      #Quit the game

            elif event.type == KEYDOWN:     #If a key gets pressed down;

                if event.key == K_p:    #If it is the p key;
                    unpause()        #Call the unpause function

                elif event.key == K_m:  #Or else and if it is the m key
                    if mute:           #If mute is True;
                        mute = False        #Reset the mute flag
                    else:              #If mute is False;
                        mute = True         #Flag that mute is True

        largeText = font.SysFont("helvetica",80)                        #Setup a large text font
        TextSurf, TextRect = renderText("Paused", largeText, white)    #Render text, get its surface and rectangle through the renderText function
        TextRect.center = ((width_of_display/2), (height_of_display/2))       #Set the center of the Texts' rectangle as the center of the screen
        SCREEN.blit(TextSurf, TextRect)                                 #Print the text at the center of the screen

        button("Continue!", 150, 500, 100, 50, green, bright_green, unpause)      #Create a continue button
        button("Main Menu", 350, 500, 100, 50, yellow, bright_yellow, main_menu)  #Create a Main Menu button
        button("Quit!", 550, 500, 100, 50, red, bright_red, quit)                 #Create a Quit button

        player.spdX = 0         #Reset the players' x spd to 0
        player.spdY = 0         #Reset the players' x spd to 0

        if mute:                           #Checks if mute is flagged/True;
            for sound in allSoundsAndMusicList: #For every sound and music in the allSoundsAndMusicList;
                sound.set_volume(0)                 #Mute them

        else:                              #Checks if mute is False;
            for sound in allSoundsAndMusicList:     #For every sound and music in the allSoundsAndMusicList;
                sound.set_volume(1)                     #Unmute/play them at 100% volume

        display.flip() #Updates the display with new information
        clock.tick(FPS) #Caps the framerate at 60 frames per second

def crash():

    global attackShot #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
    global allSoundsAndMusicList
    global mute

    mixer.music.stop()      #Stop the game music

    attackShot = False      #Reset the attackShot flag

    crash_sound.play()      #Play the crash sound
    gameOver_music.play()   #Play the gameOver music

    mouse.set_visible(1)    #Make the mouse visible

    changingSurface = Surface((width_of_display,height_of_display))   #Creates a surface
    changingSurface.blit(introBackground, (0,0))                #Prints the introBackground picture on that surface
    changingSurface.set_alpha(0)                                #Makes it completely transparent
    change = 0                                                  #Variable that will be used to change the transparency of the background

    crash = True                    #Flag that crash is True

    while crash:                                        #While crash is True;

        if change < 255: #If the transparency variable is less than 255 (Note that when change is equal to 255 the background is completely opaque, and no changes occur whatsoever);
            change += 4                   #Add 4 to the transparency variable
        changingSurface.set_alpha(change)        #The backgrounds' transparency is changed with the new transparency value
        SCREEN.blit(changingSurface,(0,0))       #The background is printed onto the screen

        LargeFont = font.SysFont("helvetica", 80)       #Setup a large font
        SmallFont = font.SysFont("helvetica", 20)       #Setup a small font

        crashText, crashTextRect = renderText("You Crashed!", LargeFont, white)    #Render a crash message with the renderText function
        crashTextRect.center = ((width_of_display/2), (height_of_display/2))              #Set the center of the crash text rectangle as the center of the screen
        SCREEN.blit(crashText, crashTextRect)                                       #Print the crash text at the center of the screen

        scoreText, scoreTextRect = renderText(("You had a score of "+str(score)+", reached level "+str(level)+", and survived for "+str("%.0f"% time)+" seconds!"), SmallFont, white)                                      #Render a score message with the renderText function
        scoreTextRect.center = ((width_of_display/2), ((height_of_display/2) + 45))       #Set the center of the score text rectangle right under the crash message
        SCREEN.blit(scoreText, scoreTextRect)                                       #Print the score text right under the crash message

        shotsFiredText, shotsFiredRect = renderText("Shots Fired: "+str(attacksFired), SmallFont, white)   #Render a shots fired message with the renderText function
        shotsFiredRect.center = ((width_of_display/2), ((height_of_display/2) + 65))                   #Set the center of the shots fired text rectangle right under the score message
        SCREEN.blit(shotsFiredText, shotsFiredRect)                                                         #Print the shots fired text right under the score message

        shotsHitText, shotsHitRect = renderText("Shots Hit: "+str(attacksHit), SmallFont, white)   #Render a shots hit message with the renderText function
        shotsHitRect.center = ((width_of_display/2), ((height_of_display/2) + 85))                        #Set the center of the shots hit text rectangle right under the shots fired message
        SCREEN.blit(shotsHitText, shotsHitRect)                                                     #Print the shots hit text right under the shots fired message

        if attacksFired > 0:                            #If attacksFired is greater than 0;
            accuracy = (attacksHit/attacksFired)*100                                        #Setup an accuracy variable that calculates the percentage of attacks that hit blocks
            accuracyText, accuracyTextRect = renderText("Accuracy: "+str("%.0f"%accuracy)+"%", SmallFont, white)   #Render an accuracy message with the renderText function
            accuracyTextRect.center = ((width_of_display/2), ((height_of_display/2) + 105))       #Set the center of the accuray text rectangle right under the shots hit message
            SCREEN.blit(accuracyText, accuracyTextRect)                                     #Print the accuracy text right under the shots hit message

        for event in pygame.event.get(): #Retrieves all events currently in the queue in the form of a loop

            if event.type == QUIT:      #If the user wants to quit
                quit()                      #Quit the game

            elif event.type == KEYDOWN:    #Or else and if a key gets pressed down

                if event.key == K_m:        #If it is the m key;
                    if mute:                    #If mute is True;
                        mute = False                #Reset the mute flag
                    else:                       #Or else if mute is False;
                        mute = True                 #Flag that mute is True

        button("Play Again", 150, 500, 100, 50, green, bright_green, game)          #Create a play again button
        button("Main Menu", 350, 500, 100, 50, yellow, bright_yellow, main_menu)    #Create a main menu button
        button("Quit", 550, 500, 100, 50, red, bright_red, quit)                    #Create a quit button

        SCREEN.blit(mutelogo, (width_of_display-35, 5))                               #Print the music note in the top right corner of the screen

        if mute:                                            #If mute is flagged;
            for sound in allSoundsAndMusicList:                 #For every sound in allSoundsAndMusicList;
                sound.set_volume(0)                                 #Mute the sounds
            SCREEN.blit(not_permitted, (width_of_display-32, 5))          #Print the "no" sign over the mutelogo in the top right corner of the screen

        else:                                               #Or else if mute is False/not flagged
            for sound in allSoundsAndMusicList:                 #For every sound in allSoundsAndMusicList;
                sound.set_volume(1)                                 #Set the volume of the sounds to 100%

        display.flip() #Updates the display with new information
        clock.tick(FPS) #Caps the framerate at 60 frames per second

def win():

    global attackShot #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
    global allSoundsAndMusicList
    global mute

    mixer.music.stop()          #Stop the game music

    attackShot = False          #Reset the attackShot flag

    gameOver_music.play()       #Play the game over music

    mouse.set_visible(1)        #Make the mouse visible

    changingSurface = Surface((width_of_display,height_of_display))   #Creates a surface
    changingSurface.blit(introBackground, (0,0))                #Prints the introBackground picture on that surface
    changingSurface.set_alpha(0)                                #Makes it completely transparent
    change = 0                                                  #Variable that will be used to change the transparency of the background

    done = True                                                #Flag that win is True

    while done:                                                #While done is True

        if change < 255: #If the transparency variable is less than 255 (Note that when change is equal to 255 the background is completely opaque, and no changes occur whatsoever);
            change += 4                   #Add 4 to the transparency variable
        changingSurface.set_alpha(change)        #The backgrounds' transparency is changed with the new transparency value
        SCREEN.blit(changingSurface,(0,0))       #The background is printed onto the screen

        LargeFont = font.SysFont("helvetica", 80)   #Setup a large font
        SmallFont = font.SysFont("helvetica", 20)   #Setup a small font

        winText, winTextRect = renderText("You Have Won The Game!", LargeFont, white)       #Render a win message with the renderText function
        winTextRect.center = ((width_of_display/2), (height_of_display/2))                    #Set the center of the win text rectangle as the center of the screen
        SCREEN.blit(winText, winTextRect)                                               #Print the win text at the center of the screen

        scoreText, scoreTextRect = renderText(("You had a score of "+str(score)+", reached level "+str(level)+", and survived for "+str("%.0f"% time)+" seconds!"), SmallFont, white)                                      #Render a score message with the renderText function
        scoreTextRect.center = ((width_of_display/2), ((height_of_display/2) + 45))       #Set the center of the score text rectangle right under the crash message
        SCREEN.blit(scoreText, scoreTextRect)                                       #Print the score text right under the crash message

        shotsFiredText, shotsFiredRect = renderText("Shots Fired: "+str(attacksFired), SmallFont, white)   #Render a shots fired message with the renderText function
        shotsFiredRect.center = ((width_of_display/2), ((height_of_display/2) + 65))                   #Set the center of the shots fired text rectangle right under the score message
        SCREEN.blit(shotsFiredText, shotsFiredRect)                                                         #Print the shots fired text right under the score message

        shotsHitText, shotsHitRect = renderText("Shots Hit: "+str(attacksHit), SmallFont, white)   #Render a shots hit message with the renderText function
        shotsHitRect.center = ((width_of_display/2), ((height_of_display/2) + 85))                        #Set the center of the shots hit text rectangle right under the shots fired message
        SCREEN.blit(shotsHitText, shotsHitRect)                                                     #Print the shots hit text right under the shots fired message

        if attacksFired > 0:                            #If attacksFired is greater than 0;
            accuracy = (attacksHit/attacksFired)*100                                        #Setup an accuracy variable that calculates the percentage of attacks that hit blocks
            accuracyText, accuracyTextRect = renderText("Accuracy: "+str("%.0f"%accuracy)+"%", SmallFont, white)   #Render an accuracy message with the renderText function
            accuracyTextRect.center = ((width_of_display/2), ((height_of_display/2) + 105))       #Set the center of the accuray text rectangle right under the shots hit message
            SCREEN.blit(accuracyText, accuracyTextRect)                                     #Print the accuracy text right under the shots hit message

        for event in pygame.event.get(): #Retrieves all events currently in the queue in the form of a loop

            if event.type == QUIT:      #If the user wants to quit
                quit()                      #Quit the game

            elif event.type == KEYDOWN:    #Or else and if a key gets pressed down

                if event.key == K_m:        #If it is the m key;
                    if mute:                    #If mute is True;
                        mute = False                #Reset the mute flag
                    else:                       #Or else if mute is False;
                        mute = True                 #Flag that mute is True

        button("Play Again", 150, 500, 100, 50, green, bright_green, game)          #Create a play again button
        button("Main Menu", 350, 500, 100, 50, yellow, bright_yellow, main_menu)    #Create a main menu button
        button("Quit", 550, 500, 100, 50, red, bright_red, quit)                    #Create a quit button

        SCREEN.blit(mutelogo, (width_of_display-35, 5))                               #Print the music note in the top right corner of the screen

        if mute:                                            #If mute is flagged;
            for sound in allSoundsAndMusicList:                 #For every sound in allSoundsAndMusicList;
                sound.set_volume(0)                                 #Mute the sounds
            SCREEN.blit(not_permitted, (width_of_display-32, 5))          #Print the "no" sign over the mutelogo in the top right corner of the screen

        else:                                               #Or else if mute is False/not flagged
            for sound in allSoundsAndMusicList:                 #For every sound in allSoundsAndMusicList;
                sound.set_volume(1)                                 #Set the volume of the sounds to 100%

        display.flip() #Updates the display with new information
        clock.tick(FPS) #Caps the framerate at 60 frames per second


def main_menu():

    global mute #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
    global mainmenumusicON
    global allSoundsAndMusicList

    if not mainmenumusicON:             #If mainmenumusicON is not flagged/false;
        mainmenu_music.play(-1)             #Play the music in an infinite loop

    gameOver_music.stop()               #Stop the gameOver music

    changingSurface = Surface((width_of_display,height_of_display))   #Creates a surface
    changingSurface.blit(introBackground, (0,0))                #Prints the introBackground picture on that surface
    changingSurface.set_alpha(0)                                #Makes it completely transparent
    change = 0                                                  #Variable that will be used to change the transparency of the background

    menu = True                 #Flag that menu is True

    while menu:                                         #While menu is True;

        if change < 255: #If the transparency variable is less than 255 (Note that when change is equal to 255 the background is completely opaque, and no changes occur whatsoever);
            change += 4                   #Add 4 to the transparency variable
        changingSurface.set_alpha(change)        #The backgrounds' transparency is changed with the new transparency value
        SCREEN.blit(changingSurface,(0,0))       #The background is printed onto the screen

        for event in pygame.event.get(): #Retrieves all events currently in the queue in the form of a loop

            if event.type == QUIT:      #If the user wants to quit
                quit()                      #Quit the game

            elif event.type == KEYDOWN:    #Or else and if a key gets pressed down

                if event.key == K_m:        #If it is the m key;
                    if mute:                    #If mute is True;
                        mute = False                #Reset the mute flag
                    else:                       #Or else if mute is False;
                        mute = True                 #Flag that mute is True

        SmallFont = font.SysFont("helvetica", 20)                                                       #Setup a small font
        CopyrightText, CopyrightTextRect = renderText("Copyright FM Games 2017", SmallFont, white)     #Render a copyright message with the renderText function
        CopyrightTextRect = (5, (height_of_display - 25))                                        #Set the coordinates of the copyright rectangle at the bottom left corner of the screen
        SCREEN.blit(CopyrightText, CopyrightTextRect)                                                   #Print the copyright message at the bottom left corner of the screen

        LogoRect = Logo.get_rect()                                  #Get the rectangle of the logo picture
        LogoRect.center = ((width_of_display/2), (height_of_display/2))   #Set the rectangle of the logo as the center of the screen
        SCREEN.blit(Logo, LogoRect)                                 #Print the logo in the middle of the screen

        button("Begin",150,450,100,50,green,bright_green,game)              #Create a start button
        button("Controls",350,450,100,50,yellow,bright_yellow,help_screen)      #Create a help button
        button("Leave Game",550,450,100,50,red,bright_red,quit)                   #Create a quit button

        SCREEN.blit(mutelogo, (width_of_display-35, 5))                               #Print the music note in the top right corner of the screen

        if mute:                                            #If mute is flagged;
            for sound in allSoundsAndMusicList:                 #For every sound in allSoundsAndMusicList;
                sound.set_volume(0)                                 #Mute the sounds
            SCREEN.blit(not_permitted, (width_of_display-32, 5))          #Print the "no" sign over the mutelogo in the top right corner of the screen

        else:                                               #Or else if mute is False/not flagged
            for sound in allSoundsAndMusicList:                 #For every sound in allSoundsAndMusicList;
                sound.set_volume(1)                                 #Set the volume of the sounds to 100%

        display.flip() #Updates the display with new information
        clock.tick(FPS) #Caps the framerate at 60 frames per second
def help_screen():

    global mute      #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
    global allSoundsAndMusicList
    global mainmenumusicON

    mainmenumusicON = True      #Flag that main menu music is on

    changingSurface = Surface((width_of_display,height_of_display))   #Creates a surface
    changingSurface.blit(helpScreenBackground, (0,0))                #Prints the introBackground picture on that surface
    changingSurface.set_alpha(0)                                #Makes it completely transparent
    change = 0                                                  #Variable that will be used to change the transparency of the background

    while help_screen:          #While help_screen is True;

        if change < 255: #If the transparency variable is less than 255 (Note that when change is equal to 255 the background is completely opaque, and no changes occur whatsoever);
            change += 4                   #Add 4 to the transparency variable
        changingSurface.set_alpha(change)        #The backgrounds' transparency is changed with the new transparency value
        SCREEN.blit(changingSurface,(0,0))       #The background is printed onto the screen

        for event in pygame.event.get(): #Retrieves all events currently in the queue in the form of a loop

            if event.type == QUIT:      #If the user wants to quit
                quit()                      #Quit the game

            elif event.type == KEYDOWN:    #Or else and if a key gets pressed down

                if event.key == K_m:        #If it is the m key;
                    if mute:                    #If mute is True;
                        mute = False                #Reset the mute flag
                    else:                       #Or else if mute is False;
                        mute = True                 #Flag that mute is True

        SmallFont = font.SysFont("helvetica", 20)                                                       #Setup a small font
        CopyrightText, CopyrightTextRect = renderText("Copyright FM Games 2017", SmallFont, white)     #Render a copyright message with the renderText function
        CopyrightTextRect = (5, (height_of_display - 25))                                        #Set the coordinates of the copyright rectangle at the bottom left corner of the screen
        SCREEN.blit(CopyrightText, CopyrightTextRect)                                                   #Print the copyright message at the bottom left corner of the screen

        button("Back",200,500,100,50,yellow,bright_yellow,main_menu)                                    #Create a main menu button
        button("Quit!",500,500,100,50,red,bright_red,quit)                                              #Create a quit button

        SCREEN.blit(mutelogo, (width_of_display-35, 5))                               #Print the music note in the top right corner of the screen

        if mute:                                            #If mute is flagged;
            for sound in allSoundsAndMusicList:                 #For every sound in allSoundsAndMusicList;
                sound.set_volume(0)                                 #Mute the sounds
            SCREEN.blit(not_permitted, (width_of_display-32, 5))          #Print the "no" sign over the mutelogo in the top right corner of the screen

        else:                                               #Or else if mute is False/not flagged
            for sound in allSoundsAndMusicList:                 #For every sound in allSoundsAndMusicList;
                sound.set_volume(1)                                 #Set the volume of the sounds to 100%

        display.flip() #Updates the display with new information
        clock.tick(FPS) #Caps the framerate at 60 frames per second

def game():

    global blockList  #Globals (allows) the variables to be changed globally, across the game in between functions, instead of locally inside of functions as a scope
    global attackList
    global allSoundsAndMusicList
    global mainmenumusicON
    global score
    global attacksFired
    global attacksHit
    global time
    global level
    global leveladded
    global player
    global gamechange
    global changingSurface

    mixer.music.play(-1)        #Plays the game music in an infinite loop
    mainmenu_music.stop()       #Stops the music coming from the main_menu
    gameOver_music.stop()       #Stops the gameOver music from when a player crashes or wins (this is effective when a player quickly plays again after crashing or winning)

    mouse.set_visible(0)        #Makes the mouse invisible during gameplay

    blockList = []              #Resets the blocklist and attacklist for a new game
    attackList = []

    score = 0                 #Resets all important game related variables
    level = 1
    time = 0
    attacksFired = 0
    attacksHit = 0

    player = Player(width_of_display/2, height_of_display/2, 75, 75)            #Creates a Player named player using the 'Player'

    blockList.append(Block(random.randrange(0,width_of_display-25), -600, 20 + level * 5, 20 + level * 5, 4, random.choice(listOfBlockColours), DOWN)) #Creates 4 blocks
    blockList.append(Block(random.randrange(0,width_of_display-25), 630, 20 + level * 5, 20 + level * 5, -4, random.choice(listOfBlockColours), UP))   #and adds them to
    blockList.append(Block(-30, random.randrange(0,height_of_display-25), 20 + level * 5, 20 + level * 5, 4, random.choice(listOfBlockColours), RIGHT)) #the blockList
    blockList.append(Block(830, random.randrange(0,height_of_display-25), 20 + level * 5, 20 + level * 5, -4, random.choice(listOfBlockColours), LEFT))

    leveladded = False              #Resets the leveladded and mainmenumusicOn flags
    mainmenumusicON = False

    changingSurface = Surface((width_of_display,height_of_display))   #Creates a surface
    changingSurface.blit(gameBackground, (0,0))                 #Prints the gameBackground picture on the screen
    changingSurface.set_alpha(0)                                #Makes it completely transparent
    gamechange = 0                                              #Variable that will be used to change the transparency of the background

    gameOn = True       #Sets gameOn flag to True

    while gameOn:           #While gameOn is True:

        if gamechange < 255:       #If the transparency variable is less than 255 (Note that when gamechange is equal to 255 the background is completely opaque, and no changes occur whatsoever);
            gamechange += 4          #Add 4 to the transparency variable
        changingSurface.set_alpha(gamechange)           #The backgrounds' transparency is changed with the new transparency value
        SCREEN.blit(changingSurface,(0,0))              #The background is printed onto the screen

        player.draw()                                   #Handles player movement, borders, key input, collisions with blocks, and level status
        player.checkBorders()
        player.handleMovementAndKeys()
        player.handleCollisions()
        player.checkLevel()

        for block in blockList:                     #For every block in the blockList it is drawn onto the screen and it is moved along the screen
            block.draw()
            block.handleMovement()

        Block.generate()                          #Handles the generation of blocks

        for attack in attackList:              #For every attack in the attackList it is drawn, handles collisions, and handles movement
            attack.draw()
            attack.handleCollisions()
            attack.handleMovement()

        if mute:                           #Checks if mute is flagged/True;
            for sound in allSoundsAndMusicList: #For every sound and music in the allSoundsAndMusicList;
                sound.set_volume(0)                 #Mute them
            mixer.music.set_volume(0)             #Mute the game music

        else:                              #Checks if mute is False;
            for sound in allSoundsAndMusicList:     #For every sound and music in the allSoundsAndMusicList;
                sound.set_volume(1)                     #Unmute/play them at 100% volume
            mixer.music.set_volume(1)                 #Unmute/play the game music at 100% volume

        time += 1/FPS                           #Adds the time (in seconds) to the variable time which keeps track of in-game time

        info()             #Displays the information (like score, how to pause, time, etc.) on the screen

        clock.tick(FPS)         #Caps the framerate at 60 frames per second
        display.flip()          #Updates the display with new information

main_menu()  #Calls the main menu function to start the game in the main menu
