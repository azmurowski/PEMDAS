import random
from tkinter import *
import time

#Create a PEMDAS equation
def MakeEquation(answer_range,options):
    opsAS = ('+', '-')
    opsDM = ('*','/')
    nums = [str(x) for x in range(1, 10)]

    equation = ''


    while True:
        random.seed() #initialize random seed

        # create initial equation
        for i in range(7):
            #assign a number to every odd location
            if not i % 2:
                equation = equation + nums[random.randrange(0, 9)]
            #assign op placeholder for every even location
            else:
                equation = equation + '$'
            #choose an option for final formatting
            option = random.randrange(0,options)
            #option = 13

            # option n(+-)n(*/)n(+-)
            if(option == 0):
                n_eq = ''
                for i,el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1,5):
                            n_eq += opsAS[random.randrange(0,2)]
                        else:
                            n_eq += opsDM[random.randrange(0,2)]
            # option n(*/)n(+-)n(*/)
            if (option == 1):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 5):
                            n_eq += opsDM[random.randrange(0, 2)]
                        else:
                            n_eq += opsAS[random.randrange(0, 2)]
            # option n(*/)n(+-)n(*/)n
            if (option == 2):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 3):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]
            # option n(*/)n(+-)n(+-)n
            if (option == 3):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (3, 5):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]

            # option n(+-)n(+-)n(*/)n
            if (option == 4):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 3):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]

            # option [n(+-)n](*/)n(+-)n
            if option == 5:
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 5):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]
                n_eq = '(' + n_eq[0:3] + ')' + n_eq[3::]
            # option n(+-)n(*/)[n(+-)n]
            if option == 6:
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 5):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]
                n_eq = n_eq[0:4] + '(' + n_eq[4::] + ')'

            # option n(*/)[n(+-)n](*/)n
            if (option == 7):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 5):
                            n_eq += opsDM[random.randrange(0, 2)]
                        else:
                            n_eq += opsAS[random.randrange(0, 2)]
                n_eq = n_eq[0:2] + '(' + n_eq[2:5] + ')' +  n_eq[5::]
            # option n(*/)[n(+-)n(*/)n]
            if (option == 8):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 5):
                            n_eq += opsDM[random.randrange(0, 2)]
                        else:
                            n_eq += opsAS[random.randrange(0, 2)]
                n_eq = n_eq[0:2] + '(' + n_eq[2::] + ')'

            # option n(*/)[n(+-)n(*/)n]
            if (option == 9):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 5):
                            n_eq += opsDM[random.randrange(0, 2)]
                        else:
                            n_eq += opsAS[random.randrange(0, 2)]
                n_eq = '(' + n_eq[0:5] + ')' + n_eq[5::]

            # option [n(+-)n(+-)n](*/)n
            if (option == 10):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 3):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]

                n_eq = '(' + n_eq[0:5] + ')' + n_eq[5::]

            # option n(+-)[n(+-)n](*/)n
            if (option == 11):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (1, 3):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]

                n_eq = n_eq[0:2] + '(' + n_eq[2:5] + ')' + n_eq[5::]

            # option n(*/)n(+-)n(+-)n
            if (option == 12):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (3, 5):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]
                n_eq = n_eq[0:2] + '(' + n_eq[2:5] + ')' + n_eq[5::]

            # option n(*/)n(+-)n(+-)n
            if (option == 13):
                n_eq = ''
                for i, el in enumerate(equation):
                    if el.isdigit():
                        n_eq = n_eq + el
                    else:
                        if i in (3, 5):
                            n_eq += opsAS[random.randrange(0, 2)]
                        else:
                            n_eq += opsDM[random.randrange(0, 2)]
                n_eq = n_eq[0:2] + '(' + n_eq[2::] + ')'


        equation = n_eq
        #check if equation gives an integer answer
        try:
            if eval(equation) in answer_range:  return equation
        except:
            pass
        #clear equation for next loop
        equation = ''
# clamp value
def clamp(value,max):
    if value>max:
        return max
    return value
#Define which options will be used in the MakeEquation function
options = [4,6,8,12,13]
#Define the answer range for the MakeEquation function
answer_ranges= [[x for x in range(21)],[x for x in range(31)],[x for x in range(41)],[x-10 for x in range(41)],[x-20 for x in range(41)] ]

#These variables track the level which is used for the previous two variables to select the range and options (previous level isn't used)
current_level = 1
previous_level = 0


answerGR = '' #stores the answer from the GUI
check_answer = False #this variable triggers checking if the answer is correct
equation = MakeEquation(answer_ranges[clamp(current_level-1,4)],options[clamp(current_level-1,4)]) #create the equation presented to the user
screen_update = False #this variable controls weather the next equation should be genereted and the screen refreshed
correct = int(eval(equation)) #stores the correct answer to the current equation (updated with every new screen)
answered_correctly = False #this variable triggers the screen update routine
question_counter = 0 #stores the number of questions asked in a session
correct_counter = 0 #stores the number of correct answers
#update_level = False
update_level = False #this variable is checked to see if the level can be increased - happens every 10 correct answers


# this function is bound to the enter key in the root of the app - it allows
# 1. adding numbers to the answerGR and ignoring non numeric values
# 2. deleting a number from the answerGR using backspace
# 3. triggering the routine which checks the answer when enter is pressed
def enterKey(event):
    global answerGR #so many globals
    global check_answer
    if(event.char.isnumeric() or event.char == '-'): # if the pressed character is numeric or - then add it to answerGR
        answerGR += event.char
    if(event.char == '\b'):
        answerGR = answerGR[:-1] #if backspace is pressed remove the last character from answerGR
    if(event.char == '\r'):
        check_answer = True #if enter is pressed the checkanswer routing will be triggered next loop



#generates a fresh equation and resets the check_answer flag. Sets screen update to True so that the screen is updated next loop
def nextQuestion(event):
    global equation
    global check_answer
    global screen_update
    global correct
    global current_level
    global answer_ranges
    global options
    equation = MakeEquation(answer_ranges[clamp(current_level-1,4)],options[clamp(current_level-1,4)])
    correct = int(eval(equation))
    check_answer = False #set check_answer flag to false
    screen_update = True #set screen_update flag to true - both checked in the mainlooop
#logging data on window close
def on_closing(root):

    with open('log.txt', 'a+') as f:
        f.write('\nYou scored {} out of {} and reacher level {}'.format(correct_counter,question_counter,current_level))
        f.write('-------------------------------------------------------------\n')
    root.destroy()






#TKINTER
#declaring the window size
root = Tk()
#create canvas
canvas = Canvas(width = 540,height = 760)
#insert canvas
canvas.pack()
#Bunch of text displayed on the canvas
main_text = canvas.create_text((270,75),text = 'Hello Oliver!', font=('Arial',40), fill = '#E1E1E1' )
prompt_text = canvas.create_text((270,325),text = 'What is', font=('Arial',20) )
answer_text = canvas.create_text((270, 600), text=answerGR, font=('Roboto Bold', 80))
equation_text = canvas.create_text((270,400),text = equation.replace('/',':').replace('*','·'), font=('Roboto Bold',80) )
correct_label = canvas.create_text((270, 500), text='', font=('Roboto Bold', 40), fill = '#75de04')
correct_answer = canvas.create_text((270, 700), text='', font=('Arial', 40), fill = '#de0404')
score = canvas.create_text((270,180),text = 'Score', font=('Arial',20), fill = '#E1E1E1')
score_count = canvas.create_text((270,225),text = '{}/{}'.format(correct_counter,question_counter), font=('Roboto Bold',50), fill = '#E1E1E1')

#this bind the keyboard to the root
root.bind('<KeyPress>', enterKey)

#more eyecandy
score_line_bg = canvas.create_line((0,275),(540,275), width=25, capstyle = ROUND, fill = '#E1E1E1' )
score_line = canvas.create_line((0,275),(54*(correct_counter%10),275), width=25, capstyle = ROUND, fill = '#75de04' )

level_info = canvas.create_text((270,135), text = 'Level {}'.format(current_level), font=('Roboto', 30))
splash_screen = canvas.create_oval(0,0,0,0, fill =  '',outline = '#ffd561', width=0)

#this is just to run the close window logging
root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))


while True:
    try:
        root.update()

        # default state, updates the answer_text object
        if not check_answer:
            root.bind('<KeyPress>', enterKey)
            canvas.itemconfigure(answer_text, text = (answerGR))

        #when enter is pressed the answer stored in answerGR is checked
        if check_answer:

            if int(answerGR) == correct: # if the answer is correct it displays a message
            #if int(answerGR) == 1: #this is just for testing
                canvas.itemconfigure(correct_label, text='CORRECT!', fill = '#75de04' )
                answered_correctly = True #this flag is for screen update

            else: #if it's wrong just diplay message and move to the screen update
                canvas.itemconfigure(correct_label, text='Incorrect', fill = '#de0404')
                canvas.itemconfigure(correct_answer, text='should be {}'.format(correct), fill='#de0404')


            root.bind('<KeyPress>', nextQuestion) # not enter key is bound to the function that sets the screen update flag to true
            # and generates new quation while resetting the answer
        #routine that refreshes the screen and logs the equation and answer
        if screen_update:
            with open('log.txt', 'a+') as f:
                f.write('\nEquation: {} Correct answer {} Your answer {}'.format(equation.replace('/',':').replace('*','·'),correct,answerGR))
            if answered_correctly:
                with open('log.txt', 'a+') as f:
                    f.write('   CORRECT')
                correct_counter +=1 # increase the correct counter
                answered_correctly = False #reset the flag
                if not correct_counter % 10: #sets update level to true every 10 correct answer
                    update_level = True
            else:
                with open('log.txt', 'a+') as f:
                    f.write('   INCORRECT')

            question_counter += 1 # increases the question counter

            #update relevant canvas objects
            canvas.itemconfigure(score_count, text='{}/{}'.format(correct_counter, question_counter))
            canvas.itemconfigure(correct_label, text='', fill='#de0404')
            canvas.itemconfigure(equation_text, text=equation.replace('/',':').replace('*','·'))
            canvas.coords(score_line,0,275,54*(correct_counter%10),275)
            answerGR = '' # reset answerGr
            canvas.itemconfigure(answer_text, text=(answerGR))
            canvas.itemconfigure(correct_answer, text='', fill='#de0404')

            screen_update = False #reset the screen update flag
        #level update and a little animation probably messy as well
        if update_level:
            update_level = False
            previous_level = current_level
            scale = 0
            while scale<.4:
                scale = scale + .05
                canvas.coords(splash_screen,270-600*scale,380-600*scale,270+600*scale,380+600*scale)
                canvas.itemconfigure(splash_screen,width=200*scale)
                time.sleep(1/50)
                root.update()

            previous_level = current_level
            current_level += 1
            canvas.itemconfigure(level_info, text='Level {}'.format(current_level))
            while scale<1:
                scale = scale + .05
                canvas.coords(splash_screen,270-600*scale,380-600*scale,270+600*scale,380+600*scale)
                canvas.itemconfigure(splash_screen,width=200*scale)
                time.sleep(1/50)
                root.update()
            update_level = False



        root.update_idletasks() #justtkinterthings
    except:
       pass
    #all inside try/except because I was getting a bunch of errors when quitting the app




