running = True

def start():
    print('aplication lancée')
def quit():
        global running
        running = False

while running:
    state = input('start/quit ')
    if state == 'start':
        start()
    elif state == 'quit':
        quit()
