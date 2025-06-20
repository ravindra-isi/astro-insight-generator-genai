# astro-insight-generator-genai

# 🪐 Astro Insight Generator using Zodiac + LLM (GenAI)

## 🚀 How to Run?

### 🔗 **Project Repo**

**Clone this repository**

```bash
git clone https://github.com/ravindra-isi/astro-insight-generator-genai.git
cd astro-insight-generator-genai
```

---

### ✅ **STEP 01 — Create and activate a virtual environment**

Using `conda` (recommended):

```bash
conda create -n astrobot python=3.10 -y
conda activate astrobot

```

Or using `venv`:

```bash
python3 -m venv astrobot
source astrobot/bin/activate
```

---

### ✅ **STEP 02 — Install dependencies**

```bash
pip install -r requirements.txt
```

> If you plan to use OpenAI, HuggingFace, or other APIs later, add your credentials to a `.env` file:

```
OPENAI_API_KEY = "your-api-key-here"
```

---

### ✅ **STEP 03 — Run the Flask application**

#### **Run Flask App**:

In the **first terminal window**, start the Flask app:

```bash
python app.py
```

This will start your Flask server locally. The output should look like this:

```
 * Running on http://127.0.0.1:8000
```

Your Flask app is now running and can be accessed locally at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

---

### ✅ **STEP 04 — Test the API via cURL or Postman**

Now, **open another terminal window** to send a **POST request** to the Flask API.

#### **Using cURL**:

In the **second terminal window**, run the following `cURL` command to send a POST request to your running Flask app:

```bash
curl -X POST http://127.0.0.1:8000/horoscope \
-H "Content-Type: application/json" \
-d '{"name": "Ritika", "birth_date": "1995-08-20"}'
```

> This sends a POST request with `name` and `birth_date` as JSON data to your Flask endpoint `/horoscope`.

#### **Using Postman**:

1. Open **Postman**.
2. Set the **method** to **POST**.
3. Set the **URL** to `http://127.0.0.1:8000/horoscope`.
4. In the **Body** section, select **raw** and set the type to **JSON**.
5. Paste the following JSON body:

```json
{
  "name": "Ritika",
  "birth_date": "1995-08-20"
}
```

6. Click **Send** to get the response.

You should receive a JSON response like:

```json
{
  "zodiac": "Leo",
  "insight": "Your innate leadership and warmth will shine today. Embrace spontaneity and avoid overthinking.",
  "language": "en"
}
```

---

## 📦 Folder Structure

```
astro-insight-generator-genai/
├── app.py                  # Entry point for Flask app
├── src/
│   ├── zodiac_utils.py     # Zodiac sign logic (date to zodiac)
│   ├── insight_generator.py # Insight generation logic with LLM
│   └── __init__.py         # Initialization file for the src package
├── .env                    # Environment variables (for API keys)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📌 Sample Input

```json
{
  "name": "Ritika",
  "birth_date": "1995-08-20",
  "birth_time": "14:30",
  "birth_place": "Jaipur, India"
}
```

## 📌 Sample Output

```json
{
  "zodiac": "Leo",
  "insight": "Your innate leadership and warmth will shine today. Embrace spontaneity and avoid overthinking.",
  "language": "en"
}
```

---

## 🛠️ Tech Stack Used

* **Python 3.10**
* **Flask** for creating the API
* **Pydantic** for schema validation
* **LangChain** for LLM-based horoscope generation
* **OpenAI** for using GPT-4.1 (or other models like `gpt-4.1-nano`)
* **dotenv** for managing API keys in `.env`
* **Optional:** HuggingFace for multilingual support (stub for IndicTrans/NLLB)

---

## 📝 Additional Notes

* The app generates personalized horoscopes based on the user's birth date.
* The **Flask API** allows you to access the horoscope generation functionality via `POST` request.
* You can extend this system with **multilingual support** using HuggingFace or other APIs.

```
---

### **Quick Recap of How to Run**:

1. **Step 1**: **Clone the repo** and **create a virtual environment**.
2. **Step 2**: **Install dependencies**.
3. **Step 3**: **Run the Flask app** in the first terminal.
4. **Step 4**: **Test the API** in the second terminal with `cURL` or Postman.

---
