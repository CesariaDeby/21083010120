#!/usr/bin/env python

import random
import string
import time

pilih = int(input("Main game apa?Pilih game {1/2}"))

if pilih == 1:
   angka_acak = random.randint(1, 100)

   print('=' * 20)
   print('Angka telah dipilih, ayo tebak!')
   print('=' * 20)

   batas_percobaan = 5

   for percobaan in range(batas_percobaan):
       jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: ')) 
       if jawaban == angka_acak:
           print('Selamat, tebakanmu benar!')
           break
       else:
           print('Tebakanmu terlalu', 'kecil' if jawaban < angka_acak else 'besar')
   else:
       print(f'\nSayang sekali, kamu sudah salah menebak sebanyak {batas_percobaan}x!')


elif pilih == 2:

#                        Welcome to Hangman Game Sisop:


# Langkah awal untuk memanggil Hangman Game:
    print("\nWelcome to Hangman game by Sisop\n")
    name = input("Enter your name: ")
    print("Hello " + name + "! Best of Luck!")
    time.sleep(2)
    print("The game is about to start!\n Let's play Hangman!")
    time.sleep(3)


# Parameter untuk menjalankan Hangman Game:
    def main():
        global count
        global display
        global word
        global already_guessed
        global length
        global play_game
        words_to_guess = ["bored","photos","film","promise","kids","kind","angry","tired", "happy"] 
#kata untuk ditebak
        word = random.choice(words_to_guess)
        length = len(word)
        count = 0
        display = '_' * length
        already_guessed = []
        play_game = ""
    

# Menjalankan kembali permainan saat permainan pertama berakhir:
    def play_loop():
        global play_game
        play_game = input("Do You want to play again? y = yes, n = no \n")
        while play_game not in ["y", "n","Y","N"]:
            play_game = input("Do You want to play again? y = yes, n = no \n")
        if play_game == "y":
            main()
        elif play_game == "n":
            print("Thanks For Playing!")
            exit()

# Inisialisasi kondisi yang diperlukan untuk game:
    def hangman():
        global count
        global display
        global word
        global already_guessed
        global play_game
        limit = 5
        guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
        guess = guess.strip()
        if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
            print("Invalid Input, Try a letter\n")
            hangman()


        elif guess in word:
            already_guessed.extend([guess])
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            print(display + "\n")
    
        elif guess in already_guessed:
            print("Try another letter.\n")

        else:
            count += 1

            if count == 1:
                time.sleep(1)
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

            elif count == 2:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

            elif count == 3:
               time.sleep(1)
               print("   _____ \n"
                     "  |     | \n"
                     "  |     |\n"
                     "  |     | \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "__|__\n")
               print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

            elif count == 4:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

            elif count == 5:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
                print("Wrong guess. You are hanged!!!\n")
                print("The word was:",already_guessed,word)
                play_loop()

        if word == '_' * length:
            print("Congrats! You have guessed the word correctly!")
            play_loop()

        elif count != limit:
            hangman()

main()

hangman()
