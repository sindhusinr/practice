from fastapi import FastAPI
emp = [
    {"id":101,"name":"Sindhu","place":"Chennai"},
    {"id":102,"name":"Abi","place":"Bangalore"}
]
app = FastAPI()

@app.get("/display/{id}")
def view(id):
    for e in emp:
        if e['id']==id:
            return e
    return {"message": "Employee not found"}