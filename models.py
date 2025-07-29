from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class UserProfile(BaseModel):
    age: int
    weight: float
    height: float
    health_conditions: Optional[List[str]] = Field(default_factory=list)
    allergies: Optional[List[str]] = Field(default_factory=list)

class Preferences(BaseModel):
    diet_type: str
    cuisines: List[str]
    fasting_mode: Optional[str] = None

class Pantry(BaseModel):
    ingredients: List[str]

class MealPlanRequest(BaseModel):
    profile: UserProfile
    preferences: Preferences
    pantry: Pantry

class Meal(BaseModel):
    name: str
    ingredients: List[str]
    instructions: str
    macros: Dict[str, float]

class MealPlanResponse(BaseModel):
    meals: List[Meal]
    snacks: List[Meal]
    missing_ingredients: List[str]

class BlinkitOrderRequest(BaseModel):
    missing_ingredients: List[str]







#how to use 
#In your main.py, import these models like this:
from models import UserProfile, Preferences, Pantry, MealPlanRequest, Meal, MealPlanResponse, BlinkitOrderRequest
