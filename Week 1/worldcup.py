import random

# Customise your team

print(f"Enter your country name or leave blank to choose from preset: ")
country = input().strip()
if country == "":
    print(
        f"Choose a country from the preset list: 1. Uganda, 2. South Africa, 3. Brazil, 4. Ghana, 5. Kenya"
    )
    country = input("Enter your choice (1-5): ").strip()
    if country == "1":
        country = "Uganda"
    elif country == "2":
        country = "South Africa"
    elif country == "3":
        country = "Brazil"
    elif country == "4":
        country = "Ghana"
    elif country == "5":
        country = "Kenya"
else:
    print(f"You have chosen: {country}")


# TEAM ATTRIBUTES
print(f"Customise your team attributes")
print(
    f"Pick between strength oriented, fitness oriented, morale oriented, or balanced team"
)
orientation = int(input("Enter your choice between 1 - 4): "))
print()
if orientation == 1:
    team_strength = random.randint(80, 100)
    fitness = 40
    morale = 40
elif orientation == 2:
    team_strength = random.randint(60, 80)
    fitness = random.randint(80, 100)
    morale = 40
elif orientation == 3:
    team_strength = random.randint(55, 75)
    fitness = random.randint(40, 60)
    morale = random.randint(80, 100)
elif orientation == 4:
    team_strength = random.randint(60, 80)
    fitness = random.randint(40, 60)
    morale = random.randint(40, 60)
else:
    print("Invalid choice. Defaulting to balanced team.")
    team_strength = random.randint(60, 80)
    fitness = random.randint(40, 60)
    morale = random.randint(40, 60)


form = 50

group_points = 0

print("----Welcome to the World Cup Simulation!----")
print(f"Selected Country: {country}")

# --------------------------
# GROUP STAGE
# --------------------------
intense = 0

for match in range(1, 4):

    print(f"\nGROUP MATCH {match}")

    print("1. Intensive Training")
    print("2. Recovery")
    print("3. Team Bonding\n")

    choice = int(input("Choose preparation: "))

    if choice == 1:
        match intense:
            case 1:
                form += 5
                fitness += 20
                intense = 2
            case 2:
                form -= 10
                fitness -= 10
            case _:
                form += 10
                fitness -= 5
                intense = 1

    elif choice == 2:
        match intense:
            case 1:
                fitness += 20
                form += 2
                intense = 2
            case 2:
                fitness += 10
                form += 1
            case _:
                fitness += 15
                intense = 1

    elif choice == 3:
        match intense:
            case 1:
                morale += 15
                form += 2
                intense = 2
            case 2:
                morale += 10
                fitness += 5
            case _:
                morale += 12
                intense = 1

    # Calculate team power

    print(
        f"Current fitness: {fitness}\nCurrent form: {form}\nCurrent intensity: {intense}\n"
    )

    team_power = team_strength + form * 0.3 + fitness * 0.2 + morale * 0.2

    if orientation == 1:
        opponent_power = random.randint(115, 135)
    elif orientation == 2:
        opponent_power = random.randint(100, 130)
    elif orientation == 3:
        opponent_power = random.randint(90, 110)
    else:
        opponent_power = random.randint(100, 120)

    print(f"Your Power: {team_power:.1f}")
    print(f"Opponent Power: {opponent_power}")

    # Match result

    if team_power > opponent_power:
        print("WIN")
        group_points += 3

    elif abs(team_power - opponent_power) <= 3:
        print("DRAW")
        group_points += 1
    else:
        print("LOSS")

print("\nGROUP STAGE COMPLETE")
print("Points:", group_points)

# --------------------------
# QUALIFICATION CHECK
# --------------------------

qualified = False

if group_points >= 7:
    qualified = True

elif group_points >= 5:
    if team_power > opponent_power:
        qualified = True

if qualified:
    print("Qualified for Round of 32")
else:
    print("Eliminated")
    exit()

# --------------------------
# KNOCKOUT STAGE
# --------------------------

print("\n====================================")
print("KNOCKOUT TOURNAMENT BEGINS")
print("====================================\n")

opponent_names = [
    "France",
    "Germany",
    "Spain",
    "Italy",
    "Netherlands",
    "Argentina",
    "Belgium",
    "England",
    "Portugal",
    "Japan",
    "Australia",
    "Mexico",
    "Senegal",
    "Croatia",
    "Switzerland",
    "Denmark",
    "Sweden",
    "Norway",
    "Poland",
    "Russia",
    "Morocco",
    "Saudi Arabia",
    "Iran",
    "South Korea",
    "Thailand",
    "Vietnam",
    "Turkey",
    "Greece",
    "Czech Republic",
    "Austria",
    "Ireland",
]

rounds = [
    {"name": "Round of 32", "opponent_range": (100, 120)},
    {"name": "Quarterfinals", "opponent_range": (110, 130)},
    {"name": "Semifinals", "opponent_range": (120, 140)},
    {"name": "Final", "opponent_range": (130, 150)},
]

fatigue = 0
consecutive_wins = 0
knockout_stage = True
used_opponents = []

for round_info in rounds:
    if not knockout_stage:
        break

    # Pick random opponent that hasn't been used
    available_opponents = [
        name for name in opponent_names if name not in used_opponents
    ]
    opponent_name = random.choice(available_opponents)
    used_opponents.append(opponent_name)

    print(f"\n{round_info['name'].upper()}")
    print(f"Facing: {opponent_name}")
    print("1. Aggressive Push (more power, more fatigue)")
    print("2. Tactical Rest (recover, less fatigue)")
    print("3. Mental Preparation (better shootout odds)")

    # CONTROL FLOW EXAMPLE 1: Validate input with continue
    while True:
        try:
            choice = int(input("Choose preparation (1-3): "))
            if choice not in [1, 2, 3]:
                print("Invalid choice! Pick 1, 2, or 3.")
                continue  # Skip back to input prompt
            break  # Exit while loop when valid
        except ValueError:
            print("Please enter a number.")
            continue  # Skip back to input prompt

    team_power_adjusted = team_power - (fatigue * 0.5)
    momentum_bonus = consecutive_wins * 2
    team_power_adjusted += momentum_bonus

    if choice == 1:
        # Aggressive Push: temporary boost but adds fatigue
        team_power_adjusted += 5
        fatigue += 1.5

    elif choice == 2:
        # Tactical Rest: reduce fatigue penalty
        fatigue = max(0, fatigue - 0.5)

    elif choice == 3:
        # Mental Preparation: boosts morale for shootout advantage
        morale += 5

    opponent_power = random.randint(*round_info["opponent_range"])

    print(
        f"Your Power: {team_power_adjusted:.1f} (Fatigue: {fatigue:.1f}, Wins: {consecutive_wins})"
    )
    print(f"Opponent Power: {opponent_power}")

    # Match result
    if team_power_adjusted > opponent_power:
        print(f"✓ WON {round_info['name']}!")
        consecutive_wins += 1

    else:
        # Check for penalty shootout if close
        power_diff = abs(team_power_adjusted - opponent_power)

        if power_diff <= 5:
            shootout_chance = 0.5 + (morale * 0.01)  # Morale helps shootout odds
            print(f"Close match! Penalty shootout...")

            if random.random() < shootout_chance:
                print(f"✓ WON {round_info['name']} on penalties!")
                consecutive_wins += 1

            else:
                print(f"✗ LOST {round_info['name']} on penalties")
                knockout_stage = False

        else:
            print(f"✗ LOST {round_info['name']}")
            knockout_stage = False

    fatigue += 1

# Final outcome
print("\n------------------------------------")
if consecutive_wins == 4:
    print(f"🏆 WORLD CUP CHAMPIONS! 🏆")
    print(f"Congratulations, {country}!")
elif consecutive_wins == 3:
    print(f"🥈 Runners-up in the Final")
elif consecutive_wins == 2:
    print(f"🥉 Semifinals - Third Place Playoff")
elif consecutive_wins == 1:
    print(f"Quarterfinals - Better Luck Next Time")
else:
    print(f"Eliminated in Round of 32")
print(f"Final Win Streak: {consecutive_wins}")
print("=====================================")
