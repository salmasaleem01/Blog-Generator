import os
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Make sure to set your API key before running:
# export GOOGLE_API_KEY="your_api_key_here"   (Linux/Mac)
# set GOOGLE_API_KEY="your_api_key_here"      (Windows)

def main():
    # Initialize the Gemini model
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

    # Define a simple prompt template
    template = """
    You are a helpful assistant.
    Write a short blog on the topic: {topic}.
    Keep it under {word_limit} words.
    """

    prompt = PromptTemplate(
        input_variables=["topic", "word_limit"],
        template=template,
    )

    # Format the prompt with inputs
    final_prompt = prompt.format(topic="Future of Artificial Intelligence", word_limit=150)

    # Get response from Gemini
    response = llm.invoke(final_prompt)

    print("\n--- AI Generated Blog ---\n")
    print(response.content)


if __name__ == "__main__":
    main()
