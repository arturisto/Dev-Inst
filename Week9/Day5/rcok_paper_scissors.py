import random


def print_output(score_computer, score_user, draw):
    print(f"""
            The score is as follows:
            User Score:    {score_user}
            Computer Score:{score_computer}
            Draws:         {draw}
    """)


def game():
    print("""
        Choose you move:
        (r) - rock
        (p) - paper
        (s) - scissors
    """)
    user_input = input(">>")

    if user_input not in ["r","p","s"]:
        print("wrong input, try again")
    else:

        computer_choice = random.choice(["rock","paper","scissors"])

        # draw cases
        if computer_choice == user_input:
            print(f"computer also chose {computer_choice} , it's a draw")
            return "draw"
        # computer wins cases
        if (computer_choice == "rock" and user_input == "s") or (computer_choice == "paper" and user_input == "r") or (
                computer_choice == "scissors" and user_input == "p"):
            print(f"computer chose {computer_choice} , he wins")
            return "computer"
        else:
            print(f"computer chose {computer_choice} , you win")
            return "user"
    return None

def main():
    score_computer = 0
    score_user = 0
    draw = 0
    while True:
        print("""Menu:
                (g) - play a game
                (s) - show current score
                (x) - exit game
                you choice: 
        """)
        user_input = input(">>")

        if user_input not in ['g','s','x']:
            print("wrong input, try again")
        elif user_input == "x":
            print_output(score_computer, score_user, draw)
            break
        elif user_input == "s":
            print_output(score_computer, score_user, draw)
        else:
            winner = game()
            if winner == "draw":
                draw += 1
            elif winner == "computer":
                score_computer += 1
            elif winner == "user":
                score_user += 1


if __name__ == "__main__":
    main()
