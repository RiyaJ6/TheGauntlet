import random

def play_game():
    print("-----------------------> ROCK PAPER SCISSORS <----------------")
    print("Welcome dear player - Can you win against a computer?. ")
    print("The RULES are as follows:  ")
    print("   1. Rock vs Scissors - Rock wins!")
    print("   2. Paper vs Rock - Paper wins! ")
    print("   3. Scissors vs Paper - Scissors wins!")
    
    while True: # Main Game Session Loop
        try:
            total_rounds = int(input("\nHow many rounds would you like to play in this set? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Reset scores for the new set of rounds
        user_score = 0
        cpu_score = 0
        choices = ['ROCK', 'PAPER', 'SCISSORS']

        # Loop for the specific number of rounds mentioned
        for current_round in range(1, total_rounds + 1):
            print(f"\n--- ROUND {current_round} OF {total_rounds} ---")
            for index, val in enumerate(choices):
                print(f"{index + 1} - {val}")

            try:
                user_input = int(input("Your choice (1-3): ")) - 1
                if user_input not in [0, 1, 2]:
                    print("❌ Invalid choice! Skipping this round...")
                    continue
                user_choice = choices[user_input]
            except ValueError:
                print("❌ Invalid input! Skipping this round...")
                continue

            cpu_idx = random.randint(0, 2)
            cpu_choice = choices[cpu_idx]

            print(f"Player: {user_choice} | Computer: {cpu_choice}")

            # Win/Loss Logic
            if user_choice == cpu_choice:
                print("🤝 IT'S A DRAW!")
            elif (user_choice == 'ROCK' and cpu_choice == 'SCISSORS') or \
                 (user_choice == 'PAPER' and cpu_choice == 'ROCK') or \
                 (user_choice == 'SCISSORS' and cpu_choice == 'PAPER'):
                print(f"🎉 {user_choice} beats {cpu_choice}! YOU WIN THIS ROUND!")
                user_score += 1
            else:
                print(f"💀 {cpu_choice} beats {user_choice}! COMPUTER WINS THIS ROUND!")
                cpu_score += 1

        # End of the Round Set
        print("\n", "="*30)
        print("SET COMPLETE!")
        print(f"FINAL SCORE - Player: {user_score} | Computer: {cpu_score}")
        
        if user_score > cpu_score:
            print("🏆 RESULT: YOU ARE THE CHAMPION!")
        elif cpu_score > user_score:
            print("📉 RESULT: THE MACHINE HAS DEFEATED YOU.")
        else:
            print("⚖️  RESULT: A PERFECT STALEMATE.")
        print("="*30)

        # Ask to play again only after all rounds are finished
        repeat = input("\nThou human wish to repeat thy misery again? (y/n): ").lower()
        if repeat != 'y':
            print("HMM.. GOOD CHOICE PLAYER. SEE YOU AGAIN!")
            break
        else:
            print("\nWELL LETS SEE HOW THIS GOES.. PREPARING NEXT SET.")

if __name__ == "__main__":
    play_game()
