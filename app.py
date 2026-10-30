import streamlit as st
import pandas as pd
import joblib

# Website er Title ebong Design
st.set_page_config(page_title="FPL AI Predictor", page_icon="⚽", layout="centered")
st.title("⚽ Fantasy Premier League - AI Predictor")
st.write("Apnar player-er data din ebong AI diye tar Total Points predict korun!")

# Model load kora (Ensure kora j file ta eki folder e ache)
try:
    model = joblib.load('fpl_point_predictor.pkl')
except:
    st.error("Model file 'fpl_point_predictor.pkl' khuje pawa jacche na! File-ti eki folder-e rakhun.")

st.markdown("---")

# User er kach theke Data neyar jonno form toiri
st.subheader("Player er Match Data Din:")
col1, col2 = st.columns(2)

with col1:
    minutes = st.number_input("Minutes Played", min_value=0, max_value=90, value=90)
    goals_scored = st.number_input("Goals Scored", min_value=0, max_value=10, value=0)
    assists = st.number_input("Assists", min_value=0, max_value=10, value=0)
    value = st.number_input("Player Value (eg. 85 for 8.5m)", min_value=30, max_value=150, value=50)

with col2:
    clean_sheets = st.selectbox("Clean Sheet?", options=[0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    goals_conceded = st.number_input("Goals Conceded", min_value=0, max_value=10, value=0)
    yellow_cards = st.number_input("Yellow Cards", min_value=0, max_value=2, value=0)
    was_home = st.selectbox("Home Match?", options=[0, 1], format_func=lambda x: "Home" if x==1 else "Away")

# Predict Button
if st.button("Predict Points 🚀"):
    # User input theke DataFrame toiri kora
    input_data = pd.DataFrame({
        'minutes': [minutes],
        'goals_scored': [goals_scored],
        'assists': [assists],
        'clean_sheets': [clean_sheets],
        'goals_conceded': [goals_conceded],
        'yellow_cards': [yellow_cards],
        'value': [value],
        'was_home': [was_home]
    })
    
    # Prediction kora
    prediction = model.predict(input_data)[0]
    
    # Result dekhano
    st.success(f"### Predicted Total Points: {prediction:.2f} 🔥")