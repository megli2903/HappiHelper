from flask import Flask, render_template, request
import main  # Import your Python script (main.py)
from main import Trainer

app = Flask(__name__)

# @app.route('/')
# def home():
#     # Call a function from your main.py script to get data
#     data = main.get_data()  # Replace with your actual function
#     return render_template('startjourney.html', data=data)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_name = None  # Initialize user_name to None

    if request.method == 'POST':
        # If the form is submitted, get the user's name from the form
        user_name = request.form.get('user_name')

    return render_template('trainerinfo.html', user_name=user_name)


# @app.route("/")
# def home():
#     return render_template('trainerinfo.html')
# @app.route('/social')
# def social():
#     user = Trainer(social=None, name=None, thinking=None, obs=None, plan=None, currentpath=None, party=None)   # You might want to replace this with the actual user data
#     # Modify this function to return relevant data for the social path
#     return render_template('social.html', user=user)

# @app.route('/spontaneous')
# def spontaneous():
#     user = Trainer(social=None, name=None, thinking=None, obs=None, plan=None, currentpath=None, party=None)   # You might want to replace this with the actual user data
#     # Modify this function to return relevant data for the spontaneous path
#     return render_template('spontaneous.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
