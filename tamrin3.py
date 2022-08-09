import pyfiglet
from typing import Dict

result = pyfiglet.figlet_format('   nasrin dictionary'   , font = 'digital')
print(result)
WORDS = []

def file_to_list():
        try:
                file = open('database.txt' , 'r')
                my_words = file.read().split('\n')
                for i in range(len(my_words)):
                        #dict = {}
                        if i % 2 == 0:
                                dict = {}
                                dict['english'] = my_words[i]
                        else:
                                dict['persian'] = my_words[i]
                                WORDS.append(dict)
        except:
                print('Cant find file. ')        

def show_menu( ) :
    print (      "menu dic ")
    print ("1- add new word to dic ")
    print ("2- translate persian to english in dic ")
    print ("3- translate english to persian in dic ")
    print ("4- exit dic ")

dict_translate=[]
def load():
   print("LOADING...")
   load=open("database.txt","r")


   for i in range (len(dict_translate)):
        file_translate={}
        if i % 2 == 0:
           load[i]=file_translate["english"]
        else:
            load[i]=file_translate["pershian"]
            dict_translate.append(file_translate)

def Add_a_word():
    english=input(" Please put the English word to add : ")
    pershian=input("Please put the meaning : ")
    dict_translate.append({"english" : english ,"persian" : pershian})
    file_translate=open("translate.txt" , "a")
    file_translate.write("\n" + english) 
    file_translate.write("\n" + pershian )
    print(" its done , word added !)")
    file_translate.close()


def translate_english_to_persian():
        sentences = input('Please enter your sentence: ')
        translate_to_persian = ' '
        sentence = sentences.split('.')
        for i in range(len(sentence)):
                word = sentence[i].split(' ')
                for z in range(len(word)):
                        for j in range(len(WORDS)):
                                if WORDS[j]['english'] == word[z]:
                                        if z == len(word)-1:
                                                translate_to_persian += WORDS[j]['persian'] + '.'
                                        else:
                                                translate_to_persian += WORDS[j]['persian'] + ' '  
        print('Translate: ' , translate_to_persian)

def translate_persian_to_english():
        sentences = input('Please enter your sentence: ')
        translate_to_english = ''
        sentence = sentences.split('.')
        for i in range(len(sentence)):
                word = sentence[i].split(' ')
                for z in range(len(word)):
                        for j in range(len(WORDS)):
                                if WORDS[j]['persian'] == word[z]:
                                        if z == len(word)-1:
                                                translate_to_english += WORDS[j]['english'] + '.'
                                        else:
                                                translate_to_english += WORDS[j]['english'] + ' '  
        print('Translate: ' , translate_to_english)


def exit_Dictionary():
    while True:
        save_item = input("Do You Want to Save Please Enter s ")
        if save_item=="s":
            break

while True:
        show_menu()
        file_to_list()
        choice = int(input('Please choose which one: '))
        if choice == 1:
                Add_a_word()
        elif choice == 2:
                translate_english_to_persian()
        elif choice == 3:
                translate_persian_to_english()
        elif choice == 4:
                exit()
        else:
                print('Try again. ')