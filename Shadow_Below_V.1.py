import sys
import random
import time

# TYPING
def typeout(text, speed=0.02):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Player information
Player = {
    "Name": "",
    "Role": "",
    "Health": 100,
    "Inventory": [],
    "Location": "Start",
    "Completed routes": [],
    "Shield_charges": 0,
    "Elven_wine_active": False,
    "Tech_Energy": 100,  # Added for Sci-Fi
    "Cyber_Augmentations": []  # Added for Sci-Fi
}

# Monsters
Thornbeast = {
    "Health": 30
}

Bonecrawler = {
    "Health": 40
}

Chasm_Harpy = {
    "Health": 50
}

# Sci-Fi Monsters
Security_Drone = {
    "Health": 45
}

Cyborg_Enforcer = {
    "Health": 55
}

Rogue_AI = {
    "Health": 65
}

# Multiple in-games
Games = {
    "Fantasy": "A Fantasy Dungeon is a perilous, mystical realm filled with ancient magic, hidden treasures, mythical creatures, and secrets waiting to be uncovered.",
    "Sci-fi/Tech": "A Sci-Fi/Tech Dungeon is a high-tech labyrinth of rogue AI, futuristic traps, and cybernetic threats lurking in the shadows of advanced machinery.",
    "Mystry/Horror": "A Mystery/Horror Dungeon is a dark, eerie domain shrouded in secrets, where every shadow hides a whisper and every step leads deeper into fear and the unknown."
}

# Roles in fantasy
Roles_Fantasy = {
    "Cursed Knight": "Skill: Redemption Strike - Deals massive damage to undead, heals slightly if enemy is slain.",
    "Time Mage": "Skill: Temporal Rewind - Reverts self or ally to a state from 1 turn ago (HP, position, etc.).",
    "Relic Hunter": "Skill: Treasure Sense - Detects hidden loot, secret passages, or mimics within range.",
    "Shadowblade": "Skill: Vanish - Instantly becomes invisible for 2 turns, immune to traps.",
    "Wild Druid": "Skill: Nature's Grasp - Summons roots to entangle enemies, reducing movement or actions.",
}

# Roles in Sci-Fi
Roles_SciFi = {
    "Techno Mage": "Skill: Holo-Projection - Creates a hologram to distract enemies for one turn.",
    "Cyber Ninja": "Skill: Stealth Mode - Becomes invisible for one turn, avoiding all damage.",
    "Gunner": "Skill: Rapid Fire - Deals extra damage with ranged attacks.",
    "Engineer": "Skill: Repair Drone - Summons a drone to heal you or an ally for 30 HP.",
    "Hacker": "Skill: System Override - Temporarily disables enemy abilities for one turn.",
}

#Roles in Horror
Roles_Horror = {
    "Paranormal Investigator": "Skill: Spectral Scan - Detects hidden spirits and reveals weak points (20% damage boost against ghosts).",
    "Ghost Hunter": "Skill: Spirit Trap - Captures malevolent entities for 2 turns (enemy skips attacks).",
    "Occultist": "Skill: Dark Pact - Sacrifices 15 HP to summon a demonic ally for 3 attacks.",
    "Survivor": "Skill: Adrenaline Rush - Gains +50% evasion and +3 damage for 3 turns when below 30% HP.",
    "Exorcist": "Skill: Holy Banishing - Deals massive damage to undead/possessed enemies (3 turn cooldown)."
}


def Fantasy():
    typeout("\nA fantasy world is a magical realm filled with mythical creatures, enchanted lands, ancient legends, and heroic quests beyond the bounds of reality.\n")
    Choose_roles = f"Choose the role you want to start your journey with.\n1. Cursed Knight : {Roles_Fantasy['Cursed Knight']}\n2. Relic Hunter: {Roles_Fantasy['Relic Hunter']}\n3. Shadowblade : {Roles_Fantasy['Shadowblade']}\n4. Time Mage : {Roles_Fantasy['Time Mage']}\n5. Wild Druid : {Roles_Fantasy['Wild Druid']}\n"
    print(Choose_roles)
    role_choice = str(input("> "))
    try:
        role_key = role_choice.lower()
        if role_key in ["cursed knight", "1"]:
            Player['Role'] = "Cursed Knight"
            typeout("> You are Cursed Knight, a fallen warrior bound by a dark curse, seeking redemption through battle and sacrifice.\n")
        elif role_key in ["shadowblade", "2"]:
            Player['Role'] = "Shadowblade"
            typeout("> Shadowblade, a stealthy assassin from the shadows, swift and silent, striking before anyone knows they're there.\n")
        elif role_key in ['wild druid', "3"]:
            Player['Role'] = "Wild Druid"
            typeout("> Wild Druid, a guardian of nature who commands beasts and the elements, blending magic with wilderness instincts.\n")
        elif role_key in ["time mage", "4"]:
            Player['Role'] = "Time Mage"
            typeout("> Time Mage, a master of temporal magic, able to rewind moments and manipulate time to outsmart enemies.\n")
        elif role_key in ["relic hunter", "5"]:
            Player['Role'] = "Relic Hunter"
            typeout("> Relic Hunter, an adventurous explorer obsessed with uncovering ancient magical artifacts hidden in the dungeon.\n")
        else:
            typeout("> Enter valid input....\n")
            return Fantasy()
    except:
        typeout("> Enter valid input....")
    Fantasy_Story()

def Fantasy_Story():
    start_scene = """The wind howls as dark clouds gather above the crumbling kingdom of Elaria. Centuries ago, this land
flourished with magic and honor. Now, it lies broken—its dungeons cursed, its heroes forgotten, and its
creatures twisted by an ancient evil.

You awaken at the edge of a ruined shrine, the air thick with enchantment and ash.
A glowing sigil pulses beneath your feet, whispering choices into your mind…"""
    typeout(start_scene)
    explore_fantasy = ["🗡️ Worn Traveler's Blade",
                       "🕯️ Flickering Torch",
                       "📜 Crumpled Map Fragment",
                       "🧴 Small Healing Flask",
                       "🧿 Unknown Trinket"]
    while True:
        typeout("> Do you want to open the Sanctum Chest? (y/n): ")
        yes_or_no = str(input("> ").strip().lower())
        if yes_or_no in ["y", "yes"]:
            item_picked = random.choice(explore_fantasy)
            Player["Inventory"].append(item_picked)
            typeout(f"> You got {item_picked} from the sanctum chest....")
            break
        elif yes_or_no in ["n", "no"]:
            break
        else:
            print("> Enter valid input")
    while True:
        typeout("> (A) To start adventure.\n> (B) To check Inventory.\n")
        start_1 = input("> ").strip().lower()
        if start_1 in ["(a)", "a", "start adventure", "adventure"]:
            fantasy_adv()
            break
        elif start_1 in ["(b)", "b", "inventory", "check inventory", "open inventory"]:
            show_inventory()
        else:
            print("Enter valid input......")

def show_inventory():
    if not Player["Inventory"]:
        print("> Your inventory is empty")
        return
    
    print("\n> Inventory:")
    for i, item in enumerate(Player["Inventory"], 1):
        print(f"{i}. {item}")

Paths_fantasy = [
    "Whispering Forest",
    "Moss-Covered Cave",
    "Chasm Bridge"
]

def choose_path(paths):
    while paths:
        typeout("\n🌲 Available Paths:")
        for i, path in enumerate(paths, 1):
            print(f"{i}. {path}")
        print("Q. Quit adventure")
        choice = input("\nChoose a path (1/2/3) or Q to quit: ").strip().lower()
        if choice in ["q", "quit"]:
            print("\n📋 You step away from the dungeon... for now.")
            return None
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(paths):
                selected_path = paths.pop(index)
                print(f"\n🔮 You venture into the {selected_path}...\n")
                return selected_path.lower()
        print("⚠️ Please enter a valid number or 'Q' to quit.")
    print("\n🎉 All paths explored. A new journey awaits...")

def health_bar(current, maximum, bar_length=20):
    ratio = current / maximum
    filled = int(ratio * bar_length)
    empty = bar_length - filled
    return f"[{'█' * filled}{'░' * empty}] {current}/{maximum}"

victory_gifts = [
    "🧙‍♂️ Spell Scroll of Healing",
    "🛡️ Shield of Resilience", 
    "⚔️ Enchanted Dagger",
    "🍷 Bottle of Elven Wine"
]

def use_item(item, monster_name, damage):
    if item == "🧙‍♂️ Spell Scroll of Healing":
        Player["Health"] = min(100, Player["Health"] + 50)
        typeout("> The scroll glows bright blue as you're healed for 50 HP!")
        return True
        
    elif item == "🛡️ Shield of Resilience":
        Player["Shield_charges"] = 3
        typeout("> A shimmering barrier forms around you! Next 3 attacks will be reduced.")
        return True
        
    elif item == "⚔️ Enchanted Dagger":
        typeout("> The dagger hums with energy! Your next attack will deal 2x damage!")
        return 2.0  
        
    elif item == "🍷 Bottle of Elven Wine":
        Player["Elven_wine_active"] = True
        typeout("> The wine fills you with vigor! All damage increased by 20% for rest of battle!")
        return True
        
    elif item == "🧴 Small Healing Flask":
        Player["Health"] = min(100, Player["Health"] + 20)
        typeout("> You drink the flask and heal for 20 HP!")
        return True
    
    # Non-combat items
    elif item in ["🕯️ Flickering Torch", "📜 Crumpled Map Fragment", "🧿 Unknown Trinket"]:
        typeout(f"> The {item.split()[1]} has no effect in battle.")
        return False
    
    else:
        typeout(f"> You're not sure how to use {item} in battle.")
        return False

def fantasy_adv():
    scene = """
The air grows colder as you step beyond the shrine. 
A winding path stretches into the distance, swallowed by thick fog and twisted trees. 
Carved into a stone nearby is a faded inscription:

    'Only the brave enter Eldergloom... and even fewer return.'

Suddenly, a soft chime rings in your ears. The sigil beneath your feet glows one last time, then vanishes.

You take your first steps forward.

Ahead, the path splits into three...
"""
    typeout(scene)
    
    while Paths_fantasy:
        path = choose_path(Paths_fantasy)
        if not path:
            break

        # Set up monster based on path
        if path in ["whispering forest", "forest", "1", "trail"]:
            monster = {"Name": "Thornbeast", "Health": 40, "Max": 40, "Damage": (1, 9)}
        elif path in ["moss-covered cave", "cave", "2", "moss cave"]:
            monster = {"Name": "Bonecrawler", "Health": 45, "Max": 45, "Damage": (2, 10)}
        elif path in ["chasm bridge", "bridge", "3", "chasm"]:
            monster = {"Name": "Chasm Harpy", "Health": 50, "Max": 50, "Damage": (3, 12)}
        else:
            continue

        typeout(f"\n> You encountered a {monster['Name']}! (HP: {monster['Health']})")
        typeout("> Choose your action:\n1. Fight\n2. Run")
        
        while True:
            action = input("> ").strip().lower()
            if action in ["1", "fight", "f"]:
                break
            elif action in ["2", "run", "r"]:
                typeout("> You barely escape with your life!")
                return
            else:
                typeout("⚠️ Enter valid input (1/Fight or 2/Run)")
        
        # Combat setup
        base_damage = (15, 20) if "🗡️ Worn Traveler's Blade" in Player["Inventory"] else (8, 12)
        damage_multiplier = 1.0
        Player["Elven_wine_active"] = False
        
        # Combat loop
        while monster["Health"] > 0 and Player["Health"] > 0:
            typeout(f"\n{Player['Name']}: {health_bar(Player['Health'], 100)}")
            typeout(f"{monster['Name']}: {health_bar(monster['Health'], monster['Max'])}")
            
            typeout("\n> Choose action:\n1. Attack\n2. Defend\n3. Use Item")
            choice = input("> ").strip().lower()
            
            if choice in ["1", "attack", "a"]:
                # Player attack phase
                damage = int(random.randint(*base_damage) * damage_multiplier)
                if Player["Elven_wine_active"]:
                    damage = int(damage * 1.2)
                
                monster["Health"] -= damage
                typeout(f"> You attack for {damage} damage!")
                
                # Check if monster was defeated before it can attack
                if monster["Health"] <= 0:
                    monster["Health"] = 0  # Ensure HP doesn't show negative
                    break  # Exit combat loop immediately
                
                # Monster attack phase (only if still alive)
                monster_dmg = random.randint(*monster["Damage"])
                if Player["Shield_charges"] > 0:
                    reduced = max(1, monster_dmg // 2)
                    typeout(f"> Shield reduces {monster['Name']}'s {monster_dmg} damage to {reduced}!")
                    monster_dmg = reduced
                    Player["Shield_charges"] -= 1
                
                Player["Health"] -= monster_dmg
                typeout(f"> {monster['Name']} hits you for {monster_dmg} damage!")
            
            elif choice in ["2", "defend", "d"]:
                monster_dmg = random.randint(*monster["Damage"]) // 2
                Player["Health"] -= monster_dmg
                typeout(f"> You defend against {monster['Name']}'s attack! (Took {monster_dmg} damage)")
            
            elif choice in ["3", "use item", "item", "i"]:
                if not Player["Inventory"]:
                    typeout("> Your inventory is empty!")
                    continue
                    
                show_inventory()
                typeout("> Select item to use (number):")
                try:
                    item_idx = int(input("> ")) - 1
                    if 0 <= item_idx < len(Player["Inventory"]):
                        item = Player["Inventory"][item_idx]
                        result = use_item(item, monster["Name"], base_damage)
                        
                        if item in ["⚔️ Enchanted Dagger"] and result:
                            damage_multiplier = result
                        elif result:
                            Player["Inventory"].remove(item)
                    else:
                        typeout("⚠️ Invalid item number")
                except:
                    typeout("⚠️ Please enter a number")
            
            # Reset temporary buffs
            if damage_multiplier != 1.0 and choice in ["1", "attack", "a"]:
                damage_multiplier = 1.0
        
        # Battle conclusion
        if Player["Health"] <= 0:
            Player["Health"] = 1
            typeout("> You've been defeated! (Left with 1 HP)")
            return
        elif monster["Health"] <= 0:
            victory_gift = random.choice(victory_gifts)
            Player["Inventory"].append(victory_gift)
            typeout(f"\n> You defeated the {monster['Name']}! Received {victory_gift}!")
            Player["Completed routes"].append(monster["Name"])
            Player["Shield_charges"] = 0
            Player["Elven_wine_active"] = False

# Sci-Fi Functions
def SciFi():
    typeout("\nA Sci-Fi world is a high-tech labyrinth filled with rogue AI, futuristic traps, and cybernetic threats lurking in the shadows of advanced machinery.\n")
    Choose_roles = f"Choose the role you want to start your journey with.\n1. Techno Mage : {Roles_SciFi['Techno Mage']}\n2. Cyber Ninja: {Roles_SciFi['Cyber Ninja']}\n3. Gunner : {Roles_SciFi['Gunner']}\n4. Engineer : {Roles_SciFi['Engineer']}\n5. Hacker : {Roles_SciFi['Hacker']}\n"
    print(Choose_roles)
    role_choice = str(input("> "))
    try:
        role_key = role_choice.lower()
        if role_key in ["techno mage", "1"]:
            Player['Role'] = "Techno Mage"
            typeout("> You are a Techno Mage, wielding the power of technology to manipulate the battlefield.\n")
        elif role_key in ["cyber ninja", "2"]:
            Player['Role'] = "Cyber Ninja"
            typeout("> Cyber Ninja, a master of stealth and agility, striking from the shadows.\n")
        elif role_key in ['gunner', "3"]:
            Player['Role'] = "Gunner"
            typeout("> Gunner, a sharpshooter with unmatched precision and firepower.\n")
        elif role_key in ["engineer", "4"]:
            Player['Role'] = "Engineer"
            typeout("> Engineer, a brilliant inventor who can repair and enhance technology.\n")
        elif role_key in ["hacker", "5"]:
            Player['Role'] = "Hacker"
            typeout("> Hacker, a digital wizard who can manipulate systems and disable threats.\n")
        else:
            typeout("> Enter valid input....\n")
            return SciFi()
    except:
        typeout("> Enter valid input....")
    SciFi_Story()

def SciFi_Story():
    start_scene = """You awaken in a futuristic city, where neon lights flicker and the hum of machinery fills the air.
The world is a blend of advanced technology and lurking dangers, where rogue AI and cybernetic threats roam the streets.

You find yourself in a hidden lab, the walls lined with advanced tech and holographic displays.
A console flickers to life, offering you choices to explore this high-tech realm..."""
    typeout(start_scene)
    explore_scifi = ["🔧 Tech Toolkit",
                     "💉 Nano-Boost (20HP)",
                     "📡 Signal Jammer",
                     "💡 Glow Rod",
                     "🔋 Energy Cell"]
    while True:
        typeout("> Do you want to open the Tech Cache? (y/n): ")
        yes_or_no = str(input("> ").strip().lower())
        if yes_or_no in ["y", "yes"]:
            item_picked = random.choice(explore_scifi)
            Player["Inventory"].append(item_picked)
            typeout(f"> You got {item_picked} from the tech cache....")
            break
        elif yes_or_no in ["n", "no"]:
            break
        else:
            print("> Enter valid input")
    
    while True:
        typeout("> (A) To start adventure.\n> (B) To check Inventory.\n")
        start_1 = input("> ").strip().lower()
        if start_1 in ["(a)", "a", "start adventure", "adventure"]:
            scifi_adv()
            break
        elif start_1 in ["(b)", "b", "inventory", "check inventory", "open inventory"]:
            show_inventory()
        else:
            print("Enter valid input......")

def scifi_adv():
    scene = """
The air is charged with electricity as you step into the neon-lit streets of the city. 
A winding path stretches into the distance, filled with the sounds of machinery and the glow of holograms. 
A warning sign flickers nearby:

    'Danger: Rogue AI detected. Proceed with caution.'

You take your first steps forward.

Ahead, the path splits into three...
"""
    typeout(scene)
    
    Paths_scifi = [
        "Neon Alley",
        "Abandoned Factory",
        "Cybernetic Lab"
    ]
    
    while Paths_scifi:
        path = choose_path(Paths_scifi)
        if not path:
            break

        # Set up monster based on path
        if path in ["neon alley", "alley", "1"]:
            monster = {"Name": "Security Drone", "Health": 45, "Max": 45, "Damage": (6, 10)}
        elif path in ["abandoned factory", "factory", "2"]:
            monster = {"Name": "Cyborg Enforcer", "Health": 55, "Max": 55, "Damage": (8, 13)}
        elif path in ["cybernetic lab", "lab", "3"]:
            monster = {"Name": "Rogue AI", "Health": 65, "Max": 65, "Damage": (10, 16)}
        else:
            continue

        typeout(f"\n> You encountered a {monster['Name']}! (HP: {monster['Health']})")
        typeout("> Choose your action:\n1. Fight\n2. Run")
        
        while True:
            action = input("> ").strip().lower()
            if action in ["1", "fight", "f"]:
                break
            elif action in ["2", "run", "r"]:
                typeout("> You barely escape with your life!")
                return
            else:
                typeout("⚠️ Enter valid input (1/Fight or 2/Run)")
        
        # Combat setup
        base_damage = (15, 20) if "🔧 Tech Toolkit" in Player["Inventory"] else (8, 12)
        damage_multiplier = 1.0
        
        # Combat loop
        while monster["Health"] > 0 and Player["Health"] > 0:
            typeout(f"\n{Player['Name']}: {health_bar(Player['Health'], 100)}")
            typeout(f"{monster['Name']}: {health_bar(monster['Health'], monster['Max'])}")
            
            typeout("\n> Choose action:\n1. Attack\n2. Defend\n3. Use Item")
            choice = input("> ").strip().lower()
            
            if choice in ["1", "attack", "a"]:
                # Player attack phase
                damage = int(random.randint(*base_damage) * damage_multiplier)
                monster["Health"] -= damage
                typeout(f"> You attack for {damage} damage!")
                
                # Check if monster was defeated before it can attack
                if monster["Health"] <= 0:
                    monster["Health"] = 0  # HP doesn't show negative
                    break  # Exit combat loop immediately
                
                # Monster attack phase (only if still alive)
                monster_dmg = random.randint(*monster["Damage"])
                Player["Health"] -= monster_dmg
                typeout(f"> {monster['Name']} hits you for {monster_dmg} damage!")
            
            elif choice in ["2", "defend", "d"]:
                monster_dmg = random.randint(*monster["Damage"]) // 2
                Player["Health"] -= monster_dmg
                typeout(f"> You defend against {monster['Name']}'s attack! (Took {monster_dmg} damage)")
            
            elif choice in ["3", "use item", "item", "i"]:
                if not Player["Inventory"]:
                    typeout("> Your inventory is empty!")
                    continue
                    
                show_inventory()
                typeout("> Select item to use (number):")
                try:
                    item_idx = int(input("> ")) - 1
                    if 0 <= item_idx < len(Player["Inventory"]):
                        item = Player["Inventory"][item_idx]
                        result = use_item(item, monster["Name"], base_damage)
                        if result:
                            Player["Inventory"].remove(item)
                    else:
                        typeout("⚠️ Invalid item number")
                except:
                    typeout("⚠️ Please enter a number")
        
        # Battle conclusion
        if Player["Health"] <= 0:
            Player["Health"] = 1
            typeout("> You've been defeated! (Left with 1 HP)")
            return
        elif monster["Health"] <= 0:
            victory_gift = random.choice(victory_gifts)
            Player["Inventory"].append(victory_gift)
            typeout(f"\n> You defeated the {monster['Name']}! Received {victory_gift}!")

# Horror Functions
def Horror():
    typeout("\nWelcome to a world of nightmares, where shadows whisper and the air is thick with dread.\n")
    Choose_roles = f"Choose the role you want to start your journey with.\n1. Paranormal Investigator: {Roles_Horror['Paranormal Investigator']}\n2. Survivor: {Roles_Horror['Survivor']}\n3. Exorcist: {Roles_Horror['Exorcist']}\n4. Occultist: {Roles_Horror['Occultist']}\n5. Ghost Hunter: {Roles_Horror['Ghost Hunter']}\n"
    print(Choose_roles)
    role_choice = str(input("> "))
    try:
        role_key = role_choice.lower()
        if role_key in ["paranormal investigator", "1"]:
            Player['Role'] = "Paranormal Investigator"
            typeout("> You are a Paranormal Investigator, equipped with tools to uncover the supernatural.\n")
        elif role_key in ["survivor", "2"]:
            Player['Role'] = "Survivor"
            typeout("> Survivor, a resourceful individual fighting to stay alive in a world of horror.\n")
        elif role_key in ['exorcist', "3"]:
            Player['Role'] = "Exorcist"
            typeout("> Exorcist, a brave soul who confronts the dark forces head-on.\n")
        elif role_key in ["occultist", "4"]:
            Player['Role'] = "Occultist"
            typeout("> Occultist, a master of dark rituals and forbidden knowledge.\n")
        elif role_key in ["ghost hunter", "5"]:
            Player['Role'] = "Ghost Hunter"
            typeout("> Ghost Hunter, armed with gadgets to capture the spirits that haunt the night.\n")
        else:
            typeout("> Enter valid input....\n")
            return Horror()
    except:
        typeout("> Enter valid input....")
    Horror_Story()

def Horror_Story():
    start_scene = """You awaken in a desolate town, where fog creeps through the streets and the moon casts eerie shadows.
The world is a blend of terror and despair, where malevolent spirits and unspeakable horrors lurk in the darkness.

You find yourself in an abandoned house, the walls lined with old photographs and the air thick with the scent of decay.
A dusty journal lies open on a table, offering you choices to explore this haunted realm..."""
    typeout(start_scene)
    explore_horror = ["🔦 Flashlight",
                      "🕯️ Candle (20HP)",
                      "📜 Ritual Scroll",
                      "🔪 Dagger",
                      "🧿 Amulet of Protection"]
    while True:
        typeout("> Do you want to open the Horror Cache? (y/n): ")
        yes_or_no = str(input("> ").strip().lower())
        if yes_or_no in ["y", "yes"]:
            item_picked = random.choice(explore_horror)
            Player["Inventory"].append(item_picked)
            typeout(f"> You got {item_picked} from the horror cache....")
            break
        elif yes_or_no in ["n", "no"]:
            break
        else:
            print("> Enter valid input")
    
    while True:
        typeout("> (A) To start adventure.\n> (B) To check Inventory.\n")
        start_1 = input("> ").strip().lower()
        if start_1 in ["(a)", "a", "start adventure", "adventure"]:
            horror_adv()
            break
        elif start_1 in ["(b)", "b", "inventory", "check inventory", "open inventory"]:
            show_inventory()
        else:
            print("Enter valid input......")

def horror_adv():
    scene = """
The air is thick with tension as you step into the fog-laden streets of the town. 
A narrow path stretches into the darkness, filled with the sounds of distant wails and the rustle of unseen creatures. 
A warning sign creaks ominously nearby:

    'Beware: Malevolent spirits roam these grounds. Proceed with caution.'

You take your first steps forward.

Ahead, the path splits into three...
"""
    typeout(scene)
    
    Paths_horror = [
        "Creepy Cemetery",
        "Abandoned Asylum",
        "Haunted Manor"
    ]
    
    while Paths_horror:
        path = choose_path(Paths_horror)
        if not path:
            break

        # Set up monster based on path
        if path in ["creepy cemetery", "cemetery", "1"]:
            monster = {"Name": "Wraith", "Health": 40, "Max": 40, "Damage": (5, 10)}
        elif path in ["abandoned asylum", "asylum", "2"]:
            monster = {"Name": "Mad Spirit", "Health": 50, "Max": 50, "Damage": (7, 12)}
        elif path in ["haunted manor", "manor", "3"]:
            monster = {"Name": "Vengeful Ghost", "Health": 60, "Max": 60, "Damage": (9, 15)}
        else:
            continue

        typeout(f"\n> You encountered a {monster['Name']}! (HP: {monster['Health']})")
        typeout("> Choose your action:\n1. Fight\n2. Run")
        
        while True:
            action = input("> ").strip().lower()
            if action in ["1", "fight", "f"]:
                break
            elif action in ["2", "run", "r"]:
                typeout("> You barely escape with your life!")
                return
            else:
                typeout("⚠️ Enter valid input (1/Fight or 2/Run)")
        
        # Combat setup
        base_damage = (10, 15) if "🔦 Flashlight" in Player["Inventory"] else (5, 10)
        damage_multiplier = 1.0
        
        # Combat loop
        while monster["Health"] > 0 and Player["Health"] > 0:
            typeout(f"\n{Player['Name']}: {health_bar(Player['Health'], 100)}")
            typeout(f"{monster['Name']}: {health_bar(monster['Health'], monster['Max'])}")
            
            typeout("\n> Choose action:\n1. Attack\n2. Defend\n3. Use Item")
            choice = input("> ").strip().lower()
            
            if choice in ["1", "attack", "a"]:
                # Player attack phase
                damage = int(random.randint(*base_damage) * damage_multiplier)
                monster["Health"] -= damage
                typeout(f"> You attack for {damage} damage!")
                
                # Check if monster was defeated before it can attack
                if monster["Health"] <= 0:
                    monster["Health"] = 0  # HP doesn't show negative
                    break  
                
                # Monster attack 
                monster_dmg = random.randint(*monster["Damage"])
                Player["Health"] -= monster_dmg
                typeout(f"> {monster['Name']} hits you for {monster_dmg} damage!")
            
            elif choice in ["2", "defend", "d"]:
                monster_dmg = random.randint(*monster["Damage"]) // 2
                Player["Health"] -= monster_dmg
                typeout(f"> You defend against {monster['Name']}'s attack! (Took {monster_dmg} damage)")
            
            elif choice in ["3", "use item", "item", "i"]:
                if not Player["Inventory"]:
                    typeout("> Your inventory is empty!")
                    continue
                    
                show_inventory()
                typeout("> Select item to use (number):")
                try:
                    item_idx = int(input("> ")) - 1
                    if 0 <= item_idx < len(Player["Inventory"]):
                        item = Player["Inventory"][item_idx]
                        result = use_item(item, monster["Name"], base_damage)
                        if result:
                            Player["Inventory"].remove(item)
                    else:
                        typeout("⚠️ Invalid item number")
                except:
                    typeout("⚠️ Please enter a number")
        
        # Battle conclusion
        if Player["Health"] <= 0:
            Player["Health"] = 1
            typeout("> You've been defeated! (Left with 1 HP)")
            return
        elif monster["Health"] <= 0:
            victory_gift = random.choice(victory_gifts)
            Player["Inventory"].append(victory_gift)
            typeout(f"\n> You defeated the {monster['Name']}! Received {victory_gift}!")


# Main Game Function
def Start():
    Title = "=" * 15 + "🌘 🕷️  S H A D O W   B E L O W  🕷️ 🌘" + "=" * 15
    print(Title)
    typeout("> Welcome to the shadow below.\n> What is your name, adventurer? ")
    Player["Name"] = input("> ").strip()
    Options = f"\n> S H A D O W   B E L O W <\n\nEmbark on One of Three Epic Journeys.\n\n1. Fantasy - {Games['Fantasy']}\n\n2. Sci-Fi - {Games['Sci-fi/Tech']}\n\n3. Horror/Mystery - {Games['Mystry/Horror']}"
    print(Options)
    typeout("\n> What story mode would you like to play: ")
    
    while True:
        choice = input("> ").strip().lower()
        if choice in ["1", "fantasy"]:
            Fantasy()
            break
        elif choice in ["2", "sci-fi", "scifi", "tech"]:
            SciFi()
            break
        elif choice in ["3", "horror", "mystery"]:
            Horror() 
            break
        else:
            typeout("⚠️ Please choose 1 (Fantasy), 2 (Sci-Fi), or 3 (Horror/Mystery)")
    typeout("> Exited the game successfully......")
Start()
