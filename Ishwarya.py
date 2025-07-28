import streamlit as st
import random

# Mock recipe database
MOCK_RECIPES = [
    {
        "name": "Grilled Veggie Bowl",
        "ingredients": ["zucchini", "bell pepper", "quinoa", "olive oil"],
        "macros": {"calories": 450, "protein": "12g", "fat": "18g", "carbs": "50g"},
        "instructions": "Grill veggies, cook quinoa, combine and drizzle with olive oil."
    },
    {
        "name": "Chickpea Salad",
        "ingredients": ["chickpeas", "cucumber", "tomato", "lemon", "olive oil"],
        "macros": {"calories": 350, "protein": "14g", "fat": "10g", "carbs": "40g"},
        "instructions": "Mix all ingredients in a bowl and serve chilled."
    }
]

st.set_page_config(page_title="Diettly AI Meal Planner", layout="centered")

st.title("🥗 Diettly – Smart AI Meal Planner")

# --- 1. User Profile Intake ---
st.header("1️⃣ Your Profile")
age = st.number_input("Age", min_value=10, max_value=100, step=1)
weight = st.number_input("Weight (kg)", min_value=30.0)
height = st.number_input("Height (cm)", min_value=100.0)

bmi = weight / ((height / 100) ** 2) if height > 0 else 0
st.success(f"✅ Your BMI is {bmi:.2f}")

health_issues = st.multiselect("Health Conditions", ["Diabetes", "PCOD", "Thyroid", "None"])
allergies = st.text_input("Food Allergies (comma separated)", placeholder="e.g. peanuts, gluten")

# --- 2. Preferences ---
st.header("2️⃣ Preferences")
diet_type = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan", "Jain"])
cuisine = st.multiselect("Preferred Cuisine", ["Indian", "Mediterranean", "Korean", "Mexican"])
fasting = st.selectbox("Fasting Mode", ["None", "Intermittent Fasting", "OMAD"])

# --- 3. Pantry Check ---
st.header("3️⃣ Pantry Check")
pantry = st.text_area("List your available ingredients (comma separated)",
                      placeholder="e.g. tomato, rice, paneer, cucumber")
pantry_items = [item.strip().lower() for item in pantry.split(",") if item.strip()]

# --- 4. Meal Generation ---
st.header("4️⃣ Personalized Meal Plan")

if st.button("🔍 Generate Meal Plan"):
    filtered_recipes = []
    for recipe in MOCK_RECIPES:
        if any(item in pantry_items for item in recipe["ingredients"]):
            if not any(allergy.strip().lower() in recipe["ingredients"] for allergy in allergies.split(",")):
                filtered_recipes.append(recipe)

    if not filtered_recipes:
        st.warning("No suitable meals found with your pantry and preferences.")
    else:
        for i, recipe in enumerate(filtered_recipes):
            st.subheader(f"🍽️ {recipe['name']}")
            st.write("**Ingredients:**", ", ".join(recipe["ingredients"]))
            st.write("**Nutritional Info:**", recipe["macros"])
            st.write("**Instructions:**", recipe["instructions"])

            missing = [i for i in recipe["ingredients"] if i not in pantry_items]
            if missing:
                st.info(f"❌ Missing ingredients: {', '.join(missing)}")

                if st.checkbox(f"Do you allow Diettly to order missing ingredients for **{recipe['name']}** via Blinkit?", key=f"consent_{i}"):
                    st.success("📦 Order placed for missing items! (simulated)")
                else:
                    st.warning("⚠️ Consent not given. Please purchase manually.")
            else:
                st.success("✅ All ingredients available!")

