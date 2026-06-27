import streamlit as st
from utils.db import run_query
from llm.sql_generator import generate_sql
from llm.self_healing import fix_query

# Cargar schema
with open("database/schema.sql", "r") as f:
    schema = f.read()

st.title("🧠 SQL Query Genie")

user_input = st.text_input("Ask your database:")

if st.button("Generate Query"):

    sql_query = generate_sql(user_input, schema)

    st.subheader("Generated SQL")
    st.code(sql_query, language="sql")

    results, error = run_query(sql_query)

    if error:
        st.error(f"Error: {error}")

        st.info("Attempting to fix query...")

        fixed_query = fix_query(user_input, schema, error)

        st.subheader("Fixed Query")
        st.code(fixed_query, language="sql")

        results, error = run_query(fixed_query)

    if results:
        st.subheader("Results")
        st.write(results)