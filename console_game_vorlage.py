import curses
import random
import time # externe Bibliothek um Zeit zu managen

def main(stdscr):
    # Initialize color support

    # 1 Farbenpaar bestimmen, Vordergrundfarbe Blau, Hintergrundfarbe Grün
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)  # Player (magenta)


    # Setze den gesamten Bildschirm-Hintergrund auf schwarz
    stdscr.clear()  # Löscht den Bildschirm
    stdscr.refresh()  # Refresh, um den Bildschirm zu zeichnen





    # Set up initial position
    pos_y = 2 # Zeile 0
    pos_x = 3 # Spalte 3
    obstacle_x =  50 # Zeile 10
    obstacle_y = random.randint(1,5 ) # Spalte 2

    zeit1 = time.time()


    meine_kor = [[30,random.randint(1, 5)], [40,random.randint(1, 5)], [50,random.randint(1, 5)]]
    """
    for index in range(len(meine_kor)):
        meine_kor[index][0] = meine_kor[index][0] + 1
        meine_kor.append(meine_kor[index])
        meine_kor.pop(0)
"""

    # Define the square shaped block
    l_block = [
        (0, 0),  # 1st block of the square
        (1, 0)   # 2st block of the square

    ]

    # Define the obstacle block

    obstacle_block = [
    (0, 0),  # 1st block of the obstacle
    (1, 0)   # 2st block of the obstacle
    ]

    # Turn off cursor
    curses.curs_set(0)

    # Get the dimensions of the window
    height, width = stdscr.getmaxyx()
    score = 0  # Score-Zähler initialisieren

    while True:

        # Clear the screen before drawing
        stdscr.clear()
        stdscr.nodelay(1) # wartet bei stdscr.getch() nicht mehr
        stdscr.addch(1, 60)


        # Draw the square block
        for dx, dy in l_block:
            x, y = pos_x + dx, pos_y + dy
            # Farbe auswählen
            stdscr.attron(curses.color_pair(2))
            try:
                # Zeichen malen
                stdscr.addch(y, x, '█')
            except:
                pass
            # Farbe abwählen
            stdscr.attroff(curses.color_pair(1))

        # Draw the obstacle block
        for obst_x, obst_y in meine_kor:

          for dx, dy in obstacle_block:
              x, y = obst_x + dx, obst_y + dy
              # Farbe auswählen
              stdscr.attron(curses.color_pair(1))
              try:
                  # Zeichen malen
                  stdscr.addch(y, x, '█')
              except:
                  pass
              # Farbe abwählen
              stdscr.attroff(curses.color_pair(1))






             #🎯 Score während des Spiels anzeigen
              stdscr.addstr(0, 2, f" score: {score}")  # Zeigt den Score oben links an

           # Refresh the screen to show the update
              stdscr.refresh()



        # Get user input

        key = stdscr.getch()


        # Move right with right arrow key
        if key == curses.KEY_UP and pos_y > 1:
            pos_y -= 1
        elif key == curses.KEY_DOWN and pos_y <5:
            pos_y += 1
        elif key == ord('q'):
             break

        # Move the obstacle left with left arrow key
        if key == curses.KEY_ENTER:  # Spiel starten
          stdscr.keypad(True)



        for element in meine_kor:
          element[0] -= 1
          # Score erst erhöhen, wenn das erste Element verschwindet  
          if meine_kor and meine_kor[0][0] < 0:
            score += 1
            meine_kor.pop(0)  # Hindernis entfernen
        # Refresh the screen to show the update
        stdscr.refresh()
        #🎯 Score während des Spiels anzeigen
        #stdscr.addstr(0, 2, f"Score: {score}")  # Zeigt den Score oben links an


        time.sleep(0.15)

        if time.time() - zeit1 > 0.75:
          zeit1 = time.time()
          meine_kor.append([50,random.randint(1,5)])

        # Verbesserte Kollisionserkennung
        for obstacle in meine_kor:
            obst_x, obst_y = obstacle
            for dx, dy in l_block:
                player_x, player_y = pos_x + dx, pos_y + dy
                for ox, oy in obstacle_block:
                    obstacle_x, obstacle_y = obst_x + ox, obst_y + oy
                    if player_x == obstacle_x and player_y == obstacle_y:
                        stdscr.addstr(10, 10, f"GAME OVER Score: {score}")
                        stdscr.refresh()
                        time.sleep(2)
                        return
        if key != -1: # Damit es keinen Fehler gibt falls nichts gedrückt wird
            time.sleep(0.075) # wartet kurze Zeit vor das es die Schleife wiederholt

        meine_kor = [ob for ob in meine_kor if ob[0] >= 0]



        # Refresh the screen to show the update
        stdscr.refresh()
        #🎯 Score während des Spiels anzeigen



      



curses.wrapper(main)

