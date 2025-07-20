🧮 Text to Math Problem Solver & Data Search Assistant
This Streamlit-based AI assistant uses Groq's LLaMA 3, LangChain, and Wikipedia to:

🔢 Solve math word problems

🧠 Answer logic/reasoning questions

🌐 Fetch factual info from Wikipedia

🚀 Features
✅ Input math-related or logic questions in plain text

🧮 Evaluates math expressions safely with numexpr

📚 Searches Wikipedia for factual answers

🧠 Uses LLaMA 3 to handle reasoning-style questions

💬 Streamlit chat interface with conversation history

🛠️ Tech Stack
Tool	Purpose
Streamlit	Web interface
LangChain	LLM chaining and agent management
Groq	Runs LLaMA 3 for fast, low-latency inference
Wikipedia API Wrapper	Wikipedia search
numexpr	Secure math expression evaluation

🔑 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/text-math-solver.git
cd text-math-solver
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add a .env file
Create a .env file in the root directory:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
5. Run the App
bash
Copy
Edit
streamlit run app.py
🧪 Example Input
I had 12 apples. I gave 4 to my friend and ate 2 myself. Then I bought 3 baskets of apples, each containing 5 apples.
How many apples do I have now?

📂 File Structure
bash
Copy
Edit
📁 text-math-solver/
├── app.py               # Main Streamlit app
├── requirements.txt     # All dependencies
└── README.md            # This file
✅ Todo / Improvements
 Add voice input (SpeechRecognition)

 Add graphical solution explanations (e.g. pie/bar charts)

 Add memory/chat history download

📜 License
This project is open-source and free to use under the MIT License.

