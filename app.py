from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load model
with open("Titanic.pkl", "rb") as f:
    pipeline = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])  # ✅ Allow both GET and POST
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])  # ✅ Allow both GET and POST
def predict():
    if request.method == "POST":  # ✅ Ensure only POST processes data
        try:
            user_input = {
                "Pclass": int(request.form["Pclass"]),
                "Sex": request.form["Gender"],
                "Age": int(request.form["Age"]),
                "SibSp": int(request.form["SibSp"]),
                "Parch": int(request.form["Parch"]),
                "total_member": int(request.form["Total Members"]),
                "is_alone": request.form["Is Alone"],
                "single_price": float(request.form["Single Price"]),
                "Embarked": request.form["Embarked"]
            }

            # ✅ Fix Mappings
            user_input["Sex"] = 1 if user_input["Sex"] == "Male" else 2
            user_input["is_alone"] = 1 if user_input["is_alone"] == "Yes" else 0
            user_input["Embarked"] = {"S": 1, "C": 2, "Q": 3}.get(user_input["Embarked"], 0)

            new_data = pd.DataFrame([user_input])
            prediction = pipeline.predict(new_data)[0]
            return render_template("index.html", prediction_text=f"Prediction: {'Survived' if prediction == 1 else 'Did Not Survive'}")

        except Exception as e:
            return render_template("index.html", prediction_text=f"Error: {e}")
    
    return render_template("index.html")  # ✅ Handle GET requests properly

if __name__ == "__main__":
    app.run(debug=True)
