import streamlit as st

st.title("💰 Budget Estimation")

if 'selected_crop' not in st.session_state:
    st.warning("No crop selected. Please go back to Suggestions page")
    st.stop()

cost_data = {
    "Paddy": {
        "operational": 31800,
        "fertilizer": 4540,
        "fixed": 10540,
        "yield_per_acre": 2135,  # kg/acre
        "price_per_kg": 25        # Increased from ₹20 to ₹25 (+25%)
    },
    "Cholam (Jowar)": {
        "operational": 12000,
        "fertilizer": 2000,
        "fixed": 4000,
        "yield_per_acre": 1124,   # kg/acre
        "price_per_kg": 18        # Increased from ₹15 to ₹18 (+20%)
    },
    "Cumbu (Bajra)": {
        "operational": 10000,
        "fertilizer": 1800,
        "fixed": 3500,
        "yield_per_acre": 1275,   # kg/acre
        "price_per_kg": 16        # Increased from ₹14 to ₹16 (+14%)
    },
    "Ragi": {
        "operational": 11500,
        "fertilizer": 2200,
        "fixed": 3800,
        "yield_per_acre": 1630,   # kg/acre
        "price_per_kg": 22        # Increased from ₹20 to ₹22 (+10%)
    },
    "Maize": {
        "operational": 24923,
        "fertilizer": 3673,
        "fixed": 7290,
        "yield_per_acre": 2044,   # kg/acre
        "price_per_kg": 21        # Increased from ₹18 to ₹21 (+17%)
    },
    "Sugarcane": {
        "operational": 28500,
        "fertilizer": 5000,
        "fixed": 9500,
        "yield_per_acre": 80000,  # kg/acre
        "price_per_kg": 1.65      # Increased from ₹1.45 to ₹1.65 (+14%)
    },
    "Black gram": {
        "operational": 9000,
        "fertilizer": 1500,
        "fixed": 3000,
        "yield_per_acre": 592,    # kg/acre
        "price_per_kg": 55        # Increased from ₹50 to ₹55 (+10%)
    },
    "Groundnut": {
        "operational": 12500,
        "fertilizer": 2500,
        "fixed": 4200,
        "yield_per_acre": 1809,   # kg/acre
        "price_per_kg": 35        # Increased from ₹30 to ₹35 (+17%)
    },
    "Green gram": {
        "operational": 9500,
        "fertilizer": 1800,
        "fixed": 3500,
        "yield_per_acre": 743,    # kg/acre
        "price_per_kg": 55        # Increased from ₹50 to ₹55 (+10%)
    },
    "Red gram": {
        "operational": 10500,
        "fertilizer": 2300,
        "fixed": 4000,
        "yield_per_acre": 538,    # kg/acre
        "price_per_kg": 85        # Increased from ₹80 to ₹85 (+6%)
    },
    "Horse gram": {
        "operational": 8700,
        "fertilizer": 1700,
        "fixed": 3200,
        "yield_per_acre": 488,    # kg/acre
        "price_per_kg": 55        # Increased from ₹50 to ₹55 (+10%)
    },
    "Bengal gram": {
        "operational": 10800,
        "fertilizer": 2100,
        "fixed": 3800,
        "yield_per_acre": 595,    # kg/acre
        "price_per_kg": 65        # Increased from ₹60 to ₹65 (+8%)
    },
    "Cotton": {
        "operational": 20000,
        "fertilizer": 4500,
        "fixed": 6000,
        "yield_per_acre": 500,    # kg/acre
        "price_per_kg": 95        # Increased from ₹90 to ₹95 (+6%)
    }
}

crop = st.session_state.selected_crop
area = st.session_state.form_inputs['area']

if crop not in cost_data:
    st.error(f"No budget data available for {crop}")
    st.stop()

data = cost_data[crop]

# Calculate totals
total_cost = (data['operational'] + data['fertilizer'] + data['fixed']) * area
total_revenue = data['yield_per_acre'] * area * data['price_per_kg']
profit = total_revenue - total_cost

# Display results
st.subheader(f"Budget for {crop} ({area} acres)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Costs (₹)")
    st.metric("Operational Costs", f"₹{data['operational'] * area:,.0f}")
    st.metric("Fertilizer Costs", f"₹{data['fertilizer'] * area:,.0f}")
    st.metric("Fixed Costs", f"₹{data['fixed'] * area:,.0f}")
    st.metric("**Total Costs**", f"₹{total_cost:,.0f}", delta_color="inverse")

with col2:
    st.markdown("### Revenue & Profit")
    st.metric("Expected Yield", f"{data['yield_per_acre'] * area:,.0f} kg")
    st.metric("Market Price", f"₹{data['price_per_kg']}/kg")
    st.metric("**Total Revenue**", f"₹{total_revenue:,.0f}")
    st.metric("**Estimated Profit**", f"₹{profit:,.0f}", 
              delta_color="off" if profit == 0 else "normal")

if st.button("← Back to Recommendations"):
    st.switch_page("pages/2_🌱_Suggestions.py")
