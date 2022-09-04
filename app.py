

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from forecasting import Forecasting
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("RF_tuned.sav","rb")
RF_model=pickle.load(pickle_in)


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Forecasting value with the confidence
@app.post('/predict')
def predict_Forecasting(data:Forecasting):
    data = data.dict()
    MortgageRate=data['MortgageRate']
    Inflation=data['Inflation']
    TreasuryYield=data['TreasuryYield']
    UnemploymentRate=data['UnemploymentRate']
    GDP=data['GDP']
    ConsumerConfidenceIndex=data['ConsumerConfidenceIndex']
    DisposableIncome=data['DisposableIncome']
   

    prediction = RF_model.predict([[MortgageRate,Inflation,TreasuryYield,UnemploymentRate,GDP,ConsumerConfidenceIndex,DisposableIncome]])
   
    return {
        #'prediction': prediction
        "The forecasting value is {}".format(prediction)
    }

# 4. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload