import streamlit as st
from models.user_model import User
from models.split_model import WorkoutSplit
from src.GetResponseClass import WorkoutGenerator

AiWorkoutGenerator = WorkoutGenerator()

st.title("AI Workout Generator 🏋️")


# Use st.form for better form handling
with st.form("user_info"):
    # Input fields
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.slider("Age", min_value=18, max_value=60)
    level = st.selectbox("Level", options=["Beginner", "Intermediate", "Advanced"])
    weight = st.slider("Weight (kg)", min_value=40, max_value=200)
    height = st.slider("Height (cm)", min_value=50, max_value=300)
    workout_split = st.selectbox("Workout split", options=["Body Part Workout Split", "Upper-Lower Split", "Push-Pull-Legs Split",
                                                           "Classic Bodybuilding Split", "Five-Day Split"])
    frequency = st.selectbox("Frequency", options=["1 day" ,"1 week", "1 month"])
    goal = st.selectbox("Goal", options=["Fat Loss" ,"Gaining", "Body Tone"])
    
    
    # Submit button within the form
    submit_button = st.form_submit_button("Submit")

# Handle form submission outside the form context
if submit_button:
    # Validation logic
    if name and email and age and level and weight and height:
        # Display user details
        st.subheader("User Details 📌")
        st.write(f"- **Name:** {name}")
        st.write(f"- **Email:** {email}")
        st.write(f"- **Age:** {age}")
        st.write(f"- **Level:** {level}")
        st.write(f"- **Weight (kg):** {weight}")
        st.write(f"- **Height (cm):** {height}")
        st.write(f"- **Workout Split :** {workout_split}")
        st.write(f"- **workout Frequency :** {frequency}")
        st.write(f"- **Goal :** {goal}")
        
        user = User(id="01", username= name, age=age ,email = email, level=level, weight=weight,
                    height=height)
        split = WorkoutSplit(split=workout_split, frequency=frequency, goal=goal)
        
        with st.spinner('Generating workout plan...'):
            response = AiWorkoutGenerator.get_response(user=user, workoutsplit=split, advanced=level.lower())
            if response:
                st.subheader("Generated Workout Plan 💪")
                st.markdown(response.content)
            else:
                st.write("No response")
                
    else:
        st.error("Please fill in all the fields.")