from flask import Flask, render_template, request
import pickle
import numpy as np

# import sklearn

# Load the Logistic Regression model
classifier = pickle.load(open('finalmodel1.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        rate_marriage= float(request.form['rate_marriage'])
        age= float(request.form['age'])
        children= float(request.form['children'])
        religious= float(request.form['religious'])
        educ= float(request.form['educ'])
        occupation= float(request.form['occupation'])
        occupation_husb= float(request.form['occupation_husb'])
        affairs= float(request.form['affairs'])

        # int_features = [int(x) for x in request.form.values()]

        # final_features = [np.array(int_features)]

        data = np.array([[rate_marriage, age, children, religious, educ, occupation, occupation_husb, affairs]])
        my_prediction = classifier.predict(data)

        if my_prediction == 1:
            result = "Great! No Affair."
        if my_prediction == 0:
            result = "Oops! You Have Affair"

        return render_template('result.html', Prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True)