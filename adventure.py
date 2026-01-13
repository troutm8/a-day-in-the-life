#!/usr/bin/env python3
"""
A Day in the Life - Text Adventure Game
A simple choose-your-own-adventure game where you navigate through a day.
"""

import random
import sys
import time


def print_slow(text, delay=0.03):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_divider():
    """Print a divider line."""
    print("\n" + "=" * 60 + "\n")


def get_choice(options):
    """Get a valid choice from the user."""
    while True:
        choice = input("\nYour choice: ").strip()
        if choice in options:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(options)}")


def wake_up_scene(is_workday):
    """The initial wake-up scene."""
    print_divider()
    print_slow("You slowly open your eyes as sunlight filters through the curtains.")
    print_slow("Your alarm buzzes insistently on the nightstand.")
    time.sleep(0.5)

    day_type = "WORKDAY" if is_workday else "WEEKEND"
    print_slow(f"\nYou remember... it's a {day_type}!")

    if is_workday:
        print_slow("You have to be at the office by 9 AM.")
    else:
        print_slow("No obligations today - the whole day is yours!")

    print_divider()
    return morning_routine(is_workday)


def morning_routine(is_workday):
    """Handle the morning routine choices."""
    print_slow("What do you want to do first?")
    print("\n1. Hit snooze and sleep a bit more")
    print("2. Get up immediately and check your phone")
    print("3. Stretch and do some morning exercises")

    choice = get_choice(['1', '2', '3'])

    if choice == '1':
        return snooze_choice(is_workday)
    elif choice == '2':
        return check_phone_choice(is_workday)
    else:
        return exercise_choice(is_workday)


def snooze_choice(is_workday):
    """Handle the snooze button choice."""
    print_divider()
    print_slow("You hit the snooze button and drift back to sleep...")
    time.sleep(1)
    print_slow("*10 minutes later*")

    if is_workday:
        print_slow("\nOh no! You're running late now!")
        print_slow("You jump out of bed in a panic.")
        print("\nWhat do you do?")
        print("1. Skip breakfast and rush to get ready")
        print("2. Call in sick and go back to sleep")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You rush through your morning routine.")
            print_slow("You make it to work just in time, but you're exhausted.")
            print_slow("\nYou survived the day, barely!")
            return "rushed_workday"
        else:
            print_divider()
            print_slow("You call your boss and fake a cough.")
            print_slow("'I think I have a cold,' you say convincingly.")
            print_slow("You spend the rest of the day relaxing guilt-free!")
            return "sick_day"
    else:
        print_slow("\nYou wake up feeling refreshed.")
        print_slow("The extra sleep was exactly what you needed!")
        print_slow("You have the whole day ahead of you.")
        return "relaxed_weekend"


def check_phone_choice(is_workday):
    """Handle checking phone choice."""
    print_divider()
    print_slow("You grab your phone from the nightstand.")
    print_slow("You scroll through notifications...")

    if is_workday:
        print_slow("\nYou see an urgent email from your boss!")
        print_slow("'Need that report ASAP!'")
        print("\nWhat do you do?")
        print("1. Start working on it from bed")
        print("2. Ignore it for now and get ready normally")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You spend an hour working from bed.")
            print_slow("You finish the report but now you're definitely late!")
            print_slow("At least your boss is happy...")
            return "productive_but_late"
        else:
            print_divider()
            print_slow("You decide it can wait until you get to the office.")
            print_slow("You get ready at your own pace and have a calm morning.")
            return "balanced_workday"
    else:
        print_slow("\nYou see messages from friends wanting to hang out!")
        print_slow("'Beach day? Coffee? Movie marathon?'")
        print("\nWhat do you do?")
        print("1. Say yes to everything - FOMO is real!")
        print("2. Politely decline and enjoy a solo day")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You text everyone back with enthusiasm.")
            print_slow("You have an amazing day filled with friends and fun!")
            return "social_weekend"
        else:
            print_divider()
            print_slow("You decide today is a self-care day.")
            print_slow("You enjoy your own company and recharge.")
            return "peaceful_weekend"


def exercise_choice(is_workday):
    """Handle morning exercise choice."""
    print_divider()
    print_slow("You roll out of bed and stretch your arms above your head.")
    print_slow("You do some light exercises and feel energized!")

    if is_workday:
        print_slow("\nYou feel great and ready to tackle the day!")
        print_slow("You have time for a proper breakfast before work.")
        print("\nWhat do you make?")
        print("1. Quick smoothie")
        print("2. Full breakfast with eggs and toast")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You blend up a delicious smoothie.")
            print_slow("You arrive at work early, energized, and ready!")
            print_slow("Your colleagues comment on your positive energy.")
            return "perfect_workday"
        else:
            print_divider()
            print_slow("You take your time making a delicious breakfast.")
            print_slow("You enjoy every bite and still get to work on time.")
            print_slow("It's a great start to your day!")
            return "great_workday"
    else:
        print_slow("\nYou feel motivated to make the most of your free day!")
        print("\nWhat do you want to do?")
        print("1. Go for a run or hit the gym")
        print("2. Do some yoga at home")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You go for an invigorating run!")
            print_slow("The fresh air and exercise make you feel alive.")
            print_slow("You spend the rest of the day feeling accomplished!")
            return "active_weekend"
        else:
            print_divider()
            print_slow("You roll out your yoga mat and practice mindfully.")
            print_slow("You feel centered and at peace.")
            print_slow("It's a perfect mindful weekend!")
            return "mindful_weekend"


def main():
    """Main game function."""
    print_divider()
    print_slow("Welcome to 'A Day in the Life' - A Text Adventure Game", delay=0.05)
    print_divider()

    time.sleep(0.5)

    # Randomly determine if it's a workday or weekend
    is_workday = random.choice([True, False])

    # Start the game
    ending = wake_up_scene(is_workday)

    # Show ending
    print_divider()
    print_slow("THE END", delay=0.1)
    print_divider()
    print(f"\nYou reached the '{ending}' ending!")
    print("\nThanks for playing! Run the game again for a different experience.")
    print_divider()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
