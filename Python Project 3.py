import pygame
import time

pygame.init()

pygame.mixer.music.load("background.mp3")
win_sound = pygame.mixer.Sound("win.mp3")
gameover_sound = pygame.mixer.Sound("gameover.mp3")

pygame.mixer.music.play(-1)

RED, GREEN, YELLOW, BLUE, CYAN, RESET = "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[36m", "\033[0m"

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print(f"{YELLOW}🏝️ Welcome to Treasure Island! 🏝️{RESET}")
print(f"{CYAN}🗺️ Your mission is to find the hidden treasure! 💰{RESET}")

choice1 = input(f"{BLUE}🚶‍♂️ You're at a crossroad. Where do you want to go? Type 'left' ⬅️ or 'right' ➡️\n{RESET}").lower()

if choice1 == "left":
    choice2 = input(f"{CYAN}🌊 You've come to a lake. Type 'wait' ⏳ to wait for a boat 🛶, OR, Type 'swim' 🏊‍♂️ to swim across\n{RESET}").lower()

    if choice2 == "wait":
        choice3 = input(f"{GREEN}🏝️ You arrive at the island. There is a house 🏠 with 3 doors🚪: Red 🔴, Green 🟢, Blue 🔵. Which one?\n{RESET}").lower()

        if choice3 == "red":
            pygame.mixer.Sound.play(gameover_sound)
            print(f"{RED}🔥 It's a room full of fire! GAME OVER. 💀{RESET}")
        elif choice3 == "green":
            pygame.mixer.Sound.play(win_sound)
            print(f"{YELLOW}🎉 You found the treasure! 🏆💰 YOU WIN! 🎊{RESET}")
        elif choice3 == "blue":
            pygame.mixer.Sound.play(gameover_sound)
            print(f"{RED}🦁 You enter a room of beasts! GAME OVER. 💀{RESET}")
        else:
            pygame.mixer.Sound.play(gameover_sound)
            print(f"{RED}❓ You chose a door that doesn't exist. GAME OVER 🤷‍♂️{RESET}")
    else:
        pygame.mixer.Sound.play(gameover_sound)
        print(f"{RED}🐟 You got attacked by an angry trout! GAME OVER. 💀{RESET}")
else:
    pygame.mixer.Sound.play(gameover_sound)
    print(f"{RED}🕳️ You fell into a hole! GAME OVER. 💀{RESET}")

time.sleep(20)
pygame.mixer.music.stop()
pygame.quit()
