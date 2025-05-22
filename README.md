# 💪 Workout Generator

Streamlit app that generates personalized home workout routines based on your preferences and fitness goals!

## ✨ Features

- 🎯 **5 Exercise Types**: Cardio, Balance, Strength, Flexibility, and Stamina
- ⚙️ **Customizable Settings**: Duration, difficulty, reps, and rest periods
- 🎲 **Smart Generation**: Randomly creates balanced workouts from extensive exercise database
- 📊 **Detailed Instructions**: Step-by-step exercise descriptions and equipment requirements
- 📈 **Progress Tracking**: Estimated workout time and exercise metrics
- 📄 **Downloadable Plans**: Export your workout as CSV for offline use
- 🎨 **Beautiful UI**: Clean, responsive design with custom styling

## 🚀 Quick Start

### Prerequisites
```bash
pip install streamlit pandas
```

### Installation & Run
1. 📥 Clone this repository:
   ```bash
   git clone https://github.com/qusai-Kagalwala/workout-generator.git
   cd workout-generator
   ```

2. 🌐 Run the Streamlit app:
   ```bash
   streamlit run workout_generator.py
   ```

3. 📱 Open your browser to `http://localhost:8501`

## 🏋️‍♀️ How to Use

### Step 1: Choose Exercise Types
Select from these categories based on your fitness goals:
- **💓 Cardio**: Heart health and calorie burning
- **⚖️ Balance**: Stability and core strength  
- **💪 Strength**: Muscle building and metabolism
- **🤸 Flexibility**: Range of motion and injury prevention
- **🔥 Stamina**: Endurance and mental toughness

### Step 2: Set Your Preferences
- ⏱️ **Duration**: 5-60 minutes
- 🎚️ **Difficulty**: Easy, Moderate, or Challenging
- 🔢 **Repetitions**: Customize rep ranges for strength exercises
- ⏰ **Timing**: Set duration ranges for timed exercises
- 😴 **Rest**: Adjust rest periods between exercises

### Step 3: Generate & Follow
- 🎯 Click "Generate Workout" to create your routine
- 📋 Review the workout overview table
- 📖 Follow detailed exercise instructions
- 📥 Download your plan for offline use

## 🎯 Exercise Database

The app includes **30+ exercises** across all categories:

### 💓 Cardio (7 exercises)
- Jumping Jacks, High Knees, Burpees, Mountain Climbers, and more

### ⚖️ Balance (5 exercises)  
- Single Leg Stand, Tree Pose, Warrior III, Standing Figure Four, and more

### 💪 Strength (9 exercises)
- Push-ups, Squats, Lunges, Plank, Tricep Dips, and more

### 🤸 Flexibility (7 exercises)
- Hamstring Stretch, Child's Pose, Cobra Stretch, Butterfly Stretch, and more

### 🔥 Stamina (6 exercises)
- Tabata Sequence, Jump Squats, Plank Jacks, Bear Crawls, and more

## ⚙️ Smart Features

### 🎲 Intelligent Generation
- Automatically balances exercise types based on your selections
- Filters exercises by difficulty level
- Randomizes order to keep workouts fresh
- Calculates optimal number of exercises for your time limit

### 📊 Workout Analytics
- **Exercise Count**: Total number of exercises in your routine
- **Estimated Time**: Calculated workout duration including rest
- **Type Distribution**: Visual breakdown of exercise categories
- **Equipment Tracking**: Lists all equipment needed

### 📱 User Experience
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Custom Styling**: Beautiful CSS styling for better UX
- **Interactive Sidebar**: Easy-to-use controls and settings
- **Expandable Cards**: Detailed exercise instructions on demand

## 🛠️ Technical Details

### Built With
- **Frontend**: Streamlit
- **Data Handling**: Pandas
- **Styling**: Custom CSS
- **Logic**: Python 3.x

### Project Structure
```
workout-generator/
├── workout_generator.py    # Main application file
├── README.md              # This file
└── requirements.txt       # Dependencies (optional)
```

### Key Components
- **Exercise Database**: Structured dictionary with detailed exercise info
- **Filtering System**: Difficulty-based exercise selection
- **Generation Algorithm**: Smart workout creation logic
- **Export Feature**: CSV download functionality

## 🎨 Customization

Want to add your own exercises? Edit the `exercise_database` dictionary:

```python
"your_category": [
    {
        "name": "Exercise Name",
        "description": "How to perform the exercise",
        "difficulty": "easy/medium/hard",
        "equipment": "Equipment needed or None",
        "time_based": True/False
    }
]
```

## 💡 Tips for Best Results

- 🎯 **Mix Categories**: Combine different exercise types for balanced fitness
- 📈 **Progress Gradually**: Start with easier difficulties and work up
- ⏰ **Be Realistic**: Choose durations that fit your schedule
- 🔄 **Stay Consistent**: Generate new workouts regularly to avoid plateaus
- 💧 **Stay Hydrated**: Keep water nearby during your workout

## 🤝 Contributing

Contributions are welcome! Here are some ideas:
- 🏃‍♀️ Add new exercise categories (HIIT, Yoga, Pilates)
- 🎵 Integrate music or timer features
- 📱 Add mobile app version
- 🏆 Implement progress tracking and achievements
- 🤖 Add AI-powered workout recommendations

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Qusai Kagalwala**
- GitHub: [@qusai-Kagalwala](https://github.com/qusai-Kagalwala)

---

💪 **Ready to get fit? Generate your first workout now!** 💪
