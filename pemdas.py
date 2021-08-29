import random
from tkinter import *
import time

#constants

BACKSPACE = '\b'
RETURN = '\r'
ESCAPE = '\x1b'
REGULAR = 'Roboto'
BOLD = 'Roboto Bold'

#text position
MAINTEXT = 0.1
LEVEL = 0.17
SCORE = 0.22
SCORECOUNT = 0.27
SCORELINE = 0.17
PROMPT = 0.4
EQUATION = 0.5
CORRECT = 0.6
ANSWER = 0.7
CORRECTION = 0.8
QUITMESSAGE=0.95



#colours
CORRECTGREEN = '#06da79'
INCORRECTRED = '#fe7cba'
EQUATIONFILL = '#FFFFFF'
ANSWERFILL = '#FFFFFF'
ORANGE = '#ff8d8d'

#Create a PEMDAS equation

def AS():
    return random.choice(('+','-'))
def DM():
    return random.choice(('*','/'))

def MakeEquation(game_object):


    while True:
        equation = ''

        random.seed() #initialize random seed

        n1 = random.randint(1,9)
        n2 = random.randint(1,9)
        n3 = random.randint(1,9)
        n4 = random.randint(1,9)

        option = random.randrange(0,game_object.options[clamp(game_object.current_level,game_object.max_level)])

        if option == 0: equation = '{}{}{}{}{}{}{}'.format(n1,AS(),n2,DM(),n3,AS(),n4)
        if option == 1: equation = '{}{}{}{}{}{}{}'.format(n1, DM(), n2, AS(), n3, DM(), n4)
        if option == 2: equation = '{}{}{}{}{}{}{}'.format(n1, DM(), n2, AS(), n3, AS(), n4)
        if option == 3: equation = '{}{}{}{}{}{}{}'.format(n1, AS(), n2, AS(), n3, DM(), n4)

        if option == 4: equation = '({}{}{}){}{}{}{}'.format(n1, AS(), n2, DM(), n3, AS(), n4)
        if option == 5: equation = '{}{}{}{}({}{}{})'.format(n1, AS(), n2, DM(), n3, AS(), n4)

        if option == 6: equation = '{}{}({}{}{}){}{}'.format(n1, DM(), n2, AS(), n3, DM(), n4)
        if option == 7: equation = '{}{}({}{}{}{}{})'.format(n1, DM(), n2, AS(), n3, DM(), n4)
        if option == 8: equation = '({}{}{}{}{}){}{}'.format(n1, DM(), n2, AS(), n3, DM(), n4)

        if option == 9: equation = '{}{}({}{}{}){}{}'.format(n1, DM(), n2, AS(), n3, AS(), n4)
        if option == 10: equation = '{}{}({}{}{}{}{})'.format(n1, DM(), n2, AS(), n3, AS(), n4)

        if option == 11: equation = '({}{}{}{}{}){}{}'.format(n1, AS(), n2, AS(), n3, DM(), n4)
        if option == 12: equation = '{}{}({}{}{}){}{}'.format(n1, AS(), n2, AS(), n3, DM(), n4)

        try:
            if eval(equation) in game_object.answer_ranges[clamp(game_object.current_level,game_object.max_level)]:

                return equation #check if result is within range
        except:
            pass


# clamp value
def clamp(value,mx):
    if value>mx:
        return mx
    return value

class gameClass:
    def __init__(self):
        self.answer = ''
        self.options = [4,6,8,12,13]
        self.answer_ranges= [[x for x in range(21)],[x for x in range(31)],[x for x in range(41)],[x-10 for x in range(41)],[x-20 for x in range(41)] ]
        self.max_level = 4
        self.current_level = 1
        self.previous_level = 0
        self.equation = MakeEquation(self)
        self.question_counter = 0  # stores the number of questions asked in a session
        self.correct_counter = 0
        self.next_level = False
    def updateEquation(self):
        self.answer = ''
        self.equation = MakeEquation(self)
        self.question_counter += 1







def keyboardEvents(event,root_object,canvas_object,game_object):

    if event.char == ESCAPE:
        root_object.destroy()
    if event.char.isnumeric() or event.char == '-':
        game_object.answer += event.char
        canvas_object.itemconfigure(answer_text, text=game_object.answer)

    if event.char == BACKSPACE:
        game_object.answer = game_object.answer[:-1] #if backspace is pressed remove the last character from answerGR
        canvas_object.itemconfigure(answer_text, text=game_object.answer)

    if event.char == RETURN and game_object.answer !='':
        root_object.bind('<KeyPress>', lambda event : nextQuestion(root_object,canvas_object,game_object))
        checkAnswer(canvas_object,game_object)

def checkAnswer(canvas_object,game_object):

    if int(game_object.answer) == int(eval(game_object.equation)):
    #if int(game_object.answer) == 1: #this is just for testing
        canvas_object.itemconfigure(correct_label, text='CORRECT!', fill= CORRECTGREEN)
        game_object.correct_counter +=1
        if not game_object.correct_counter % 10:
            game_object.next_level = True

    else:  # if it's wrong just diplay message and move to the screen update
        canvas.itemconfigure(correct_label, text='Incorrect', fill= INCORRECTRED )
        canvas.itemconfigure(correct_answer, text='actually it\'s {}'.format(int(eval(game_object.equation))), fill=INCORRECTRED)

#generates a fresh equation and resets the check_answer flag. Sets screen update to True so that the screen is updated next loop
def nextQuestion(root_object,canvas_object,game_object):

    game_object.updateEquation()

    canvas_object.itemconfigure(score_count, text='{}'.format(game_object.correct_counter))
    canvas_object.itemconfigure(correct_label, text='', fill='#de0404')
    canvas_object.itemconfigure(equation_text, text=game_object.equation.replace('/', ':').replace('*', '·'))
    canvas_object.coords(score_line, 0, canvas_object.coords(score_line)[1], (root_object.winfo_width()/10) * (game_object.correct_counter % 10), canvas_object.coords(score_line)[1])
    canvas_object.itemconfigure(answer_text, text=(game_object.answer))
    canvas_object.itemconfigure(correct_answer, text='', fill='#de0404')
    if not game_object.correct_counter % 10 and game_object.next_level :
        changeLevel(root_object, canvas_object, game_object)
        game_object.next_level = False

    root.bind('<KeyPress>', lambda event: keyboardEvents(event, root_object, canvas_object, game_object))
    root_object.update()


def changeLevel(root_object,canvas_object,game_object):
    root.bind('<KeyPress>')
    HEIGH = root_object.winfo_height()
    WIDHT = root_object.winfo_width()
    scale = 0

    while scale < .4:
        scale = scale + .05
        canvas_object.coords(splash_screen, WIDTH//2 - HEIGHT * scale, HEIGHT//2 - HEIGHT * scale,  WIDTH//2 + HEIGHT * scale, HEIGHT//2 + HEIGHT * scale)
        canvas_object.itemconfigure(splash_screen, width=200 * scale)
        time.sleep(1 / 50)
        root_object.update()


    game_object.current_level += 1
    canvas_object.itemconfigure(level_info, text='Level {}'.format(game_object.current_level))
    while scale < 1:
        scale = scale + .05
        canvas_object.coords(splash_screen, WIDTH//2 - HEIGHT * scale, HEIGHT//2 - HEIGHT * scale,  WIDTH//2 + HEIGHT * scale, HEIGHT//2 + HEIGHT * scale)
        canvas_object.itemconfigure(splash_screen, width=200 * scale)
        time.sleep(1 / 50)
        root_object.update()

    root.bind('<KeyPress>', lambda event: keyboardEvents(event, root_object, canvas_object, game_object))

#logging data on window close
def on_closing(root,game_object):

    with open('log.txt', 'a+') as f:
        f.write('\nYou scored {} out of {} and reacher level {}'.format(game_object.correct_counter,game_object.question_counter,game_object.current_level))
        f.write('-------------------------------------------------------------\n')
    root.destroy()



#TKINTER
#declaring the window size
root = Tk()

root.overrideredirect(1)

try:
    BACKGROUND = PhotoImage(file='background.pbm')
except:
    print('Image not found')
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
#SCREEN_HEIGHT = 500
WINDOW_SCALE = (SCREEN_HEIGHT-100)/960
WIDTH = int(540*WINDOW_SCALE)
HEIGHT = int(960*WINDOW_SCALE)

root.geometry('{}x{}+{}+{}'.format(WIDTH,HEIGHT,int(SCREEN_WIDTH/2 - WIDTH/2),int(SCREEN_HEIGHT/2 - HEIGHT/2)))
root.resizable(False, False)

#text weight
HEADLINE = int((8/100)*HEIGHT)
HEADLINE2 = int((4/100)*HEIGHT)
HEADLINE3 = int((3/100)*HEIGHT)
SCORESIZE = int((5/100)*HEIGHT)
REGULAR = int((2/100)*HEIGHT)
SMALL = int((1/100)*HEIGHT)

#Bunch of text displayed on the canvas
game = gameClass()

canvas = Canvas(width = WIDTH,height = HEIGHT,highlightthickness=0)
try:
    bg = canvas.create_image(0,0,image = BACKGROUND, anchor = NW)
except:
    pass
canvas.pack()

root.bind('<KeyPress>', lambda event: keyboardEvents(event,root,canvas,game))








main_text = canvas.create_text((WIDTH/2,MAINTEXT*HEIGHT),text = 'Hello Oliver!', font=(REGULAR,HEADLINE2), fill = '#E1E1E1' )

score_line_bg = canvas.create_line((0,SCORELINE*HEIGHT),(WIDTH,SCORELINE*HEIGHT), width=int(.05*HEIGHT), capstyle = BUTT, fill = '#E1E1E1' )
score_line = canvas.create_line((0,SCORELINE*HEIGHT),((WIDTH//10)*(game.correct_counter%10),SCORELINE*HEIGHT), width=int(.05*HEIGHT), capstyle = BUTT, fill = '#75de04' )

level_info = canvas.create_text((WIDTH/2,LEVEL*HEIGHT), text = 'Level {}'.format(game.current_level), font=(REGULAR, HEADLINE3), fill = ORANGE)
splash_screen = canvas.create_oval(0,0,0,0, fill =  '',outline = ORANGE, width=0)


score = canvas.create_text((WIDTH/2,SCORE*HEIGHT),text = 'Score', font=(REGULAR,SMALL), fill = '#E1E1E1')
score_count = canvas.create_text((WIDTH/2,SCORECOUNT*HEIGHT),text = '{}'.format(game.correct_counter), font=(BOLD,SCORESIZE), fill = '#E1E1E1')




prompt_text = canvas.create_text((WIDTH/2,PROMPT*HEIGHT),text = 'What is', font=(REGULAR,20) )
answer_text = canvas.create_text((WIDTH/2, ANSWER*HEIGHT), text=game.answer, font=(BOLD, HEADLINE), fill = ANSWERFILL)
equation_text = canvas.create_text((WIDTH/2,EQUATION*HEIGHT),text = game.equation.replace('/',':').replace('*','·'), font=(BOLD,HEADLINE), fill = EQUATIONFILL )
correct_label = canvas.create_text((WIDTH/2,CORRECT*HEIGHT), text='', font=(BOLD, HEADLINE2), fill = CORRECTGREEN)
correct_answer = canvas.create_text((WIDTH/2,CORRECTION*HEIGHT), text='', font=(BOLD, HEADLINE2), fill = INCORRECTRED)

quite_message = canvas.create_text((WIDTH/2,QUITMESSAGE*HEIGHT), text='Press esc to quit', font=(REGULAR, SMALL), fill = ORANGE)


#this bind the keyboard to the root


#more eyecandy




#this is just to run the close window logging
root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root,game))


root.mainloop()




