from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from app.model import GiftPredictor

app = FastAPI(title="Birthday Gift Predictor API", version="1.0.0")

# Initialize the predictor
predictor = GiftPredictor()


class PredictionInput(BaseModel):
    age: int = Field(..., gt=0, le=120, description="User's age (1-120)")
    interest: str = Field(
        ..., min_length=2, max_length=30, description="User's primary interest"
    )


class PredictionOutput(BaseModel):
    predicted_gift: str
    suggested_category: str
    confidence_score: float | None = Field(
        None, ge=0, le=1, description="Model's confidence (0.0-1.0)"
    )


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home():
    if not predictor.is_loaded():
        raise HTTPException(
            status_code=503, detail="Model not loaded. Service unavailable."
        )

    interests = predictor.get_valid_interests()
    interests_list = "\n".join([f"<li>{interest}</li>" for interest in interests])

    return f"""
    <html>
        <head>
            <title>Gift Predictor API</title>
            <style>
                body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1 {{ color: #2c3e50; }}
                h2 {{ color: #34495e; }}
                ul {{ list-style-type: none; padding: 0; }}
                li {{ 
                    display: inline-block;
                    margin: 5px;
                    padding: 8px 15px;
                    background-color: #f0f0f0;
                    border-radius: 15px;
                    font-size: 14px;
                }}
                .docs-link {{ 
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #3498db;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                }}
            </style>
        </head>
        <body>
            <h1>🎁 Birthday Gift Predictor API</h1>
            <h2>Wanna cool gift for the next birthday?</h2>
            <p>Just let me know your <b>Age</b> and one of the <b>Interests</b> below:</p>
            
            <ul>
                {interests_list}
            </ul>
            
            <a href="/docs" class="docs-link">Try it out in the API Documentation →</a>
        </body>
    </html>
    """


@app.post("/predict/", response_model=PredictionOutput, tags=["Predictions"])
async def predict_birthday_gift(payload: PredictionInput):
    if not predictor.is_loaded():
        raise HTTPException(
            status_code=503, detail="Model not loaded. Service unavailable."
        )

    try:
        predicted_gift, suggested_category, confidence = predictor.predict(
            age=payload.age, interest=payload.interest
        )

        return PredictionOutput(
            predicted_gift=predicted_gift,
            suggested_category=suggested_category,
            confidence_score=confidence,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
