import string
import itertools

def generate_wordlist(birthday):
    letters = string.ascii_lowercase
    wordlist = []
    
    for first_letter in string.ascii_uppercase:
        for comb in itertools.product(letters, repeat=3):
            word = f"{first_letter}{''.join(comb)}{birthday}"
            wordlist.append(word)
    
    return wordlist

def main():
    birthday = input("Enter the birthday (DDMM format): ")
    
    if len(birthday) != 4 or not birthday.isdigit():
        print("Invalid birthday date format. Use DDMM format.")
        return
    
    wordlist = generate_wordlist(birthday)
    
    with open("wordlist.txt", "w") as file:
        for word in wordlist:
            file.write(f"{word}\n")
    
    print("Word list generated and saved in wordlist.txt ")

if __name__ == "__main__":
    main()
