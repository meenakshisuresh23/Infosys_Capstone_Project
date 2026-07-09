import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["AQ.Ab8RN6J2-WCaqdurN3kUbMgKpz1PFVxNH_WUqu_j0doEjALk_g"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Learning Buddy Meenu",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy Meenu")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        else:
            prompt = topic

        with st.spinner("Generating..."):
            response = model.generate_content(prompt)

        st.write(response.text)
