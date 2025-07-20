import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
import numexpr

# Streamlit page setup
st.set_page_config(page_title="Text To Math Problem Solver And Data Search Assistant", page_icon="🧮")
st.title("Text To Math Problem Solver Using LLAMA 3")

# API Key input
groq_api_key = st.sidebar.text_input(label="Enter your Groq API Key", type="password")
if not groq_api_key:
    st.error("Please enter the Groq API key")
    st.stop()

# Initialize LLM
llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)

# Wikipedia Tool
wikipedia_wrapper = WikipediaAPIWrapper()
wiki_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="Tool to search the web"
)

# Custom Math Evaluator Tool
def safe_calculator(expr: str) -> str:
    try:
        result = numexpr.evaluate(expr).item()
        return f"The result of `{expr}` is: {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

calculator = Tool(
    name="Calculator",
    func=safe_calculator,
    description="Tool for solving pure math expressions like '12 * 5 - 4'"
)

# Reasoning Tool
prompt = """
You are an agent tasked with solving users' mathematical or reasoning questions.
Logically arrive at the solution and provide a detailed explanation point-wise.

Question: {question}
Answer:
"""
prompt_template = PromptTemplate(template=prompt, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt_template, llm=llm)

resoning_tool = Tool(
    name="Reasoning Tool",
    func=llm_chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

# Initialize Agent
initi_agent = initialize_agent(
    tools=[wiki_tool, calculator, resoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a Math chatbot who can answer all your math and logic questions!"}
    ]

# Display Chat History
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

# Question Input
question = st.text_area("Enter your question:", "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

# Button to Trigger Answer
if st.button("Find My Answer"):
    if question.strip():
        with st.spinner("Generating response..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = initi_agent.run(question, callbacks=[st_cb])

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
    else:
        st.warning("Please enter a question.")
 # type: ignore