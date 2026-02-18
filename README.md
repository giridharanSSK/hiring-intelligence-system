# 🚀 Hiring Intelligence System

**Option 2A - Internship & Incident Management (Python Track)**
*Submitted for MindFul AI - Round 2 Interview*

## 📌 Project Overview
This project is a **Hiring Intelligence Dashboard** built to solve the problem of unorganized internship applications. It automates the process of cleaning data, scoring candidates based on skills, and visualizing applicant statistics.

## 🛠️ Tech Stack
* **Python 3.12**: Core logic.
* **Streamlit**: Interactive Web UI.
* **Pandas**: Data manipulation and cleaning.
* **Unittest**: Automated testing for validation.

## ✨ Key Features
1.  **Automated Cleaning**: Instantly removes invalid emails and duplicate entries.
2.  **Smart Scoring**: Assigns a "Suitability Score" based on skills (Python, ML, SQL, etc.).
3.  **Role-Based Filtering**: Allows recruiters to filter candidates by specific roles.
4.  **Visual Analytics**: Generates real-time charts showing the distribution of skills.
5.  **Exportable Reports**: One-click download of the ranked candidate list.

## ⚙️ Setup & Execution
1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Application:**
    ```bash
    python -m streamlit run app.py
    ```
3.  **Run Automated Tests:**
    ```bash
    python -m unittest test_app.py
    ```

## 🧪 Testing Proof
Automated tests cover:
* ✅ Email validation logic.
* ✅ Scoring algorithm accuracy.
* ✅ Duplicate removal efficiency.

*(See `test_execution_proof.png` in the file list for verification)*