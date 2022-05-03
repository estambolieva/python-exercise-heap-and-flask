# https://realpython.com/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/
import os, random
from flask import Flask, request, render_template

app = Flask(__name__)
# from models import Result

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            sequence_of_numbers = request.form['sequence']
            print(sequence_of_numbers)
            rand_num  = random. random() 
            results = rand_num
            print(results)
        except:
            errors.append(
                "Unable to get sequence of numbers. Please type them in again."
            )
    return render_template('index.html', errors=errors, results=results)


if __name__ == '__main__':
    app.run()
