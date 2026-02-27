import random
# line 197!!!!!!!!!!
# ------class selection-----
def create_player():
    print("Choose your character class:")
    print("⚔️  Warrior - High health, bonus in battle")
    print("🗡️  Rogue - Balanced stats, finds more gold")
    print("🔮 Mage - Low health, high magic damage")
    
    damage=10
    attack=random.randint(5,15)
    choose_character = input("Type your class (warrior/rogue/mage): ").lower()
    # choose_character=random.choices["warrior","rogue","mage"]
    if choose_character == "warrior":
        damage+=5
        print("you got +5 damage")
        health = 100
        gold = 80
        attack_bonus = random.randint(5,15)
        attack+=attack_bonus #print the other shi too
    elif choose_character == "rogue":
        print(f"you got {damage} damage, regular")
        health = 100 
        gold = 100
        gold_bonus_chance = 0.3  # 30% more treasure
    elif choose_character == "mage":
        health = 80
        gold = 90
        magic_power = 10
        damage += magic_power
        attack += magic_power
        print(f"You have {attack} attack power with magic bonus.")
    else:
        print("Invalid class. Defaulting to Adventurer.")
        choose_character = "adventurer"
        health = 100
        gold = 100

    #--------player creation-----

    name = input("Enter your hero name: ")

    player = {
        "name": name,
        "class": choose_character,
        "health": health,
        "gold": gold,
        "bag": [],
        "attack":attack
    }
    player["bag"].append("potion")
    player["bag"].append("potion")
    loot=["potion","elixir","magic ring","dagger","ancient coin"]
    # player["bag"].append(random.choice(loot))
    print(f"\n🧙 Welcome, {player['name']} the {player['class'].title()}!")
    print(f"❤️ Health: {player['health']}, 💰 Gold: {player['gold']}")
    return player

#-----------monster creation-----
def monster_creation():
    monster=random.choice(["kirmara","ravan"])
    monster_health=random.randint(50,100)
    attack_power=random.randint(5,15)
    print(f"monster is {monster}, health is {monster_health}, attacking power is {attack_power}")

    monster= {
        "name": monster,
        "health": monster_health,
        "attack": attack_power
    }
    return monster
# monster_creation()
# create_player()

def use_potion(player):
    if "potion" in player["bag"]:
        heal = random.randint(15, 25)
        player["health"] += heal
        player["bag"].remove("potion")
        print(f"🩹 You healed for {heal} HP! Health is now {player['health']}.")
    else:
        return ("no potion left")
#loot=["potion","elixir","magic ring","dagger","ancient coin"]
def use(player):
    if "elixir" in player["bag"]:
        heal = random.randint(50,100)
        player["health"] += heal
        player["bag"].remove("elixir")
        print("elixir is a magical potion which works like like potion but in better way")
        print(f"You healed for {heal} HP! Health is now{player['health']}.")
    elif "magic ring" in player["bag"]:
        if player["bag"].count("magic ring")==1:
            player["health"]+=100
        else:
            player["health"]+=100
            player["bag"].remove("magic ring")
        print(f"100 health power is added , Health is now{player["health"]}.")
    else:
        print("not in bag currently")
#----------combat loop-----------
def attack(player,monster):
    print(f"\n⚔️ Battle Start: {player['name']} vs {monster['name']}\n")
    while monster["health"] > 0 and player["health"] > 0:
        print(f"❤️ Your Health: {player['health']} | 👹 Monster Health: {monster['health']}")
        action=input(
            "Choose action:\n1.Attack\n2.Use Potion \n3.elixir \n4.magic ring \n5.dagger\n6.Check Bag\n> ").lower()

        if action in ["1","attack"]:
            damage_done=player["attack"]-monster["attack"]
            if player["class"]=="warrior":
                damage_done+=5
            elif player["class"]=="mage":
                damage_done+=3
        
            damage_done=max(0,damage_done)
            monster["health"]-=damage_done
            print(f"\n you attacked the {monster["name"]} for {damage_done} damage")
        elif action in ["2", "use potion"]:
            print("okay, potion here")
            use_potion(player)
        elif action in ["3","elixir"]:
            print("okay , here is elixir")
            use(player)
        elif action in ["4","magic ring"]:
            print("okay, ,magic ring here")
            use(player)
        elif action in ["5","dagger"]:
            if "dagger" in player["bag"]:
                print("okay , dagger is here")
                damage_done+=10
                print("it provides more damage no matter what class")
            else:
                print("not in bag  currently ")
        elif action in ["6", "check bag"]:
            print(f"🎒 Inventory: {player['bag']}")

        # Monster counterattack
        if monster["health"] > 0:
            damage_received = random.randint(5, 12)
            player["health"] -= damage_received
            print(f"👹 {monster['name']} attacks! You lose {damage_received} HP.")

    # Determine outcome
    if monster["health"] <= 0 and player["health"] > 0:
        print(f"\n🎉 You defeated the {monster['name']}!")
        return "win"
    elif player["health"] <= 0:
        print(f"\n💀 You were slain by the {monster['name']}...")
        return "lose"
    else:
        print("⚔️ It's a draw!")
        return "draw"
#---------post-battle rewards-------
def reward(player):
    # if monster["health"]<=0:
    #     won=player["name"]
    #     remain_health=player["health"]
        print("\nloot time")
        base_gold = random.randint(20, 50)
        bonus_gold = 0
        if player["class"] == "rogue":
            bonus_gold = int(base_gold * 0.3)
            print("🗡️ Rogue bonus! +30% gold.")
        
        total_gold = base_gold + bonus_gold
        player["gold"] += total_gold
        print(f"💰 You defeated the monster and found {total_gold} gold!")
        print(f"🎉 New gold total: {player['gold']}")

        loot = ["potion", "elixir", "magic ring", "dagger", "ancient coin"]
        item=random.choice(loot)
        player["bag"].append(item)
        print(f"You found {item} and added it to your bag.")
        if item=="magic ring" and player["class"]=="mage":
            boost=random.randint(5,10)
            player["attack"]+=boost
            print(f"🔮 The magic ring boosts your magic! +{boost} attack. Total attack: {player['attack']}")
        # player["bag"].append(item)
        # print(f"you found {item} and added to bag")
        # print(player["bag"])

def shopinventory(player):
    shop = {
        "potion": 25,
        "elixir": 40,
        "magic ring": 80,
        "dagger": 50
    }
    print("after the battle")
    while True:
        choice=input("1.view items and prices\n2.choose to buy\nwhen you are done type exit: \n")

        if choice in ["1","view"]:
            print(f"the available are:")
            for item, price in shop.items():
                if player["gold"]>=price:
                    print(f"- {item.title()} : {price} gold")
            print(f"💰 Your gold: {player['gold']}")

        if choice in ["2","choose to buy"]:
            item=input("enter the item you want to buy: ").lower()
            if item not in shop:
                print(f"{item}not in shop")
                continue

            if player["gold"]<=0:
                print(f"you dont have enough gold, {player["gold"]}gold")
                break
            else:
                player['gold']-=shop[item]
                player['bag'].append(item)
                print(f"your bag have now {player['bag']}, gold left {player['gold']}")
        elif choice=="exit":
            break
def dungeon_run(player):
    print("\n Entering the Dungeon... Prepare for 3 battles!")
    for round_num in range(1, 4):
        print(f"\n🔥 Battle {round_num}/3")
        monster = monster_creation()
        result = attack(player, monster)

        if result == "lose":
            print("💀 You fell in the dungeon...")
            return

        reward(player)  # Gold + loot
        shopinventory(player)  # Optional mid-run shop

        # Option to rest/heal if player has potions
        if "potion" in player["bag"]:
            rest = input("🏕️ Would you like to rest and use a potion? (yes/no): ").lower()
            if rest == "yes":
                use_potion(player)

    print(f"\n🎉 You cleared the dungeon! Victory is yours!")
    print(f"🏆 Final Stats: Health: {player['health']}, Gold: {player['gold']}, Bag: {player['bag']}")


def final_boss(player):
    print("\n🔥 NEW BATTLE BEGINS WITH THE FINAL BOSS!!")
    print("🐲 THE KALYUG DRAGON APPEARS!\n")

    boss_stats = {
        "name": "Kalyug",
        "health": random.randint(150, 300),
        "attack": random.randint(15, 25),
        "special": False  # Revives once
    }

    emotional_dialogues = [
        "Why must we fight?",
        "Would you beat me if I was your blood?",
        "You remind me of who I once was...",
        "All I ever wanted was peace..."
    ]

    print(f"Kalyug: \"{random.choice(emotional_dialogues)}\"")

    while player["health"] > 0 and boss_stats["health"] > 0:
        print("\n⚔️ Your Turn:")
        damage = player["attack"] + random.randint(-3, 3)
        boss_stats["health"] -= damage
        print(f"You strike for {damage} damage. Kalyug's health: {max(boss_stats['health'], 0)}")

        # Check if boss is defeated for the first time
        if boss_stats["health"] <= 0 and not boss_stats["special"]:
            boss_stats["health"] = random.randint(60, 100)
            boss_stats["special"] = True
            print("\n😈 Kalyug: \"You thought it was over? I am reborn from the ashes of betrayal...\"")
            print(f"Kalyug revives with {boss_stats['health']} HP!")
            continue
        elif boss_stats["health"] <= 0 and boss_stats["special"]:
            print("\n💀 With a final roar, Kalyug collapses. Peace returns... for now.")
            break

        print("\n🐉 Kalyug's Turn:")
        boss_damage = boss_stats["attack"] + random.randint(-2, 2)
        player["health"] -= boss_damage
        print(f"Kalyug attacks you for {boss_damage} damage. Your health: {max(player['health'], 0)}")

        # Optional: let player use potion
        if "potion" in player["bag"] and player["health"] > 0:
            choice = input("🏕️ Use a potion to heal? (yes/no): ").lower()
            if choice == "yes":
                player["health"] += 20
                player["bag"].remove("potion")
                print(f"You used a potion. Health restored to {player['health']}.")

    # After battle
    print(f"{player['name']} player , fought really well , final health: {player['health']} , gold left : {player['gold']} gold , items in bag : {player['bag']}  ")
    if player["health"] <= 0:
        print("\n☠️ You were slain by the Kalyug Dragon. The world falls into chaos.\n to our Hero: you fell but your story will be remembered")

    else:
        player["gold"] += 100
        player["bag"].append("Kalyug's Tear")
        print("\n🏆 You defeated the Kalyug Dragon!")
        print(f"You gain 100 gold and a rare item: Kalyug's Tear.")
        print(f"Final Stats — Health: {player['health']}, Gold: {player['gold']}, Bag: {player['bag']}")
        print("You made it , yeeahhhh!!!")
           
def main():
    # Main game loop
    while True:
        print("🎮 Welcome to Dungeon Quest!")
        choice = input("➡️ Type 'start' to begin or 'quit' to exit: ").lower()
        if choice == "start":
            player = create_player()
            dungeon_run(player)
            final_boss(player)
        
            replay=input("do you want to play again: (yes/no)")
            if replay!='yes':
                print("Thank you for playing. We hope you enjoyed!")
                print(f"\nThe world will remember the hero: {player['name']}")
                print(f"🎒 Final Bag: {player['bag']}")
                print(f"💰 Gold Earned: {player['gold']}")
                if "Kalyug's Tear" in player["bag"]:
                    print("💎 You carry the legendary Kalyug's Tear. A relic of pain and power.")
                break
        else:
            print("Goodbye!")
            break
        
if __name__ == "__main__":
    main()
