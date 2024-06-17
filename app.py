
from models.user_model import User
from models.split_model import WorkoutSplit
from src.GetResponseClass import WorkoutGenerator


user = User(id="123", username='john_doe', email='john@example.com', age=30, level='advance', weight="94 kg", height="5ft 10inch")
workoutsplit = WorkoutSplit(frequency='1 week', split='body part splits')
generator = WorkoutGenerator()
response = generator.get_response(user, workoutsplit)
print(response.content)