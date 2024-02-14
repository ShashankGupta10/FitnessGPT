from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chains import RetrievalQA
from langchain.llms.cohere import Cohere
import pandas as pd
import os


def get_fitness_context():
    text = ""
    df = pd.read_csv('gym.csv')
    temp = df.to_string(index=False)
    text = text + temp
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=20, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


app = Flask(__name__)
CORS(app)


@app.route("/api/chat", methods=["POST"])
def api():
    question = request.json
    print(question)
    raw_text = get_fitness_context()
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    llm = Cohere(cohere_api_key=os.environ["COHERE_API_KEY"])
    conversation_chain = RetrievalQA.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
    )
    prompt = f"You are a fitness trainer bot.\n \
        Your client wants to know about fitness and diet and exercise. \n \
        Your task is to answer the questions related to fitness and diet and exercise. \n \
        If the question is not related to fitness and diet and exercise, you can say 'I don't know I'm just a fitness bot'. \n \
        You can start the conversation by saying 'Hello'. \n \
        Max word count is 500. Don't give more than 500 words. \n \
        The question is {question}."
    answer = conversation_chain.invoke({"query": prompt})
    print(answer)
    return jsonify({"message": answer['result']})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
