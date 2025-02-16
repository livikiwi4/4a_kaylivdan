import curses
import random
import time # externe Bibliothek um Zeit zu managen

def main(stdscr):
    # Initialize color support
    curses.start_color()
    # 1 Farbenpaar bestimmen, Vordergrundfarbe Blau, Hintergrundfarbe Grün
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)

    # Clear the screen
    stdscr.clear()

    # Set up initial position
    pos_x = 0 # Zeile 0
    pos_y = 3 # Spalte 3
    obstacle_x =  10 # Zeile 10
    obstacle_y = random.randint(1, 5) # Spalte 2
    


    # Define the square shaped block
    l_block = [
        (0, 0),  # 1st block of the square
        (0, 1)   # 2st block of the square

    ]

    # Define the obstacle block

    obstacle_block = [
    (0, 0),  # 1st block of the obstacle
    (0, 1)   # 2st block of the obstacle
    ]

    # Turn off cursor
    curses.curs_set(0)

    # Get the dimensions of the window
    height, width = stdscr.getmaxyx()

    while True:

        # Clear the screen before drawing
        stdscr.clear()

        # Draw the square block
        for dy, dx in l_block:
            y, x = pos_y + dy, pos_x + dx
            # Farbe auswählen
            stdscr.attron(curses.color_pair(1))
            try:
                # Zeichen malen
                stdscr.addch(y, x, '█')
            except:
                pass
            # Farbe abwählen
            stdscr.attroff(curses.color_pair(1))

        # Draw the obstacle block
        for dy, dx in obstacle_block:
            y, x = obstacle_y + dy, obstacle_x + dx
            # Farbe auswählen
            stdscr.attron(curses.color_pair(1))
            try:
                # Zeichen malen
                stdscr.addch(y, x, '█')
            except:
                pass
            # Farbe abwählen
            stdscr.attroff(curses.color_pair(1))
        
        # Refresh the screen to show the update
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()


        # Move right with right arrow key
        if key == curses.KEY_UP and pos_y > 0:
            pos_y -= 1
        elif key == curses.KEY_DOWN and pos_y < height -1:
            pos_y += 1
        elif key == ord('q'):
             break

        # Move the obstacle left with left arrow key
        if key == curses.KEY_ENTER:  # Spiel starten
          pass
        obstacle_x -= 1
        time.sleep(0.05)

        stdscr.nodelay(1) # wartet bei stdscr.getch() nicht mehr

        if key != -1: # Damit es kein Fehler gibt falls nichts gedrückt wird
            time.sleep(1) # wartet kurze Zeit vor das es die Schleife wiederholt


        # Hindernis zurücksetzen, wenn es aus dem Fenster verschwindet
        if obstacle_x + len(obstacle_block) < 0:
            obstacle_x = width  # Optional: Hindernis von rechts neu starten lassen

        # Kollisionserkennung
        if pos_x == obstacle_x and pos_y == obstacle_y:
            break


curses.wrapper(main)

meine_kor = [x]
meine_kor = [[x1,y1], [x2, y2], [x3, y3]]
for index in range(len(meine_kor)):
    meine_kor[index][0] = meine_kor[index][0] + 1
    meine_kor.append(meine_kor[index])
    meine_kor.pop(0)
def main(stdscr):
    # Initialize color support 
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
# Clear the screen
stdscr.clear()

    def __init__(self):
        self.score = 0

    def add_points(self, points):
        self.score += points
        print(f"Punkte: {self.score}")

    def reset(self):
        self.score = 0
        print("Punkte zurückgesetzt.")

    def get_score(self):
        return self.score









