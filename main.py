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

class Trainer:
    def __init__(self, social=None, name=None, plan=None, party=None):
        self.social = social
        self.name = name
        self.plan = plan
        self.party = party

class Pokemon:
    def __init__(self, name=None, evolution=None):
        self.name = name
        self.evolution = evolution

class PokemonParty:
    def __init__(self, party=None):
        self.party = party


def welcome():
    nameask = input("Happi you are here! Please enter your name here: ")
    trainer_type = Trainer()
    trainer_type.name = nameask
    personal = input("Hello " + nameask + "! My name is Professor Banerjee, and I will be taking you to the region of Sassyland. Select your trainer type: ")
    if "E" in personal:
        trainer_type.social = "social"
    else:
        trainer_type.social = "introspect" 
    if "P" in personal:
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

user = professor_lab()


