from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/makeitdubble/")
def make_it_dubble(number : int) :
    dubble = number * 2
    return {'The dubble is' : dubble}
# pour l'appeler http://127.0.0.1:8000/makeitdubble/?number=10

class Salary(BaseModel):
    salary: float
    bonus : float
    taxes: float

@app.get("/salary/")
def get_salary(salary : float, bonus : float, taxes : float) :
    net_salary = salary + bonus - taxes
    return {"net_salary" : net_salary}


@app.post("/salary/")
def calculate(data: Salary):
    net_salary = data.salary + data.bonus - data.taxes
    return {"net_salary" : net_salary}