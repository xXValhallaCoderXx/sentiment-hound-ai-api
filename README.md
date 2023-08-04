python3 -m venv venv/ # Create VENV
source venv/bin/activate # Start VENV

uvicorn main:app --reload
