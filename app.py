import streamlit as st

st.set_page_config(page_title="Dash Line Inserter", layout="centered")

st.title("🔹 Insert Dashed Line After N Rows")

# Input: Raw text data
raw_data = st.text_area("📋 Paste your data here (each item in a new line):", height=300)

# Input: Split interval
interval = st.selectbox("🔁 Insert dashed line after every N rows:", [3, 4, 5, 6, 8, 15], index=1)

# Split the text and process
if st.button("🚀 Extract Data with Dashes"):
    lines = raw_data.strip().splitlines()
    output = []

    for i, line in enumerate(lines, 1):
        output.append(line)
        if i % interval == 0:
            output.append('------------------------------------------------------------')

    final_text = "\n".join(output)

    st.success("✅ Dash lines inserted successfully!")
    st.code(final_text, language="text")

    # Add download as .txt option
    st.download_button(
        label="⬇️ Download Output as TXT",
        data=final_text,
        file_name="dashed_output.txt",
        mime="text/plain"
    )
