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
    print_slow("The alarm on your iPhone buzzes insistently on the nightstand.")
    time.sleep(0.5)

    # Determine the season
    season = random.choice(['Spring', 'Summer', 'Fall', 'Winter'])
    print_slow(f"\nYou look outside... it's {season}.")

    work_location = None
    is_school_day = False
    is_summer_vacation = False
    at_cabin = False

    if is_workday:
        # Determine which day of the week it is
        day_of_week = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        print_slow(f"You remember... it's a {day_of_week}!")

        # Office days: Tue, Wed, Thu | WFH days: Mon, Fri
        if day_of_week in ['Tuesday', 'Wednesday', 'Thursday']:
            work_location = 'office'
            print_slow("You need to be at the office by 9 AM.")

            # In Summer, kids are on summer vacation
            if season == 'Summer':
                is_summer_vacation = True
                print_slow("The kids are on summer vacation!")
            else:
                # On office days (non-summer), randomly determine if it's a school day
                is_school_day = random.choice([True, False])
                if is_school_day:
                    print_slow("And the kids have school today!")
        else:
            work_location = 'wfh'
            print_slow("You're working from home today - no commute!")
    else:
        # Determine which weekend day it is
        day_of_week = random.choice(['Saturday', 'Sunday'])
        print_slow(f"You remember... it's a {day_of_week}!")

        # In Winter, randomly determine if at the cabin
        if season == 'Winter':
            at_cabin = random.choice([True, False])
            if at_cabin:
                print_slow("You're at the cabin in the mountains!")
            else:
                print_slow("No obligations today - the whole day is yours!")
        else:
            print_slow("No obligations today - the whole day is yours!")

    print_divider()
    return morning_routine(is_workday, work_location, is_school_day, is_summer_vacation, at_cabin)


def morning_routine(is_workday, work_location=None, is_school_day=False, is_summer_vacation=False, at_cabin=False):
    """Handle the morning routine choices."""

    # Special school day breakfast routine for office days (non-summer)
    if is_workday and work_location == 'office' and is_school_day:
        return school_day_breakfast()

    # Special summer vacation routine - walk Koda before work
    if is_workday and work_location == 'office' and is_summer_vacation:
        return summer_vacation_morning()

    # Special winter cabin routine
    if not is_workday and at_cabin:
        return cabin_weekend_morning()

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


def summer_vacation_morning():
    """Handle summer vacation morning routine - walk Koda before work."""
    print_slow("The kids are sleeping in - it's summer vacation!")
    print_slow("You have some extra time this morning.")
    print_slow("\nWhat do you want to do?")
    print("\n1. Take Koda for a walk before work")
    print("2. Let the kids sleep and enjoy a quiet breakfast")
    print("3. Wake the kids up for a family breakfast")

    choice = get_choice(['1', '2', '3'])

    if choice == '1':
        print_divider()
        print_slow("You grab Koda's leash and head out for a morning walk.")
        print_slow("The summer air is perfect, and Koda is thrilled!")
        time.sleep(0.5)
        print_slow("\nYou walk through the neighborhood, enjoying the quiet morning.")
        print("\nHow long do you walk?")
        print("1. Quick 15-minute walk")
        print("2. Full 30-minute walk")

        sub_choice = get_choice(['1', '2'])

        if sub_choice == '1':
            print_divider()
            print_slow("You keep it short but sweet.")
            print_slow("Koda got his exercise and you still have plenty of time!")
            print_slow("You arrive at the office on time and energized.")
            return "summer_dog_walk_perfect_day"
        else:
            print_divider()
            print_slow("You enjoy the full walk with Koda.")
            print_slow("It's so nice out that you lose track of time!")
            print_slow("You're a bit rushed getting to work, but it was worth it.")
            return "summer_dog_walk_late_day"

    elif choice == '2':
        print_divider()
        print_slow("You make yourself a nice breakfast in the peaceful house.")
        print_slow("You sip your coffee and enjoy the quiet before work.")
        time.sleep(0.5)
        print_slow("\nThe kids wake up just as you're leaving.")
        print_slow("You give them hugs and head to the office feeling relaxed!")
        return "peaceful_summer_morning_office"

    else:  # choice == '3'
        print_divider()
        print_slow("You wake the kids up for a family breakfast.")
        print_slow("They're groggy but happy to see you!")
        time.sleep(0.5)
        print_slow("\nYou make pancakes together - a summer tradition.")
        print("\nWhat happens next?")
        print("1. You're running late but it was worth it")
        print("2. You rush through and make it on time")

        sub_choice = get_choice(['1', '2'])

        if sub_choice == '1':
            print_divider()
            print_slow("The family breakfast took longer than expected.")
            print_slow("You arrive at work late but with a full heart.")
            print_slow("The kids text you photos of their day later!")
            return "summer_family_breakfast_late"
        else:
            print_divider()
            print_slow("You speed through breakfast but make it count.")
            print_slow("Everyone's happy and you make it to work on time!")
            return "summer_family_breakfast_perfect"


def cabin_weekend_morning():
    """Handle winter cabin weekend morning - skiing with kids."""
    print_slow("You're at the cabin and the snow looks perfect!")
    print_slow("The kids are already excited about the day.")
    print_slow("\nWhat's the plan?")
    print("\n1. Take the kids skiing")
    print("2. Build a snowman with the kids")
    print("3. Cozy day inside by the fireplace")

    choice = get_choice(['1', '2', '3'])

    if choice == '1':
        print_divider()
        print_slow("You bundle everyone up and head to the slopes!")
        print_slow("The kids are so excited they can barely sit still.")
        time.sleep(0.5)
        print_slow("\nYou spend the day skiing together.")
        print("\nHow does it go?")
        print("1. Everyone has a blast - perfect ski day")
        print("2. One kid falls and you spend time in the lodge")

        sub_choice = get_choice(['1', '2'])

        if sub_choice == '1':
            print_divider()
            print_slow("The conditions are perfect and everyone skis well!")
            print_slow("You take family photos on the mountain.")
            print_slow("Later, you all enjoy hot chocolate by the fire.")
            print_slow("This is what cabin weekends are all about!")
            return "perfect_cabin_ski_day"
        else:
            print_divider()
            print_slow("One of the kids takes a tumble - nothing serious!")
            print_slow("You spend the afternoon in the lodge with hot cocoa.")
            print_slow("They're disappointed but you make it fun anyway.")
            return "cabin_ski_day_with_break"

    elif choice == '2':
        print_divider()
        print_slow("You all head outside to build a snowman!")
        print_slow("The kids are creative and want to make it huge.")
        time.sleep(0.5)
        print_slow("\nYou work together and build an amazing snowman.")
        print_slow("The neighbors come out to see your creation!")
        print("\nWhat do you do next?")
        print("1. Have a snowball fight")
        print("2. Head inside for hot chocolate")

        sub_choice = get_choice(['1', '2'])

        if sub_choice == '1':
            print_divider()
            print_slow("Epic snowball fight ensues!")
            print_slow("Everyone is laughing and covered in snow.")
            print_slow("You all head inside cold but happy. Perfect day!")
            return "cabin_snowball_fight_day"
        else:
            print_divider()
            print_slow("You head inside and make hot chocolate together.")
            print_slow("You add marshmallows and whipped cream!")
            print_slow("Everyone's warm and happy. Great cabin day!")
            return "cabin_snowman_cocoa_day"

    else:  # choice == '3'
        print_divider()
        print_slow("You decide to stay cozy inside today.")
        print_slow("You light the fireplace and the cabin gets warm and toasty.")
        time.sleep(0.5)
        print_slow("\nThe kids want to play board games.")
        print("\nWhat do you play?")
        print("1. Monopoly - the classic")
        print("2. A quick card game")

        sub_choice = get_choice(['1', '2'])

        if sub_choice == '1':
            print_divider()
            print_slow("You start a game of Monopoly...")
            print_slow("Three hours later, you're still playing!")
            print_slow("Someone flips the board but everyone's laughing.")
            print_slow("It's a hilarious cabin memory!")
            return "cabin_monopoly_chaos_day"
        else:
            print_divider()
            print_slow("You play several rounds of cards.")
            print_slow("The kids are competitive but it's all in good fun!")
            print_slow("Perfect relaxing cabin day by the fire.")
            return "cabin_cozy_card_games_day"


def school_day_breakfast():
    """Handle school day breakfast choices."""
    print_slow("You need to get the kids ready for school and yourself ready for work!")
    print_slow("What's the breakfast plan?")
    print("\n1. Cook breakfast")
    print("2. Cereal for breakfast")
    print("3. Go to the grocery store and Jack In The Box to get breakfast")

    choice = get_choice(['1', '2', '3'])

    if choice == '1':
        print_divider()
        print_slow("You head to the kitchen and start cooking.")
        print_slow("You make scrambled eggs, toast, and some fruit.")
        time.sleep(0.5)
        print_slow("\nThe kids come down and enjoy the hot breakfast.")
        print_slow("It takes a bit longer, but everyone leaves happy and full!")
        print("\nWhat happens next?")
        print("1. You're running a bit late but feeling good")
        print("2. You rushed and made it on time")

        sub_choice = get_choice(['1', '2'])

        if sub_choice == '1':
            print_divider()
            print_slow("You drop the kids off at school with minutes to spare.")
            print_slow("You arrive at the office a few minutes late, but the home-cooked meal was worth it.")
            print_slow("The kids text you a heart emoji at lunch!")
            return "loving_parent_late_to_office"
        else:
            print_divider()
            print_slow("You somehow managed to cook, eat, and get everyone ready on time!")
            print_slow("You're a breakfast superhero. The kids and your boss are both happy.")
            return "superhero_parent_office_day"

    elif choice == '2':
        print_divider()
        print_slow("You pour cereal for everyone - quick and easy!")
        print_slow("The kids are happy with their sugary cereal choice.")
        time.sleep(0.5)
        print_slow("\nYou have plenty of time to get ready.")
        print("\nWhat do you do with the extra time?")
        print("1. Help the kids with their homework they forgot about")
        print("2. Actually enjoy your coffee in peace")

        sub_choice = get_choice(['1', '2'])

        if sub_choice == '1':
            print_divider()
            print_slow("You help them finish up their homework quickly.")
            print_slow("Crisis averted! You drop them off at school with homework in hand.")
            print_slow("You get to the office on time and feeling like parent of the year!")
            return "homework_hero_office_day"
        else:
            print_divider()
            print_slow("You savor your coffee and enjoy the morning chaos.")
            print_slow("Everyone gets out the door on time and stress-free.")
            print_slow("You arrive at the office early and relaxed. Perfect morning!")
            return "peaceful_school_morning_office_day"

    else:  # choice == '3'
        print_divider()
        print_slow("You load the kids in the car and head out.")
        print_slow("First stop: grocery store for essentials.")
        time.sleep(0.5)
        print_slow("The kids grab snacks while you grab milk and bread.")
        print_slow("\nNext stop: Jack In The Box!")
        print_slow("Everyone orders their breakfast favorites.")
        print("\nHow does it go?")
        print("1. Smooth and quick - everyone's happy")
        print("2. The drive-thru is slow and you're cutting it close")

        sub_choice = get_choice(['1', '2'])

        if sub_choice == '1':
            print_divider()
            print_slow("The line moves fast and you get your food quickly.")
            print_slow("The kids eat in the car on the way to school.")
            print_slow("You drop them off, finish your breakfast, and make it to work on time.")
            print_slow("Groceries done, everyone fed, and you're a multitasking champion!")
            return "multitasking_champion_office_day"
        else:
            print_divider()
            print_slow("Of course the line is long today...")
            print_slow("You're stressed but the kids are oblivious, enjoying their food.")
            print_slow("You drop them off just in time but you're definitely late to the office.")
            print_slow("At least you got groceries done and everyone ate!")
            return "chaotic_but_fed_office_day"


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
    print_slow("Welcome to 'A Day in Daddy's Life' - A Text Adventure Game", delay=0.05)
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
