# mealplan_generator.py

from typing import List, Dict, Any
from models import UserProfile, Preferences, Pantry, Meal, MealPlanResponse

def generate_sample_meal(name: str, ingredients: List[str], calories: float) -> Meal:
    # This function is for demonstration; plug in true LLM or recipe DB in real app
    return Meal(
        name=name,
        ingredients=ingredients,
        instructions=f"Prepare {name} using {', '.join(ingredients)}. Enjoy!",
        macros={"calories": calories, "protein": 10, "carbs": 50, "fat": 12}
    )

def analyze_ingredient_gap(meals: List[Meal], snacks: List[Meal], pantry: Pantry) -> List[str]:
    needed = set(ing.lower() for meal in meals + snacks for ing in meal.ingredients)
    owned = set(ing.lower() for ing in pantry.ingredients)
    return list(needed - owned)

def meal_plan_generator(
    profile: UserProfile,
    preferences: Preferences,
    pantry: Pantry
) -> MealPlanResponse:
    # You can add logic using profile/preferences in a real-world app.
    meals = [
        generate_sample_meal("Quinoa Salad", ["quinoa", "tomato", "olive oil", "cucumber"], 450)
    ]
    snacks = [
        generate_sample_meal("Fruit Bowl", ["banana", "apple"], 180)
    ]
    missing_ingredients = analyze_ingredient_gap(meals, snacks, pantry)
    return MealPlanResponse(
        meals=meals,
        snacks=snacks,
        missing_ingredients=missing_ingredients
    )
