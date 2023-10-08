    # personality_types = {
    # "ISTJ": ["Inspector", "Goal-setting", "Work-life balance", "Open-mindedness"], 
    # "ISFJ": ["Protector", "Boundary Setting", "Self-Care", "Creativity"],
    # "INFJ": ["Counselor", "Intuition", "Connection", "Creativity"], 
    # "INTJ": ["Mastermind", "Strategic", "Knowledge", "Independence"],
    # "ISTP": ["Craftsman", "Analytical", "Adventurous", "Self-Sufficient"], 
    # "ISFP": ["Composer", "Artistic", "Sensitive", "Expressive"], 
    # "INFP": ["Healer", "Idealistic", "Compassionate", "Imaginative"], 
    # "INTP": ["Architect", "Analytical", "Curious", "Innovative"],
    # "ESTP": ["Dynamo", "Energetic", "Bold", "Resourceful"], 
    # "ESFP": ["Performer", "Spontaneous", "Enthusiastic", "Social"], 
    # "ENFP": ["Champion", "Passionate", "Creative", "Inspirational"], 
    # "ENTP": ["Visionary", "Innovative", "Curious", "Strategic"],
    # "ESTJ": ["Supervisor", "Organized", "Responsible", "Efficient"], 
    # "ESFJ": ["Provider", "Nurturing", "Supportive", "Sociable"], 
    # "ENFJ": ["Teacher", "Inspiring", "Compassionate", "Persuasive"], 
    # "ENTJ": ["Commander", "Leadership", "Ambitious", "Strategic"]
    # }
# pokedex = {}
evolution_lines = {
    "bulbasaur": "ivysaur",
    "ivysaur": "venusaur",
    "charmander": "charmeleon",
    "charmeleon": "charizard",
    "squirtle": "wartortle",
    "wartortle": "blastoise",
    "caterpie": "metapod",
    "metapod": "butterfree",
    "weedle": "kakuna",
    "kakuna": "beedrill",
    "pidgey": "pidgeotto",
    "pidgeotto": "pidgeot",
    "rattata": "raticate",
    "spearow": "fearow",
    "ekans": "arbok",
    "pikachu": "raichu",
    "sandshrew": "sandslash",
    "nidoran♀": "nidorina",
    "nidorina": "nidoqueen",
    "nidoran♂": "nidorino",
    "nidorino": "nidoking",
    "clefairy": "clefable",
    "vulpix": "ninetales",
    "jigglypuff": "wigglytuff",
    "zubat": "golbat",
    "oddish": "gloom",
    "gloom": "vileplume",
    "paras": "parasect",
    "venonat": "venomoth",
    "diglett": "dugtrio",
    "meowth": "persian",
    "psyduck": "golduck",
    "mankey": "primeape",
    "growlithe": "arcanine",
    "poliwag": "poliwhirl",
    "poliwhirl": "poliwrath",
    "abra": "kadabra",
    "kadabra": "alakazam",
    "machop": "machoke",
    "machoke": "machamp",
    "bellsprout": "weepinbell",
    "weepinbell": "victreebel",
    "tentacool": "tentacruel",
    "geodude": "graveler",
    "graveler": "golem",
    "ponyta": "rapidash",
    "slowpoke": "slowbro",
    "magnemite": "magneton",
    "doduo": "dodrio",
    "seel": "dewgong",
    "grimer": "muk",
    "shellder": "cloyster",
    "gastly": "haunter",
    "haunter": "gengar",
    "drowzee": "hypno",
    "krabby": "kingler",
    "voltorb": "electrode",
    "exeggcute": "exeggutor",
    "cubone": "marowak",
    "koffing": "weezing",
    "rhyhorn": "rhydon",
    "horsea": "seadra",
    "goldeen": "seaking",
    "staryu": "starmie",
    "magikarp": "gyarados",
    "omanyte": "omastar",
    "kabuto": "kabutops",
    "dratini": "dragonair",
    "dragonair": "dragonite"
}



class Trainer:
    def __init__(self, social=None, name=None, thinking=None, obs=None, plan=None, currentpath=None, party=None):
        self.social = social # E or I
        self.thinking = thinking
        self.obs = obs
        self.name = name
        self.plan = plan
        self.party = party #pokemon party -> each catch appends
        self.currentpath = currentpath #path user is currently on

class Pokemon:
    def __init__(self, name=None, evolution=None):
        self.name = name

class PokemonParty:
    def __init__(self, party=None):
        self.party = party

class Task:
    def __init__(self, pokemon=None, title=None, desc=None):
        self.title = title
        self.pokemon = pokemon
        self.desc = desc

task_list = {

}

#Social path pokemon and tasks

farfetchd = Pokemon("farfetch'd")
jigglypuff = Pokemon("jigglypuff")
clefairy = Pokemon("clefairy")

fartask = Task(farfetchd, "Connect with loved ones", "Initiate social interactions regularly to maintain connections with friends and loved ones.")
jigtask = Task(jigglypuff, "Attend social event", "Attend social events, gatherings, or group activities to recharge your energy.")
cleftask = Task(clefairy, "Team Building", "Engage in team-oriented projects or collaborative activities to satisfy your need for interaction.")

#Introvert path pokemon and tasks

abra = Pokemon("abra")
cubone = Pokemon("cubone")
kabuto = Pokemon("kabuto")

abratask = Task(abra, "Allocate me-time", "Allocate regular me-time for solitude and self-reflection.")
cubtask = Task(cubone, "Create cozy atmosphere", "Create a quiet and cozy space at home for relaxation and personal activities.")
kabtask = Task(kabuto, "Explore your hobbies", "Dedicate time to your favorite solitary hobbies, such as reading, writing, or art.")

# Perceiving path pokemon and tasks

zubat = Pokemon("zubat")
bellsprout = Pokemon("bellsprout")
machop = Pokemon("machop")

zubtask = Task(zubat, "Explore new places", "Embrace spontaneity by trying new activities or exploring new places.")
beltask = Task(bellsprout, "Adapt to change", "Stay adaptable and open to change in your daily routine.")
mactask = Task(machop, "Pursuit of interest", "Dedicate time to pursue multiple interests or hobbies without rigid schedules")

# Judging path pokemon and tasks

gastly = Pokemon("gastly")
horsea = Pokemon("horsea")
vulpix = Pokemon("vulpix")

gastask = Task(gastly, "Structured Environment", "Maintain a well-organized and structured environment to reduce stress.")
hortask = Task(horsea, "Schedule Yourself", "Create daily to-do lists or schedules to manage your time effectively.")
vultask = Task(vulpix, "Goal Setting", "Set specific goals and track your progress towards achieving them.")


#all tasks list

task_list = {
"farfetch'd": fartask,
"jigglypuff": jigtask,
"clefairy": cleftask,
"abra": abratask,
"cubone": cubtask,
"kabuto": kabtask,
"bellsprout": beltask,
"zubat": zubtask,
"machop": mactask,
"gastly": gastask,
"horsea": hortask,
"vulpix": vultask

}


def welcome():
    nameask = input("Happi you are here! Please enter your name here: ")
    trainer_type = Trainer()
    trainer_type.name = nameask
    personal = input("Hello " + nameask + "! My name is Professor Banerjee, and I will be taking you to the region of Sassyland. Select your trainer type: ").upper()
    if personal[0] == "E":
        trainer_type.social = "social"
    else:
        trainer_type.social = "introspection"
    if personal[1] == "N":
        trainer_type.obs = "intuition"
    else:
        trainer_type.obs = "observation"
    if personal[2] == "F":
        trainer_type.thinking = "feeling"
    else:
        trainer_type.thinking = "thought"
    if personal[3] == "P":
        trainer_type.plan = "spontaneous"
    else:
        trainer_type.plan = "planning"
    return trainer_type
user = welcome()
def evolution():
    evolvable_pokemon = []
    evolvable_pokemon_names = []
    for pokemon in user.party.party:
        print (pokemon.name)
        if pokemon.name.lower() in evolution_lines.keys():
            evolvable_pokemon.append(pokemon)
            evolvable_pokemon_names.append(pokemon.name)
    if len(evolvable_pokemon_names) == 0:
        print("Sorry, all your pokemon are fully evolved")
        return
    print("Please select the slot of the pokemon you would like to evolve!")
    evo_idx = input(evolvable_pokemon_names) # this needs to take in an integer value
    idx = int(evo_idx)
    if idx < len(evolvable_pokemon_names):
        prevolution = evolvable_pokemon[idx].name
        evolvable_pokemon[idx].name = evolution_lines.get(evolvable_pokemon[idx].name)
        print("Congratulations! Your " + prevolution + " has evolved into a " + evolvable_pokemon[idx].name + "!")

def social_path():
    charlotte_party = PokemonParty()
    farfetchd = Pokemon("farfetch'd")
    jigglypuff = Pokemon("jigglypuff")
    clefairy = Pokemon("clefairy")
    charlotte_party.party = [farfetchd, jigglypuff, clefairy]
    charlotte_reindeer = Trainer(social="social", name="Charlotte Reindeer", party=charlotte_party)
    print("Hey trainer! My name is " + charlotte_reindeer.name + " and I will be taking you on the " + charlotte_reindeer.social + " path! To get started on your journey, we will be providing you some social tasks.")
    social_task = input("Please select one of the following paths: " + fartask.pokemon.name + ": " + fartask.title + " OR " + jigtask.pokemon.name + ": " + jigtask.title + " OR " + cleftask.pokemon.name + ": " + cleftask.title + "? ").lower()
    if (social_task == fartask.pokemon.name.lower() or social_task == jigtask.pokemon.name.lower() or social_task == cleftask.pokemon.name.lower()):
        thetask = task_list.get(social_task)
        finishedtask = input("Hiya trainer! My name is: " + thetask.pokemon.name + " and your task today is: " + thetask.desc + " Have you completed this task? ").lower()
        if (finishedtask == "yes"):
            choosecatch = input("Congratulations! You are one step closer to becoming champion of the Sassyland region! I am very inspired by what you have done. Would I be able to join your team? If not, the least I can do is help you evolve your pokemon: ").lower()
            if (choosecatch == "evolve"):
                evolution()
            else:
                user.party.party.append(thetask.pokemon)
                print("Congratulations! " + thetask.pokemon.name + " has joined your party!")
        else:
            print("It was nice to meet you! Truly sorry to see you go :(")
    else: 
        print("Did not enter the task")
    path_choice()

def introspect_path():
    meg_party = PokemonParty()
    abra = Pokemon("abra")
    kabuto = Pokemon("kabuto")
    cubone = Pokemon("cubone")
    meg_party.party = [abra, kabuto, cubone]
    meg_liger = Trainer(social="introspect", name="Meg Liger", party=meg_party)
    print("Hey trainer... I'm " + meg_liger.name + " and I will be taking you on the " + meg_liger.social + " path. This will be a great space to take some time dedicated to yourself.")
    social_task = input("Please select one of the following paths: " + abratask.pokemon.name + ": " + abratask.title + " OR " + cubtask.pokemon.name + ": " + cubtask.title + " OR " + kabtask.pokemon.name + ": " + kabtask.title + "? ").lower()
    if (social_task == abratask.pokemon.name.lower() or social_task == cubtask.pokemon.name.lower() or social_task == kabtask.pokemon.name.lower()):
        thetask = task_list.get(social_task)
        finishedtask = input("Hi I'm " + thetask.pokemon.name + " and your task today is: " + thetask.desc + " Have you completed this task? ").lower()
        if (finishedtask == "yes"):
            choosecatch = input("Congratulations! You are one step closer to becoming champion of the Sassyland region! I am very inspired by what you have done. Can I join you? If not, I'll help you evolve: ").lower()
            if (choosecatch == "evolve"):
                evolution()
            else:
                user.party.party.append(thetask.pokemon)
                print("Congratulations! " + thetask.pokemon.name + " has joined your party!")
        else:
            print("It was nice to meet you! Truly sorry to see you go :(")
    else: 
        print("Did not enter the task")    
    path_choice()

def perceiving_path():
    nate_party = PokemonParty()
    machop = Pokemon("machop")
    zubat = Pokemon("zubat")
    bellsprout = Pokemon("bellsprout")
    nate_party.party = [machop, zubat, bellsprout]
    nate_jabiru = Trainer(plan="spontaneous", name="Nate Jabiru", party=nate_party)
    print("Didn't see you coming! I'm " + nate_jabiru.name + " and I will be taking you on the " + nate_jabiru.plan + " path! You will be able to spend time really going on a true adventure.")
    social_task = input("Please select one of the following paths: " + zubtask.pokemon.name + ": " + zubtask.title + " OR " + mactask.pokemon.name + ": " + mactask.title + " OR " + beltask.pokemon.name + ": " + beltask.title + "? ").lower()
    if (social_task == zubtask.pokemon.name.lower() or social_task == mactask.pokemon.name.lower() or social_task == beltask.pokemon.name.lower()):
        thetask = task_list.get(social_task)
        finishedtask = input("Hi I'm " + thetask.pokemon.name + " and your task today is: " + thetask.desc + " Have you completed this task? ").lower()
        if (finishedtask == "yes"):
            choosecatch = input("Congrats bestie! You are one step closer to becoming champion of the Sassyland region! I am very inspired by what you have done. I know it's last minute, but I'd love to join you! Can I join you? Otherwise I'll help a buddy of yours evolve").lower()
            if (choosecatch == "evolve"):
                evolution()
            else:
                user.party.party.append(thetask.pokemon)
                print("Congratulations! " + thetask.pokemon.name + " has joined your party!")
        else:
            print("It was nice to meet you! Truly sorry to see you go :(")
    else: 
        print("Did not enter the task")    
    path_choice()

def judging_path():
    gem_party = PokemonParty()
    vulpix = Pokemon("vulpix")
    gastly = Pokemon("gastly")
    horsea = Pokemon("horsea")
    gem_party.party = [vulpix, gastly, horsea]
    gem_gemmy = Trainer(plan="planning", name="Gem of Ordinance", party=gem_party)
    print("I was expecting you, young trainer. I'm " + gem_gemmy.name + " and I will be taking you on the " + gem_gemmy.plan + " path! You will be able to plan for what's in store.")
    social_task = input("Please select one of the following paths: " + vultask.pokemon.name + ": " + vultask.title + " OR " + gastask.pokemon.name + ": " + gastask.title + " OR " + hortask.pokemon.name + ": " + hortask.title + "? ").lower()
    if (social_task == hortask.pokemon.name.lower() or social_task == vultask.pokemon.name.lower() or social_task == gastask.pokemon.name.lower()):
        thetask = task_list.get(social_task)
        finishedtask = input("Hi I'm " + thetask.pokemon.name + " and your task today is: " + thetask.desc + " Have you completed this task? ").lower()
        if (finishedtask == "yes"):
            choosecatch = input("Congrats bestie! You are one step closer to becoming champion of the Sassyland region! I am very inspired by what you have done. I know it's last minute, but I'd love to join you! Can I join you? Otherwise I'll help a buddy of yours evolve").lower()
            if (choosecatch == "evolve"):
                evolution()
            else:
                user.party.party.append(thetask.pokemon)
                print("Congratulations! " + thetask.pokemon.name + " has joined your party!")
        else:
            print("It was nice to meet you! Truly sorry to see you go :(")
    else: 
        print("Did not enter the task")    
    path_choice()

def professor_lab():
    print("Hello again " + user.name + "! It is great to see you begin your journey within Sassyland. Today is an exciting day! You will be meeting your first pokemon.")
    starter_choice = input("Please choose your starter! ").lower()
    starter_pokemon = Pokemon(starter_choice)
    if starter_choice == "bulbasaur":
        starter_pokemon.evolution = "ivysaur"
    elif starter_choice == "squirtle":
        starter_pokemon.evolution = "wartortle"
    else:
        starter_pokemon.evolution = "charmeleon"

    pokemon_list = [starter_pokemon]
    pokemon_party = PokemonParty(pokemon_list)
    user.party = pokemon_party
    print("Congratulations on your " + starter_pokemon.name + ", " + user.name + "! It seems to be really attached to you! This " + starter_pokemon.name + " will be your first buddy to explore the region.")

def path_choice():
    path_choice = input("Based on our extensive research on your personality, we have determined the routes that will prove most exciting! Please select one of the following: " + user.social + " or " + user.plan + "! ").lower()
    if path_choice == "introspection":
        introspect_path()
    elif path_choice == "social":
        social_path()
    elif path_choice == "spontaneous":
        perceiving_path()
    elif path_choice == "planning":
        judging_path()
    else:
        print("Come back another time! We look forward to seeing you again in the future.")

professor_lab()
path_choice()

# print(user.name, user.party, user.social, user.obs, user.thinking, user.plan)

# for pokemon in user.party.party:
#     print(pokemon.name)
