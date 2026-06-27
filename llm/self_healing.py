from llm.sql_generator import generate_sql

def fix_query(user_query, schema, error):
    prompt = f"""
The following SQL query failed.

Error:
{error}

Fix the query.

User request:
{user_query}

Schema:
{schema}

Return ONLY the corrected SQL.
"""

    return generate_sql(prompt, schema)