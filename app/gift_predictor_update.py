from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
from pydantic import (
    BaseModel,
    Field, 
    field_validator,     
    ValidationInfo,
)
from pydantic.functional_validators import AfterValidator
import random
from typing import Annotated

app = FastAPI()

# Load the model from the JSON file
with open('models/model.json', 'r') as json_file:
    model = json.load(json_file)

def validate_interest(value: str) -> str:
    valid_interests = [
        "painting", 
        "reading",
        "gardening",
        "gaming",
        "yoga",
        "fashion",
        "data",
        "ml",
        "programming",
        "it",
        "no"
    ]
    if value not in valid_interests:
        raise ValueError(f"Interest must be one of {valid_interests}")
    return value

InterestType = Annotated[
        str, 
        Field(description="Interest should be one of predefined categories"),
        AfterValidator(validate_interest)        
    ]

class PredictionInput(BaseModel):
    """
    Represents the input data for predicting a birthday gift.
    """
    age: int = Field(gt=0, le=100)
    interest: InterestType

    @field_validator('interest')
    @classmethod
    def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
        if not v.replace(' ', '').isalnum():
            raise ValueError(f'Field: {info.field_name} must be alphanumeric')
        return v


@app.get("/", response_class=HTMLResponse)
def get_interests() -> str:
    """
    Returns the available interests for selecting a birthday gift.
    """
    interests = list(model["interests"].keys())
    interests_str = '</li>\n  <li>'.join(interests)

    return f"""
        <html>
            <head>
                <title>Birthday Gift Predictor</title>
            </head>
            <body>
                <h1>Birthday Gift Predictor</h1>
                <h2>Wanna cool gift for the next birthday?</h2>
                <p>Just let me know your <b>Age</b> and one of the <b>Interests</b>.</p>
                
                <p>Available interests are:</p>
                <ul>
                    <li>{interests_str}</li>
                </ul>
            </body>
        </html>
    """


@app.post("/predict/")
def predict_birthday_gift(input_data: PredictionInput) -> str:
    """
    Predicts a birthday gift based on the input data.
    """
    age = input_data.age
    interest = input_data.interest.lower()

    primary_gift = model["gifts_by_age"].get(str(age), "Special Surprise Gift")
    specif_gift = model['interests'].get(interest, '')
    prob = random.randint(50, 100)
    gift = f"{primary_gift} and {specif_gift}" if specif_gift else primary_gift

    return f"predicted_gift: {gift} with probability {prob}%"

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)