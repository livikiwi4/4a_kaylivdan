# Der Code für mein Spiel kommt hier zz
import curses

def main(stdscr):
    # Initialize color support
    curses.start_color()
    # 1 Farbenpaar bestimmen, Vordergrundfarbe Blau, Hintergrundfarbe Grün
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)

    # Clear the screen
    stdscr.clear()

    # Set up initial position
    pos_x = 0 # Zeile 0
    pos_y = 0 # Spalte 0

    # Define the "L" shaped block
    l_block = [
        (0, 0),  # 1st block of the square
        (0, 1)   # 2st block of the square
             
    ]

    # Define the triangle shaped block
    triangle_block = [
    (2, 0),  # 1st block of the square
    (0, 1)   # 2st block of the square

    ]
    # Turn off cursor
    curses.curs_set(0)

    # Get the dimensions of the window
    height, width = stdscr.getmaxyx()

    while True:

        # Clear the screen before drawing
        stdscr.clear()

        # Draw the "L" block
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

        # Draw the other blocks
        for dy, dx in triangle_block:
            y, x = 2 + dy, 4 + dx
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
        if key == curses.KEY_UP and pos_y >= 1:
            pos_y -= 1
        if key == curses.KEY_DOWN and pos_y <= 1:
            pos_y += 1








        elif key == ord('q'):
            break


curses.wrapper(main)




