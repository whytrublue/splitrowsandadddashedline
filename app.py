import streamlit as st

st.set_page_config(page_title="Dash Line Inserter", layout="centered")

st.title("🔹 Insert Dashed Line After N Rows")

# Input: Raw text data
raw_data = st.text_area("📋 Paste your data here (each item in a new line):", height=300)

# Input: Split interval
interval = st.selectbox("🔁 To split text after every ___ lines, choose from the dropdown and Click On Extract Data:", 
                        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], index=1)

# Create a placeholder for cleaning the data and update as soon as the raw data changes
if "cleaned_data" not in st.session_state:
    st.session_state.cleaned_data = raw_data

# Button to clear spaces from the data with the additional instruction
st.write("❗ Double click the 'Clear Spaces' button every time a New Data is Pasted.")
if st.button("🧹 Clear Spaces"):
    # Clean the raw_data and remove empty lines
    st.session_state.cleaned_data = "\n".join([line.strip() for line in raw_data.splitlines() if line.strip()])
    
    # Show confirmation that spaces were cleared
    st.success("✅ Spaces cleared successfully!")

# Use cleaned data if it exists, otherwise fall back to the original raw_data
data_to_process = st.session_state.cleaned_data if st.session_state.cleaned_data else raw_data

# Split the text and process when the "Extract Data with Dashes" button is clicked
if st.button("🚀 Extract Data with Dashes"):
    lines = data_to_process.strip().splitlines()
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
