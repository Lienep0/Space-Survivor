framecount = 0 # The number of frames since game start
state = "MENU" # The current state of the game, written in all caps
score = 0 
paused = False

def get_game_state():
    return state

def get_framecount():
    return framecount

def get_score():
    return score

def get_paused_state():
    return paused

def set_game_state(new_state):
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

def change_pause_status():
    global paused
    paused = not paused