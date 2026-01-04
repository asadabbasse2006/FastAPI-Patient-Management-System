from fastapi import FastAPI,Path,HTTPException,Query
import json
from pydantic import BaseModel,Field,computed_field
from fastapi.responses import JSONResponse
from typing import Annotated,Literal,Optional

class Patient(BaseModel):
    
    id: Annotated[str,Field(...,description="ID of the patient",examples=["P001"])]
    name: Annotated[str,Field(...,description="Name of the Patient")]
    city: Annotated[str,Field(...,description="City where the patient living")]
    age: Annotated[int,Field(...,gt=0,lt=120,description="Age of the patient")]
    gender: Annotated[Literal['male','female','others'],Field(...,description="Gender of the patient")]
    height: Annotated[float,Field(...,gt=0,lt=10,description="Height of the patient in meters")]
    weight: Annotated[float,Field(...,gt=0,description="Weight of the patient in kilograms")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/self.height**2,2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"

class PatientUpdate(BaseModel):
    name : Annotated[Optional[str],Field(default=None)]
    city : Annotated[Optional[str],Field(default=None)]
    age  : Annotated[Optional[int],Field(default=None,gt=0)]
    gender : Annotated[Optional[Literal['male','female','other']],Field(default=None)]
    weight : Annotated[Optional[float],Field(default=None,gt=0)]
    height : Annotated[Optional[float],Field(default=None,gt=0)]


app = FastAPI()

def load_data():
    with open("patients.json","r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {"message":"Patient Management System"}

@app.get("/about")
def about():
    return {"message":"A fully functional system to manage the patient records."}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description="ID of the patient",example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient Not Found")

@app.get("/sort")
def sort_patients(sort_by = Query(...,description="Sort on the basis of heigh, weight or bmi"), order : str = Query('asc',description="Sort by asc or desc order")):
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail = f"Invalid fields, select from {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f'Invalid order, Select from {['asc','desc']}')
    
    data = load_data()

    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by,0), reverse=sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient:Patient):
    #First load data
    data = load_data()

    # Checks that the patient already existed or not

    if patient.id in data:
        raise HTTPException(status_code=400,description="Patient already exists")
    
    # Insert the patient into the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # Save into the JSON file
    save_data(data)
    return JSONResponse(status_code=201,content={"message":"Patient Created Successfully"})

@app.put('/edit/{patient_id}')
def update_patient(patient_id : str, patient_update : PatientUpdate):

    data = load_data()
    if patient_id not in data:
        return HTTPException(status_code=404,detail="Patient Not Found")
    
    existing_patient_data = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_data[key] = value

    existing_patient_data['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_data)
    existing_patient_data = patient_pydantic_object.model_dump(exclude='id')

    data[patient_id] = existing_patient_data

    save_data(data)
    return JSONResponse(status_code=200,content={'message':'Patient Updated Successfully'})
    
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id : str):
    #load data
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404,detail={"message":'Patient Not Found'})
    
    del data[patient_id]

    save_data(data)
    return JSONResponse(status_code=200,content={'message':'Patient deleted successfully'}) 