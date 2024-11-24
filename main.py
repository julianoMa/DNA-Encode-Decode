import os
import time

class COLORS:
    BLUE = '\033[94m'     # Blue
    CYAN = '\033[96m'     # Cyan
    YELLOW = '\033[93m'   # Yellow
    RED = '\033[91m'      # Red
    RESET = '\033[0m'     # Reset

class Main():
    def __init__(self):
        self.binary = ""
        self.dna_sequence = ""
        self.text = ""

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
 ░ ▒  ▒ ░ ░░   ░ ░░  ▒   ▒▒ ░    ░ ░  ░░ ░░   ░ ▒░  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░    ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░
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
        self.binary = ""  # Clear previous binary data to prevent any errors
        self.dna_sequence = ""  # Clear previous DNA sequence to prevent any errors
        string = input(COLORS.CYAN + "Write your secret phrase : " + COLORS.RESET)

        # Convert the string into an 8-bit binary
        for char in string:
            self.binary += format(ord(char), "08b")

        # Convert the binary into a DNA sequence
        for char in range(0, len(self.binary), 2):  # Starting at the first digit, by steps of 2
            digits = self.binary[char:char+2]
            for dna_base, bits in self.dna_mapping.items():
                if bits == digits:
                    self.dna_sequence += dna_base
        
        print(COLORS.CYAN + "Here is your secret phrase encoded : " + COLORS.RESET + self.dna_sequence)
        time.sleep(1)
        input(COLORS.RED + "When ready, press enter to go back to the menu" + COLORS.RESET)
        self.main()

    def decode(self):
        self.binary = ""  # Clear previous binary data to prevent any errors
        self.text = ""  # Clear previous decoded text to prevent any errors
        string = input(COLORS.CYAN + "Write your GNA sequence : " + COLORS.RESET)

        # Convert each nucleotide to its corresponding binary, using dna_mapping
        for char in string:
            if char in self.dna_mapping:
                self.binary += self.dna_mapping[char]
            else:
                print(COLORS.RED + f"Invalid character: {char}. Only A, T, G, C are allowed." + COLORS.RESET)
                return

        # Convert binary back to text
        for i in range(0, len(self.binary), 8):
            byte = self.binary[i:i+8]
            char = chr(int(byte, 2))
            self.text += char

        print(COLORS.CYAN + f"Here is your decoded message : {self.text}" + COLORS.RESET)
        time.sleep(1)
        input(COLORS.RED + "When ready, press enter to go back to the menu" + COLORS.RESET)
        self.main()
        
Main()
