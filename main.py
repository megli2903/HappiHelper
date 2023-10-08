def trainer_selection():
    personality_types = {
    "ISTJ": ["Inspector", "Goal-setting", "Work-life balance", "Open-mindedness"], 
    "ISFJ": ["Protector", "Boundary Setting", "Self-Care", "Creativity"],
    "INFJ": ["Counselor", "Intuition", "Connection", "Creativity"], 
    "INTJ": ["Mastermind", "Strategic", "Knowledge", "Independence"],
    "ISTP": ["Craftsman", "Analytical", "Adventurous", "Self-Sufficient"], 
    "ISFP": ["Composer", "Artistic", "Sensitive", "Expressive"], 
    "INFP": ["Healer", "Idealistic", "Compassionate", "Imaginative"], 
    "INTP": ["Architect", "Analytical", "Curious", "Innovative"],
    "ESTP": ["Dynamo", "Energetic", "Bold", "Resourceful"], 
    "ESFP": ["Performer", "Spontaneous", "Enthusiastic", "Social"], 
    "ENFP": ["Champion", "Passionate", "Creative", "Inspirational"], 
    "ENTP": ["Visionary", "Innovative", "Curious", "Strategic"],
    "ESTJ": ["Supervisor", "Organized", "Responsible", "Efficient"], 
    "ESFJ": ["Provider", "Nurturing", "Supportive", "Sociable"], 
    "ENFJ": ["Teacher", "Inspiring", "Compassionate", "Persuasive"], 
    "ENTJ": ["Commander", "Leadership", "Ambitious", "Strategic"]
    }

    # pokemon_party = []
    while True:
        trainer_type = input("Hello young SASE'r! My name is Professor Banerjee, and I will be taking you to the region of Sassyland. Select your trainer type: ")
        if trainer_type in personality_types:
            # pokemon_party.append(trainer_type)
            print(trainer_type + " is such a good fit! Reminds me of you :)")
            return trainer_type
        else:
            print("Sorry, " + trainer_type + " is not an option")

personality = trainer_selection()

def professor_lab():
    print("Good morning young " + personality + ". Today marks the beginning of a new journey through Sassyland")
    input("Based on your personality, you are a " + personality[1])

professor_lab()


