# ============================================================
# Program 15: Rock Paper Scissors Game
# Concepts: random module, conditionals, loops, functions, scores
# ============================================================

import random  # Used to generate the computer's random choice

# All valid moves for the game
CHOICES = ["rock", "paper", "scissors"]

# Emoji mapping for display
EMOJI = {
    "rock":     "🪨 Rock",
    "paper":    "📄 Paper",
    "scissors": "✂️  Scissors",
}

# Win rules: key beats value
# Rock beats Scissors, Scissors beats Paper, Paper beats Rock
WIN_RULES = {
    "rock":     "scissors",
    "scissors": "paper",
    "paper":    "rock",
}


def get_computer_choice():
    """Randomly pick rock, paper, or scissors for the computer."""
    return random.choice(CHOICES)


def determine_winner(player, computer):
    """
    Determine the winner of a round.
    Returns 'player', 'computer', or 'tie'.
    """
    if player == computer:
        return "tie"
    elif WIN_RULES[player] == computer:
        return "player"  # Player wins
    else:
        return "computer"  # Computer wins


def display_scoreboard(player_score, computer_score, ties):
    """Print the current scoreboard."""
    print(f"\n📊 Score → You: {player_score}  |  Computer: {computer_score}  |  Ties: {ties}")


def main():
    print("=" * 45)
    print("   🎮  Rock Paper Scissors Game  🎮")
    print("=" * 45)
    print("Best of as many rounds as you want!\n")

    # Score tracking
    player_score   = 0
    computer_score = 0
    ties           = 0

    while True:
        print("\nChoices: rock | paper | scissors | quit")
        player_input = input("Your move: ").strip().lower()

        # Quit condition
        if player_input == "quit":
            print("\n🏁 Game Over!")
            display_scoreboard(player_score, computer_score, ties)
            if player_score > computer_score:
                print("🏆 You WIN the overall game! Great job!")
            elif computer_score > player_score:
                print("🤖 Computer wins the overall game. Better luck next time!")
            else:
                print("🤝 It's an overall TIE!")
            break

        # Validate input
        if player_input not in CHOICES:
            print("⚠️  Invalid choice. Type rock, paper, scissors, or quit.")
            continue

        # Computer picks
        computer_choice = get_computer_choice()

        # Show choices
        print(f"\n  You chose    : {EMOJI[player_input]}")
        print(f"  Computer chose: {EMOJI[computer_choice]}")

        # Determine winner
        result = determine_winner(player_input, computer_choice)
        if result == "player":
            print("  ✅ You WIN this round!")
            player_score += 1
        elif result == "computer":
            print("  ❌ Computer WINS this round!")
            computer_score += 1
        else:
            print("  🤝 It's a TIE!")
            ties += 1

        # Show running score
        display_scoreboard(player_score, computer_score, ties)


if __name__ == "__main__":
    main()
