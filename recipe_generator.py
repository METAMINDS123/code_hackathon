import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_recipe_instructions(meal_name, ingredients):
    prompt = f"Give detailed, step-by-step cooking instructions for {meal_name} using {', '.join(ingredients)}."

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content
