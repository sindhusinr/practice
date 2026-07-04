py  -m venv venv
.\venv\Scripts\activate
pip install fastapi
pip install uvicorn
unicorn main:app --reload
