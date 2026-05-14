import streamlit as st

st.set_page_config(page_title="College Chatbot")

st.title("🎓 College Query Chatbot")

# Chat history store karne ke liye
if "messages" not in st.session_state:
    st.session_state.messages = []

# Old messages show karne ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask your question")

# Chatbot response function
def chatbot_response(question):

    question = question.lower()

    if "fees" in question:
        return "BTech fees is around ₹80,000 per year."

    elif "timing" in question or "college time" in question:
        return "College timing is 9 AM to 4 PM."

    elif "placement" in question:
        return "Average placement package is around 4 LPA."

    elif "branches" in question:
        return "Available branches are CSE, AIML, ECE, Civil, Mechanical."

    elif "faculty" in question:
        return "Faculty members are highly experienced."

    elif "hostel" in question:
        return "Hostel facility is available for both boys and girls."

    elif "library" in question:
        return "Library is open from 8 AM to 8 PM."

    elif "exam" in question:
        return "Semester exams are conducted twice a year."

    elif "scholarship" in question:
        return "Scholarships are available based on merit and category."

    elif "canteen" in question:
        return "College canteen provides affordable breakfast, lunch, and snacks."

    elif "transport" in question or "bus" in question:
        return "Bus and transport facilities are available in nearby areas."

    elif "labs" in question:
        return "Modern computer and science labs are available for students."

    elif "attendance" in question:
        return "Minimum 75% attendance is required."

    elif "admission" in question:
        return "Admissions are based on entrance exam and counseling process."

    elif "sports" in question:
        return "Sports facilities include cricket, football, badminton, and indoor games."

    elif "wifi" in question:
        return "Free WiFi facility is available across the campus."

    else:
        return "Sorry, I don't understand your question."

# User message process
if user_input:

    # User message save
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # User message display
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    response = chatbot_response(user_input)

    # Bot response save
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    # Bot response display
    with st.chat_message("assistant"):
        st.markdown(response)