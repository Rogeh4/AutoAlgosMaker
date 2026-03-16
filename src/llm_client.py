import os
import re
from openai import OpenAI
from config import PROMPT_FOR_TASK, PROMPT_ROLE
from src.objects import Task, SolvedTask
from dotenv import load_dotenv

class KMSolver:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv('OPENAI_API_KEY')
        )
        self.model = os.getenv('MODEL_NAME2')

    def solve_task(self, task: Task) -> SolvedTask:
        """Решает одну конкретную задачу"""
        prompt_content = f"Имя файла: {task.name}\nУсловие: {task.description}\nОграничения: {task.task_req}"

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                PROMPT_ROLE,
                PROMPT_FOR_TASK(prompt_content)
            ],
            temperature=0.1
        )

        raw_code = re.search(r"```python\s*(.*?)\s*```", response.choices[0].message.content, re.DOTALL)
        if raw_code:
            return SolvedTask(name=task.name, code=raw_code.group())
        else:
            return SolvedTask(name=task.name, code=response.choices[0].message.content)

