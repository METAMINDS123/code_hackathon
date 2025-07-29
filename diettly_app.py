# diettly_app.py

import streamlit as st
from utils.bmi import calculate_bmi
from utils.storage import save_consent_log

st.set_page_config(page_title="Diettly - AI Meal Planner", layout="wide")

# Session state initialization
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'consent_log' not in st.session_state:
    st.session_state.consent_log = []
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Page Navigation Sidebar
with st.sidebar:
    st.title("🍽️ Diettly")
    st.markdown("### Navigate")
    st.session_state.page = st.radio("Go to", ["home", "onboarding", "pantry", "meals", "consent_log"])

# PAGE: Home
if st.session_state.page == 'home':
    st.title("🥗 Diettly – Your Smart AI Meal Planner")
    st.markdown("AI-powered meals tailored to your health, lifestyle and taste.")
    st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c", use_column_width=True)
    if st.button("Start Planning Meals"):
        st.session_state.page = 'onboarding'

# PAGE: Onboarding
elif st.session_state.page == 'onboarding':
    st.header("👤 User Profile")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=1, key='age')
        weight = st.number_input("Weight (kg)", min_value=1, key='weight')
    with col2:
        height = st.number_input("Height (cm)", min_value=1, key='height')
        if weight and height:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI: {bmi:.2f}")

    health_conditions = st.multiselect("Health Conditions", ["Diabetes", "PCOD", "Thyroid", "None"])
    allergies = st.multiselect("Allergies / Intolerances", ["Peanuts", "Dairy", "Gluten", "None"])

    st.header("🍽️ Preferences")
    diet_type = st.selectbox("Diet Type", ["Veg", "Non-Veg", "Vegan", "Jain"])
    cuisine_pref = st.multiselect("Cuisine Preferences", ["Indian", "Mediterranean", "Korean", "Mexican"])
    fasting_mode = st.selectbox("Fasting Mode", ["None", "Intermittent", "OMAD"])

    st.session_state.user_data.update({
        "age": age, "weight": weight, "height": height,
        "health_conditions": health_conditions,
        "allergies": allergies,
        "diet_type": diet_type,
        "cuisine_pref": cuisine_pref,
        "fasting_mode": fasting_mode
    })

    if st.button("Continue to Pantry"):
        st.session_state.page = 'pantry'

# PAGE: Pantry
elif st.session_state.page == 'pantry':
    st.header("🧂 Pantry Input")
    pantry = st.text_input("List available ingredients (comma-separated)", key='pantry_items')
    if st.button("Generate Meal Plan"):
        st.session_state.user_data["pantry_items"] = [item.strip().lower() for item in pantry.split(",")]
        st.session_state.page = 'meals'

# PAGE: Meal Plan
elif st.session_state.page == 'meals':
    st.header("🍱 Your AI-Generated Meal Plan")

    # Simulated Meals
    meals = [
        {
            "name": "Paneer Power Bowl",
            "macros": {"Calories": 450, "Protein": 22, "Carbs": 40},
            "missing": ["Cucumber", "Avocado"]
        },
        {
            "name": "Mixed Fruit Snack",
            "macros": {"Calories": 120, "Protein": 1, "Carbs": 28},
            "missing": []
        }
    ]

    for meal in meals:
        with st.expander(f"🍽️ {meal['name']}"):
            st.subheader("Nutritional Info")
            st.json(meal["macros"])

            if meal["missing"]:
                st.warning(f"Missing ingredients: {', '.join(meal['missing'])}")
                consent_key = f"consent_{meal['name']}"
                if st.checkbox(f"I consent to order missing items for '{meal['name']}'", key=consent_key):
                    save_consent_log(f"Consent given for ordering: {meal['missing']} in '{meal['name']}'")
                    st.success("Consent captured. Order initiated (simulated).")
            else:
                st.info("You have all ingredients!")

            if st.button(f"Show Cooking Instructions for {meal['name']}"):
                st.write("🔪 Step 1: Prep ingredients\n🔥 Step 2: Cook accordingly\n🍽️ Step 3: Serve and enjoy!")

# PAGE: Consent Log
elif st.session_state.page == 'consent_log':
    st.header("🔒 Consent Log")
    if st.session_state.consent_log:
        for log in st.session_state.consent_log:
            st.code(log)
    else:
        st.info("No consent actions yet.")
