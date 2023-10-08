from flask import Flask, render_template
import main  # Import your Python script (main.py)

app = Flask(__name__)

@app.route('/')
def home():
    # Call a function from your main.py script to get data
    data = main.get_data()  # Replace with your actual function
    return render_template('startjourney.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
