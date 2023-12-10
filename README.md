FastAPI based service for the Birthday Gift Predictor
===================================================

The Birthday Gift Predictor is a FastAPI-based web application designed to suggest unique and personalized gift ideas based on the user's age and interests. Utilizing a JSON-based model, the app offers a fun and interactive way to discover the perfect birthday present.

## Install

To get started with the Birthday Gift Predictor, you need to have Python installed on your system. Follow these steps to install the necessary dependencies:

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   Navigate to the project directory and create a virtual environment:

   ```bash
    python3 -m venv .venv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     .\.venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source .venv/bin/activate
     ```

3. **Install Dependencies**

   With the virtual environment activated, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Run Application

After installing the dependencies, you're ready to run the application:

1. **Start the FastAPI Server**

   Run the following command in the terminal:

   ```bash
   uvicorn app.git_predictor:app --reload
   ```

   The `--reload` flag enables auto-reload so the server will restart after changes in the code.

2. **Access the Application**

   Open your web browser and navigate to:

   ```
   http://localhost:8000/
   ```

   You will see the Birthday Gift Predictor's homepage where you can interact with the application.
