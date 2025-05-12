from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from ai_question_answering.data_loader import load_excel_as_text


def create_vector_store(file_path, embedding_model_path, persist_directory="./chroma_db"):
    # 1️⃣ 读取文本
    texts = load_excel_as_text(file_path)

    # 2️⃣ 转换为 Document 对象（langchain 需要 Document）
    documents = [Document(page_content=text) for text in texts]

    # 3️⃣ 加载本地 embedding 模型
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_path)

    # 4️⃣ 创建 Chroma 向量数据库
    vectordb = Chroma.from_documents(documents, embedding=embeddings, persist_directory=persist_directory)

    # 5️⃣ 保存数据库
    vectordb.persist()
    print(f"✅ 向量数据库已保存到 {persist_directory}")

    return vectordb

if __name__ == "__main__":
    excel_file_path = "/Users/linhao/ImageProcessor_demo/data/input/worksheet.xlsx"
    embedding_model_path = "BAAI/bge-small-zh-v1.5"
 # 模型目录，记得用实际路径
    create_vector_store(excel_file_path, embedding_model_path)
