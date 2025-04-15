import json
import random 

#Loading Flashcards 
def load_flashcards(filename):
    try:
        with open(filename,'r') as f:
            return json.load(f)
    except FileExistsError:
        return []
    
#Saving Flashcards
def save_flashcards(flashcards,filename):
    with open(filename,'w') as f:
        json.dump(flashcards,f)

#Quiz 
def take_quiz(flashcards):
    if not flashcards:
        print('No Flashcards!')
        return
    
    random.shuffle(flashcards)
    for card in flashcards:
        answer = input(f'Q:{card['question']} \nYour Answer')
