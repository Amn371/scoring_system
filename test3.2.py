
questions = [
    ("what is my name? ","amn"),
    ("what is my year of birth ", "2007"),
    ("where am I from ?", "egypt"),
    ("say my name.", "amn")
]

win_score=25
start_score=10


def ask_to_restart():
    choice = input("do you want to play again? (y/n)").strip().lower()
    return choice == "y"



while True:
    total_score=start_score
    x=0 
    print("\n--- Welcome to the Quiz Game! ---")
    print(f"You start with {start_score}  points. Try not to lose them all!  reach {win_score} to win early\n")


    while x <len(questions):
        the_question, correct_answer = questions[x]
        print(f"Question {x + 1}: {the_question}")
        user_answer = input("Your answer: ").strip().lower()

        


        if user_answer == correct_answer:
            print("Correct!")
            total_score += 5  
        else:
            print(f"Wrong! The correct answer was '{correct_answer}'.")
            total_score -= 5 
        print(f"Your current score: {total_score}\n")




        if total_score <= 0:
            print("You lost all your points!\n")
            if ask_to_restart():
                break
            else:
                print("thanks for playing ")
                exit()




        if total_score >= win_score:
            print(f"awesome u reached {total_score} to win early")  
            if ask_to_restart():
                break
            else:
                print("thx for playing" )  
                exit()
        

        x +=1
    if x==len(questions):
            if total_score>0:
                print(f"u finished all the questions with {total_score}")
                if ask_to_restart():
                    continue
                else:
                    print("thx for playing")
                    break
            else:
                print("u finish and has no point left ")
                if ask_to_restart():
                    continue
                else:
                    print("thx for playing")
        
                    break
        

