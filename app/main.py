from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests


delete_request = requests.delete("https://teste2026-b8066-default-rtdb.firebaseio.com/.json",
                                 json={"name": "Teste3", "idade": 31})

get_inform = requests.get("https://teste2026-b8066-default-rtdb.firebaseio.com/.json")

try:
    print(get_inform.json())
except Exception as err:
    print("erro: ", err)
print(get_inform)