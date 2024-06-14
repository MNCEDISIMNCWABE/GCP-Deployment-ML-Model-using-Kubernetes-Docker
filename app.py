from flask import Flask, request, jsonify
from flasgger import Swagger
import joblib
import pandas as pd

app = Flask(__name__)
swagger = Swagger(app)

# Load the trained model
model_path = 'loan_pred_model.pkl'
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict loan approval based on user features
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            ApplicantIncome:
              type: integer
              description: Applicant's income
            CoapplicantIncome:
              type: float
              description: Coapplicant's income
            LoanAmount:
              type: float
              description: Loan amount
            Loan_Amount_Term:
              type: float
              description: Loan amount term
            Gender_Female:
              type: integer
              description: Gender (Female = 1, Male = 0)
            Gender_Male:
              type: integer
              description: Gender (Male = 1, Female = 0)
            Married_No:
              type: integer
              description: Marital Status (No = 1, Yes = 0)
            Married_Yes:
              type: integer
              description: Marital Status (Yes = 1, No = 0)
            Dependents_0.0:
              type: integer
              description: Number of Dependents (0)
            Dependents_1.0:
              type: integer
              description: Number of Dependents (1)
            Dependents_2.0:
              type: integer
              description: Number of Dependents (2)
            Dependents_3.0:
              type: integer
              description: Number of Dependents (3+)
            Self_Employed_No:
              type: integer
              description: Self Employed (No = 1, Yes = 0)
            Self_Employed_Yes:
              type: integer
              description: Self Employed (Yes = 1, No = 0)
            Credit_History_0.0:
              type: integer
              description: Credit History (0.0)
            Credit_History_1.0:
              type: integer
              description: Credit History (1.0)
            Property_Area_Rural:
              type: integer
              description: Property Area (Rural = 1, Urban = 0, Semiurban = 0)
            Property_Area_Semiurban:
              type: integer
              description: Property Area (Semiurban = 1, Urban = 0, Rural = 0)
            Property_Area_Urban:
              type: integer
              description: Property Area (Urban = 1, Rural = 0, Semiurban = 0)
            Education_Graduate:
              type: integer
              description: Education Level (Graduate = 1, Not Graduate = 0)
            Education_Not_Graduate:
              type: integer
              description: Education Level (Not Graduate = 1, Graduate = 0)
          example:
            ApplicantIncome: 5000
            CoapplicantIncome: 2000.0
            LoanAmount: 150.0
            Loan_Amount_Term: 360.0
            Gender_Female: 0
            Gender_Male: 1
            Married_No: 0
            Married_Yes: 1
            Dependents_0.0: 1
            Dependents_1.0: 0
            Dependents_2.0: 0
            Dependents_3.0: 0
            Self_Employed_No: 1
            Self_Employed_Yes: 0
            Credit_History_0.0: 0
            Credit_History_1.0: 1
            Property_Area_Rural: 0
            Property_Area_Semiurban: 0
            Property_Area_Urban: 1
            Education_Graduate: 1
            Education_Not Graduate: 0
    responses:
      200:
        description: Prediction result
        schema:
          type: object
          properties:
            prediction:
              type: integer
              description: Prediction result (1 = Approved, 0 = Not Approved)
              example: 1
            probability:
              type: float
              description: Probability of being approved
              example: 0.85
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: string
              description: Error message
              example: "Error message"
    """
    try:
        data = request.get_json(force=True)
        features = pd.DataFrame([{
            'ApplicantIncome': data['ApplicantIncome'],
            'CoapplicantIncome': data['CoapplicantIncome'],
            'LoanAmount': data['LoanAmount'],
            'Loan_Amount_Term': data['Loan_Amount_Term'],
            'Gender_Female': data['Gender_Female'],
            'Gender_Male': data['Gender_Male'],
            'Married_No': data['Married_No'],
            'Married_Yes': data['Married_Yes'],
            'Dependents_0.0': data['Dependents_0.0'],
            'Dependents_1.0': data['Dependents_1.0'],
            'Dependents_2.0': data['Dependents_2.0'],
            'Dependents_3.0': data['Dependents_3.0'],
            'Self_Employed_No': data['Self_Employed_No'],
            'Self_Employed_Yes': data['Self_Employed_Yes'],
            'Credit_History_0.0': data['Credit_History_0.0'],
            'Credit_History_1.0': data['Credit_History_1.0'],
            'Property_Area_Rural': data['Property_Area_Rural'],
            'Property_Area_Semiurban': data['Property_Area_Semiurban'],
            'Property_Area_Urban': data['Property_Area_Urban'],
            'Education_Graduate': data['Education_Graduate'],
            'Education_Not Graduate': data['Education_Not Graduate']
        }])
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)[:, 1]  # Probability of a loan being 1=Approved
        prediction_label = "Approved" if int(prediction[0]) == 1 else "Rejected"
        return jsonify({'prediction': prediction_label, 'probability of loan approval': float(prediction_proba[0])})
    except KeyError as e:
        return jsonify({'error': f"Missing parameter: {str(e)}"}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
