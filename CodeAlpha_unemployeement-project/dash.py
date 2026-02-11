import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load cleaned data
# -----------------------------
df = pd.read_csv("Unemployment_cleaned.csv")
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# App title
# -----------------------------
st.title("📊 Unemployment Analysis in India")
st.write("Interactive dashboard based on cleaned unemployment data")

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filter Options")

regions = st.sidebar.multiselect(
    "Select Region(s)",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

areas = st.sidebar.multiselect(
    "Select Area",
    options=df["Area"].unique(),
    default=df["Area"].unique()
)

df_f = df[(df["Region"].isin(regions)) & (df["Area"].isin(areas))]

# -----------------------------
# 1️⃣ Average Unemployment Trend
# -----------------------------
st.subheader("📈 Average Unemployment Rate Over Time")

avg_unemp = (
    df_f.groupby("Date")["Estimated Unemployment Rate (%)"]
        .mean()
        .reset_index()
)

fig1, ax1 = plt.subplots(figsize=(10,4))
ax1.plot(avg_unemp["Date"], avg_unemp["Estimated Unemployment Rate (%)"], linewidth=2)
ax1.set_xlabel("Date")
ax1.set_ylabel("Unemployment Rate (%)")
ax1.set_title("Average Unemployment Rate in India")
ax1.grid(alpha=0.3)
st.pyplot(fig1)

# -----------------------------
# 2️⃣ Covid-19 Impact
# -----------------------------
st.subheader("🦠 Covid-19 Impact on Unemployment")

before_covid = avg_unemp[avg_unemp["Date"] < "2020-03-01"]
after_covid  = avg_unemp[avg_unemp["Date"] >= "2020-03-01"]

st.metric(
    "Before Covid (Avg)",
    round(before_covid["Estimated Unemployment Rate (%)"].mean(), 2)
)
st.metric(
    "During Covid (Avg)",
    round(after_covid["Estimated Unemployment Rate (%)"].mean(), 2)
)

fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(before_covid["Date"], before_covid["Estimated Unemployment Rate (%)"], label="Before Covid")
ax2.plot(after_covid["Date"], after_covid["Estimated Unemployment Rate (%)"], label="During Covid")
ax2.legend()
ax2.set_title("Impact of Covid-19 on Unemployment")
ax2.grid(alpha=0.3)
st.pyplot(fig2)

# -----------------------------
# 3️⃣ Region-wise Analysis
# -----------------------------
st.subheader("🌍 Region-wise Average Unemployment Rate")

region_avg = (
    df_f.groupby("Region")["Estimated Unemployment Rate (%)"]
        .mean()
        .sort_values(ascending=False)
)

fig3, ax3 = plt.subplots(figsize=(8,4))
region_avg.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Unemployment Rate (%)")
ax3.set_title("Average Unemployment Rate by Region")
st.pyplot(fig3)

# -----------------------------
# 4️⃣ Seasonal Trend
# -----------------------------
st.subheader("📅 Seasonal (Monthly) Unemployment Trend")

df_f["Month"] = df_f["Date"].dt.month
monthly_avg = df_f.groupby("Month")["Estimated Unemployment Rate (%)"].mean()

fig4, ax4 = plt.subplots(figsize=(8,4))
monthly_avg.plot(ax=ax4)
ax4.set_xlabel("Month")
ax4.set_ylabel("Unemployment Rate (%)")
ax4.set_title("Seasonal Trend in Unemployment")
ax4.grid(alpha=0.3)
st.pyplot(fig4)

# -----------------------------
st.success("✅ Dashboard loaded using cleaned data")
