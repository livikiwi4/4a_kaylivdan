import curses
import random
import time # externe Bibliothek um Zeit zu managen

def main(stdscr):
    # Initialize color support
    curses.start_color()
    # 1 Farbenpaar bestimmen, Vordergrundfarbe Blau, Hintergrundfarbe Grün
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Player (magenta)


    # Setze den gesamten Bildschirm-Hintergrund auf schwarz
    stdscr.clear()  # Löscht den Bildschirm
    stdscr.refresh()  # Refresh, um den Bildschirm zu zeichnen
    stdscr.bkgd(' ', curses.color_pair(0))  # Setzt den Hintergrund auf schwarz





    # Set up initial position
    pos_x = 0 # Zeile 0
    pos_y = 3 # Spalte 3
    obstacle_x =  50 # Zeile 10
    obstacle_y = random.randint(1,5 ) # Spalte 2

    zeit1 = time.time()


    meine_kor = [[50,random.randint(1, 5)], [60,random.randint(1, 5)], [70,random.randint(1, 5)]]
    """
    for index in range(len(meine_kor)):
        meine_kor[index][0] = meine_kor[index][0] + 1
        meine_kor.append(meine_kor[index])
        meine_kor.pop(0)
"""

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
    score = 0  # Score-Zähler initialisieren

    while True:

        # Clear the screen before drawing
        stdscr.clear()
        stdscr.nodelay(1) # wartet bei stdscr.getch() nicht mehr
        stdscr.addch(1, 60)


        # Draw the square block
        for dx, dy in l_block:
            x, y = pos_y + dx, pos_x + dy
            # Farbe auswählen
            stdscr.attron(curses.color_pair(2))
            try:
                # Zeichen malen
                stdscr.addch(x, y, '█')
            except:
                pass
            # Farbe abwählen
            stdscr.attroff(curses.color_pair(1))

        # Draw the obstacle block
        for obst_y, obst_x in meine_kor:

          for dx, dy in obstacle_block:
              x, y = obst_x + dx, obst_y + dy
              # Farbe auswählen
              stdscr.attron(curses.color_pair(1))
              try:
                  # Zeichen malen
                  stdscr.addch(x, y, '█')
              except:
                  pass
              # Farbe abwählen
              stdscr.attroff(curses.color_pair(1))






             #🎯 Score während des Spiels anzeigen
              stdscr.addstr(0, 2, f"Score: {score}")  # Zeigt den Score oben links an

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
        stdscr.addstr(0, 2, f"Score: {score}")  # Zeigt den Score oben links an


        time.sleep(0.15)

        if time.time() - zeit1 > 2:
          zeit1 = time.time()
          meine_kor.append([50,random.randint(1,5)])


        """
        elif time.time() - zeit1 > 2000:
          meine_koor.append(meine_koor[2])

        """

        #Kollisionserkennung
        collision_count = 0  # Zählt, wie viele Teile des Blocks kollidieren
        for obstacle in meine_kor:
          obst_x, obst_y = obstacle
          for dx, dy in l_block:  # Überprüfe ALLE Teile des Spielerblocks
            player_x, player_y = pos_x + dy, pos_y + dx  # Berechne echte Spielerkoordinaten
            for ox, oy in obstacle_block:  # Überprüfe ALLE Teile des Hindernisblocks
                if (player_y, player_x) == (obst_y + dy, obst_x + dx):
                  collision_count += 1  # Erhöhe den Zähler

        # Nur wenn ALLE Teile des Blocks auf das Hindernis treffen → Spiel beenden
                  if collision_count == len(l_block) * len(obstacle_block):  
                            stdscr.addstr(10, 10, f"GAME OVER Score: {score}")
                            stdscr.refresh()
                            time.sleep(2)
                            return  # Beendet das Spiel


        if key != -1: # Damit es keinen Fehler gibt falls nichts gedrückt wird
            time.sleep(0.1) # wartet kurze Zeit vor das es die Schleife wiederholt

            meine_kor = [ob for ob in meine_kor if ob[0] >= 0]



        # Refresh the screen to show the update
            stdscr.refresh()
        #🎯 Score während des Spiels anzeigen


curses.wrapper(main)

