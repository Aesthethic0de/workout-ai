import os
from langchain_community.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from models.split_model import WorkoutSplit
from models.user_model import User
from prompts.workout_prompt import workout_ai



class WorkoutGenerator:
    
    def __init__(self):
        self.apikey = os.getenv("OPEN_API_KEY")
        self.url = os.getenv("OPEN_API_BASE")
        self.set_env_var()
        
    def set_env_var(self):
        os.environ['OPENAI_API_KEY'] = self.apikey
        os.environ['OPENAI_API_TYPE'] = 'azure'
        os.environ['OPENAI_API_VERSION'] = '2023-03-15-preview'
        os.environ['OPENAI_API_BASE'] = self.url
        
    def llm_obj(self):
        llm = AzureChatOpenAI(
            deployment_name="ChatGeneric",
            model_name="gpt-35-turbo",
            temperature=0)
        return llm
    
    def generate_user_data(self, user: User):
        data = f"""
            User Profile:
            ID: {user.id}
            Username: {user.username}
            Email: {user.email}
            Age: {user.age}
            Fitness Level: {user.level}
            Weight (kg): {user.weight}
            Height (cm): {user.height}
            """
        return data
    
    def generate_question(self, workoutsplit: WorkoutSplit, advanced):
        question = f"Create a brief workout plan for {workoutsplit.frequency} focusing on {workoutsplit.goal} with a {workoutsplit.split}. \
                    The plan should include only the number of reps and sets, and must have 6 exercises plus cardio."
        if advanced:
            question += " Include advanced techniques like supersets, drop sets, and progressive overload."
        return question
    
    def create_prompt(self):
        llm = self.llm_obj()
        workout_creator_assistant_template = PromptTemplate(
            input_variables=["question", "context"],
            template=workout_ai
        )
        sequence = workout_creator_assistant_template | llm
        return sequence
    
    def get_response(self, user: User, workoutsplit: WorkoutSplit, advanced=False):
        sequence = self.create_prompt()
        question = self.generate_question(workoutsplit, advanced=advanced)
        context = self.generate_user_data(user)
        response = sequence.invoke({'question': question, 'context': context})
        return response
        
        
        

