# AI Study Assistant

![GitHub](https://img.shields.io/badge/Status-Completed-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-orange)

---

## **Project Description**

AI Study Assistant is a **web-based educational tool** built with **Python and Flask**.  
It allows users to:

1. **Generate study notes** for any topic.  
2. **Take MCQ tests** on the topic and calculate scores.  

The assistant uses **fuzzy matching** to improve accuracy, and the UI is **modern, professional, and user-friendly**.

---

## **Features**

- ✅ Generate study notes for any topic  
- ✅ Take multiple-choice question tests  
- ✅ Score calculation for submitted tests  
- ✅ Copy-protection: prevents selecting or copying text  
- ✅ Fully responsive and modern UI  
- ✅ Rule-based AI with fuzzy matching for better results  

---
## **Folder Structure**
```
ai-study-assistant/
│
├─ app.py # Main Flask app
├─ study_assistant.py # Study content + MCQs + fuzzy matching
├─ requirements.txt # Python dependencies
├─ .gitignore # Ignore virtual env & pycache
├─ templates/
│ ├─ index.html # Home / Study page
│ └─ test.html # Test page
└─ static/
└─ style.css # Modern CSS
```
---

## **Screenshots**

**Home / Study Page:**  

![Study Page Screenshot](link-to-your-screenshot)  

**Test Page:**  

![Test Page Screenshot](link-to-your-screenshot)  

> You can add your screenshots here after running the app locally.

---

## **Installation & Running**

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
```
3. Activate the virtual environment:

Windows:
```bash
.venv\Scripts\activate
```
Mac/Linux:
```bash
source .venv/bin/activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Run the Flask app:
```
python app.py
```
