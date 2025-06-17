# Python & Automation 

## Objective
This project demonstrates automation skills using real-world event data. It involves data cleaning, personalized messaging, and optional automation via email—all using **pure Python (no external libraries)**.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `clean_data.py` | Script to clean the input dataset: removes duplicates, normalizes values, and flags missing fields. |
| `cleaned_output.csv` | Cleaned dataset saved after running `clean_data.py`. |
| `generate_messages.py` | Script that generates personalized messages based on the cleaned data. |
| `personalized_messages.csv` | Output CSV containing user emails and generated messages. |
| `messages/` | Folder containing `.txt` files with each user’s message individually saved. |
| `send_email.py` *(optional)* | Bonus script to send messages via email using built-in `smtplib`. |

---

## 🧪 Step-by-Step Usage

### Step 1: Clean the Data
```bash
python clean_data.py
