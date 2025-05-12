# AI 商品QAシステム

Excelの商品情報をもとに、AIによる自動QA（質問応答）を行うシステムです。  
Retrieval-Augmented Generation (RAG) 構成を実現しています。

## 機能概要

✅ Excelから商品情報を読み込む  
✅ 文章をembedding（ベクトル化）  
✅ ChromaでローカルベクトルDBを構築  
✅ 質問に対して関連情報を検索  
✅ DeepSeek-8B（Ollama）で簡潔なカスタマー対応風の回答を生成

## 技術スタック

- Python
- Langchain
- Chroma
- Sentence-Transformers (bge-small-zh-v1.5)
- Ollama (DeepSeek-8B)
- VS Code

## 使用方法

### 1️⃣ 環境構築

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: .\venv\Scripts\activate
pip install -r requirements.txt
2️⃣ ベクトルDB構築
bash
复制
编辑
python -m ai_question_answering.vector_store
3️⃣ QAシステム起動
bash
复制
编辑
python -m ai_question_answering.qa_system
質問を入力し、「exit」で終了します。

ディレクトリ構成
markdown
复制
编辑
ai-question-answering/
├── ai_question_answering/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── vector_store.py
│   ├── qa_system.py
├── .gitignore
├── README.md
├── requirements.txt
工夫ポイント
モジュール構成（data_loader / vector_store / qa_system に分割）

クラスではなく関数ベースでシンプルに実装

LangchainとChromaを使用し、RAGパイプラインを構築

LLM応答にsystem promptで30文字以内のカスタマーサポート調回答を指定

自己PR
このプロジェクトは、AI・自然言語処理・Pythonプログラミングの実践力を高めるために個人で開発しました。
要件定義から設計、実装、テストまで一貫して行い、モジュール設計、ドキュメンテーション、GitHub管理を意識しました。