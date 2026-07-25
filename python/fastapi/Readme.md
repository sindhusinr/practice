## Fast API

- FastAPI → Framework for creating APIs.
- Uvicorn → Server that runs FastAPI.

1. Import FastAPI
`
from fastapi import FastAPI
`
Imports the FastAPI class.

2. Create Application
`
app = FastAPI()
`
FastAPI() → creates a FastAPI application
app → refers to that application
Create a FastAPI web application(website/API) that can receive requests and send responses.


3. Create a Route
`
@app.get("/")
`
This tells FastAPI: If someone visits /, run the function below.

```bash
py  -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

