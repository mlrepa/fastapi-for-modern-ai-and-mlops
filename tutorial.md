<img src="assets/images/fastapi-banner-1.png" width="800" alt="FastAPI Basics for Modern AI and MLOps">

# 🚀 Tutorial: FastAPI Basics for Modern AI and MLOps

## 👀 Description

🎓 **What is this?** The "FastAPI Basics for Modern AI and MLOps" tutorial is your comprehensive journey into building web services with FastAPI, specially designed for AI Developers and ML Engineers. This tutorial will show you how easily and quickly you can use FastAPI to build robust, high-performance APIs to serve your ML models and integrate them into larger MLOps workflows.

👩‍💻 **Who is this for?** If you're a AI Developer, ML Engineer, or anyone looking to deploy machine learning models as scalable web services, this tutorial is for you. It covers the essentials to get you started quickly and effectively.

🎯 **What will you learn?**

- Why FastAPI is an excellent choice for serving ML models in AI/MLOps (performance, data validation, ease of use).
- Core FastAPI concepts: path operations (GET, POST), request/response handling.
- Leveraging Pydantic for defining clear data contracts and robust input/output validation for your models.
- Integrating trained ML models (using a simplified example) into your FastAPI service.
- Locally testing your API endpoints, including using the interactive documentation.
- Containerizing your FastAPI application with Docker for consistent deployment.

🔍 **How is it structured?** Clear, step-by-step instructions with comprehensive code examples in Markdown format. You'll build up from a simple "Hello World" to a containerized ML model serving application.

⏱️ **How much time will it take?** Approximately **45-60 minutes** – giving you a solid foundation to build and deploy your own ML-powered APIs.

---

## 📖 Table of Contents

1. [🚀 Tutorial: FastAPI Basics for Modern AI and MLOps](#-tutorial-fastapi-basics-for-modern-ai-and-mlops)
   1. [👀 Description](#-description)
   2. [📖 Table of Contents](#-table-of-contents)
   3. [⚙️ 1 - Prerequisites \& Installation](#️-1---prerequisites--installation)
2. [🤔 2 - Why FastAPI for AI \& MLOps?](#-2---why-fastapi-for-ai--mlops)
   1. [⭐ 3 - Core FastAPI: GET \& POST Requests](#-3---core-fastapi-get--post-requests)
      1. [Step 1: Create a Simple API with a GET Request](#step-1-create-a-simple-api-with-a-get-request)
      2. [Step 2: Run the FastAPI Service](#step-2-run-the-fastapi-service)
      3. [Step 3: Test the Service](#step-3-test-the-service)
      4. [Step 4: Create an API with a POST Request (Introducing Pydantic)](#step-4-create-an-api-with-a-post-request-introducing-pydantic)
      5. [Step 5: Test the POST Request](#step-5-test-the-post-request)
      6. [Step 6: Automatic API Documentation](#step-6-automatic-api-documentation)
   2. [🛠️ 4 - Integrating an ML Model with FastAPI](#️-4---integrating-an-ml-model-with-fastapi)
      1. [Step 1: The Model Module - A Simplified Example](#step-1-the-model-module---a-simplified-example)
      2. [Step 2: Defining Input/Output Data Structures with Pydantic](#step-2-defining-inputoutput-data-structures-with-pydantic)
      3. [Step 3: Creating the API Endpoints](#step-3-creating-the-api-endpoints)
      4. [Step 4: Running the Full Application](#step-4-running-the-full-application)
      5. [Step 5: Testing the Prediction Endpoint](#step-5-testing-the-prediction-endpoint)
   3. [🐳 5 - Running Your FastAPI Web Service in a Docker Container](#-5---running-your-fastapi-web-service-in-a-docker-container)
      1. [Step 1: Prepare the Dockerfile](#step-1-prepare-the-dockerfile)
      2. [Step 2: Build the Docker Image](#step-2-build-the-docker-image)
      3. [Step 3: Run the Docker Container](#step-3-run-the-docker-container)
   4. [🧪 6 - Pydantic Power-Up: Advanced Validation](#-6---pydantic-power-up-advanced-validation)
      1. [Python Type Annotations: A Quick Refresher](#python-type-annotations-a-quick-refresher)
      2. [Pydantic Basics Recap](#pydantic-basics-recap)
      3. [Advanced Validation with `Field` and `Annotated`](#advanced-validation-with-field-and-annotated)
      4. [Custom Logic with Field Validators (`@field_validator`)](#custom-logic-with-field-validators-field_validator)
      5. [Reusable Validations with `typing.Annotated`](#reusable-validations-with-typingannotated)
      6. [Testing the Enhanced Validation](#testing-the-enhanced-validation)
   5. [🔗 7 - Additional Resources](#-7---additional-resources)
   6. [🎉 8 - Next Steps \& Conclusion](#-8---next-steps--conclusion)

---

## ⚙️ 1 - Prerequisites & Installation

Before we dive in, let's ensure your environment is ready.

Prerequisites:

- Python 3.9+ installed. (FastAPI supports 3.8+, but newer versions are recommended).
- `uv` (Python package installer) installed. `uv` is a fast, modern package manager.
  - If you don't have `uv`, install it: `pip install uv` (or `pipx install uv`). Refer to the [official `uv` documentation](https://github.com/astral-sh/uv) for more installation options.
- Basic understanding of Python and the command line/terminal.
- Basic understanding of web concepts (HTTP methods like GET/POST, what an API is).
- Docker installed (for the Docker containerization section).

Please follow the [Quick Start: Installation & Setup](README.md#-quick-start-installation--setup) section in the README to set up your development environment. This will guide you through:

1. Cloning the repository
2. Creating and activating a virtual environment
3. Installing the required dependencies

---

Rewrite this section

- make shorter

# 🤔 2 - Why FastAPI for AI & MLOps?

FastAPI has rapidly become a favorite for building APIs, especially for serving machine learning models in MLOps pipelines. Here's why:

- 🚀 **High Performance:** FastAPI is built on Starlette (for web parts) and Pydantic (for data parts), and uses ASGI servers like Uvicorn, making it one of the fastest Python frameworks. **Low latency is critical for real-time ML model inference.**
- 🛡️ **Robust Data Validation with Pydantic:** Python type hints are used with Pydantic to define clear, validated data schemas for your requests and responses. This means:
  - **Clear Data Contracts:** Your ML model's expected input features and output structure are explicitly defined. This is vital for seamless integration in an MLOps pipeline where different services interact.
  - **Reduced Runtime Errors:** Invalid data is caught early with descriptive errors before it even reaches your model logic.
- ⏱️ **Rapid Development:** Intuitive syntax, great editor support (autocompletion!), and less boilerplate code mean you can develop, test, and iterate on your ML APIs much faster.
- 📚 **Automatic Interactive Documentation:** FastAPI automatically generates OpenAPI (Swagger UI) and ReDoc documentation from your code. This makes it incredibly easy for your team or other services to understand, test, and integrate with your ML API.
- 🧩 **Asynchronous Support (`async`/`await`):** Natively supports asynchronous code, which is beneficial for I/O-bound operations that might be part of your pre/post-processing logic around the model inference step.
- 🌐 **Standards-Based:** Adheres to open standards like OpenAPI and JSON Schema.
- 🏢 **Microservice Friendly:** Its lightweight nature and focus make it ideal for building ML models as independent microservices within a larger MLOps architecture.

In short, FastAPI helps you build production-ready, maintainable, and performant APIs for your AI/ML models with less effort.

---

## ⭐ 3 - Core FastAPI: GET & POST Requests

Let's start with the fundamentals of creating API endpoints.

### Step 1: Create a Simple API with a GET Request

Create a file named `main.py` (we'll create new files for steps to keep them distinct):

```python
# main.py
from fastapi import FastAPI

app = FastAPI(title="My First FastAPI App")

@app.get("/") # Path operation decorator for GET requests to the root path
async def read_root(): # Path operation function (can be async or sync)
    return {"message": "Hello from FastAPI!"}
```

### Step 2: Run the FastAPI Service

Open your terminal, navigate to the directory with `main.py`, and run:

```bash
uvicorn main:app --reload
```

- `main`: The Python file.

- `app`: The `FastAPI` instance inside `main.py`.
- `--reload`: For auto-restarting the server on code changes during development.

### Step 3: Test the Service

Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/). You should see:

```json
{"message":"Hello from FastAPI!"}
```

### Step 4: Create an API with a POST Request (Introducing Pydantic)

POST requests are typically used to send data to the server to create or update resources. FastAPI uses **Pydantic** models to define the structure and validate this incoming data.

Update `main.py`:

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel # Import BaseModel from Pydantic

app = FastAPI(title="FastAPI with POST")

# 1. Define a Pydantic model for the request body
class Item(BaseModel):
    name: str
    description: str | None = None  # Python 3.10+ for `| None`, or use `Optional[str]`
    price: float
    is_offer: bool | None = None

@app.get("/")
async def read_root():
    return {"message": "Send data to /items/ via POST!"}

# 2. Create a POST endpoint
@app.post("/items/") # Handles POST requests to /items/
async def create_item(item: Item): # FastAPI validates incoming data against the Item model
    # 'item' is now an instance of Item, with validated data
    return {"item_name": item.name, "item_price": item.price, "description": item.description}
```

- **Pydantic `BaseModel`:** We define `Item` inheriting from `pydantic.BaseModel`. Its attributes with type hints define the expected JSON structure.

- **Type Hinting:** `item: Item` in `create_item` tells FastAPI to expect a request body matching the `Item` model. FastAPI handles parsing the JSON, validating it, and converting it to an `Item` object. If validation fails, FastAPI automatically returns a 422 error.

### Step 5: Test the POST Request

Stop the previous server (Ctrl+C) and run the new one:

```bash
uvicorn main:app --reload
```

Use `curl` (or Postman/Insomnia) to send a POST request:

```bash
curl -X 'POST' 'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "string",
    "description": "string",
    "price": 0,
    "is_offer": true
    }'
```

**Expected Response:**

```json
{"item_name":"Super Gadget","item_price":49.99,"description":"An amazing new gadget for all your needs"}
```

Try sending invalid data (e.g., `price` as a string) to see FastAPI's automatic `422 validation error`!

### Step 6: Automatic API Documentation

FastAPI automatically generates interactive API documentation. With `main.py` running:

- **Swagger UI:** Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** Open [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

You can see your `/` (GET) and `/items/` (POST) endpoints, including the expected request body schema for `/items/` derived from the `Item` Pydantic model. You can even "Try it out" directly from Swagger UI!

---

## 🛠️ 4 - Integrating an ML Model with FastAPI

Let's integrate a fake "model" into FastAPI. For this tutorial, we'll use the simplified `gift_predictor.py` example.

### Step 1: The Model Module - A Simplified Example

Our "ML model" for this tutorial is a JSON file (`models/model.json`) that acts as a lookup table for gift suggestions.

> 👉 **Real-World Model Persistence:**
> This JSON file is a stand-in for a real ML model. In practice, you would:
>
> 1. **Train your model** using scikit-learn, TensorFlow, PyTorch, etc.
> 2. **Save (serialize) the trained model** to a file:
>     - `joblib.dump(model, 'model.joblib')` for scikit-learn.
>     - `model.save('tf_model_directory')` for TensorFlow.
>     - `torch.save(model.state_dict(), 'pytorch_model.pth')` for PyTorch.
>     - Or use ONNX for a framework-agnostic format.
> The principles of loading this saved model at FastAPI startup and using it in your prediction endpoint remain the same.

To work with this model, we'll create a `GiftPredictor` class in `app/model.py`. This module encapsulates all model-related logic:

- Loading and managing the model data from `model.json`
- Validating inputs
- Making predictions
- Error handling

The `GiftPredictor` class provides a clean interface for working with our model data, making it easy to:
1. Load the model at startup
2. Check if the model is loaded
3. Get a list of valid interests
4. Make predictions based on age and interest

### Step 2: Defining Input/Output Data Structures with Pydantic

Now, let's create our FastAPI application in `app/gift_predictor.py`:

```python
# app/gift_predictor.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from app.models.model import GiftPredictor

app = FastAPI(title="Birthday Gift Predictor API", version="1.0.0")

# Initialize the predictor
predictor = GiftPredictor()

class PredictionInput(BaseModel):
    age: int = Field(..., gt=0, le=120, description="User's age (1-120)")
    interest: str = Field(..., min_length=2, max_length=30, description="User's primary interest")

class PredictionOutput(BaseModel):
    predicted_gift: str
    suggested_category: str
    confidence_score: float | None = Field(None, ge=0, le=1, description="Model's confidence (0.0-1.0)")
```

### Step 3: Creating the API Endpoints

Add the endpoints to `app/gift_predictor.py`:

```python
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home():
    # ...
    # Return a simple HTML page with the available interests

@app.post("/predict/", response_model=PredictionOutput, tags=["Predictions"])
async def predict_birthday_gift(payload: PredictionInput):
    if not predictor.is_loaded():
        raise HTTPException(status_code=503, detail="Model not loaded. Service unavailable.")

    try:
        predicted_gift, suggested_category, confidence = predictor.predict(
            age=payload.age,
            interest=payload.interest
        )
        
        return PredictionOutput(
            predicted_gift=predicted_gift,
            suggested_category=suggested_category,
            confidence_score=confidence
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
```

This modular structure provides several benefits:
1. **Separation of Concerns**: Model logic is separate from API handling
2. **Better Error Handling**: Clear distinction between model and API errors
3. **Improved Maintainability**: Changes to model logic don't affect API code
4. **Easier Testing**: Can test model and API independently
5. **Better Code Organization**: Clear responsibilities for each component

### Step 4: Running the Full Application

Ensure your project structure looks like this:

```plaintext
fastapi-for-modern-ai-and-mlops/
├── app/
│   ├── model.py
│   └── gift_predictor.py
├── models/
│   └── model.json
└── requirements.txt
```

Then run:

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
  "predicted_gift": "A new tech gadget related to Coding.",
  "suggested_category": "coding",
  "confidence_score": 0.85
}
```

Or test via Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs):
Expand the `/predict/` endpoint, click "Try it out," enter valid JSON, and execute. You'll see the structured request and response. Try invalid input (e.g., age < 1 or invalid interest) to see the validation in action.

---

## 🐳 5 - Running Your FastAPI Web Service in a Docker Container

Containerizing your application with Docker ensures consistency across different environments and simplifies deployment.

### Step 1: Prepare the Dockerfile

A typical structure (ensure `Dockerfile` is at the root):

```plaintext
fastapi-for-modern-ai-and-mlops/
├── app/
├── models/
└── Dockerfile
...
```

Create/update your [Dockerfile](Dockerfile) at the project root.

### Step 2: Build the Docker Image

```bash
docker build -t fastapi-gift-predictor .
```

### Step 3: Run the Docker Container

```bash
# Remove old container if it exists
docker rm -f mygiftapp-container

# Run the new container
docker run --name mygiftapp-container -p 8000:8000 -d fastapi-gift-predictor
```

Your application is now running inside Docker, accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Test it as before!

---

## 🧪 6 - Pydantic Power-Up: Advanced Validation

Pydantic is incredibly powerful for defining precise data validation rules. Let's enhance our gift predictor API with advanced validation while keeping our existing `GiftPredictor` class.

### Python Type Annotations: A Quick Refresher

As discussed in "Why FastAPI?", type hints are fundamental. They declare the *expected* type of variables, function parameters, and return values. Pydantic leverages these.

### Pydantic Basics Recap

You've used `BaseModel` to define data structures and `Field` to add basic constraints (e.g., `gt`, `le`, `min_length`).

### Advanced Validation with `Field` and `Annotated`

Let's enhance our `PredictionInput` model with advanced validation while using our existing `GiftPredictor` class:

```python
# app/gift_predictor_updated.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, field_validator, ValidationInfo
from typing import Annotated
from pydantic.functional_validators import AfterValidator
from app.model import GiftPredictor

# Initialize the predictor
predictor = GiftPredictor()

# Get valid interests from the model
VALID_INTERESTS = predictor.get_valid_interests()

def validate_interest(value: str) -> str:
    """Validate and normalize interest value."""
    normalized_value = value.strip().lower()
    if normalized_value not in VALID_INTERESTS:
        raise ValueError(f"Interest must be one of: {', '.join(VALID_INTERESTS)}")
    return normalized_value

# Reusable Annotated type for interest validation
InterestType = Annotated[
    str,
    Field(description=f"Interest should be one of: {', '.join(VALID_INTERESTS)}"),
    AfterValidator(validate_interest)
]

class PredictionInput(BaseModel):
    """
    Represents the input data for predicting a birthday gift.
    """
    age: int = Field(..., gt=0, le=120, description="User's age (1-120)")
    interest: InterestType

    @field_validator('interest')
    @classmethod
    def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
        """Ensure interest contains only alphanumeric characters."""
        if not v.replace(' ', '').isalnum():
            raise ValueError(f'Field: {info.field_name} must be alphanumeric')
        return v

    @field_validator('age')
    @classmethod
    def validate_age_range(cls, v: int) -> int:
        """Additional age validation logic."""
        if v < 1 or v > 120:
            raise ValueError("Age must be between 1 and 120")
        return v
```

This enhanced validation:
1. Uses `Annotated` to create a reusable validated interest type
2. Automatically normalizes and validates interests against the model's valid interests
3. Adds multiple validators for both age and interest fields
4. Maintains compatibility with our existing `GiftPredictor` class

### Custom Logic with Field Validators (`@field_validator`)

The `@field_validator` decorator allows us to add custom validation logic. In our example, we have two validators:

1. **Age Validation**:

```python
@field_validator('age')
@classmethod
def validate_age_range(cls, v: int) -> int:
    """Additional age validation logic."""
    if v < 1 or v > 120:
        raise ValueError("Age must be between 1 and 120")
    return v
```

2. **Interest Validation**:
```python
@field_validator('interest')
@classmethod
def check_alphanumeric(cls, v: str, info: ValidationInfo) -> str:
    """Ensure interest contains only alphanumeric characters."""
    if not v.replace(' ', '').isalnum():
        raise ValueError(f'Field: {info.field_name} must be alphanumeric')
    return v
```

These validators:
- Run after the basic field validation
- Can access other fields through the `info` parameter
- Can modify the value before it's stored
- Raise `ValueError` for invalid values
- Can be chained together for multiple validation steps

### Reusable Validations with `typing.Annotated`

The `InterestType` shows how to create reusable validation:

```python
def validate_interest(value: str) -> str:
    """Validate and normalize interest value."""
    normalized_value = value.strip().lower()
    if normalized_value not in VALID_INTERESTS:
        raise ValueError(f"Interest must be one of: {', '.join(VALID_INTERESTS)}")
    return normalized_value

InterestType = Annotated[
    str,
    Field(description=f"Interest should be one of: {', '.join(VALID_INTERESTS)}"),
    AfterValidator(validate_interest)
]
```

Benefits of this approach:
1. Validation logic is reusable across different models
2. The validation function is pure and testable
3. Error messages are clear and helpful
4. The validation is automatically applied when the type is used
5. Can be combined with field validators for additional checks

### Testing the Enhanced Validation

Try these test cases with the updated API:

```bash
# Valid request
curl -X POST "http://127.0.0.1:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"age": 28, "interest": "Programming"}'

# Invalid age
curl -X POST "http://127.0.0.1:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"age": 150, "interest": "Programming"}'

# Invalid interest (non-alphanumeric)
curl -X POST "http://127.0.0.1:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"age": 28, "interest": "Programming!"}'

# Invalid interest (not in list)
curl -X POST "http://127.0.0.1:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"age": 28, "interest": "Skydiving"}'
```

Each invalid request will return a `422` error with a descriptive message about what went wrong.

---

## 🔗 7 - Additional Resources

- **FastAPI Official Documentation:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) - The ultimate source.
- **Pydantic Official Documentation:** [docs.pydantic.dev](https://docs.pydantic.dev/latest/) - Essential for data validation.
- **Uvicorn Official Documentation:** [www.uvicorn.org](https://www.uvicorn.org/) - The ASGI server.
- **TestDriven.io - FastAPI Courses & Articles:** [testdriven.io/courses/fastapi-crud/](https://testdriven.io/courses/fastapi-crud/)
- **RealPython - Python Type Checking Guide:** [realpython.com/python-type-checking/](https://realpython.com/python-type-checking/)

---

## 🎉 8 - Next Steps & Conclusion

Congratulations! You've successfully navigated the basics of FastAPI for AI and MLOps, from simple endpoints to a containerized "ML" service with robust data validation. You now have a strong foundation to build upon.

**Where to go from here?**

- 📦 **Real Model Integration:** Replace the JSON "model" with a real, serialized ML model (scikit-learn, TensorFlow, PyTorch, ONNX).
- 🧪 **Testing:** Implement unit and integration tests for your API using `pytest` and FastAPI's `TestClient`.
- 🔐 **Authentication & Authorization:** Secure your API endpoints (e.g., OAuth2 with JWT tokens).
- ⚙️ **Configuration Management:** Use Pydantic's `BaseSettings` for managing application configurations (e.g., model paths, API keys).
- 📊 **Databases:** Integrate with databases (SQLAlchemy, Tortoise ORM, SQLModel) if your application needs persistence.
- 🔄 **Asynchronous Tasks:** For long-running operations (e.g., complex model inference, batch processing), explore FastAPI's background tasks or integrate with task queues like Celery or RQ.
- 🚀 **Deployment:** Explore advanced deployment options:
  - Kubernetes for orchestration.
  - Serverless platforms (AWS Lambda + API Gateway, Google Cloud Functions/Run).
  - Managed PaaS (Heroku, AWS Elastic Beanstalk).
- 🔗 **MLOps Integration:**
  - Connect with ML experiment tracking tools (e.g., **MLflow**, DVC) for model versioning and lineage.
  - Implement proper logging and monitoring (e.g., Prometheus, Grafana) for your API's performance and model behavior.
  - Consider how your FastAPI service fits into a larger CI/CD pipeline for MLOps.
- 🧩 **Advanced FastAPI:** Explore features like WebSockets, dependencies with `Depends`, middleware, and custom responses.

FastAPI provides the tools to build powerful and efficient APIs. The journey into MLOps involves continuous learning and integration of various tools and practices, and FastAPI is an excellent component in that ecosystem.

Happy building, and may your models always serve with excellence! 🚀

[⬆️ Back to Table of Contents](#-table-of-contents)
