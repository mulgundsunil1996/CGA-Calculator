# cga_calculator_ddmmyyyy.py
import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

st.set_page_config(page_title="Corrected Gestational Age (CGA) Calculator", layout="centered")

# Title
st.title("Corrected Gestational Age (CGA) Calculator")

# Inputs
dob = st.date_input("Date of Birth (DOB)")
ga_weeks = st.number_input("Gestational Age at Birth (Weeks)", min_value=20, max_value=45, value=28)
ga_days = st.number_input("Gestational Age at Birth (Days)", min_value=0, max_value=6, value=3)
current_date = st.date_input("Current Date", value=datetime.today())

# Calculate Day of Life
day_of_life = (current_date - dob).days

# Calculate Corrected GA
total_days = ga_weeks * 7 + ga_days + day_of_life
cga_weeks = total_days // 7
cga_days = total_days % 7

st.markdown("---")
st.subheader("Result")
st.write(f"**Day of Life:** {day_of_life}")
st.write(f"**Corrected GA:** {cga_weeks} weeks {cga_days} days")

# Option: Generate daily CGA table
show_table = st.checkbox("Show Daily CGA Table (Day 0 → Current Day)")
if show_table:
    data = []
    for i in range(day_of_life + 1):
        total = ga_weeks * 7 + ga_days + i
        weeks = total // 7
        days = total % 7
        date = dob + timedelta(days=i)
        data.append({"Day": i, "Date": date.strftime("%d/%m/%Y"), "CGA Weeks": weeks, "CGA Days": days})
    
    df = pd.DataFrame(data)
    st.dataframe(df)
    
    # Option to download table
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "CGA_table.csv", "text/csv")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Created by Dr. Sunil Mulgund</p>", unsafe_allow_html=True)
