import random

def rock_paper_scissors():
    print("Let's play Rock paper Scissors\n")
    
    r = "rock"
    p = "paper" 
    s = "scissors"
    all_choices = (r, p, s)
    
    user = input(f"Enter a choice ({r}, {p}, {s}): ")
    
    if user not in all_choices:
        print("\Invalid choice!\n")
        return
    
    computer = random.choice(all_choices)
    print(f"You choose {user}, computer chose {computer}.")
    
    #r>s p>r, s>p
    
    if user == computer:
        print("Tie!\n")
    elif(
        (user == r and computer == s)
        or (user == p and computer == r)
        or (user == s and computer == p)
    ):
        print("You win!\n")
    else:
        print("You Lose!\n")