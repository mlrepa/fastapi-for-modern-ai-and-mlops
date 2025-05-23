import json
from typing import Dict, Any, Optional
from pathlib import Path

class GiftPredictor:
    def __init__(self, model_path: str = "models/model.json"):
        self.model_path = model_path
        self.model_data: Optional[Dict[str, Any]] = None
        self.valid_interests: list[str] = []
        self._load_model()

    def _load_model(self) -> None:
        """Load the model data from JSON file."""
        try:
            with open(self.model_path, 'r') as f:
                self.model_data = json.load(f)
            self.valid_interests = list(self.model_data.get("interests", {}).keys())
            print(f"Successfully loaded model data from {self.model_path}")
        except FileNotFoundError:
            print(f"ERROR: Model file not found at {self.model_path}")
            self.model_data = None
        except json.JSONDecodeError:
            print(f"ERROR: Could not decode JSON from {self.model_path}")
            self.model_data = None

    def is_loaded(self) -> bool:
        """Check if the model is loaded."""
        return self.model_data is not None

    def get_valid_interests(self) -> list[str]:
        """Get list of valid interests."""
        return self.valid_interests

    def predict(self, age: int, interest: str) -> tuple[str, str, float]:
        """
        Make a prediction based on age and interest.
        
        Args:
            age: User's age (1-120)
            interest: User's interest (must be in valid_interests)
            
        Returns:
            tuple: (predicted_gift, suggested_category, confidence_score)
            
        Raises:
            ValueError: If interest is not valid
        """
        if not self.is_loaded():
            raise RuntimeError("Model not loaded")

        interest_lower = interest.lower()
        if interest_lower not in self.valid_interests:
            raise ValueError(f"Invalid interest. Must be one of: {', '.join(self.valid_interests)}")

        age_str = str(age)
        primary_gift = self.model_data.get("gifts_by_age", {}).get(age_str, "A thoughtful surprise")
        interest_category = self.model_data.get("interests", {}).get(interest_lower, "General Interest")
        
        final_gift_suggestion = f"{primary_gift} related to {interest_category}."
        if interest_category == "General Interest" and primary_gift == "A thoughtful surprise":
            final_gift_suggestion = "A very special and unique surprise, just for you!"
            
        # In a real application, this would be calculated by the model
        confidence = 0.85  # Simplified for example

        return final_gift_suggestion, interest_category, confidence 
