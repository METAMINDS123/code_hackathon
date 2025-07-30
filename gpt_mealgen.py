import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_meal_plan(user_data):
    prompt = f"""
    Based on the following details:
    - Age: {user_data.age}
    - Weight: {user_data.weight}
    - Height: {user_data.height}
    - Health: {', '.join(user_data.health_conditions)}
    - Allergies: {', '.join(user_data.allergies)}
    - Diet Type: {user_data.diet_type}
    - Cuisine: {', '.join(user_data.cuisine_pref)}
    - Pantry: {', '.join(user_data.pantry_items)}

    Suggest 3 meals and 2 snacks with a JSON structure:
    [
        {{
            "name": "Meal Name",
            "description": "...",
            "calories": 400,
            "macros": {{"protein": 20, "carbs": 30, "fat": 10}},
            "ingredients": [...],
            "missing": [...]
        }},
        ...
    ]
    """

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    output = res.choices[0].message.content
    return output  # parse if JSON
