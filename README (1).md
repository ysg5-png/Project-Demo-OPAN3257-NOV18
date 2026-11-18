# Hilltop Voyages demo dashboard (Session 24 walk-through)

A stand-in dashboard for the 30-minute Streamlit demo. Simulated data only.
Teams should build on the official Canvas starter template; this app uses the same two data patterns.

- `data/revenue_by_type.csv`, `stays_by_month.csv`, `segment_vs_company.csv`: query results exported from Colab (pattern 1)
- `data/voyages_bookings.csv`, `voyages_properties.csv`: raw files read by DuckDB inside the app (pattern 2)

Run locally: `pip install -r requirements.txt` then `streamlit run app.py`
Deploy: put this folder in a GitHub repo, then share.streamlit.io > Create app > "Yup, I have an app" > repository, branch, main file `app.py` > Deploy.
