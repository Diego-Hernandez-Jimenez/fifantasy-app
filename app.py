import duckdb
import streamlit as st

@st.cache_resource
def get_duckdb_memory():
    return duckdb.connect("data/fc_players_out.duckdb")

conn = get_duckdb_memory()

st.title("FIFAntasy 11")
st.subheader("Optimize your team")

#################### USER INPUT ####################

user_final_query = """
    SELECT *
    FROM dim_sofifa__players_enriched
"""

#################### SELECT DATA ####################
filtered_df = conn.sql(user_final_query).df()



#################### BUILD AND RUN OPTIMIZATION MODEL ####################


#################### EXTRACT RESULTS ####################


#################### DISPLAY OUTPUT TO USER ####################
st.dataframe(filtered_df)

