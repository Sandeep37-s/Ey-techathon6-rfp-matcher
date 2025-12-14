# agents/technical_agent.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to load product dataset
def load_products_data(path="C:/Users/sande/Downloads/EY/data/product.csv"):
    df = pd.read_csv(path)
    return df


# Function to find best matching product (SKU) for an RFP request
def match_rfp_to_product(rfp_text, products_df):
    # Combine RFP text with product descriptions
    texts = [rfp_text] + products_df["description"].tolist()

    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(texts)

    # Compare first vector (RFP) with all product descriptions
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Find index of highest similarity score
    best_index = similarities.argmax()

    # Get the best matched product details
    best_product = products_df.iloc[best_index]
    match_score = similarities[best_index]

    return {
        "sku_id": best_product["sku_id"],
        "product_name": best_product["product_name"],
        "description": best_product["description"],
        "price": int(best_product["price"]),
        "match_score": round(float(match_score), 2)
    }

# ✅ Testing the function (you can delete this later)
if __name__ == "__main__":
    products_df = load_products_data()
    sample_rfp = "Need 2000L waterproof white paint for exterior walls."
    result = match_rfp_to_product(sample_rfp, products_df)
    print("Best Match:", result)
