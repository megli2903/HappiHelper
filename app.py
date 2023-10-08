from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

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
        self.social = social  # E or I
        self.thinking = thinking
        self.obs = obs
        self.name = name
        self.plan = plan
        self.party = party  # pokemon party -> each catch appends
        self.currentpath = currentpath  # path user is currently on

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

task_list = {}

# Social path pokemon and tasks

farfetchd = Pokemon("farfetch'd")
jigglypuff = Pokemon("jigglypuff")
clefairy = Pokemon("clefairy")

fartask = Task(farfetchd, "Connect with loved ones", "Initiate social interactions regularly to maintain connections with friends and loved ones.")
jigtask = Task(jigglypuff, "Attend social event", "Attend social events, gatherings, or group activities to recharge your energy.")
cleftask = Task(clefairy, "Team Building", "Engage in team-oriented projects or collaborative activities to satisfy your need for interaction.")

# Introvert path pokemon and tasks

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

# all tasks list

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

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        personality_type = request.form.get('personality_type')
        starter_pokemon = request.form.get('starter_pokemon')

        # Create the Trainer object with user inputs
        trainer_type = Trainer(name=user_name, social=personality_type)

        # Store the chosen starter Pokémon
        starter_choice = starter_pokemon.lower()
        starter_pokemon_obj = Pokemon(starter_choice)
        if starter_choice == "bulbasaur":
            starter_pokemon_obj.evolution = "ivysaur"
        elif starter_choice == "squirtle":
            starter_pokemon_obj.evolution = "wartortle"
        else:
            starter_pokemon_obj.evolution = "charmeleon"

        # Create a PokemonParty with the chosen starter Pokémon
        pokemon_list = [starter_pokemon_obj]
        pokemon_party = PokemonParty(pokemon_list)
        trainer_type.party = pokemon_party

        return render_template('startjourney.html', user_name=user_name, starter_pokemon=starter_pokemon_obj)

    return render_template('startjourney.html')

@app.route('/selectpath', methods=['GET', 'POST'])
def pathselect():
    url = ""
    if request.method == 'POST':
        selected_path = request.form.get('selected_path')
        url = f"confirmation/{selected_path}"
        return render_template('pathselect.html')
    return redirect(url)

@app.route('/confirmation', methods=["POST"])
def confirmation():
    selected_path = request.form.to_dict()["selected_path"]
    return render_template('confirmation.html', selected_path=selected_path)



# @app.route('/selectpath', methods=['GET', 'POST'])
# def pathselect():
#     if request.method == 'POST':
#         selected_path = request.form.get('selected_path')
#         url = f"confirmation/{selected_path}"
#         return redirect(url)
    
#     return render_template('pathselect.html')

# @app.route('/confirmation/<selected_path>')
# def confirmation(selected_path):
#     return render_template('confirmation.html', selected_path=selected_path)



# def professor_lab():
#     print("Hello again " + user.name + "! It is great to see you begin your journey within Sassyland. Today is an exciting day! You will be meeting your first pokemon.")
#     starter_choice = input("Please choose your starter! ").lower()
#     starter_pokemon = Pokemon(starter_choice)
#     if starter_choice == "bulbasaur":
#         starter_pokemon.evolution = "ivysaur"
#     elif starter_choice == "squirtle":
#         starter_pokemon.evolution = "wartortle"
#     else:
#         starter_pokemon.evolution = "charmeleon"

#     pokemon_list = [starter_pokemon]
#     pokemon_party = PokemonParty(pokemon_list)
#     user.party = pokemon_party
#     print("Congratulations on your " + starter_pokemon.name + ", " + user.name + "! It seems to be really attached to you! This " + starter_pokemon.name + " will be your first buddy to explore the region.")
# def welcome():
#     nameask = input("Happi you are here! Please enter your name here: ")
#     trainer_type = Trainer()
#     trainer_type.name = nameask
#     personal = input(
#         "Hello " + nameask + "! My name is Professor Banerjee, and I will be taking you to the region of Sassyland. Select your trainer type: ").upper()
#     if personal[0] == "E":
#         trainer_type.social = "social"
#     else:
#         trainer_type.social = "introspection"
#     if personal[1] == "N":
#         trainer_type.obs = "intuition"
#     else:
#         trainer_type.obs = "observation"
#     if personal[2] == "F":
#         trainer_type.thinking = "feeling"
#     else:
#         trainer_type.thinking = "thought"
#     if personal[3] == "P":
#         trainer_type.plan = "spontaneous"
#     else:
#         trainer_type.plan = "planning"
#     return trainer_type

# user = welcome()

# def evolution():
#     evolvable_pokemon = []
#     evolvable_pokemon_names = []
#     for pokemon in user.party.party:
#         print(pokemon.name)
#         if pokemon.name.lower() in evolution_lines.keys():
#             evolvable_pokemon.append(pokemon)
#             evolvable_pokemon_names.append(pokemon.name)
#     if len(evolvable_pokemon_names) == 0:
#         print("Sorry, all your pokemon are fully evolved")
#         return
#     print("Please select the slot of the pokemon you would like to evolve!")
#     evo_idx = input(evolvable_pokemon_names)  # this needs to take in an integer value
#     idx = int(evo_idx)
#     if idx < len(evolvable_pokemon_names):
#         prevolution = evolvable_pokemon[idx].name
#         evolvable_pokemon[idx].name = evolution_lines.get(evolvable_pokemon[idx].name)
#         print("Congratulations! Your " + prevolution + " has evolved into a " + evolvable_pokemon[idx].name + "!")

# def social_path():
#     charlotte_party = PokemonParty()
#     farfetchd = Pokemon("farfetch'd")
#     jigglypuff = Pokemon("jigglypuff")
#     clefairy = Pokemon("clefairy")
#     charlotte_party.party = [farfetchd, jigglypuff, clefairy]
#     charlotte_reindeer = Trainer(social="social", name="Charlotte Reindeer", party=charlotte_party)
#     print("Hey trainer! My name is " + charlotte_rseindeer.name + " and I will be taking you on the " + charlotte_reindeer.social + " path! To get started on your journey, we will be providing you some social tasks.")
#     social_task = input(
#         "Please select one of the following paths: " + fartask.pokemon.name + ": " + fartask.title + " OR " + jigtask.pokemon.name + ": " + jigtask.title + " OR " + cleftask.pokemon.name + ": " + cleftask.title + "? ").lower()

if __name__ == '__main__':
    app.run(debug=True)
