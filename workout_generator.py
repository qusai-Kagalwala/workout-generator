import streamlit as st
import random
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Home Workout Generator",
    page_icon="💪",
    layout="wide"
)

# Add custom CSS for better styling
st.markdown("""
<style>
    .workout-container {
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .exercise-item {
        background-color: #ffffff;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .header-style {
        font-size: 40px;
        font-weight: bold;
        color: #3366ff;
        margin-bottom: 20px;
    }
    .subheader-style {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Exercise database
exercise_database = {
    "cardio": [
        {"name": "Jumping Jacks", "description": "Stand with feet together, arms at sides. Jump to spread legs and raise arms overhead. Jump back to starting position.", "difficulty": "easy", "equipment": None, "time_based": True},
        {"name": "High Knees", "description": "Run in place, lifting knees as high as possible towards chest.", "difficulty": "medium", "equipment": None, "time_based": True},
        {"name": "Burpees", "description": "Begin in standing position, drop to squat, kick feet back to plank, return to squat, jump up with arms extended.", "difficulty": "hard", "equipment": None, "time_based": True},
        {"name": "Mountain Climbers", "description": "Begin in plank position, alternately bring knees toward chest in running motion.", "difficulty": "medium", "equipment": None, "time_based": True},
        {"name": "Jump Rope", "description": "Simulate or use actual jump rope, jumping lightly on toes.", "difficulty": "medium", "equipment": "Optional jump rope", "time_based": True},
        {"name": "Squat Jumps", "description": "Perform a regular squat, then explosively jump upward. Land softly and repeat.", "difficulty": "medium", "equipment": None, "time_based": True},
        {"name": "Lateral Shuffles", "description": "Stand with feet shoulder-width apart, bend knees slightly, shuffle laterally for specified distance then return.", "difficulty": "medium", "equipment": None, "time_based": True}
    ],
    "balance": [
        {"name": "Single Leg Stand", "description": "Stand on one foot, hold position. For added difficulty, close eyes.", "difficulty": "easy", "equipment": None, "time_based": True},
        {"name": "Tree Pose", "description": "Stand on one leg, place other foot on inner thigh, hands in prayer position or extended overhead.", "difficulty": "medium", "equipment": None, "time_based": True},
        {"name": "Warrior III", "description": "Balance on one leg, extend arms forward and other leg backward parallel to floor.", "difficulty": "hard", "equipment": None, "time_based": True},
        {"name": "Standing Figure Four", "description": "Stand on one leg, rest opposite ankle on standing knee, maintaining upright posture.", "difficulty": "medium", "equipment": None, "time_based": True},
        {"name": "Single Leg Deadlift", "description": "Stand on one leg, hinge at hips while extending other leg behind you. Return to standing.", "difficulty": "medium", "equipment": None, "time_based": False}
    ],
    "strength": [
        {"name": "Push-ups", "description": "Begin in plank position with hands shoulder-width apart, lower body until chest nearly touches floor, push back up.", "difficulty": "medium", "equipment": None, "time_based": False},
        {"name": "Squats", "description": "Stand with feet shoulder-width apart, lower body by bending knees and pushing hips back, then return to standing.", "difficulty": "medium", "equipment": None, "time_based": False},
        {"name": "Lunges", "description": "Step forward with one leg, lowering hips until both knees are bent at 90 degrees. Push back to starting position.", "difficulty": "medium", "equipment": None, "time_based": False},
        {"name": "Plank", "description": "Hold position similar to top of push-up, keeping body in straight line from head to heels.", "difficulty": "medium", "equipment": None, "time_based": True},
        {"name": "Glute Bridges", "description": "Lie on back with knees bent, feet flat. Lift hips toward ceiling, squeezing glutes at top. Lower and repeat.", "difficulty": "easy", "equipment": None, "time_based": False},
        {"name": "Tricep Dips", "description": "Using chair or couch, place hands on edge, legs extended. Lower body by bending elbows, then push back up.", "difficulty": "medium", "equipment": "Chair or couch", "time_based": False},
        {"name": "Bicycle Crunches", "description": "Lie on back, hands behind head, alternately bring elbow to opposite knee while extending other leg.", "difficulty": "medium", "equipment": None, "time_based": False},
        {"name": "Supermans", "description": "Lie face down, simultaneously lift arms, chest, and legs off floor. Hold briefly, then lower.", "difficulty": "medium", "equipment": None, "time_based": False},
        {"name": "Wall Sit", "description": "Lean against wall with back flat, lower until thighs are parallel to floor, hold position.", "difficulty": "medium", "equipment": None, "time_based": True}
    ],
    "flexibility": [
        {"name": "Standing Hamstring Stretch", "description": "Stand with one foot slightly in front, toes up. Hinge at hips, keeping back straight, until stretch is felt in hamstring.", "difficulty": "easy", "equipment": None, "time_based": True},
        {"name": "Child's Pose", "description": "Kneel on floor, sit back on heels, extend arms forward and lower chest to floor.", "difficulty": "easy", "equipment": None, "time_based": True},
        {"name": "Cobra Stretch", "description": "Lie face down, place hands under shoulders, push chest up while keeping hips on floor.", "difficulty": "easy", "equipment": None, "time_based": True},
        {"name": "Butterfly Stretch", "description": "Sit with soles of feet together, knees out. Gently press knees toward floor.", "difficulty": "easy", "equipment": None, "time_based": True},
        {"name": "Standing Quad Stretch", "description": "Stand on one leg, grab other foot behind you, pull heel toward buttock.", "difficulty": "easy", "equipment": None, "time_based": True},
        {"name": "Cat-Cow Stretch", "description": "On hands and knees, alternate between arching back upward (cat) and letting it sag (cow).", "difficulty": "easy", "equipment": None, "time_based": True},
        {"name": "Neck Stretch", "description": "Gently tilt head to each side, holding position when stretch is felt along side of neck.", "difficulty": "easy", "equipment": None, "time_based": True}
    ],
    "stamina": [
        {"name": "Tabata Sequence", "description": "20 seconds of intense work followed by 10 seconds of rest, repeated 8 times.", "difficulty": "hard", "equipment": None, "time_based": True},
        {"name": "Jump Squats", "description": "Perform squat, then jump explosively. Land softly and immediately lower into next squat.", "difficulty": "hard", "equipment": None, "time_based": False},
        {"name": "Plank Jacks", "description": "Begin in plank position, jump feet out wide and back together, similar to jumping jack motion.", "difficulty": "hard", "equipment": None, "time_based": True},
        {"name": "Burpee Variations", "description": "Standard burpees with added push-up at bottom position or jump higher at top.", "difficulty": "hard", "equipment": None, "time_based": True},
        {"name": "Bear Crawls", "description": "On hands and feet with knees slightly off ground, move forward/backward/laterally while maintaining position.", "difficulty": "medium", "equipment": None, "time_based": True},
        {"name": "Box Steps", "description": "Using stairs or sturdy platform, step up and down quickly, alternating leading leg.", "difficulty": "medium", "equipment": "Step, stairs, or sturdy platform", "time_based": True}
    ]
}

def main():
    # Title and introduction
    st.markdown("<h1 class='header-style'>🏋️‍♀️ Personalized Home Workout Generator</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    Create your customized workout routine by selecting your preferences below. 
    Mix and match different exercise types to build a balanced workout routine!
    """)
    
    # Create sidebar for inputs
    st.sidebar.markdown("## Workout Preferences")
    
    # Exercise type selection
    st.sidebar.markdown("### Exercise Types")
    exercise_types = ["cardio", "balance", "strength", "flexibility", "stamina"]
    selected_types = []
    
    for ex_type in exercise_types:
        if st.sidebar.checkbox(f"{ex_type.capitalize()}", key=f"check_{ex_type}"):
            selected_types.append(ex_type)
    
    # Workout duration
    st.sidebar.markdown("### Workout Duration")
    total_duration = st.sidebar.slider("Total workout time (minutes)", 5, 60, 30, 5)
    
    # Exercise difficulty
    st.sidebar.markdown("### Difficulty Level")
    difficulty = st.sidebar.select_slider(
        "Select difficulty level",
        options=["Easy", "Moderate", "Challenging"],
        value="Moderate"
    )
    
    # Repetition settings
    st.sidebar.markdown("### Repetition Settings")
    rep_range = st.sidebar.slider("Repetition range (for strength exercises)", 5, 30, (8, 15))
    time_range = st.sidebar.slider("Duration range (seconds, for timed exercises)", 10, 120, (20, 60))
    
    # Rest periods
    st.sidebar.markdown("### Rest Periods")
    rest_between_exercises = st.sidebar.slider("Rest between exercises (seconds)", 10, 90, 30, 5)
    
    # Generate workout button
    if st.sidebar.button("Generate Workout"):
        if not selected_types:
            st.warning("Please select at least one exercise type to generate a workout!")
        else:
            generate_workout(selected_types, total_duration, difficulty, rep_range, time_range, rest_between_exercises)
    
    # Information section at the bottom
    with st.expander("ℹ️ About This App"):
        st.markdown("""
        ### How to Use This Workout Generator
        
        1. **Select Exercise Types**: Choose from cardio, balance, strength, flexibility, and stamina
        2. **Set Duration**: Determine how long your workout should be
        3. **Choose Difficulty**: Select a difficulty level that matches your fitness
        4. **Adjust Repetitions**: Set your preferred repetition and time ranges
        5. **Set Rest Periods**: Determine how long to rest between exercises
        6. **Generate**: Click the button to create your personalized workout
        
        ### Benefits of Mixed Exercise Types
        
        * **Cardio**: Improves heart health and burns calories
        * **Balance**: Enhances stability and core strength
        * **Strength**: Builds muscle and increases metabolism
        * **Flexibility**: Improves range of motion and prevents injury
        * **Stamina**: Builds endurance and mental toughness
        
        Remember to consult with a healthcare professional before starting any new exercise program.
        """)

def difficulty_filter(exercises, level):
    """Filter exercises based on selected difficulty level"""
    if level == "Easy":
        return [ex for ex in exercises if ex["difficulty"] == "easy"]
    elif level == "Moderate":
        return [ex for ex in exercises if ex["difficulty"] in ["easy", "medium"]]
    else:  # Challenging
        return exercises  # Include all difficulty levels

def get_intensity_factor(difficulty):
    """Return intensity factor based on difficulty level"""
    if difficulty == "Easy":
        return 0.8
    elif difficulty == "Moderate":
        return 1.0
    else:  # Challenging
        return 1.2

def generate_workout(selected_types, total_duration, difficulty, rep_range, time_range, rest_between_exercises):
    """Generate a personalized workout based on user preferences"""
    
    st.markdown("<h2 class='subheader-style'>Your Personalized Workout</h2>", unsafe_allow_html=True)
    
    # Calculate approximate number of exercises based on duration and rest periods
    intensity_factor = get_intensity_factor(difficulty)
    avg_exercise_time = 60  # seconds (approximation including exercise + transition)
    rest_time = rest_between_exercises * intensity_factor
    
    cycle_time = avg_exercise_time + rest_time
    total_seconds = total_duration * 60
    
    num_exercises = int(total_seconds / cycle_time)
    
    # Ensure a minimum number of exercises
    num_exercises = max(num_exercises, 5)
    
    # Calculate exercises per type
    exercises_per_type = max(1, num_exercises // len(selected_types))
    
    all_selected_exercises = []
    
    # Get exercises for each selected type
    for ex_type in selected_types:
        available_exercises = difficulty_filter(exercise_database[ex_type], difficulty)
        
        # If not enough exercises of the selected difficulty, use all available
        if len(available_exercises) < exercises_per_type:
            available_exercises = exercise_database[ex_type]
        
        # Randomly select exercises of this type
        if available_exercises:
            selected = random.sample(
                available_exercises, 
                min(exercises_per_type, len(available_exercises))
            )
            for exercise in selected:
                exercise_info = exercise.copy()
                exercise_info['type'] = ex_type
                all_selected_exercises.append(exercise_info)
    
    # Shuffle exercises to mix different types
    random.shuffle(all_selected_exercises)
    
    # Create workout plan
    workout_data = []
    
    for i, exercise in enumerate(all_selected_exercises):
        # Determine reps or time
        if exercise["time_based"]:
            # For time-based exercises
            duration = random.randint(time_range[0], time_range[1])
            reps = "N/A"
            time_display = f"{duration} seconds"
        else:
            # For rep-based exercises
            reps = random.randint(rep_range[0], rep_range[1])
            duration = "N/A"
            time_display = f"{reps} reps"
        
        workout_data.append({
            "Order": i + 1,
            "Exercise": exercise["name"],
            "Type": exercise["type"].capitalize(),
            "Description": exercise["description"],
            "Duration/Reps": time_display,
            "Rest": f"{rest_between_exercises} seconds",
            "Equipment": exercise["equipment"] if exercise["equipment"] else "None"
        })
    
    # Display workout as a table and detailed cards
    workout_df = pd.DataFrame(workout_data)
    
    # Calculate estimated workout stats
    total_exercises = len(workout_data)
    est_workout_time = total_exercises * (avg_exercise_time/60 + rest_between_exercises/60)
    
    # Display workout summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Exercises", total_exercises)
    with col2:
        st.metric("Estimated Time", f"{est_workout_time:.1f} min")
    with col3:
        st.metric("Exercise Types", len(selected_types))
    
    # Show overview table
    st.markdown("### Workout Overview")
    st.dataframe(workout_df[["Order", "Exercise", "Type", "Duration/Reps", "Equipment"]])
    
    # Show detailed exercise cards
    st.markdown("### Detailed Exercise Instructions")
    
    for i, exercise in enumerate(workout_data):
        with st.expander(f"{i+1}. {exercise['Exercise']} ({exercise['Type']})"):
            st.markdown(f"""
            * **Type:** {exercise['Type']}
            * **Duration/Reps:** {exercise['Duration/Reps']}
            * **Rest After:** {exercise['Rest']}
            * **Equipment Needed:** {exercise['Equipment']}
            
            **Instructions:**  
            {exercise['Description']}
            """)
    
    # Add download option
    csv = workout_df.to_csv(index=False)
    st.download_button(
        label="Download Workout Plan (CSV)",
        data=csv,
        file_name="my_workout_plan.csv",
        mime="text/csv",
    )
    
    # Add warmup and cooldown recommendations
    st.markdown("### Don't Forget!")
    st.info("""
    **Warm-up**: Start with 5 minutes of light cardio (marching in place, light jogging) and dynamic stretches.
    
    **Cool-down**: End with 5 minutes of static stretching, focusing on the major muscle groups you worked.
    """)

if __name__ == "__main__":
    main()