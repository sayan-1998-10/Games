import simplegui

# checking for the third term to be zero or not.If it is zero,
#then it will be a whole number
third_term = 4
#timer
tenth_second = 0
#inital time
string = "0:00.0"
#score variables
#successful stops
x=0
#total stops
y=0
#check is True when timer is running
check = True

def format(t):
    
    first_term = 0
    global third_term
    third_term= t%10
    t=t-third_term
    t /=10
    if (t<=59):
        second_term = t
    else:
        first_term = t //60
        second_term = t - (first_term*60)
    if len(str(second_term))==1:
        second_term="0"+str(second_term)
    string = str(first_term)+ ":" +str(second_term)+"."+str(third_term)
    return string

    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global check
    timer1.start()
    check = True
    
def stop():
    global x,y,check
    timer1.stop()
    if check is True:
        if third_term is 0 :
            x +=1
        y += 1

    check = False    
    
def reset():
    global string,tenth_second,x,y
    timer1.stop()
    string="0:00.0"
    tenth_second = 0
    x=y=0

# define event handler for timer with 0.1 sec interval
def tenth():
    global tenth_second,string
    tenth_second += 1
    string=format(tenth_second)
    return string
    
# define draw handler
def draw(canvas):
    canvas.draw_text(string,(100,150),45,'red')
    canvas.draw_text(str(x)+"/"+str(y),(260,30),21,'yellow')
# create frame
frame = simplegui.create_frame("Stopwatch",300,300)

# register event handlers
frame.set_draw_handler(draw)
timer1 = simplegui.create_timer(100,tenth)
frame.add_button("START",start,100)
frame.add_button("STOP",stop,100)
frame.add_button("RESET",reset,100)


# start frame
frame.start()


