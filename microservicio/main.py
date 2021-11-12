from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()
# Declaracion del req
class Drink(BaseModel):
    id:int
    nombre:str
    licores:List[str]
    receta:str


# Tipo de respuestas 

def drink(item)->dict:
    return {
        "id":item["id"],
        "nombre":item["nombre"],
        "licores":item["licores"],
        "receta":item["receta"]
    }

def drinks(entity)->list:
    return [drink(item) for item in entity]

cocteles = [
        {"id":1,"nombre":"paloma","licores":["tequila"],"receta":"mezclar hielos, limon, tequila"},
        {"id":2,"nombre":"margarita","licores":["tequila","triple sec"],"receta":"mezclar hielos, limon, tequila y triple sex"}
        
        ]
# Rutas

@app.get('/api/sps/helloworld/v1')
def get_drinks(response:Response):
    response.status_code = status.HTTP_200_OK
    return drinks(cocteles)

@app.get('/api/sps/helloworld/v1/{id}')
def get_drink(id:int,response:Response):
    respuesta=[]
    for ele in cocteles:
        if(ele["id"] ==int(id)): 
            respuesta.append(ele)
            response.status_code = status.HTTP_200_OK
    
    return drink(respuesta[0]) 

@app.post('/api/sps/helloworld/v1')
def create_drink(drink:Drink,response:Response):
    cocteles.append(drink)
    response.status_code = status.HTTP_201_CREATED
    return {"msg":"creado coctel","contenido":cocteles}

@app.put('/api/sps/helloworld/v1/{id}')
def actualizar_drink(id:int,drink:Drink,response:Response):
    drinkUpdate = dict(drink)
    for ele in cocteles:
        if(ele["id"] ==id): 
            ele["nombre"]=drinkUpdate["nombre"]
            ele["licores"]=drinkUpdate["licores"]
            ele["receta"]=drinkUpdate["receta"]
            response.status_code = status.HTTP_202_ACCEPTED

    return {"msg":"actualizado","contenido":cocteles}

@app.delete('/api/sps/helloworld/v1/{id}')
def delete_drinl(id:int,response:Response):
    for ele in cocteles:
        if(ele["id"] ==id): 
            cocteles.remove(ele)
            response.status_code = status.HTTP_200_OK
    return {"msg":"eliminado","contenido":cocteles}



