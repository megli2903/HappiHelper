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
evolution_lines = {"Bulbasaur":"Ivysaur", "Ivysaur":"Venusaur",
    "Charmander":"Charmeleon","Charmeleon":"Charizard",
    "Squirtle":"Wartortle", "Wartortle":"Blastoise",
    "Caterpie": "Metapod", "Metapod":"Butterfree",
    "Weedle":"Kakuna", "Kakuna":"Beedrill",
    "Pidgey":"Pidgeotto", "Pidgeotto":"Pidgeot",
    "Rattata":"Raticate",
    "Spearow":"Fearow",
    "Ekans":"Arbok",
    "Pikachu":"Raichu",
    "Sandshrew":"Sandslash",
    "Nidoran♀":"Nidorina", "Nidorina":"Nidoqueen", #special pokemon
    "Nidoran♂":"Nidorino", "Nidorino":"Nidoking", #special pokemon
    "Clefairy":"Clefable",
    "Vulpix":"Ninetales",
    "Jigglypuff":"Wigglytuff",
    "Zubat":"Golbat",
    "Oddish":"Gloom", "Gloom":"Vileplume",
    "Paras":"Parasect",
    "Venonat":"Venomoth",
    "Diglett":"Dugtrio",
    "Meowth":"Persian",
    "Psyduck":"Golduck",
    "Mankey":"Primeape",
    "Growlithe":"Arcanine",
    "Poliwag":"Poliwhirl", "Poliwhirl":"Poliwrath",
    "Abra":"Kadabra", "Kadabra":"Alakazam",
    "Machop":"Machoke", "Machoke":"Machamp",
    "Bellsprout":"Weepinbell", "Weepinbell":"Victreebel",
    "Tentacool":"Tentacruel",
    "Geodude":"Graveler", "Graveler":"Golem",
    "Ponyta":"Rapidash",
    "Slowpoke":"Slowbro",
    "Magnemite":"Magneton",
    "Doduo":"Dodrio",
    "Seel":"Dewgong",
    "Grimer":"Muk",
    "Shellder":"Cloyster",
    "Gastly":"Haunter","Haunter":"Gengar",
    "Drowzee":"Hypno",
    "Krabby":"Kingler",
    "Voltorb":"Electrode",
    "Exeggcute":"Exeggutor",
    "Cubone":"Marowak",
    "Koffing":"Weezing",
    "Rhyhorn":"Rhydon",
    "Horsea":"Seadra",
    "Goldeen":"Seaking",
    "Staryu":"Starmie",
    "Magikarp":"Gyarados",
    #"Eevee", "Vaporeon", "Jolteon", "Flareon",
    "Omanyte":"Omastar",
    "Kabuto":"Kabutops",
    "Dratini":"Dragonair", "Dragonair":"Dragonite"
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

farfetchd = Pokemon("Farfetch'd")
jigglypuff = Pokemon("Jigglypuff")
clefairy = Pokemon("Clefairy")

fartask = Task(farfetchd, "Connect with loved ones", "Initiate social interactions regularly to maintain connections with friends and loved ones.")
jigtask = Task(jigglypuff, "Attend social event", "Attend social events, gatherings, or group activities to recharge your energy")
cleftask = Task(clefairy, "Team Building", "Engage in team-oriented projects or collaborative activities to satisfy your need for interaction.")

#Introvert path pokemon and tasks

abra = Pokemon("Abra")
cubone = Pokemon("Cubone")
kabuto = Pokemon("Kabuto")

abratask = Task("Abra", "Allocate me-time", "Allocate regular me-time for solitude and self-reflection.")
cubtask = Task("Cubone", "Create cozy atmosphere", "Create a quiet and cozy space at home for relaxation and personal activities.")
kabtask = Task("Kabuto", "Explore your hobbies", "Dedicate time to your favorite solitary hobbies, such as reading, writing, or art.")

task_list = {
"farfetch'd": fartask,
"jigglypuff": jigtask,
"clefairy": cleftask
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

def professor_lab():
    print("Hello again " + user.name + "! It is great to see you begin your journey within Sassyland. Today is an exciting day! You will be meeting your first pokemon.")
    starter_choice = input("Please choose your starter! ").lower()
    starter_pokemon = Pokemon(starter_choice)
    if starter_choice == "bulbusaur":
        starter_pokemon.evolution = "ivysaur"
    elif starter_choice == "squirtle":
        starter_pokemon.evolution = "ivysaur"
    else:
        starter_pokemon.evolution = "charmeleon"

    pokemon_list = [starter_pokemon]
    pokemon_party = PokemonParty(pokemon_list)
    user.party = pokemon_party
    print("Congratulations on your " + starter_pokemon.name + ", " + user.name + "! It seems to be really attached to you! This " + starter_pokemon.name + " will be your first buddy to explore the region.")
    path_choice = input("Based on our extensive research on your personality, we have determined the routes that will prove most exciting! Please select one of the following: " + user.social + " or " + user.plan + "! ").lower()
    if path_choice == user.social or path_choice == user.plan:
        print("Great choice!")
        user.currentpath = path_choice

professor_lab()


# print(user.name, user.party, user.social, user.obs, user.thinking, user.plan)

def evolution():
    evolvable_pokemon = []
    evolvable_pokemon_names = []
    for pokemon in user.party.party:
        if evolution_lines.has_key(pokemon):
            evolvable_pokemon.append(pokemon)
            evolvable_pokemon_names.append(pokemon.name)
    if evolvable_pokemon_names.len() == 0:
        print("Sorry, all your pokemon are fully evolved")
    toevolve = input("Please select a pokemon to evolve: " + evolvable_pokemon_names + ": ")
    if toevolve.lower() in       
    print("insert evolution print here")



def social_path():
    charlotte_party = PokemonParty()
    farfetchd = Pokemon("Farfetch'd")
    jigglypuff = Pokemon("Jigglypuff")
    clefairy = Pokemon("Clefairy")
    charlotte_party.party = [farfetchd, jigglypuff, clefairy]
    charlotte_reindeer = Trainer(social="social", name="Charlotte Reindeer", party=charlotte_party)
    print("Hey trainer! My name is " + charlotte_reindeer.name + " and I will be taking you on the " + charlotte_reindeer.social + " path! To get started on your journey, we will be providing you some social tasks.")
    social_task = input("Please select one of the following paths: " + fartask.pokemon.name + ": " + fartask.title + " OR " + jigtask.pokemon.name + ": " + jigtask.title + " OR " + cleftask.pokemon.name + ": " + cleftask.title + "? ").lower()
    if (social_task == fartask.pokemon.name.lower() or social_task == jigtask.pokemon.name.lower() or social_task == cleftask.pokemon.name.lower()):
        thetask = task_list.get(social_task)
        finishedtask = input("Hiya trainer! My name is: " + thetask.pokemon.name + " and your task today is: " + thetask.desc + ". Have you completed this task?").lower()
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



social_path()
