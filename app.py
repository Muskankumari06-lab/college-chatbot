import streamlit as st
import time
from datetime import datetime

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="AI College Assistant",
    page_icon="🎓",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #0b3d91;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 25px;
}

.stChatMessage {
    border-radius: 15px;
    padding: 12px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER SECTION
# =========================

st.markdown(
    '<div class="title">🎓 AI College Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Professional AI-Powered Chatbot for Student Support Services</div>',
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("📌 About Project")

st.sidebar.info(
    "This AI-powered chatbot helps students get instant answers related to admissions, placements, hostel, attendance, transport, scholarships, labs, and campus facilities."
)

st.sidebar.title("🛠 Technologies Used")
st.sidebar.write("✔ Python")
st.sidebar.write("✔ Streamlit")
st.sidebar.write("✔ OOP Concepts")
st.sidebar.write("✔ NLP-Based Logic")
st.sidebar.write("✔ Session State Management")

st.sidebar.title("✨ Features")
st.sidebar.write("✔ Interactive Chat UI")
st.sidebar.write("✔ Real-Time Responses")
st.sidebar.write("✔ Smart Keyword Detection")
st.sidebar.write("✔ Chat History")
st.sidebar.write("✔ Professional Dashboard")

st.sidebar.title("👩‍💻 Developer")
st.sidebar.success("Muskan Kumari")

# =========================
# OOP CONCEPT
# =========================

class CollegeChatbot:

    def __init__(self):

        self.responses = {

            "fees":
            "💰 The annual BTech tuition fee is approximately ₹80,000. Additional charges for hostel, examination, and transportation may apply separately. Students can also apply for scholarship programs based on merit and category.",

            "placement":
            "📈 The college has a dedicated Training and Placement Cell that organizes campus drives, mock interviews, coding sessions, and aptitude training. The average package is around 4 LPA, while the highest package reached 12 LPA last year.",

            "hostel":
            "🏠 Hostel facilities are available for both boys and girls with 24/7 security, WiFi, clean rooms, mess facilities, and study areas. Rooms are available on a sharing basis.",

            "library":
            "📚 The central library contains thousands of academic books, journals, research papers, and digital learning resources. It remains open from 8 AM to 8 PM on working days.",

            "transport":
            "🚌 The college provides transport facilities covering nearby city areas. Students can register for bus services during the admission process.",

            "attendance":
            "📌 Students must maintain at least 75% attendance to appear in semester examinations as per academic guidelines.",

            "faculty":
            "👨‍🏫 The college faculty includes experienced professors, assistant professors, and industry experts who guide students in academics, projects, and placements.",

            "canteen":
            "🍔 The college canteen offers hygienic and affordable food items including breakfast, lunch, snacks, and beverages.",

            "wifi":
            "📶 Free high-speed WiFi is available across classrooms, labs, library, and hostel areas.",

            "sports":
            "⚽ Sports facilities include cricket, football, volleyball, badminton, indoor games, and annual sports competitions.",

            "labs":
            "💻 The college has modern computer labs, AI labs, IoT labs, and electronics laboratories equipped with updated systems and software tools.",

            "admission":
            "📋 Admissions are conducted through entrance exams and counseling procedures. Students need to submit academic documents during verification.",

            "scholarship":
            "🎓 Scholarships are provided for meritorious students, reserved categories, and economically weaker sections according to government norms.",

            "exam":
            "📝 Semester examinations are conducted twice every academic year. Internal assessments, assignments, and practical exams are also included in evaluation.",

            "training":
            "🧠 The Training Cell conducts coding classes, aptitude preparation, soft skill development, communication training, and interview preparation sessions.",

            "internship":
            "💼 Internship opportunities are provided through industry collaborations and placement partnerships to help students gain practical experience."
        }

    # =========================
    # RESPONSE FUNCTION
    # =========================

    def generate_response(self, user_query):

        user_query = user_query.lower()

        for keyword in self.responses:

            if keyword in user_query:
                return self.responses[keyword]

        if "hello" in user_query or "hi" in user_query:
            return "👋 Hello! Welcome to the AI College Assistant. How may I help you today?"

        elif "thank" in user_query:
            return "😊 You're welcome! Feel free to ask more college-related questions."

        else:
            return "❌ Sorry, I could not understand your query. Please ask questions related to fees, placements, hostel, transport, scholarship, or college facilities."

# =========================
# CHATBOT OBJECT
# =========================

bot = CollegeChatbot()

# =========================
# SESSION STATE
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# DISPLAY OLD CHATS
# =========================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================
# USER INPUT
# =========================

user_input = st.chat_input("Ask your question here...")

# =========================
# PROCESS USER MESSAGE
# =========================

if user_input:

    current_time = datetime.now().strftime("%H:%M")

    # Save user message
    st.session_state.messages.append({

        "role": "user",
        "content": f"{user_input}\n\n🕒 {current_time}"
    })

    # Show user message
    with st.chat_message("user"):

        st.markdown(user_input)
        st.caption(current_time)

    # Bot response
    with st.chat_message("assistant"):

        with st.spinner("Analyzing Query..."):

            time.sleep(1.5)

            response = bot.generate_response(user_input)

            st.markdown(response)

            st.caption(current_time)

    # Save bot response
    st.session_state.messages.append({

        "role": "assistant",
        "content": f"{response}\n\n🕒 {current_time}"
    })

# =========================
# FOOTER
# =========================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Departments", "10+")

with col2:
    st.metric("Placement Rate", "85%")

with col3:
    st.metric("Students", "5000+")

st.markdown(
    '<div class="footer">🚀 Developed using Python, Streamlit, and Object-Oriented Programming Concepts</div>',
    unsafe_allow_html=True
)