# https://realpython.com/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/
import os, random
from flask import Flask, request, render_template

from median_maintenance import get_median

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
            arr_of_numbers = sequence_of_numbers.split(" ")
            median = get_median(arr_of_numbers)
            results = median
        except:
            errors.append(
                "Unable to get sequence of numbers. Please type them in again."
            )
    return render_template('index.html', errors=errors, results=results)


if __name__ == '__main__':
    app.run()
