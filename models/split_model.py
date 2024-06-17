from pydantic import BaseModel

class WorkoutSplit(BaseModel):
    split : str
    frequency : str
    goal : str