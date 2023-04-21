framecount = 0 # The number of frames since game start
state = "MENU" # The current state of the game, written in all caps
score = 0 

def get_state():
    return state

def get_framecount():
    return framecount

def get_score():
    return score

def set_state(new_state):
    global state
    state = new_state

def update_framecount():
    global framecount
    framecount += 1

def reset_framecount():
    global framecount
    framecount = 0

def add_score(points):
    global score
    score += points