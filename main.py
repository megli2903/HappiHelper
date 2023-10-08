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
evolution_lines = [
    ["Bulbasaur", "Ivysaur", "Venusaur"],
    ["Charmander", "Charmeleon", "Charizard"],
    ["Squirtle", "Wartortle", "Blastoise"],
    ["Caterpie", "Metapod", "Butterfree"],
    ["Weedle", "Kakuna", "Beedrill"],
    ["Pidgey", "Pidgeotto", "Pidgeot"],
    ["Rattata", "Raticate"],
    ["Spearow", "Fearow"],
    ["Ekans", "Arbok"],
    ["Pikachu", "Raichu"],
    ["Sandshrew", "Sandslash"],
    ["Nidoran♀", "Nidorina", "Nidoqueen"],
    ["Nidoran♂", "Nidorino", "Nidoking"],
    ["Clefairy", "Clefable"],
    ["Vulpix", "Ninetales"],
    ["Jigglypuff", "Wigglytuff"],
    ["Zubat", "Golbat"],
    ["Oddish", "Gloom", "Vileplume"],
    ["Paras", "Parasect"],
    ["Venonat", "Venomoth"],
    ["Diglett", "Dugtrio"],
    ["Meowth", "Persian"],
    ["Psyduck", "Golduck"],
    ["Mankey", "Primeape"],
    ["Growlithe", "Arcanine"],
    ["Poliwag", "Poliwhirl", "Poliwrath"],
    ["Abra", "Kadabra", "Alakazam"],
    ["Machop", "Machoke", "Machamp"],
    ["Bellsprout", "Weepinbell", "Victreebel"],
    ["Tentacool", "Tentacruel"],
    ["Geodude", "Graveler", "Golem"],
    ["Ponyta", "Rapidash"],
    ["Slowpoke", "Slowbro"],
    ["Magnemite", "Magneton"],
    ["Farfetch'd"],
    ["Doduo", "Dodrio"],
    ["Seel", "Dewgong"],
    ["Grimer", "Muk"],
    ["Shellder", "Cloyster"],
    ["Gastly", "Haunter", "Gengar"],
    ["Onix"],
    ["Drowzee", "Hypno"],
    ["Krabby", "Kingler"],
    ["Voltorb", "Electrode"],
    ["Exeggcute", "Exeggutor"],
    ["Cubone", "Marowak"],
    ["Hitmonlee"],
    ["Hitmonchan"],
    ["Lickitung"],
    ["Koffing", "Weezing"],
    ["Rhyhorn", "Rhydon"],
    ["Chansey"],
    ["Tangela"],
    ["Kangaskhan"],
    ["Horsea", "Seadra"],
    ["Goldeen", "Seaking"],
    ["Staryu", "Starmie"],
    ["Mr. Mime"],
    ["Scyther"],
    ["Jynx"],
    ["Electabuzz"],
    ["Magmar"],
    ["Pinsir"],
    ["Tauros"],
    ["Magikarp", "Gyarados"],
    ["Lapras"],
    ["Ditto"],
    ["Eevee", "Vaporeon", "Jolteon", "Flareon"],
    ["Porygon"],
    ["Omanyte", "Omastar"],
    ["Kabuto", "Kabutops"],
    ["Aerodactyl"],
    ["Snorlax"],
    ["Articuno"],
    ["Zapdos"],
    ["Moltres"],
    ["Dratini", "Dragonair", "Dragonite"],
    ["Mewtwo"],
    ["Mew"],
]



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
        print("Great choice to choose the " + path_choice + " path! A thrilling journey of resilience with " + starter_choice + " awaits!")
        user.currentpath = path_choice

professor_lab()

print(user.name, user.party, user.social, user.obs, user.thinking, user.plan)

def social_path():
    charlotte_party = PokemonParty()
    farfetchd = Pokemon("Farfetch'd", None)
    jigglypuff = Pokemon("Jigglypuff", "Wigglytuff")
    clefairy = Pokemon("Clefairy", "Clefable")
    charlotte_party.append(farfetchd, jigglypuff, clefairy)
    charlotte_reindeer = Trainer(social="social", name="Charlotte Reindeer", party=charlotte_party)
    print("Hey trainer! My name is " + charlotte_reindeer.name + " and I will be taking you on the" + charlotte_reindeer.social + "path! To get started on your journey, we will be providing you some social tasks.")

