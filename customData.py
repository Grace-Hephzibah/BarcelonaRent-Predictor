from pydantic import BaseModel

class InputData(BaseModel):
    Year : int 
    Trimester: int    
    District: str 
    Neighbourhood : str
    Average_rent: str

class EncodedData(BaseModel):
    Year : int      
    Trimester: int    
    District: int
    Neighbourhood : int
    Average_rent: int  

