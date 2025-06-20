from __future__ import annotations
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from src.insight_generator import generate_insight
import datetime

load_dotenv()

app = Flask(__name__)

@app.route("/horoscope", methods=["POST"])
def horoscope():
    """Return zodiac + LLM-generated daily insight."""
    data = request.get_json(force=True)
    # Basic validation for the required fields
    name = data.get("name")
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    birth_place = data.get("birth_place")

    if not name or not birth_date or not birth_time or not birth_place:
        return jsonify({"error": "name, birth_date, birth_time, and birth_place are required"}), 400
    
    # Validate birth_date format 
    try:
        datetime.datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "birth_date must be in the format YYYY-MM-DD"}), 400

    # Validate birth_time format 
    try:
        datetime.datetime.strptime(birth_time, "%H:%M")
    except ValueError:
        return jsonify({"error": "birth_time must be in the format HH:MM"}), 400
    
    try:
        insight = generate_insight(name, birth_date, birth_time, birth_place)
        return jsonify(insight)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
