import pandas as pd

def load_excel_as_text(file_path):
    df = pd.read_excel(file_path)

    documents = []
    for index, row in df.iterrows():
        text = (
            f"产品编号: {row['model']}; "
            f"产品类型: {row['name']}; "
            f"牌子: {row['brand']}; "
            f"描述: {row['detail']}"
        )
        documents.append(text)

    return documents

if __name__ == "__main__":
    file_path = "/Users/linhao/ImageProcessor_demo/data/input/worksheet.xlsx"
    docs = load_excel_as_text(file_path)
    for doc in docs:
        print(doc)
