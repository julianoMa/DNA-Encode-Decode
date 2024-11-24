import os
import time

class COLORS:
    MAGENTA = '\033[95m'  # Magenta
    BLUE = '\033[94m'     # Blue
    CYAN = '\033[96m'     # Cyan
    GREEN = '\033[92m'    # Green
    YELLOW = '\033[93m'   # Yellow
    RED = '\033[91m'      # Red
    RESET = '\033[0m'     # Reset
    BOLD = '\033[1m'      # Bold
    UNDERLINE = '\033[4m' # Underline

class Main():
    def __init__(self):
        self.binary = ""
        self.dna_sequence = ""

        self.dna_mapping = {
            "A": "00",
            "T": "01",
            "G": "10",
            "C": "11",
        }
    
        self.main()

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(COLORS.BLUE + """

▓█████▄  ███▄    █  ▄▄▄         ▓█████  ███▄    █  ▄████▄   ▒█████  ▓█████▄ ▓█████    ▓█████▄ ▓█████  ▄████▄   ▒█████  ▓█████▄ ▓█████ 
▒██▀ ██▌ ██ ▀█   █ ▒████▄       ▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀    ▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ 
░██   █▌▓██  ▀█ ██▒▒██  ▀█▄     ▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▒██░  ██▒░██   █▌▒███      ░██   █▌▒███   ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   
░▓█▄   ▌▓██▒  ▐▌██▒░██▄▄▄▄██    ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄    ░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ 
░▒████▓ ▒██░   ▓██░ ▓█   ▓██▒   ░▒████▒▒██░   ▓██░▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒   ░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒
 ▒▒▓  ▒ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░   ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░    ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░
 ░ ▒  ▒ ░ ░░   ░ ▒░  ▒   ▒▒ ░    ░ ░  ░░ ░░   ░ ▒░  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░    ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░
 ░ ░  ░    ░   ░ ░   ░   ▒         ░      ░   ░ ░ ░        ░ ░ ░ ▒   ░ ░  ░    ░       ░ ░  ░    ░   ░        ░ ░ ░ ▒   ░ ░  ░    ░   
   ░             ░       ░  ░      ░  ░         ░ ░ ░          ░ ░     ░       ░  ░      ░       ░  ░░ ░          ░ ░     ░       ░  ░
 ░                                                ░                  ░                 ░             ░                  ░             
        """ + COLORS.RESET)
        print("What do you want to do?\n1. Encode text to DNA\n2. Decode DNA to text")
        time.sleep(1)
        choice = input(COLORS.YELLOW + "\nType the number of your choice : " + COLORS.RESET)

        if choice == "1":
            self.encode()
        elif choice == "2":
            self.decode()
        else:
            print(COLORS.RED + "Please only type the number 1 or 2")
            time.sleep(3)
            self.main()

    def encode(self):
        string = input(COLORS.CYAN + "Write your secret phrase : " + COLORS.RESET)

        # We first convert the string into an 8-bit binary
        for char in string:
            self.binary += format(ord(char), "08b")

        # Then we convert the binary into a DNA sequence, using the mapping defined before
        for char in range(0, len(self.binary), 2): # Starting at the first digit, by steps of 2
            digits = self.binary[char:char+2]

            for dna_base, bits in self.dna_mapping.items():
                if bits == digits:
                    self.dna_sequence += dna_base
        
        print(COLORS.CYAN + "Here is your secret phrase encoded : " + COLORS.RESET + self.dna_sequence)
        input(COLORS.RED + "When ready, types something to go back to the menu" + COLORS.RESET)

    def decode(self):
        string = input(COLORS.CYAN + "Write your GNA sequence : " + COLORS.RESET)

        # We first convert each letter to an 8-bit binary
        for char in string:
            if char != "A" or "T" or "G" or "C":
                print(COLORS.RED + "Please only enter an DNA sequence (A T G C) !" + COLORS.RESET)
                time.sleep(3)
                self.main()
Main()