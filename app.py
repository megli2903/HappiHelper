from flask import Flask, render_template
import main  # Import your Python script (main.py)
from main import Trainer

app = Flask(__name__)

@app.route('/')
def home():
    # Call a function from your main.py script to get data
    data = main.get_data()  # Replace with your actual function
    return render_template('startjourney.html', data=data)

@app.route('/')
def index():
    user = Trainer(social=None, name=None, thinking=None, obs=None, plan=None, currentpath=None, party=None) 
    return render_template('pathselect.html', user=user)

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
