# # # from flask import Flask, render_template, request
# # # import joblib

# # # app = Flask(__name__)

# # # # Load your trained ML model
# # # model = joblib.load("lung/model/lung.pickle")
# # # # model = joblib.load("model/lung.pickle")

# # # # 🟢 Landing page route
# # # @app.route('/')
# # # def landing():
# # #     return render_template('landing_page.html')

# # # # 🟢 Form page route
# # # @app.route('/form')
# # # def index():
# # #     return render_template('index.html')

# # # # 🟢 Prediction route
# # # @app.route('/predict', methods=['POST'])
# # # def predict():
# # #     if request.method == 'POST':
# # #         # Collect data from form (update field names according to your index.html form)
# # #         features = [
# # #             int(request.form['AGE']),
# # #             int(request.form['GENDER']),
# # #             int(request.form['SMOKING']),
# # #             int(request.form['YELLOW_FINGERS']),
# # #             int(request.form['ANXIETY']),
# # #             int(request.form['PEER_PRESSURE']),
# # #             int(request.form['CHRONIC DISEASE']),
# # #             int(request.form['FATIGUE']),
# # #             int(request.form['ALLERGY']),
# # #             int(request.form['WHEEZING']),
# # #             int(request.form['ALCOHOL CONSUMING']),
# # #             int(request.form['COUGHING']),
# # #             int(request.form['SHORTNESS OF BREATH']),
# # #             int(request.form['SWALLOWING DIFFICULTY']),
# # #             int(request.form['CHEST PAIN'])
# # #         ]

# # #         # Make prediction
# # #         prediction = model.predict([features])[0]

# # #         # Output message
# # #         if prediction == 1:
# # #             result_text = "High chance of Lung Cancer. Please consult a doctor."
# # #         else:
# # #             result_text = "Low chance of Lung Cancer. Stay healthy!"

# # #         return render_template('result.html', prediction=result_text)

# # # if __name__ == '__main__':
# # #     app.run(debug=True)



# # # from flask import Flask, render_template, request
# # # import pickle
# # # import numpy as np

# # # app = Flask(__name__)

# # # # Load the model
# # # try:
# # #     with open(r'D:\Appro_Project_1(image_classification)\prediction\lung\model\lung.pickle', 'rb') as file:
# # #         model1 = pickle.load(file)
# # # except Exception as e:
# # #     print(f"Error loading model: {e}")
# # #     model1 = None
# # # @app.route('/')
# # # def landing():
# # #     return render_template('landing_page.html') 

# # # @app.route("/")
# # # def index():
# # #     return render_template("index.html")

# # # @app.route("/predict", methods=['POST'])
# # # def predict():
# # #     try:
# # #         # Get form data
# # #         d1 = int(request.form['GENDER'])
# # #         # sex_input = request.form['AGE']  # "male" or "female"
# # #         # d2 = 1 if sex_input.lower() == "male" else 0
# # #         d2 = int(request.form['AGE'])
# # #         d3 = int(request.form['SMOKING'])
# # #         d4 = int(request.form['YELLOW_FINGERS'])
# # #         d5 = int(request.form['ANXIETY'])
# # #         d6 = int(request.form['PEER_PRESSURE'])
# # #         d7 = int(request.form['CHRONIC DISEASE'])
# # #         d8 = int(request.form['FATIGUE'])
# # #         d9 = int(request.form['ALLERGY'])
# # #         d10 = float(request.form['WHEEZING'])  # should be float
# # #         d11 = int(request.form['ALCOHOL CONSUMING'])  
# # #         d12 = int(request.form['COUGHING'])
# # #         d13 = int(request.form['SHORTNESS OF BREATH'])
# # #         d14 = int(request.form['SWALLOWING DIFFICULTY'])
# # #         d15 = int(request.form['CHEST PAIN'])

    
# # #         # Create input array for prediction
# # #         arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13,d14, d15]])

# # #         # Predict
# # #         if model1:
# # #             pred1 = model1.predict(arr)
# # #             risk = int(pred1[0])
# # #         else:
# # #             risk = 0  # fallback if model isn't loaded

# # #         # Pass result to template
# # #         return render_template("result.html", prediction=risk,risk=risk)

# # #     except Exception as e:
# # #         return f"An error occurred: {e}"

# # # if __name__ == "__main__":
# # #     app.run(debug=True)

# # from flask import Flask, request, render_template
# # import pickle
# # import numpy as np

# # app = Flask(__name__)

# # # Load the model
# # try:
# #     with open(r'D:\Appro_Project_1(image_classification)\prediction\lung\model\lung.pickle', 'rb') as file:
# #         model1 = pickle.load(file)
# # except Exception as e:
# #     print(f"Error loading model: {e}")
# #     model1 = None


# # @app.route("/predict", methods=['POST'])
# # def predict():
# #     try:
# #         def parse(val):
# #             return 1 if val.lower() == 'yes' else 0
        
# #         # Convert 'yes'/'no' inputs to 1/0
# #         d1 = parse(request.form['GENDER'])
# #         d2 = int(request.form['AGE'])  # Keep AGE as int
# #         d3 = parse(request.form['SMOKING'])
# #         d4 = parse(request.form['YELLOW_FINGERS'])
# #         d5 = parse(request.form['ANXIETY'])
# #         d6 = parse(request.form['PEER_PRESSURE'])
# #         d7 = parse(request.form['CHRONIC DISEASE'])
# #         d8 = parse(request.form['FATIGUE'])
# #         d9 = parse(request.form['ALLERGY'])
# #         d10 = parse(request.form['WHEEZING'])  # Assume yes/no
# #         d11 = parse(request.form['ALCOHOL CONSUMING'])
# #         d12 = parse(request.form['COUGHING'])
# #         d13 = parse(request.form['SHORTNESS OF BREATH'])
# #         d14 = parse(request.form['SWALLOWING DIFFICULTY'])
# #         d15 = parse(request.form['CHEST PAIN'])

# #         arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15]])

# #         if model1:
# #             pred1 = model1.predict(arr)
# #             risk = int(pred1[0])
# #             return render_template("result.html", prediction=risk)
# #         else:
# #             return render_template("result.html", prediction=None)

# #     except Exception as e:
# #         return render_template("result.html", prediction=None, error=str(e))


# # if __name__ == "__main__":
# #     app.run(debug=True)

# # from flask import Flask, render_template, request
# # import joblib
# # import numpy as np
# # # import os

# # app = Flask(__name__)

# # # --- Load Model Safely ---
# # # Adjust path: model is inside "lung/model/lung.pickle"
# # model_path = os.path.join(os.path.dirname(__file__), "model", "lung.pickle")

# # try:
# #     model = joblib.load(model_path)
# # except Exception as e:
# #     model = None
# #     print(f"⚠ Error loading model: {e}")


# # # --- Home Page (Form) ---
# # @app.route("/")
# # def index():
# #     return render_template("index.html")


# # # --- Prediction Route ---
# # @app.route("/predict", methods=["POST"])
# # def predict():
# #     if model is None:
# #         return render_template("result.html", prediction=None, error="Model not loaded properly.")

# #     try:
# #         # Collect form data
# #         features = [
# #             float(request.form.get("age", 0)),
# #             float(request.form.get("smoking", 0)),
# #             float(request.form.get("yellow_fingers", 0)),
# #             float(request.form.get("anxiety", 0)),
# #             float(request.form.get("peer_pressure", 0)),
# #             float(request.form.get("chronic_disease", 0)),
# #             float(request.form.get("fatigue", 0)),
# #             float(request.form.get("allergy", 0)),
# #             float(request.form.get("wheezing", 0)),
# #             float(request.form.get("alcohol", 0)),
# #             float(request.form.get("coughing", 0)),
# #             float(request.form.get("shortness_of_breath", 0)),
# #             float(request.form.get("swallowing_difficulty", 0)),
# #             float(request.form.get("chest_pain", 0)),
# #         ]

# #         # Convert to numpy array for prediction
# #         input_data = np.array(features).reshape(1, -1)
# #         prediction = model.predict(input_data)[0]

# #         return render_template("result.html", prediction=int(prediction), error=None)

# #     except Exception as e:
# #         return render_template("result.html", prediction=None, error=str(e))


# # # --- Run Flask ---
# # if __name__ == "__main__":
# #     app.run(debug=True)

# # from flask import Flask, render_template, request
# # import joblib
# # import numpy as np

# # app = Flask(__name__)

# # # Load the trained model
# # # model = joblib.load("D:\Appro_Project_1(image_classification)\prediction\lung\model\lung.pickle")
# # import os
# # import joblib

# # # Correct relative path
# # MODEL_PATH = os.path.join("D:\Appro_Project_1(image_classification)\prediction\lung\model\lung (2).pkl")
# # model = joblib.load(MODEL_PATH)




# # @app.route("/")
# # def home():
# #     return render_template("index.html")

# # @app.route("/form")
# # def form():
# #     return render_template("form.html")

# # @app.route("/predict", methods=["POST"])
# # def predict():
# #     try:
# #         # Get all form values
# #         features = [float(x) for x in request.form.values()]

# #         # ✅ Ensure only 13 features are passed (trim or adjust)
# #         expected_features = 13
# #         if len(features) > expected_features:
# #             features = features[:expected_features]   # take first 13
# #         elif len(features) < expected_features:
# #             return render_template("result.html", prediction=None,
# #                                    error=f"Expected {expected_features} features, but got {len(features)}")

# #         # Reshape for prediction
# #         features = np.array(features).reshape(1, -1)

# #         # Make prediction
# #         prediction = model.predict(features)[0]

# #         return render_template("result.html", prediction=prediction)

# #     except Exception as e:
# #         return render_template("result.html", prediction=None, error=str(e))

# # if __name__ == "__main__":
# #     app.run(debug=True)


# from flask import Flask, request, render_template
# import pickle
# import numpy as np
# import sys, traceback


# # Load trained model (pipeline with preprocessing + Logistic Regression)
# with open("D:\Appro_Project_1(image_classification)\prediction\lung\model\lung.pickle", "rb") as f:
#     model = pickle.load(f)

# app = Flask(__name__)

# try:
#     with open(r"D:\Appro_Project_1(image_classification)\heart-disease\model\heart (1).pickle", "rb") as file:
#         model1 = pickle.load(file)
#     print("[INFO] Model loaded successfully.")
# except Exception as e:
#     print(f"[ERROR] Loading model failed: {e}")
#     model1 = None

# FEATURES=["GENDER","AGE","SMOKING","YELLOW_FINGERS","ANXIETY","PEER_PRESSURE","CHRONIC_DISEASE","FATIGUE","ALLERGY","WHEEZING","ALCOHOL_CONSUMING","COUGHING","SHORTNESS_OF_BREATH","SWALLOWING_DIFFICULTY","CHEST_PAIN"]

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         print("\n====== /predict CALLED ======")
#         print("[RAW FORM] ->", request.form.to_dict())

#         d1 = int(request.form.get("GENDER", 0))
#         d2 = int(request.form.get("AGE", 0))
#         d3 = int(request.form.get("SMOKING", 0))
#         d4 = int(request.form.get("YELLOW_FINGERS", 0))
#         d5 = int(request.form.get("ANXIETY", 0))
#         d6 = int(request.form.get("PEER_PRESSURE", 0))
#         d7 = int(request.form.get("CHRONIC_DISEASE", 0))
#         d8 = int(request.form.get("FATIGUE", 0))
#         d9 = int(request.form.get("ALLERGY", 0))
#         d10 = float(request.form.get("WHEEZING", 0))
#         d11 = int(request.form.get("ALCOHOL_CONSUMING", 0))
#         d12 = int(request.form.get("COUGHING", 0))
#         d13 = int(request.form.get("SHORTNESS_OF_BREATH", 0))
#         d14 = int(request.form.get("SWALLOWING_DIFFICULTY", 0))
#         d15 = int(request.form.get("CHEST_PAIN", 0))

#         # Create array in correct order
#         arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15]], dtype=float)

#         print("[ORDER ] ->", FEATURES)
#         print("[PARSED] ->", arr.tolist())
#         print("[SHAPE ] ->", arr.shape)

        
#         # -------------------------------
#         # Prediction
#         # -------------------------------
#         if model1:
#             # Check if model supports probability
#             proba, score = None, None
#             if hasattr(model1, "predict_proba"):
#                 proba = model1.predict_proba(arr)[0]
#                 print("[PROBA ] ->", proba)
#             if hasattr(model1, "decision_function"):
#                 score = model1.decision_function(arr)
#                 print("[DECISION] ->", score)

#             pred1 = model1.predict(arr)
#             risk = int(pred1[0])
#             print("[PRED  ] ->", risk)
#         else:
#             print("[WARN] Model not loaded, defaulting risk=0")
#             risk = 0

#         return render_template(
#             "result.html",
#             risk=risk,
#             features=FEATURES,
#             values=arr.tolist()[0],
#             proba=None if proba is None else [float(p) for p in proba],
#         )

#     except Exception as e:
#         print("[EXCEPTION]", e, file=sys.stderr)
#         traceback.print_exc()
#         return f"An error occurred: {e}", 500




#     # try:
#     #     # Get input from form (all values as float)
#     #     input_data = [float(x) for x in request.form.values()]
#     #     input_array = np.array(input_data).reshape(1, -1)

#     #     # Predict using pipeline
#     #     prediction = model.predict(input_array)[0]

#     #     # If you want probability also:
#     #     probability = model.predict_proba(input_array)[0][1] * 100

#     #     result = "Positive (Lung Disease Detected)" if prediction == 1 else "Negative (No Lung Disease)"
#     #     return render_template(
#     #         "result.html",
#     #         prediction_text=f"Prediction: {result} | Confidence: {probability:.2f}%"
#     #     )

#     # except Exception as e:
#     #     return render_template("result.html", prediction_text=f"⚠ Error: {str(e)}")

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request, render_template
import pickle
import numpy as np
import os

# ==============================
# Config & Model Loading
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "lung.pickle")

app = Flask(__name__)
 
FEATURES = [
    "GENDER", "AGE", "SMOKING", "YELLOW_FINGERS", "ANXIETY",
    "PEER_PRESSURE", "CHRONIC_DISEASE", "FATIGUE", "ALLERGY",
    "WHEEZING", "ALCOHOL_CONSUMING", "COUGHING",
    "SHORTNESS_OF_BREATH", "SWALLOWING_DIFFICULTY", "CHEST_PAIN"
]

# Load model once at startup
model = None

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print(f"[INFO] Model loaded successfully from {MODEL_PATH}")
    if hasattr(model, "n_features_in_"):
        print(f"[INFO] Model expects {model.n_features_in_} features")
except Exception as e:
    print(f"[ERROR] Failed to load model: {e}")
# try:
#     with open(MODEL_PATH, "rb") as f:
#         model = pickle.load(f)
#     print("[INFO] Lung model loaded successfully.")
# except Exception as e:
#     print(f"[ERROR] Failed to load model: {e}")
#     model = None

# ==============================
# Flask App
# ==============================

# # Features expected by the model
# FEATURES = [
#     "GENDER", "AGE", "SMOKING", "YELLOW_FINGERS", "ANXIETY",
#     "PEER_PRESSURE", "CHRONIC_DISEASE", "FATIGUE", "ALLERGY",
#     "WHEEZING", "ALCOHOL_CONSUMING", "COUGHING",
#     "SHORTNESS_OF_BREATH", "SWALLOWING_DIFFICULTY", "CHEST_PAIN"
# ]

@app.route("/")
def home():
    return render_template("index.html",features=FEATURES)

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return "<h2 style='color:red;'>⚠ Model not loaded. Check server logs.</h2>", 500

    try:
        # Collect form data in the same order as FEATURES
        input_data = []
        for feature in FEATURES:
            value = request.form.get(feature, 0)
            try:
                input_data.append(float(value))
            except ValueError:
                input_data.append(0.0)

        arr = np.array([input_data], dtype=float)

        # Debugging: print what we are sending to the model
        print("[DEBUG] Features received:", request.form.to_dict())
        print("[DEBUG] Input array shape:", arr.shape)
        if hasattr(model, "n_features_in_"):
            print("[DEBUG] Model expects:", model.n_features_in_)

        # Prediction
        prediction = int(model.predict(arr)[0])
        proba = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(arr)[0].tolist()

        return render_template(
            "result.html",
            prediction=prediction,
            features=FEATURES,
            values=input_data,
            proba=proba
        )

    except ValueError as e:
        return f"<h2 style='color:red; text-align:center;'>⚠ Invalid input: {str(e)}</h2>", 400

    # except Exception as e:
    #     return f"<h2 style='color:red; text-align:center;'>⚠ Error during prediction: {str(e)}</h2>", 500

    # if not model:
    #     return "Model not loaded. Please check logs.", 500

    # try:
    #     # Collect form data dynamically
    #     input_data = []
    #     for feature in FEATURES:
    #         value = request.form.get(feature, 0)
    #         try:
    #             input_data.append(float(value))
    #         except ValueError:
    #             input_data.append(0.0)

    #     arr = np.array([input_data], dtype=float)

    #     # Make prediction
    #     prediction = int(model.predict(arr)[0])
    #     proba = None
    #     if hasattr(model, "predict_proba"):
    #         proba = model.predict_proba(arr)[0].tolist()

    #     return render_template(
    #         "result.html",
    #         prediction=prediction,
    #         features=FEATURES,
    #         values=input_data,
    #         proba=proba
    #     )
    
    # except Exception as e:
    #     return f"<h2 style='color:red; text-align:center;'>⚠ Error: {str(e)}</h2>", 500
    # except Exception as e:
    #     return render_template("error.html", message=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True)
