from fastapi import FastAPI, Query, Path
emp = [
    {"id":101,"name":"Sindhu","place":"Chennai"},
    {"id":102,"name":"Abi","place":"Bangalore"}
]
app = FastAPI()

@app.get("/display/{id}")
def viewforpath(id:int =Path(ge=100,le=200)):
    for e in emp:
        if e['id']==id:
            return e
    return {"message": "Employee not found"}

@app.get("/display/")
def viewforquery(id:int = Query(ge=100,le=200)):
    for e in emp:
        if e["id"] ==id:
            return e
    return {"message":"Employee not found"}