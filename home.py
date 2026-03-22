import streamlit as st

st.set_page_config(
    page_title="MedAI Health Assistant",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS for Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #ffffff;
            min-height: 100vh;
        }

        /* Main Title */
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            margin-bottom: 15px;
            text-shadow: 0px 0px 20px rgba(255, 255, 255, 0.3);
            background: linear-gradient(45deg, #ffffff, #e0e7ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Subtitle */
        .subtitle {
            font-size: 22px;
            color: #e0e7ff;
            text-align: center;
            font-weight: 400;
            margin-bottom: 50px;
            opacity: 0.9;
        }

        /* Sections */
        .section {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 8px 32px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
            transition: all 0.4s ease-in-out;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .section:hover {
            transform: translateY(-8px);
            box-shadow: 0px 12px 40px rgba(0, 0, 0, 0.15);
            background: rgba(255, 255, 255, 0.98);
        }

        .section h3 {
            color: #4c51bf;
            font-weight: 600;
            margin-bottom: 15px;
            font-size: 24px;
        }

        .section p {
            color: #2d3748;
            line-height: 1.6;
            font-size: 16px;
        }

        /* Sidebar */
        .sidebar-text {
            font-size: 16px;
            color: #ffffff;
            text-align: center;
            margin-bottom: 25px;
            line-height: 1.5;
            opacity: 0.9;
        }

        /* Contact Section */
        .contact {
            text-align: left;
            font-size: 18px;
            color: #ffffff;
            margin-top: 50px;
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        .contact h2 {
            color: #ffffff;
            margin-bottom: 20px;
            font-weight: 600;
        }

        .contact a {
            color: #fbb6ce;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .contact a:hover {
            color: #f687b3;
            text-decoration: underline;
        }

        /* Profile Links */
        .profile-links {
            text-align: center;
            margin-top: 30px;
            background: rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        .profile-links h2 {
            color: #ffffff;
            margin-bottom: 20px;
            font-weight: 600;
        }

        .profile-links a {
            font-size: 16px;
            color: #fbb6ce;
            text-decoration: none;
            margin: 0 20px;
            font-weight: 500;
            transition: all 0.3s ease;
            padding: 8px 16px;
            border-radius: 8px;
        }

        .profile-links a:hover {
            color: #f687b3;
            background: rgba(255, 255, 255, 0.1);
            text-decoration: none;
        }

        /* Technology sections */
        .tech-section {
            background: rgba(255, 255, 255, 0.9);
            color: #2d3748;
            text-align: center;
        }

        .tech-section h3 {
            color: #4c51bf;
            font-weight: 600;
        }

        /* Why use section */
        .why-use-section {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.9), rgba(118, 75, 162, 0.9));
            color: #ffffff;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .why-use-section h2 {
            color: #ffffff;
            text-align: center;
            margin-bottom: 25px;
        }

        /* Feature headers */
        h2 {
            color: #ffffff;
            text-align: center;
            font-weight: 600;
            margin: 50px 0 30px 0;
            font-size: 32px;
            text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.3);
        }

    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("<h2 style='color: #ffffff;'>📌 Navigation</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p class='sidebar-text'>Explore MedAI Health Assistant - your intelligent healthcare companion powered by advanced AI for accurate medical diagnosis, safe drug recommendations, and comprehensive health monitoring.</p>", unsafe_allow_html=True)
st.sidebar.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80", use_container_width=True)

# Main Content
st.markdown("<div class='title'>🏥 MedAI Health Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Intelligent Healthcare Companion - AI-Powered Medical Diagnosis & Wellness Platform</div>", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2069&q=80", use_container_width=True)

# Features Section
st.markdown("<h2 style='text-align: center; color: #ffffff;'>✨ Features</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='section'>
        <h3>� Disease Prediction</h3>
        <p>Advanced AI-powered diagnostic system that analyzes symptoms and predicts potential health conditions with high accuracy.</p>
    </div>

    <div class='section'>
        <h3>💊 Drug Recommendation</h3>
        <p>Intelligent medication guidance system that ensures safe prescriptions and suggests optimal treatment options.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='section'>
        <h3>❤️ Heart Health Assessment</h3>
        <p>Comprehensive cardiovascular risk evaluation using advanced ML models for precise heart health monitoring.</p>
    </div>

    <div class='section'>
        <h3>🤖 MedBot AI Assistant</h3>
        <p>Conversational AI healthcare companion providing instant medical insights and reliable health information.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Technologies Used
st.markdown("<h2 style='text-align: center; color: #ffffff;'>⚙️ Technologies Used</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='section tech-section'>
        <h3>🤖 Machine Learning</h3>
        <p>Advanced algorithms including RandomForest, LightGBM, and ensemble methods for accurate medical predictions.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='section tech-section'>
        <h3>🗂️ NLP & AI</h3>
        <p>Grok LLM integration with RAG technology for intelligent medical conversations and knowledge retrieval.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='section tech-section'>
        <h3>☁️ Modern Stack</h3>
        <p>Built with Streamlit, Docker, and cloud-native technologies for scalable healthcare solutions.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Why Use This App? (Separate Block)
st.markdown("""
    <div class='section why-use-section'>
        <h2>🌟 Why Choose MedAI Health Assistant?</h2>
        <p>
            ✅ <b>Advanced AI Diagnostics:</b> State-of-the-art machine learning models trained on comprehensive medical datasets for accurate predictions.<br><br>
            ✅ <b>Intelligent Drug Safety:</b> NLP-powered drug interaction analysis ensuring safe and effective medication recommendations.<br><br>
            ✅ <b>Comprehensive Health Monitoring:</b> Complete cardiovascular risk assessment with personalized preventive care strategies.<br><br>
            ✅ <b>24/7 AI Health Companion:</b> Always-available MedBot providing instant medical insights and reliable healthcare information.<br><br>
            ✅ <b>Privacy-First Design:</b> Enterprise-grade security with HIPAA-compliant data handling and user privacy protection.<br><br>
            ✅ <b>User-Centric Interface:</b> Intuitive, modern design built specifically for healthcare professionals and individual users.
        </p>
    </div>
    """ , unsafe_allow_html=True)

st.markdown("---")

# Contact Us (Left Aligned)
st.markdown("""
    <div class='contact'>
        <h2>📬 Contact & Support</h2>
        <p>Have questions, feedback, or need technical assistance? Our team is here to help you make the most of MedAI Health Assistant.</p>
        📧 <a href="mailto:mrameez16dev@gmail.com">mrameez16dev@gmail.com</a>
    </div>
    """, unsafe_allow_html=True)

# Profile Links (Centered)
st.markdown("""
    <div class='profile-links'>
        <h2>🌐 Connect With Me</h2>
        <a href="https://github.com/Rameezayb" target="_blank">🐙 GitHub</a> |
        <a href="https://www.linkedin.com/in/muhammad-rameez-b4751928a" target="_blank">💼 LinkedIn</a> |
        <a href="mailto:mrameez16dev@gmail.com" target="_blank">📧 Email</a>
    </div>
    """, unsafe_allow_html=True)
