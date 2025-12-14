from flask import Flask, render_template, request
from agents.reader_agent import extract_text_from_pdf, summarize_rfp_with_groq
from agents.technical_agent import load_products_data, match_rfp_to_product
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
PRODUCTS_PATH = "data/product.csv"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pdf_file = request.files["pdf"]
        if pdf_file:
            pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
            pdf_file.save(pdf_path)

            # Step 1 – Extract text and summarize
            text = extract_text_from_pdf(pdf_path)
            summary = summarize_rfp_with_groq(text)

            # Step 2 – Load products and find best match
            products_df = load_products_data(PRODUCTS_PATH)
            best_match = match_rfp_to_product(summary, products_df)

            return render_template("result.html",
                                   summary=summary,
                                   best_match=best_match)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
