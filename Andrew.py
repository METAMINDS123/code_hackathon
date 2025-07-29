import json
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

# Placeholder functions for modularity (you can replace these with real implementations)
def generate_meal_plan(user_profile):
    # Mock response; replace with LLM logic
    return {
        "meals": [
            {"name": "Tofu Stir Fry", "macros": {"calories": 400, "protein": 25, "carbs": 30, "fat": 20}, "steps": ["Cut vegetables", "Stir fry with tofu"]},
            {"name": "Quinoa Salad", "macros": {"calories": 350, "protein": 15, "carbs": 40, "fat": 10}, "steps": ["Cook quinoa", "Mix with vegetables"]},
            {"name": "Lentil Soup", "macros": {"calories": 300, "protein": 20, "carbs": 35, "fat": 5}, "steps": ["Boil lentils", "Add spices"]},
        ],
        "snacks": [
            {"name": "Almonds", "macros": {"calories": 200, "protein": 8, "carbs": 5, "fat": 18}},
            {"name": "Fruit Bowl", "macros": {"calories": 150, "protein": 2, "carbs": 35, "fat": 1}}
        ]
    }

def check_ingredient_availability(required_ingredients, user_pantry):
    missing = [item for item in required_ingredients if item not in user_pantry]
    return missing

def order_from_blinkit(items):
    print(f"Ordering from Blinkit: {items}")

def suggest_alternative():
    return "Try oatmeal with fruits as an alternative."

# Initialize language model and memory
llm = ChatOpenAI(temperature=0, model_name="gpt-4")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Tools / skills that can be invoked by the agent
tools = [
    Tool(
        name="Meal Planner",
        func=lambda x: json.dumps(generate_meal_plan(x)),
        description="Generate a personalized meal plan."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# Simulated chat interaction
def run_agent():
    user_pantry = set()
    user_profile = {}

    print("👋 Hello! I’m Diettly, your smart meal planner bot. Let’s get started!")
    
    user_profile['age'] = int(input("What's your age? "))
    user_profile['weight'] = float(input("Your weight in kg? "))
    user_profile['height'] = float(input("Your height in cm? "))
    
    user_profile['conditions'] = input("Any health conditions (e.g., Diabetes, PCOD, etc.)? ").split(',')
    user_profile['allergies'] = input("Any allergies or intolerances? ").split(',')
    user_profile['diet_type'] = input("Preferred diet type (Veg, Vegan, etc.)? ")
    user_profile['cuisine'] = input("Preferred cuisines (e.g., Indian, Mediterranean)? ")
    user_profile['fasting'] = input("Do you follow any fasting mode (e.g., Intermittent)? ")

    response = generate_meal_plan(user_profile)
    print("\n🍽️ Your personalized meal plan:")
    for meal in response['meals']:
        print(f"- {meal['name']} | Calories: {meal['macros']['calories']} kcal")
    for snack in response['snacks']:
        print(f"- {snack['name']} (Snack) | Calories: {snack['macros']['calories']} kcal")

    # Collect user pantry
    pantry_input = input("\nEnter ingredients you have (comma-separated): ")
    user_pantry = set([item.strip().lower() for item in pantry_input.split(',')])

    required_ingredients = ['tofu', 'quinoa', 'lentils', 'vegetables', 'almonds', 'fruit']
    missing = check_ingredient_availability(required_ingredients, user_pantry)

    if missing:
        print(f"\nYou're missing these ingredients: {missing}")
        consent = input("Would you like me to order them from Blinkit? (yes/no): ").strip().lower()
        if consent == 'yes':
            order_from_blinkit(missing)
            print("✅ Order placed! Meals will be ready soon.")
        else:
            print(f"Okay! Here's an alternative: {suggest_alternative()}")
    else:
        print("✅ You have everything needed. Let's start cooking!")

    # Show cooking steps and macros
    print("\n📋 Step-by-step guide for your first meal:")
    first_meal = response['meals'][0]
    for i, step in enumerate(first_meal['steps'], 1):
        print(f"Step {i}: {step}")

    print("\n🔬 Nutrition Breakdown:")
    for macro, value in first_meal['macros'].items():
        print(f"{macro.capitalize()}: {value}")

if __name__ == '__main__':
    run_agent()
