import requests
from PyPDF2 import PdfReader



def extract_text_from_pdf(pdf_path):
    """Extract text from PDF"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

def summarize_rfp_with_groq(text):
    """Summarize RFP using Groq API"""
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile", 
        "messages": [
            {"role": "user", "content": f"Summarize this RFP in bullet points:\n{text[:4000]}"}
        ],
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"


if __name__ == "__main__":
    pdf_path = "C:/Users/sande/Downloads/EY/sample_rfp.pdf"
    text = extract_text_from_pdf(pdf_path)
    print("\n--- Extracted Text ---\n", text[:400])
    summary = summarize_rfp_with_groq(text)
    print("\n--- Groq Summary ---\n", summary)
