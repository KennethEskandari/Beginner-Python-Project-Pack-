import json
import random 


    #Menu 
def main():
    filename = flashcards.json
    flashcards = load_flashcards(filename)

    while True:
        print("\   -- Flashcard Quiz App ---")
        print("1. Take a quiz")
        print("2. Add a flashcard")
        print("3. Save flashcards")
        print("4. Exit")

        choice = input('Enter Choice!')
        
        if choice == 1:
            take_quiz(flashcards)
        elif choice == 2:
            add_flashcard(flashcards)
        elif choice == 3:
            save_flashcards(flashcards)
        elif choice == 4:
            print('Goodbye!')
            break
        else:
             print("Invalid Choice!")

if __name__ == "__main__":
    main()


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
        answer = input(f'Q:{card['question']} \nYour Answer: ')
        if answer.strip().lower() == card['answer'].strip().lower():
            print("Correct!\n")
        else:
            print('Incorrect!\n')

    #Adding Flashcard
def add_flashcard(flashcards):
    question = input('Enter Question')
    answer = input('Enter Answer')
    flashcards.append({'questions': question, 'answer': answer})
    print("Flashcard Added!\n")

