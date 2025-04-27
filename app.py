import streamlit as st

st.set_page_config(page_title="Dash Line Inserter", layout="centered")

st.title("🔹 Insert Dashed Line After N Rows")

# Input: Raw text data
raw_data = st.text_area("📋 Paste your data here (each item in a new line):", height=300)

# Input: Split interval
interval = st.selectbox("🔁 To split text after every ___ lines, choose from the dropdown and Click On Extract Data:", 
                        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], index=1)

# Button to clear spaces from the data
if st.button("🧹 Clear Spaces"):
    # Remove extra spaces (leading/trailing and between lines)
    raw_data = " ".join(raw_data.split())

    st.success("✅ Spaces cleared successfully!")
    st.text_area("📋 Pasted Data (Spaces Cleared)", value=raw_data, height=300)

# Split the text and process when the "Extract Data with Dashes" button is clicked
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
