from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import joblib
import numpy as np
import pandas as pd
import os



# ===============================
# FASTAPI APP
# ===============================


app = FastAPI(
    title="AI Predictive Maintenance API"
)



# ===============================
# CORS (React Connection)
# ===============================


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)



# ===============================
# PATH SETTINGS
# ===============================


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)



# ===============================
# LOAD MODEL FILES
# ===============================


model = joblib.load(

    os.path.join(
        BASE_DIR,
        "model.pkl"
    )

)


scaler = joblib.load(

    os.path.join(
        BASE_DIR,
        "scaler.pkl"
    )

)



# ===============================
# LOAD REAL AI4I DATASET
# ===============================


dataset_path = os.path.join(

    BASE_DIR,

    "..",

    "ml",

    "dataset",

    "ai4i2020.csv"

)



dataset = pd.read_csv(

    dataset_path

)



# ===============================
# INPUT MODEL
# ===============================


class MachineData(BaseModel):

    air_temperature: float

    process_temperature: float

    rotational_speed: float

    torque: float

    tool_wear: int





# ===============================
# HOME API
# ===============================


@app.get("/")


def home():


    return {

        "message":

        "Industrial AI Predictive Maintenance API Running"

    }





# ===============================
# GET REAL MACHINE DATA
# ===============================


@app.get("/machine")


def get_machine():


    machine = dataset.sample(1).iloc[0]



    return {


        "machine_id":

        int(
            machine["UDI"]
        ),


        "machine_type":

        str(
            machine["Type"]
        ),


        "air_temperature":

        float(
            machine["Air temperature [K]"]
        ),


        "process_temperature":

        float(
            machine["Process temperature [K]"]
        ),


        "rotational_speed":

        int(
            machine["Rotational speed [rpm]"]
        ),


        "torque":

        float(
            machine["Torque [Nm]"]
        ),


        "tool_wear":

        int(
            machine["Tool wear [min]"]
        ),


        "actual_failure":

        int(
            machine["Machine failure"]
        )


    }





# ===============================
# ML PREDICTION API
# ===============================


@app.post("/predict")


def predict(data: MachineData):


    values = np.array(

        [

            [

                data.air_temperature,

                data.process_temperature,

                data.rotational_speed,

                data.torque,

                data.tool_wear

            ]

        ]

    )



    scaled_values = scaler.transform(

        values

    )



    prediction = model.predict(

        scaled_values

    )[0]



    probability = (

        model.predict_proba(

            scaled_values

        )[0][1]

        *

        100

    )




    if prediction == 1:


        status = "Failure Risk"


        recommendation = (

            "High machine stress detected. "
            "Schedule preventive maintenance."

        )


    else:


        status = "Healthy"


        recommendation = (

            "Machine condition is normal. "
            "Continue monitoring."

        )




    return {


        "prediction":

        status,


        "probability":

        round(
            probability,
            2
        ),


        "recommendation":

        recommendation

    }