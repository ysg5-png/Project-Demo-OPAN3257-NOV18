import duckdb
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Hilltop Voyages - Stays Dashboard", layout="wide")
st.title("Hilltop Voyages: where the stay revenue comes from")
st.caption("Simulated data. Every number below comes from a query in our Colab notebook.")


@st.cache_data
def load(name):
    return pd.read_csv(f"data/{name}.csv")


revenue = load("revenue_by_type")          # pattern 1: a CSV exported from Colab
months = load("stays_by_month")
segments = load("segment_vs_company")

# pattern 2: run the SQL right here with DuckDB, straight over the raw CSV files
check = duckdb.sql("""
    SELECT COUNT(*) AS stays, ROUND(SUM(b.total), 2) AS revenue
    FROM 'data/voyages_bookings.csv' b
    JOIN 'data/voyages_properties.csv' p ON p.property_id = b.property_id
    WHERE b.status = 'completed'
""").df().iloc[0]

c1, c2, c3 = st.columns(3)
c1.metric("Completed stays", f"{int(check['stays']):,}")
c2.metric("Stay revenue", f"${check['revenue']:,.0f}")
c3.metric("Company average stay", f"${segments['company_avg'].iloc[0]:,.2f}")

left, right = st.columns(2)
with left:
    st.subheader("Revenue by property type")
    st.bar_chart(revenue, x="property_type", y="revenue")
with right:
    st.subheader("Completed stays by check-in month")
    st.line_chart(months, x="month", y="stays")

st.subheader("Average stay by segment (company average = $771.81)")
st.bar_chart(segments, x="segment", y="avg_stay")

st.header("Recommendations")
st.markdown(
    """
1. **Protect Hotels first.** They bring most of the completed stay revenue, so a hotel
   rate or availability problem costs more than anything else.
2. **Target Family and Retiree travelers.** Their average stay beats the company average
   by wide margins.
3. **Lift Business spend.** Business has the most stays but the lowest average stay.
"""
)
