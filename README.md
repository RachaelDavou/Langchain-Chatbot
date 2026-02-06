# LangChain Chatbot

A simple chatbot built with LangChain and OpenAI API that accepts user questions and returns answers using LangChain chains. It features a Streamlit web interface with conversation history and 5 sample test queries.


## Requirements

Install the dependencies:

```
pip install streamlit langchain langchain-openai langchain-core
```


## API Key Setup

This application requires an OpenAI API key.

1. Open `app.py`
2. Replace `"your-openai-api-key-here"` with your actual API key on line 7

```python
api = "your-openai-api-key-here"
```

To get an API key, go to https://platform.openai.com/api-keys, sign-in to your account and create a new secret key.


## How to Run

Run the application from the command line:

```
streamlit run app.py
```

The app will open a local host in your browser.

## Sample Queries

The chatbot includes 5 sample questions for testing:

1. How to remove the filter from an AC?
2. How do I know when an avocado is ripe?
3. What is the difference between baking soda and baking powder?
4. Why do cats purr?
5. What is the world's fastest bird?

Click the "Run Sample Questions" button in the sidebar to test all 5 queries at once.


## How It Works

The chatbot is built using LangChain's runnable chain pipeline and a Streamlit interface.

1. **User Input** - The user enters a question in the Streamlit text box
2. **PromptTemplate** - A PromptTemplate formats the input by combining the user's question with the previous conversation history, giving the model context.
3. **LangChain Chain** - The template is connected to the OpenAI model using LangChain's pipe operator (|) to form a chain. This allows the input to flow through the prompt and into the model.
4. **OpenAI LLM** - The OpenAI language model generates a response based on the formatted prompt.
5. **Memory Handling** - Conversation history is stored using Streamlit session state so the chatbot can reference earlier questions and answers.
6. **Output Display** - The generated answer is displayed in the app, and both the user input and model response are saved to memory for future turns.
