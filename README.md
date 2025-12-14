# EY Techathon 6.0 - AI RFP Matcher 🧠

An **Agentic AI system** that reads RFP (Request for Proposal) PDFs, summarizes them using **Groq LLM**, and matches them with the best-fit product from a **catalog CSV** using **TF-IDF similarity** — all integrated into a simple **Flask web app**.

---

## 🚀 Features
- 📄 **PDF Reader Agent:** Extracts text and summarizes RFPs using Groq API  
- 🧩 **Technical Agent:** Loads product catalog and finds best matching product via TF-IDF  
- 💻 **Flask UI:** Upload RFP PDF → View AI-generated summary + Best Product Match + Match Score  
- ⚡ **Modular Agents:** Reader, Technical, Coordinator, Pricing (extendable architecture)

---

## 🧠 Tech Stack
- **Python 3.12+**
- **Flask**
- **Groq LLM API**
- **TF-IDF + Cosine Similarity (Scikit-Learn)**
- **PyPDF2**, **Pandas**, **Joblib**

---

### 📂 Project Structure

```text
EY/
├── agents/
│   ├── reader_agent.py      # Reads + summarizes RFP PDF using Groq
│   ├── technical_agent.py   # Matches RFP with product catalog (TF-IDF)
│   ├── main_agent.py        # Integrates Reader + Technical Agents
│   └── pricing_agent.py     # (Optional) Price estimation module
├── data/
│   ├── product.csv          # Product catalog
│   └── rfp_request.csv      # (Optional) RFP storage
├── templates/
│   ├── index.html           # Upload form
│   └── result.html          # Results display
├── app.py                   # Flask UI entry point
├── requirements.txt
└── sample_rfp.pdf           # Example RFP file

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/ey-techathon6-rfp-matcher.git
   cd ey-techathon6-rfp-matcher
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add your Groq API key in a .env file:

ini
Copy code
GROQ_API_KEY=your_groq_api_key_here
Run the Flask app:

bash
Copy code
python app.py
Open your browser:

cpp
Copy code
http://127.0.0.1:5000/
📊 Output Example
Upload RFP PDF

System displays:

🧾 RFP Summary

🧩 Best Match Product

💰 Price & Confidence Score

💡 Future Enhancements
Use sentence embeddings instead of TF-IDF for better semantic matching

Add pricing agent and real-time bidding API integration

Deploy on Render / Vercel for public access

👥 Team
Team Name: sandeepkumar6200187840
Member:Sandeep kumar 
Competition: EY Techathon 6.0 (Agentic AI Theme)
