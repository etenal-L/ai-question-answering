from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def run_qa_system(persist_directory="./chroma_db"):
    # 1️⃣ 加载 Chroma 数据库
    embedding_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)

    # 2️⃣ 设置 Retriever
    retriever = vectordb.as_retriever()

    # 3️⃣ 配置 Ollama （DeepSeek 模型）
    llm = Ollama(model="r1")  # 这里用 deepseek-8b 模型（必须已在本地 Ollama 可用）

    # 4️⃣ 构建 RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    print("✅ 问答系统已启动。请输入问题（输入 'exit' 退出）：")
    while True:
        question = input("📝 你的问题：")
        if question.lower() == "exit":
            break
        answer = qa_chain.run(question)
        print("🤖 AI 回答：", answer)

if __name__ == "__main__":
    run_qa_system()
