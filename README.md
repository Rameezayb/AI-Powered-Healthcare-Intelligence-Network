<p align="center">
  <a href="https://github.com/Rameezayb/MedAI-Health-Assistant">
    <img src="https://img.shields.io/github/stars/Rameezayb/MedAI-Health-Assistant?style=social" alt="GitHub Stars">
  </a>
</p>

<h1 align="center">🏥 MedAI Health Assistant</h1>

<p align="center">
  <strong>Your friendly AI healthcare companion</strong>
  <br>
  <em>Smart disease prediction • Safe drug recommendations • Heart health insights • 24/7 medical chat</em>
</p>

<p align="center">
  <img src="https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2069&q=80" alt="MedAI Health Assistant" width="500">
</p>

---

## ✨ **What it does**

**MedAI** helps you understand your health better with AI-powered tools:

- 🔬 **Disease Prediction** - Tell me your symptoms, I'll suggest possible conditions (92% accurate!)
- 💊 **Drug Safety** - Check medication interactions and find safer alternatives
- ❤️ **Heart Health** - Assess your cardiovascular risk and get prevention tips
- 🤖 **MedBot** - Chat with an AI doctor anytime for health questions

---

## 🛠️ **Tech behind it**

Built with modern AI tools: Python, Streamlit, Scikit-learn, LightGBM, LangChain, and Grok AI.

---

## 🚀 **Get started**

```bash
# Clone and run
git clone https://github.com/Rameezayb/MedAI-Health-Assistant.git
cd MedAI-Health-Assistant
pip install -r requirements.txt
streamlit run home.py
```

**Need API keys?** Add your HuggingFace and Grok API keys to a `.env` file.

---

## ⚠️ **Important**

This is a helpful tool, not a replacement for real doctors. Always consult healthcare professionals for medical decisions.

---

## 👋 **About me**

Hi! I'm **Muhammad Rameez**, an AI enthusiast passionate about making healthcare more accessible. This project combines my love for machine learning with helping people stay healthy.

- 📧 [mrameez16dev@gmail.com](mailto:mrameez16dev@gmail.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/muhammad-rameez-b4751928a)
- 🐙 [GitHub](https://github.com/Rameezayb)

---

<p align="center">
  <strong>Made with ❤️ for better health</strong>
</p>
<pre>
📦 MedAI Health Assistant
│── 📂 models/                         # Trained ML models
│── 📂 data/                           # Medical datasets (CSV)
│── 📂 vectorstore/db_faiss/           # FAISS vector database
│── 📂 utils/                          # Images, styles, and helper files
│── 📂 pages/                          # Individual module pages
│── 📜 home.py                         # Main homepage (Streamlit UI)
│── 📜 requirements.txt                 # Dependencies
│── 📜 README.md                        # Project Documentation
│── 📜 .gitignore                        # Ignored files
│── 📜 styles.css                        # Custom CSS for UI
</pre>

---

<h2>⚙️ Installation & Setup</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/Rameezayb/AI-Powered-Healthcare-Intelligence-Network.git
cd AI-Powered-Healthcare-Intelligence-System
</pre>

<h3>2️⃣ Set Up the Virtual Environment</h3>
<pre>
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
</pre>

<h3>3️⃣ Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>4️⃣ Set Up Environment Variables</h3>
<p>Create a <code>.env</code> file and add:</p>
<pre>
HF_TOKEN=your_huggingface_api_token
</pre>
<p>Ensure it is added to GitHub Secrets when deploying.</p>

<h3>5️⃣ Run the Application</h3>
<pre>
streamlit run home.py
</pre>

---

<h2>🚀 Deployment on Streamlit Cloud</h2>
<h3>1️⃣ Push code to GitHub</h3>
<pre>
git add .
git commit -m "Initial commit"
git push origin main
</pre>

<h3>2️⃣ Deploy on Streamlit</h3>
<ul>
  <li>Go to <a href="https://share.streamlit.io/">Streamlit Cloud</a> → Deploy a new app.</li>
  <li>Set <code>HF_TOKEN</code> in Streamlit Secrets.</li>
  <li>Click <strong>Deploy!</strong> 🎉</li>
</ul>

---



<h2>⚙️ Technologies Used</h2>
<ul>
  <li><strong>Machine Learning:</strong> RandomForest, LightGBM, NLP, Cosine Similarity</li>
  <li><strong>AI & NLP:</strong> Hugging Face Transformers, LangChain, FAISS</li>
  <li><strong>Data Handling:</strong> Pandas, NumPy, Pickle</li>
  <li><strong>Web Framework:</strong> Streamlit</li>
  <li><strong>Visualization:</strong> Plotly, SHAP for feature importance</li>
  <li><strong>Cloud Deployment:</strong> AWS, GCP</li>
</ul>

---

<h2>🔍 Why Use This App?</h2>
<ul>
  <li>🏥 <strong>AI-Powered Healthcare Insights:</strong> Get data-driven medical predictions.</li>
  <li>⚕️ <strong>Enhances Patient Care:</strong> Supports doctors and patients in making informed decisions.</li>
  <li>💡 <strong>Real-Time Recommendations:</strong> Provides immediate AI-assisted insights.</li>
  <li>⏳ <strong>Saves Time:</strong> Automates diagnosis and medical recommendations.</li>
  <li>🔬 <strong>Empowers Medical Research:</strong> Helps in early disease detection and prevention.</li>
</ul>

---
<h2> Docker Deployment</h2>
<p>This project is <strong>Docker-first</strong>. Docker ensures that the model can run in any environment without worrying about Python versions, dependencies, or system settings.</p>

```bash
docker pull rameezayb/ai-powered-healthcare-system
docker run -p 8501:8501 rameezayb/ai-powered-healthcare-system

```

<h3>✅ Why Docker?</h3>
<ul>
  <li>Environment-independent deployments</li>
  <li>Fast setup and teardown</li>
  <li>Easy to host on cloud (AWS, GCP, Azure)</li>
  <li>Reproducibility for teams and CI/CD pipelines</li>
</ul>

<h2>🌐 Docker hub</h2>
<ul>
  <li><strong>DockerHub</strong>: <a href="https://hub.docker.com/r/rameezayb/ai-powered-healthcare-system">https://hub.docker.com/r/rameezayb/ai-powered-healthcare-system</a></li>
</ul>


<h2>📜 License</h2>
<p>
  This project is licensed under the <strong>MIT License</strong>. Feel free to use, modify, and contribute!
</p>

---

<h2>📬 Contact Us</h2>
<p>Have questions or need support? Reach out to us at:</p>
<ul>
  <li>📧 <a href="mailto:mrameez16dev@gmail.com">mrameez16dev@gmail.com</a></li>
</ul>

---

<h2>🌐 Connect With Me</h2>
<p align="center">
  <a href="https://github.com/Rameezayb" target="_blank">🐙 GitHub</a> |
  <a href="https://www.linkedin.com/in/muhammad-rameez-b4751928a" target="_blank">💼 LinkedIn</a> |
  <a href="mailto:mrameez16dev@gmail.com" target="_blank">📧 Email</a>
</p>
