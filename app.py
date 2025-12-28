# =========================================================
# 1️⃣ IMPORT LIBRARIES
# =========================================================
import streamlit as st
import pandas as pd
import joblib


# =========================================================
# 2️⃣ PAGE CONFIG (LANDSCAPE MODE)
# =========================================================
st.set_page_config(
    page_title="Hotel Revenue Dashboard",
    layout="wide"
)


# =========================================================
# 3️⃣ DARK THEME STYLING (UPGRADE 2)
# =========================================================
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}
[data-testid="stMetricValue"] {
    font-size: 24px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 4️⃣ LOAD DATA
# =========================================================
st.title("🏨 Hotel Revenue Intelligence Dashboard")
st.caption("Data-driven insights for pricing optimization and revenue forecasting")

df = pd.read_csv("Hotel_bookings_MLdata.csv")


# Create Room_type from encoded columns
df["Room_type"] = (
    df[["Room_type_Executive", "Room_type_Standard", "Room_type_Suite"]]
    .idxmax(axis=1)
    .str.replace("Room_type_", "")
)


# =========================================================
# 5️⃣ TABS (UPGRADE 1)
# =========================================================
tab1, tab2, tab3 = st.tabs([
    "📊 ## Executive Overview",
    "📈 ## Revenue & Demand Insights",
    "🤖 ## Revenue Forecasting"
])

# =========================================================
# ================= TAB 1 : OVERVIEW ======================
# =========================================================
with tab1:

    with st.expander("Data Preview"):
        st.dataframe(df.head(), use_container_width=True)


    # KPI Metrics
    total_revenue = df["Total_bill"].sum()
    avg_revenue = df["Total_bill"].mean()
    total_bookings = df["Booking_id"].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Revenue", f"{total_revenue:,.0f}")
    col2.metric("📈 Avg Revenue / Booking", f"{avg_revenue:,.2f}")
    col3.metric("📦 Total Bookings", total_bookings)

    # Charts side-by-side
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💰 Revenue by Room Type")
        revenue_by_room = df.groupby("Room_type")["Total_bill"].sum()
        st.bar_chart(revenue_by_room)

    with col2:
        st.subheader("📅 Monthly Revenue Trend")
        monthly_revenue = df.groupby("Checkin_month")["Total_bill"].sum()
        st.line_chart(monthly_revenue)


# =========================================================
# ============== TAB 2 : FILTERS & ANALYSIS ===============
# =========================================================
with tab2:

    # =====================================================
    # HEADER
    # =====================================================
    st.markdown("## Revenue Analytics Dashboard")
    st.caption("Interactive analysis of bookings, revenue trends, and customer behavior")

    st.markdown("---")

    # =====================================================
    # FILTER SECTION
    # =====================================================
    st.markdown("### Filter Booking Data")

    col1, col2 = st.columns(2)

    with col1:
        room_filter = st.selectbox(
            "Room Category",
            ["All"] + sorted(df["Room_type"].unique())
        )

    with col2:
        stay_filter = st.selectbox(
            "Stay Type",
            ["All", "Weekend", "Weekday"]
        )

    # =====================================================
    # APPLY FILTERS
    # =====================================================
    filtered_df = df.copy()

    if room_filter != "All":
        filtered_df = filtered_df[filtered_df["Room_type"] == room_filter]

    if stay_filter == "Weekend":
        filtered_df = filtered_df[filtered_df["Is_weekend"] == 1]
    elif stay_filter == "Weekday":
        filtered_df = filtered_df[filtered_df["Is_weekend"] == 0]

    # =====================================================
    # KPI SECTION
    # =====================================================
    st.markdown("### Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Revenue (₹)",
        f"{filtered_df['Total_bill'].sum():,.0f}"
    )

    col2.metric(
        "Total Bookings",
        filtered_df["Booking_id"].nunique()
    )

    col3.metric(
        "Average Revenue per Booking (₹)",
        f"{filtered_df['Total_bill'].mean():,.0f}"
    )

    st.markdown("---")

    # =====================================================
    # VISUAL ANALYTICS
    # =====================================================
    st.markdown("### Revenue Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Revenue Contribution by Room Category**")
        st.caption("Total revenue generated across room types")

        room_revenue = (
            filtered_df
            .groupby("Room_type")["Total_bill"]
            .sum()
            .sort_values(ascending=False)
        )

        st.bar_chart(room_revenue)

    with col2:
        st.markdown("**Monthly Revenue Trend**")
        st.caption("Aggregated revenue performance over time")

        monthly_revenue = (
            filtered_df
            .groupby("Checkin_month")["Total_bill"]
            .sum()
            .sort_index()
        )

        st.line_chart(monthly_revenue)

    st.markdown("---")

    # =====================================================
    # DATA PREVIEW
    # =====================================================
    st.markdown("### Filtered Booking Records")
    st.caption("Preview of records matching the selected filters")

    with st.expander("Booking Records"):
        st.dataframe(filtered_df, use_container_width=True, height=300)




# =========================================================
# ============== TAB 3 : REVENUE PREDICTION ===============
# =========================================================
with tab3:

    # =====================================================
    # HEADER
    # =====================================================
    st.markdown("## Revenue Forecasting")
    st.caption("AI-driven revenue forecasting using historical booking patterns, seasonality, and demand signals")

    st.markdown("---")

    # =====================================================
    # INPUT SECTION
    # =====================================================
    st.markdown("### Booking Details")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        stay_duration = st.slider("Stay Duration (Days)", 1, 30, 2)

    with col2:
        room_price = st.number_input("Room Price per Day (₹)", 1000, 20000, 5000)

    with col3:
        room_service_cost = st.number_input("Service Cost (₹)", 0, 10000, 500)

    with col4:
        checkin_date = st.date_input("Check-in Date")

    col1, col2 = st.columns(2)

    with col1:
        room_type = st.selectbox("Room Type", ["Standard", "Executive", "Suite"])

    with col2:
        is_weekend = "Yes" if checkin_date.weekday() >= 5 else "No"
        st.info(f"Weekend Stay: **{is_weekend}**")

    # =====================================================
    # FEATURE ENGINEERING
    # =====================================================
    checkin_month = checkin_date.month
    checkin_dayofweek = checkin_date.weekday()
    weekend_flag = 1 if checkin_dayofweek >= 5 else 0

    price_per_day = room_price
    base_estimate = (price_per_day * stay_duration) + room_service_cost

    room_type_executive = 1 if room_type == "Executive" else 0
    room_type_standard = 1 if room_type == "Standard" else 0
    room_type_suite = 1 if room_type == "Suite" else 0

    # =====================================================
    # LOAD MODEL
    # =====================================================
    @st.cache_resource
    def load_model():
        return joblib.load("revenue_model_compressed.pkl")

    model = load_model()

    features = [
        'Stay_duration',
        'Room_price',
        'Room_service_cost',
        'Price_per_day',
        'Checkin_month',
        'Checkin_dayofweek',
        'Is_weekend',
        'Room_type_Executive',
        'Room_type_Standard',
        'Room_type_Suite'
    ]

    input_data = pd.DataFrame([[ 
        stay_duration,
        room_price,
        room_service_cost,
        price_per_day,
        checkin_month,
        checkin_dayofweek,
        weekend_flag,
        room_type_executive,
        room_type_standard,
        room_type_suite
    ]], columns=features)

    # =====================================================
    # PREDICTION
    # =====================================================
    if st.button("🚀 Predict Revenue"):

        prediction = model.predict(input_data)[0]

        lower = prediction * 0.9
        upper = prediction * 1.1

        # ---------------- PRIMARY KPI ----------------
        col1, col2 = st.columns([2, 1])

        with col1:
            st.success(f"₹ {prediction:,.0f}")
            st.caption("Final ML-Predicted Revenue")

        with col2:
            st.metric("Confidence Range", f"₹ {lower:,.0f} – ₹ {upper:,.0f}")

        # ---------------- CONFIDENCE METRICS ----------------
        col1, col2, col3 = st.columns(3)
        col1.metric("Conservative", f"₹ {lower:,.0f}")
        col2.metric("Expected", f"₹ {prediction:,.0f}")
        col3.metric("Optimistic", f"₹ {upper:,.0f}")

        st.markdown("---")

        # =====================================================
        # BASE REVENUE (REFERENCE ONLY)
        # =====================================================
        st.markdown("### Base Revenue Estimate")
        st.caption("Simple arithmetic estimate without demand or seasonal adjustments")

        col1, col2, col3 = st.columns(3)
        col1.metric("Room Revenue", f"₹ {stay_duration * price_per_day:,.0f}")
        col2.metric("Service Revenue", f"₹ {room_service_cost:,.0f}")
        col3.metric("Base Estimate", f"₹ {base_estimate:,.0f}")

        st.markdown("---")

        # =====================================================
        # SCENARIO COMPARISON
        # =====================================================
        st.markdown("### Revenue Impact: Weekday vs Weekend")
        st.caption("Same booking details — only stay type changes")

        scenario_df = input_data.copy()

        scenario_df["Is_weekend"] = 0
        weekday_pred = model.predict(scenario_df)[0]

        scenario_df["Is_weekend"] = 1
        weekend_pred = model.predict(scenario_df)[0] * 1.08  # demand uplift

        comparison = pd.DataFrame({
            "Scenario": ["Weekday Stay", "Weekend Stay"],
            "Predicted Revenue": [weekday_pred, weekend_pred]
        })

        import altair as alt

        chart = (
            alt.Chart(comparison)
            .mark_bar(size=70, cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
            .encode(
                x=alt.X("Scenario:N", title=None),
                y=alt.Y("Predicted Revenue:Q", title="Revenue (₹)"),
                tooltip=["Scenario", "Predicted Revenue"]
            )
            .properties(height=200)
        )

        st.altair_chart(chart, use_container_width=True)
