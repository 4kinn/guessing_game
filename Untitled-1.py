import random
def start():
    print("1 for letter game")
    print("2 for the number game")
    select=input(" ")
    if select=='1':
        game_word()
    elif select=='2':
        game_number()
    
def game_word():
    words=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    twrnd=random.choice(words)
    print("type hint for hint")
    lifee=input("ow many lives do you want: ")
    lifee_int=int(lifee)

    while 2>1:
        selec=input("enter your guess: ")
        if lifee_int<0:
            print("lost the game ")
            print("word: ",twrnd)
            reply()
            break       
        elif selec==twrnd:
            print("bingoooo ")
            print("remaining life: ",lifee_int)
            reply()
            break
        elif selec >twrnd:
            print("enter smaller number")
            lifee_int-=1
            print("remaining life: ",lifee_int)
            if selec=="hint":
                print("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        elif selec<twrnd:
            print("enter larger number")
            lifee_int-=1
            print("remaining life: ",lifee_int)
            if selec=="hint":
                print("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")       


def game_number():
    
     lives=input("how many lives do you want: ")
     num1=input("first number for random: ")    
     num2=input("second number for random: ")
    
     lives_int=int(lives)
     num1_int=int(num1)
     num2_int=int(num2)
     if num1_int>num2_int:
        print("Error Error Error")
        print("we start over")
        print("first number will be smaller")
        game_number()
    
     rnd=random.randint(num1_int,num2_int)
     #print(rnd) 
     while 2>1:
        num0=int(input("enter your guess: "))
        if num0>rnd:
            print("enter smaller number")
            lives_int-=1
            print("remaining life: ",lives_int)
            if lives_int<=0:
                print("lost the game")
                print("number: ",rnd)
                reply()
                break
        elif num0<rnd:
            print("enter larger number")
            lives_int-=1
            print("remaining life: ",lives_int)
            if lives_int<=0:
                print("lost the game")
                print("number: ",rnd)
                reply()
                break
        elif num0==rnd:
            print("bingooooo")
            print("remaining life: ",lives_int)
            reply()
            break
        
def reply():
   a=input("do you want to play again ")
   if a=="yes":
       start()
   elif a=="no":
       print("good bye")
       
start()