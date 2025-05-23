<img src="assets/images/fastapi-banner-1.png" width="800" alt="FastAPI Basics for Modern AI and MLOps">

# 🚀 Tutorial: FastAPI Basics for Modern AI and MLOps

## 👀 Description

🎓 **What is this?** The "FastAPI Basics for Modern AI and MLOps" tutorial is your comprehensive journey into building web services with FastAPI, specially designed for AI Developers and ML Engineers. This tutorial will show you how easily and quickly you can use FastAPI to build robust, high-performance APIs to serve your ML models and integrate them into larger MLOps workflows.

👩‍💻 **Who is this for?**

If you're an AI Developer, ML Engineer, or anyone looking to deploy machine learning models as scalable web services, this tutorial is for you. It covers the essentials to get you started quickly and effectively.

🎯 **What will you learn?**

- Why FastAPI is an excellent choice for serving ML models in AI/MLOps.
- Core FastAPI concepts: path operations (GET, POST), request/response handling.
- Leveraging Pydantic for clear data contracts and robust model validation.
- Integrating trained ML models (using a simplified example) into your FastAPI service.
- Locally testing API endpoints, including interactive documentation.
- Containerizing your FastAPI application with Docker for consistent deployment.

🔍 **How is it structured?** Clear, step-by-step instructions with comprehensive code examples in Markdown format. You'll build up from a simple "Hello World" to a containerized ML model serving application.

⏱️ **How much time will it take?** Approximately **45-60 minutes** – giving you a solid foundation to build and deploy your own ML-powered APIs.

---

## 📖 Table of Contents

- [🚀 Tutorial: FastAPI Basics for Modern AI and MLOps](#-tutorial-fastapi-basics-for-modern-ai-and-mlops)
  - [👀 Description](#-description)
  - [📖 Table of Contents](#-table-of-contents)
  - [⚙️ 1 - Prerequisites & Installation](#️-1---prerequisites--installation)
- [🤔 2 - Why FastAPI for AI & MLOps?](#-2---why-fastapi-for-ai--mlops)
- [⭐ 3 - Core FastAPI: GET & POST Requests](#-3---core-fastapi-get--post-requests)
  - [Step 1: Create a Simple API with a GET Request](#step-1-create-a-simple-api-with-a-get-request)
  - [Step 2: Run the FastAPI Service](#step-2-run-the-fastapi-service)
  - [Step 3: Test the Service](#step-3-test-the-service)
  - [Step 4: Enhance `main.py` with a POST Request (Introducing Pydantic)](#step-4-enhance-mainpy-with-a-post-request-introducing-pydantic)
  - [Step 5: Test the POST Request](#step-5-test-the-post-request)
  - [Step 6: Automatic API Documentation](#step-6-automatic-api-documentation)
- [🛠️ 4 - Integrating an ML Model with FastAPI](#️-4---integrating-an-ml-model-with-fastapi)
  - [Step 1: The Model Logic - `GiftPredictor` Class (Simplified Example)](#step-1-the-model-logic---giftpredictor-class-simplified-example)
  - [Step 2: Defining Input/Output Data Structures with Pydantic](#step-2-defining-inputoutput-data-structures-with-pydantic)
  - [Step 3: Creating the API Endpoints in `app/gift_predictor.py`](#step-3-creating-the-api-endpoints-in-appgift_predictorpy)
  - [Step 4: Running the Full Application](#step-4-running-the-full-application)
  - [Step 5: Testing the Prediction Endpoint](#step-5-testing-the-prediction-endpoint)
- [🐳 5 - Running Your FastAPI Web Service in a Docker Container](#-5---running-your-fastapi-web-service-in-a-docker-container)
  - [Step 1: Prepare the Dockerfile](#step-1-prepare-the-dockerfile)
  - [Step 2: Build the Docker Image](#step-2-build-the-docker-image)
  - [Step 3: Run the Docker Container](#step-3-run-the-docker-container)
- [🧪 6 - Pydantic Power-Up: Advanced Validation](#-6---pydantic-power-up-advanced-validation)
  - [Python Type Annotations: A Quick Refresher](#python-type-annotations-a-quick-refresher)
  - [Pydantic Basics Recap](#pydantic-basics-recap)
  - [Advanced Validation with `Field`](#advanced-validation-with-field)
  - [Custom Logic with Field Validators (`@field_validator`)](#custom-logic-with-field-validators-field_validator)
  - [Reusable Validations with `typing.Annotated`](#reusable-validations-with-typingannotated)
  - [Testing the Enhanced Validation](#testing-the-enhanced-validation)
- [🔗 7 - Additional Resources](#-7---additional-resources)
- [🎉 8 - Next Steps & Conclusion](#-8---next-steps--conclusion)

---

## ⚙️ 1 - Prerequisites & Installation

Before we dive into FastAPI, your development environment needs to be set up with Python, necessary tools, and the project code.

**Prerequisites:**

- Python 3.9+ installed. (FastAPI supports 3.8+, but newer versions are recommended).
- `uv` (Python package installer) installed. `uv` is a fast, modern package manager.
  - If you don't have `uv`, install it: `pip install uv` (or `pipx install uv`). Refer to the [official `uv` documentation](https://github.com/astral-sh/uv) for more installation options.
- Git installed (for cloning the project repository).
- Basic understanding of Python and the command line/terminal.
- Basic understanding of web concepts (HTTP methods like GET/POST, what an API is).
- Docker installed (required for the Docker containerization section later in this tutorial).

**Setup Instructions:**

For detailed, step-by-step instructions on how to:

1. Clone the project repository,
2. Create a Python virtual environment using `uv`, and
3. Install all required dependencies,

please refer to the **[👩‍💻 Quick Start: Installation & Setup section in the project's README.md file](README.md#️-quick-start-installation--setup)**.

Once you have successfully completed the setup steps outlined in the `README.md`, your environment will be ready, and you can proceed with this tutorial to learn about FastAPI.

---

## 🤔 2 - Why FastAPI for AI & MLOps?

FastAPI is a prime choice for serving ML models in MLOps due to its:

- 🚀 **High Performance:** Built on Starlette and Pydantic, FastAPI offers exceptional speed with ASGI servers like Uvicorn. This ensures **low-latency inference crucial for real-time ML applications.**
- 🛡️ **Robust Data Validation:** Leverages Pydantic and Python type hints for clear, validated data schemas. This means **reliable data contracts** for model inputs/outputs and **early error detection**, vital for stable MLOps integrations.
- ⏱️ **Rapid Development:** Its intuitive syntax, excellent editor support, and minimal boilerplate accelerate the development and iteration of ML APIs.
- 📚 **Automatic Interactive Docs:** Instantly generates OpenAPI (Swagger UI) and ReDoc documentation, simplifying API testing, integration, and team collaboration.
- 🧩 **Asynchronous Support:** Native `async`/`await` capabilities are ideal for handling I/O-bound tasks often found in ML pre/post-processing.
- 🏢 **Microservice & Standards-Friendly:** Its lightweight design is perfect for building ML models as microservices, and it adheres to open standards like OpenAPI and JSON Schema.

In short, FastAPI empowers you to efficiently build production-ready, maintainable, and performant APIs for your AI/ML models.

---

## ⭐ 3 - Core FastAPI: GET & POST Requests

Let's start with the fundamentals by creating and progressively enhancing a single `main.py` file.

### Step 1: Create a Simple API with a GET Request

Create a file named `main.py` with the following content:

```python
# main.py
from fastapi import FastAPI

app = FastAPI(title="My First FastAPI App")

@app.get("/") # Path operation decorator for GET requests to the root path
async def read_root(): # Path operation function
    return {"message": "Hello from FastAPI!"}
```

### Step 2: Run the FastAPI Service

Open your terminal, navigate to the directory containing `main.py`, and run:

```bash
uvicorn main:app --reload
```

- `main`: The `main.py` Python file.
- `app`: The `FastAPI` instance created inside `main.py`.
- `--reload`: For auto-restarting the server on code changes during development.

### Step 3: Test the Service

Open your browser and go to `http://127.0.0.1:8000/`. You should see:

```json
{"message":"Hello from FastAPI!"}
```

### Step 4: Enhance `main.py` with a POST Request (Introducing Pydantic)

Now, **update your existing `main.py` file** to handle POST requests. FastAPI uses **Pydantic** models to define the structure and validate incoming data.

```python
# main.py (Updated)
from fastapi import FastAPI
from pydantic import BaseModel # Import BaseModel from Pydantic

app = FastAPI(title="FastAPI with GET & POST")

# 1. Define a Pydantic model for the request body
class Item(BaseModel):
    name: str
    description: str | None = None  # Modern way to denote an optional string
    price: float
    is_offer: bool | None = None   # Modern way to denote an optional boolean

@app.get("/")
async def read_root():
    return {"message": "Send data to /items/ via POST or GET / to say hello!"}

# 2. Create a POST endpoint
@app.post("/items/") # Handles POST requests to /items/
async def create_item(item: Item): # FastAPI validates incoming data against the Item model
    # 'item' is now an instance of Item, with validated data
    return {"item_name": item.name, "item_price": item.price, "description": item.description}
```

- **Pydantic `BaseModel`:** `Item` inherits from `pydantic.BaseModel`. Its attributes with type hints define the expected JSON structure for the POST request body.
- **Type Hinting `item: Item`:** This tells FastAPI to expect a request body matching the `Item` model. FastAPI will parse, validate, and convert the JSON into an `Item` object. If validation fails, it automatically returns an HTTP 422 error.

### Step 5: Test the POST Request

If your `uvicorn` server is still running with `--reload`, it should have automatically picked up the changes to `main.py`. If not, restart it:

```bash
uvicorn main:app --reload
```

Use `curl` (or Postman/Insomnia) to send a POST request:

```bash
curl -X POST "http://127.0.0.1:8000/items/" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Super Gadget",
           "price": 49.99,
           "description": "An amazing new gadget for all your needs"
         }'
```

**Expected Response:**

```json
{"item_name":"Super Gadget","item_price":49.99,"description":"An amazing new gadget for all your needs"}
```

💡 **Try sending invalid data** (e.g., `price` as a string, or omitting `name`) to see FastAPI's automatic 422 validation error response!

### Step 6: Automatic API Documentation

FastAPI's interactive API documentation is automatically updated. With `main.py` running:

- **Swagger UI:** Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** Open [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Explore your `/` (GET) and `/items/` (POST) endpoints. Notice how the schema for the `/items/` request body is derived from your `Item` Pydantic model. You can "Try it out" directly from Swagger UI!

---

## 🛠️ 4 - Integrating an ML Model with FastAPI

Now, let's build the `gift_predictor` application which serves a simplified "ML model." This involves a separate Python file for the application logic (`app/gift_predictor.py`) and another for the model handling (`app/model.py`).

### Step 1: The Model Logic - `GiftPredictor` Class (Simplified Example)

Our "ML model" is represented by a JSON file (`models/model.json`) acting as a lookup table. To interact with this data cleanly, we'll encapsulate the logic in a `GiftPredictor` class within `app/model.py`.

**Create `app/model.py` with the following content:**

```python
# app/model.py
import json
from typing import Dict, Any, Optional, List # Use List for Python <3.9 for list[str]
from pathlib import Path
import random # For confidence score in this example

class GiftPredictor:
    def __init__(self, model_path: str = "models/model.json"):
        # ...

    def _load_model(self) -> None:
        """Load the model data from JSON file."""
        # ...

    def is_loaded(self) -> bool:
        """Check if the model is loaded."""
        # ...

    def get_valid_interests(self) -> List[str]:
        """Get list of valid interests."""
        # ...

    def predict(self, age: int, interest: str) -> tuple[str, str, float]:
        """
        Make a prediction based on age and interest.
        
        Args:
            age: User's age
            interest: User's interest
            
        Returns:
            tuple: (predicted_gift, suggested_category, confidence_score)
        """
        # ...
```

> 👉 **Real-World Model Persistence:**
> This JSON file and `GiftPredictor` class are simplified. In practice, you would:
>
> 1. **Train your model** (scikit-learn, TensorFlow, PyTorch, etc.).
> 2. **Save (serialize) it** using `joblib`, native framework methods, or ONNX.
> 3. Your `_load_model` method in `GiftPredictor` would then use, e.g., `joblib.load()` to load the actual model object. The `predict` method would call `your_loaded_model.predict(...)`.

### Step 2: Defining Input/Output Data Structures with Pydantic

Now, create your FastAPI application file, `app/gift_predictor.py`. This will import and use the `GiftPredictor`.

**Create `app/gift_predictor.py` and define Pydantic models:**

```python
# app/gift_predictor.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional # For Python < 3.10 compatibility for `| None`

# Import our model handler
from app.model import GiftPredictor # Assuming model.py is in the same 'app' directory

app = FastAPI(title="Birthday Gift Predictor API", version="1.0.0")

# Initialize the predictor ONCE at application startup
predictor = GiftPredictor() # Uses default model_path from GiftPredictor class

class PredictionInput(BaseModel):
    age: int = Field(..., gt=0, le=120, description="User's age (1-120)") # ... means required
    interest: str = Field(..., min_length=2, max_length=30, description="User's primary interest")

class PredictionOutput(BaseModel):
    predicted_gift: str
    suggested_category: str
    confidence_score: Optional[float] = Field(None, ge=0, le=1, description="Model's confidence (0.0-1.0)")
```

### Step 3: Creating the API Endpoints in `app/gift_predictor.py`

**Continue editing `app/gift_predictor.py` to add the endpoints:**

```python
# app/gift_predictor.py (continued from above)

@app.get("/", response_class=HTMLResponse, include_in_schema=False, tags=["General"])
async def home():
    # This HTML response is simplified. In a real app, you might use templates.
    # The content for the HTML page is intentionally kept brief here.
    # Users should refer to the /docs for API interaction.
    if not predictor.is_loaded():
        return "<h1>⚠️ Model Error</h1><p>The prediction model failed to load. Please check server logs.</p>"
    
    available_interests = predictor.get_valid_interests()
    interests_list_html = "".join(f"<li>{interest.capitalize()}</li>" for interest in available_interests)
    
    return f"""
    <html>
        <head><title>🎁 Gift Predictor API</title></head>
        <body>
            <h1>Welcome to the Birthday Gift Predictor API!</h1>
            <p>This API helps you find gift ideas. Use the <a href="/docs">interactive API documentation</a> to make predictions.</p>
            <h2>Available Interests:</h2>
            <ul>{interests_list_html if available_interests else "<li>No interests loaded</li>"}</ul>
        </body>
    </html>
    """

@app.post("/predict/", response_model=PredictionOutput, tags=["Predictions"])
async def predict_birthday_gift_endpoint(payload: PredictionInput): # Renamed for clarity
    if not predictor.is_loaded():
        # This check ensures the model was loaded correctly at startup.
        raise HTTPException(status_code=503, detail="Model not loaded. Service unavailable.")

    try:
        # Delegate prediction logic to the GiftPredictor instance
        predicted_gift, suggested_category, confidence = predictor.predict(
            age=payload.age,
            interest=payload.interest # Pydantic has already validated the payload
        )
        
        return PredictionOutput(
            predicted_gift=predicted_gift,
            suggested_category=suggested_category,
            confidence_score=confidence
        )
    except ValueError as e: # Catch specific errors from predictor.predict()
        raise HTTPException(status_code=400, detail=f"Invalid input for prediction: {str(e)}")
    except RuntimeError as e: # Catch model loading issues if predict is called when not loaded
        raise HTTPException(status_code=503, detail=str(e))
```

This modular structure (FastAPI app logic in `gift_predictor.py`, model handling in `model.py`) offers:

1. **Separation of Concerns**: API routing vs. model logic.
2. **Testability**: Easier to test `GiftPredictor` independently.
3. **Maintainability**: Changes to model internals are isolated.

### Step 4: Running the Full Application

Ensure your project structure is:

```plaintext
fastapi-for-modern-ai-and-mlops/  (or your project root)
├── app/
│   ├── __init__.py          (optional, but good practice)
│   ├── model.py             (GiftPredictor class)
│   └── gift_predictor.py    (FastAPI app instance and endpoints)
├── models/
│   └── model.json
└── requirements.txt
```

Then, from your project root (e.g., `fastapi-for-modern-ai-and-mlops/`), run:

```bash
uvicorn app.gift_predictor:app --reload
```

### Step 5: Testing the Prediction Endpoint

**Using `curl`:**

```bash
curl -X POST "http://127.0.0.1:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"age": 28, "interest": "Programming"}'
```

**Expected Response (example):**

```json
{
  "predicted_gift": "A new tech gadget related to programming.",
  "suggested_category": "programming",
  "confidence_score": 0.85 
}
```

Or test via Swagger UI at `http://127.0.0.1:8000/docs`. Try invalid inputs (e.g., age `0`, interest `"skydiving"`) to see validation from `PredictionInput` and potentially `GiftPredictor` in action.

---

## 🐳 5 - Running Your FastAPI Web Service in a Docker Container

Containerizing with Docker ensures consistency and simplifies deployment.

### Step 1: Prepare the Dockerfile

Ensure your `Dockerfile` is at the project root. For the content of the `Dockerfile` (using multi-stage builds and `uv`), please refer to the **[project's Dockerfile](Dockerfile)**.
*(Tutorial links to the Dockerfile in the repository)*

### Step 2: Build the Docker Image

From your project root directory (where `Dockerfile` is located):

```bash
docker build -t fastapi-gift-predictor .
```

### Step 3: Run the Docker Container

```bash
# Remove old container if it exists to avoid name conflicts
docker rm -f mygiftapp-container

# Run the new container
docker run --name mygiftapp-container -p 8000:8000 -d fastapi-gift-predictor
```

Your application is now running inside Docker, accessible at `http://127.0.0.1:8000/`. Test it as before!

---

## 🧪 6 - Pydantic Power-Up: Advanced Validation

Pydantic allows for precise data validation. Let's enhance `app/gift_predictor.py`'s `PredictionInput` using advanced Pydantic features.

### Python Type Annotations: A Quick Refresher

Type hints declare expected data types, which Pydantic uses for validation.

### Pydantic Basics Recap

We've used `BaseModel` and `Field` for basic structure and constraints.

### Advanced Validation with `Field`

`Field` offers many parameters (e.g., `pattern` for regex, `min_items` for lists).

```python
# Example: A Pydantic model for more complex ML features
from pydantic import BaseModel, Field
from typing import List
class MLFeaturesInput(BaseModel):
    request_id: str = Field(..., pattern=r"^[a-zA-Z0-9_-]{10,30}$")
    numerical_features: List[float] = Field(..., min_items=5, max_items=5)
    categorical_feature: str = Field(..., example="type_A")
```

### Custom Logic with Field Validators (`@field_validator`)

For custom rules, use `@field_validator`. This runs *after* `Field` constraints and type conversions.

**Update `app/gift_predictor.py`'s `PredictionInput` model:**

```python
# app/gift_predictor.py (update PredictionInput)
# ... (imports: BaseModel, Field, etc.)
from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo # For Pydantic v2

class PredictionInput(BaseModel): # (This replaces the previous PredictionInput)
    age: int = Field(..., gt=0, le=120, description="User's age (1-120)")
    interest: str = Field(..., min_length=2, max_length=30, description="User's primary interest")

    # Custom validator for 'interest'
    @field_validator('interest')
    @classmethod
    def interest_must_be_alphanumeric_and_known(cls, v: str, info: ValidationInfo) -> str:
        # 'v' is the value of interest AFTER Field constraints (min/max_length)
        # and type conversion (already a str).
        
        # 1. Alphanumeric check (allowing spaces)
        if not v.replace(' ', '').isalnum():
            raise ValueError(f"Interest '{v}' must be alphanumeric (spaces allowed).")
        
        # 2. Check against valid interests from our GiftPredictor
        #    This demonstrates accessing other parts of your app logic if needed,
        #    though for this specific case, `Annotated` (next section) is cleaner.
        normalized_v = v.strip().lower()
        if not predictor.is_loaded() or normalized_v not in predictor.get_valid_interests():
            valid_options = predictor.get_valid_interests() if predictor.is_loaded() else ["unavailable - model not loaded"]
            raise ValueError(
                f"Interest '{v}' is not a recognized option. "
                f"Valid options include: {', '.join(valid_options)}."
            )
        return normalized_v # Return the normalized value
```

This validator checks if `interest` is alphanumeric AND if it's recognized by our `GiftPredictor`.

### Reusable Validations with `typing.Annotated`

For cleaner, reusable validation logic, especially when checking against dynamic lists (like `predictor.get_valid_interests()`), `typing.Annotated` with Pydantic's functional validators is powerful.

**Let's refine `PredictionInput` in `app/gift_predictor.py` using this approach:**

```python
# app/gift_predictor.py (further update PredictionInput)
# ... (imports: BaseModel, Field, Annotated, AfterValidator, etc.)
from typing import Annotated # Ensure this is imported
from pydantic.functional_validators import AfterValidator

# This function will be used with Annotated
def check_interest_against_model_list(value: str) -> str:
    normalized_value = value.strip().lower() # Normalize first
    if not predictor.is_loaded():
        # This ideally shouldn't happen if the app starts correctly
        raise ValueError("Cannot validate interest: Model not loaded.")
    
    valid_model_interests = predictor.get_valid_interests()
    if normalized_value not in valid_model_interests:
        raise ValueError(
            f"Invalid interest: '{value}'. Must be one of: {', '.join(valid_model_interests)}"
        )
    return normalized_value # Return normalized value

# Define an Annotated type for interest
ValidatedInterestType = Annotated[
    str, # Base type
    Field(min_length=2, max_length=30, description="User's primary interest"), # Field constraints
    AfterValidator(check_interest_against_model_list) # Our custom function runs after Field constraints
]

class PredictionInput(BaseModel): # (This replaces the previous PredictionInput again)
    age: int = Field(..., gt=0, le=120, description="User's age (1-120)")
    interest: ValidatedInterestType # Use the annotated type

    # You can still have other field_validators if needed for different logic
    # For example, an alphanumeric check IF it's distinct from what check_interest_against_model_list does.
    # If check_interest_against_model_list implies alphanumeric by its list, then separate one isn't needed.
    @field_validator('interest') # This example assumes you might still want a general format check
    @classmethod
    def interest_format_check(cls, v: str) -> str: # Runs BEFORE AfterValidator in Annotated
        if not v.replace(' ', '').isalnum(): # Simple format check
             raise ValueError("Interest must contain only letters, numbers, and spaces.")
        return v # Pass through for further validation by Annotated
```

In this refined version:

- `ValidatedInterestType` bundles `Field` constraints and our custom `check_interest_against_model_list` function using `AfterValidator`.
- The `@field_validator('interest') interest_format_check` runs first for basic format validation. Then, `check_interest_against_model_list` (via `Annotated`) runs on the already (potentially) modified value.
- This makes `ValidatedInterestType` reusable if other Pydantic models need the same interest validation.

### Testing the Enhanced Validation

Ensure `app/gift_predictor.py` has the latest `PredictionInput` with `ValidatedInterestType`. Restart your `uvicorn` server:

```bash
uvicorn app.gift_predictor:app --reload
```

Test with invalid interests (e.g., `"@#$"`, `"skydiving"`) and invalid ages. FastAPI will return detailed 422 errors based on your Pydantic validators.

---

## 🔗 7 - Additional Resources

- **FastAPI Official Documentation:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)
- **Pydantic Official Documentation:** [docs.pydantic.dev](https://docs.pydantic.dev/latest/)
- **Uvicorn Official Documentation:** [www.uvicorn.org](https://www.uvicorn.org/)
- **RealPython - Python Type Checking:** [realpython.com/python-type-checking/](https://realpython.com/python-type-checking/)

---

## 🎉 8 - Next Steps & Conclusion

Congratulations! You've explored FastAPI basics for AI/MLOps, covering everything from API creation and ML model integration to Dockerization and advanced data validation with Pydantic.

**Where to go from here?**

- 📦 **Real Model Integration:** Adapt `app/model.py` to load and serve a real serialized ML model.
- 🧪 **Testing:** Implement tests using `pytest` and FastAPI's `TestClient`.
- 🔐 **Security:** Add authentication/authorization (e.g., OAuth2 JWT).
- ⚙️ **Configuration:** Manage settings with Pydantic's `BaseSettings`.
- 🚀 **Deployment & MLOps:** Explore Kubernetes, serverless, CI/CD pipelines, MLflow integration, logging, and monitoring.
- 🧩 **Advanced FastAPI:** Dive into WebSockets, `Depends` for dependency injection, middleware.

FastAPI is a powerful tool for building efficient, production-ready APIs in the MLOps landscape. Happy coding!

[⬆️ Back to Table of Contents](#-table-of-contents)
