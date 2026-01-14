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

    work_location = None
    if is_workday:
        # Determine which day of the week it is
        day_of_week = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        print_slow(f"\nYou remember... it's a {day_of_week}!")

        # Office days: Tue, Wed, Thu | WFH days: Mon, Fri
        if day_of_week in ['Tuesday', 'Wednesday', 'Thursday']:
            work_location = 'office'
            print_slow("You need to be at the office by 9 AM.")
        else:
            work_location = 'wfh'
            print_slow("You're working from home today - no commute!")
    else:
        print_slow("\nYou remember... it's a WEEKEND!")
        print_slow("No obligations today - the whole day is yours!")

    print_divider()
    return morning_routine(is_workday, work_location)


def morning_routine(is_workday, work_location=None):
    """Handle the morning routine choices."""
    print_slow("What do you want to do first?")

    if is_workday:
        print("\n1. Hit snooze and sleep a bit more")
        print("2. Get up immediately and check your phone")
        print("3. Stretch and do some morning exercises")

        choice = get_choice(['1', '2', '3'])

        if choice == '1':
            return snooze_choice(is_workday, work_location)
        elif choice == '2':
            return check_phone_choice(is_workday, work_location)
        else:
            return exercise_choice(is_workday, work_location)
    else:
        # Weekend choices - personalized!
        print("\n1. Hit snooze and sleep a bit more")
        print("2. Get up and check on the kids")
        print("3. Put Koda in the backyard")

        choice = get_choice(['1', '2', '3'])

        if choice == '1':
            return snooze_choice(is_workday, work_location)
        elif choice == '2':
            return check_on_kids()
        else:
            return let_koda_out()


def snooze_choice(is_workday, work_location=None):
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
            if work_location == 'office':
                print_slow("You barely make it to the office on time, but you're exhausted.")
                print_slow("The commute while stressed was rough!")
                return "rushed_office_day"
            else:  # WFH
                print_slow("At least you're working from home - no commute!")
                print_slow("You log in just in time, still in your pajamas.")
                return "rushed_wfh_day"
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


def check_phone_choice(is_workday, work_location=None):
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
            if work_location == 'office':
                print_slow("You finish the report but now you're definitely late!")
                print_slow("At least your boss is happy... but the commute will be rushed.")
                return "productive_but_late_office"
            else:  # WFH
                print_slow("You finish the report and just walk to your home office.")
                print_slow("Your boss is happy and you didn't even need to change!")
                return "productive_wfh_day"
        else:
            print_divider()
            if work_location == 'office':
                print_slow("You decide it can wait until you get to the office.")
                print_slow("You get ready at your own pace and have a calm morning commute.")
                return "balanced_office_day"
            else:  # WFH
                print_slow("You decide it can wait until you log in.")
                print_slow("You make a nice breakfast first - perks of working from home!")
                return "balanced_wfh_day"
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


def exercise_choice(is_workday, work_location=None):
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
            if work_location == 'office':
                print_slow("You arrive at the office early, energized, and ready!")
                print_slow("Your colleagues comment on your positive energy.")
                return "perfect_office_day"
            else:  # WFH
                print_slow("You start your work-from-home day feeling energized!")
                print_slow("You're productive and focused all day.")
                return "perfect_wfh_day"
        else:
            print_divider()
            print_slow("You take your time making a delicious breakfast.")
            if work_location == 'office':
                print_slow("You enjoy every bite and still make it to the office on time.")
                print_slow("It's a great start to your day!")
                return "great_office_day"
            else:  # WFH
                print_slow("You enjoy every bite at your own pace.")
                print_slow("You log in on time, relaxed and happy. WFH mornings are the best!")
                return "great_wfh_day"
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


def check_on_kids():
    """Handle checking on the kids choice."""
    print_divider()
    print_slow("You quietly get out of bed and walk down the hallway.")
    print_slow("You peek into the kids' rooms...")
    time.sleep(1)

    # Random scenario
    scenario = random.choice(['sleeping', 'awake', 'mischief'])

    if scenario == 'sleeping':
        print_slow("\nThey're both still sleeping peacefully.")
        print_slow("You smile and head back to enjoy the quiet morning.")
        print("\nWhat do you do next?")
        print("1. Make yourself a nice breakfast")
        print("2. Start a load of laundry while it's quiet")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You make a delicious breakfast and enjoy it in peace.")
            print_slow("When the kids wake up, you're refreshed and ready for family time!")
            return "peaceful_parent_weekend"
        else:
            print_divider()
            print_slow("You tackle some chores while the house is quiet.")
            print_slow("You feel accomplished and ahead of the day!")
            return "productive_parent_weekend"

    elif scenario == 'awake':
        print_slow("\nThey're awake! Both jumping on the bed excitedly.")
        print_slow("'Can we have pancakes? Can we go to the park?'")
        print("\nWhat do you do?")
        print("1. Make pancakes together")
        print("2. Promise the park after breakfast")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You all head to the kitchen for a pancake-making adventure.")
            print_slow("There's flour everywhere, but the memories are priceless!")
            return "fun_parent_weekend"
        else:
            print_divider()
            print_slow("You make a quick breakfast and head to the park.")
            print_slow("The kids burn off energy and you all have a great day!")
            return "active_parent_weekend"

    else:  # mischief
        print_slow("\nUh oh... they're already awake and suspiciously quiet.")
        print_slow("You find them in the bathroom with shaving cream everywhere!")
        print("\nHow do you react?")
        print("1. Laugh it off and start the cleanup")
        print("2. Sigh and ask them to help clean up")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You can't help but laugh at their creativity.")
            print_slow("You take photos and turn cleanup into a game!")
            print_slow("It becomes a funny family memory.")
            return "chaotic_fun_weekend"
        else:
            print_divider()
            print_slow("You teach them responsibility by having them help clean.")
            print_slow("It takes longer, but they learn an important lesson.")
            return "teaching_moment_weekend"


def let_koda_out():
    """Handle letting Koda out choice."""
    print_divider()
    print_slow("You hear Koda's tail thumping against his bed.")
    print_slow("He's already awake and ready to go outside!")
    time.sleep(0.5)
    print_slow("\nYou open the back door and Koda bounds into the yard.")

    # Random scenario
    scenario = random.choice(['peaceful', 'squirrel', 'zoomies'])

    if scenario == 'peaceful':
        print_slow("\nKoda calmly explores the yard, sniffing around.")
        print_slow("You enjoy your coffee on the back porch, watching him.")
        print("\nWhat do you do next?")
        print("1. Stay outside and enjoy the morning air")
        print("2. Head back in and make a nice breakfast")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You and Koda enjoy a peaceful morning outside.")
            print_slow("It's the perfect way to start the weekend!")
            return "serene_morning_weekend"
        else:
            print_divider()
            print_slow("You make a delicious breakfast while Koda plays.")
            print_slow("You feel relaxed and ready for the day ahead.")
            return "relaxed_morning_weekend"

    elif scenario == 'squirrel':
        print_slow("\nSuddenly, Koda spots a squirrel!")
        print_slow("He takes off running and barking at full speed!")
        print_slow("The squirrel escapes up a tree and Koda circles below, tail wagging.")
        print("\nWhat do you do?")
        print("1. Let him enjoy the excitement")
        print("2. Call him back inside before he wakes the neighbors")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You let Koda enjoy his morning adventure.")
            print_slow("He eventually tires out and comes back happy and exhausted.")
            print_slow("A tired dog makes for a peaceful weekend!")
            return "adventurous_dog_weekend"
        else:
            print_divider()
            print_slow("You call Koda back and he reluctantly obeys.")
            print_slow("You give him treats and play inside instead.")
            print_slow("Crisis averted - the neighbors are still asleep!")
            return "responsible_dog_parent_weekend"

    else:  # zoomies
        print_slow("\nKoda suddenly gets the zoomies!")
        print_slow("He races around the yard in wild circles at full speed!")
        print_slow("You can't help but laugh at his pure joy.")
        print("\nWhat do you do?")
        print("1. Join in and run around with him")
        print("2. Record it - this is too funny not to capture")

        choice = get_choice(['1', '2'])

        if choice == '1':
            print_divider()
            print_slow("You run around the yard with Koda!")
            print_slow("Your neighbors think you're crazy, but you don't care.")
            print_slow("You both get great exercise and have a blast!")
            return "playful_morning_weekend"
        else:
            print_divider()
            print_slow("You capture the moment on video.")
            print_slow("Later, you share it and it becomes a hit with friends!")
            print_slow("Koda's zoomies bring joy to everyone's day.")
            return "viral_dog_moment_weekend"


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
