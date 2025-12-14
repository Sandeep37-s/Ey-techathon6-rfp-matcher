# agents/main_agent.py

from reader_agent import extract_text_from_pdf, summarize_rfp_with_groq
from technical_agent import load_products_data, match_rfp_to_product

PDF_PATH = "C:/Users/sande/Downloads/EY/sample_rfp.pdf"
CSV_PATH = "C:/Users/sande/Downloads/EY/data/product.csv"

def process_rfp(pdf_path, csv_path):
    print("\n📄 Step 1: Extracting text from RFP...")
    text = extract_text_from_pdf(pdf_path)
    print("✅ Text extracted.")

    print("\n🧠 Step 2: Summarizing RFP using Groq Llama 3.3 model...")
    summary = summarize_rfp_with_groq(text)
    print("✅ Summary generated:\n", summary)

    print("\n📦 Step 3: Loading product database...")
    products_df = load_products_data(csv_path)
    print("✅ Products loaded:", len(products_df))

    print("\n🤖 Step 4: Matching RFP summary with catalog...")
    best_match = match_rfp_to_product(summary, products_df)
    print("\n✅ Best Match Found:\n", best_match)

if __name__ == "__main__":
    process_rfp(PDF_PATH, CSV_PATH)
