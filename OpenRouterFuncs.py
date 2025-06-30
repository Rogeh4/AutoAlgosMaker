import os
from openai import OpenAI
from Config import PROMPT_FOR_TASK, PROMPT_ROLE
from utilits import get_str_interval
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY
)



def make_answer_string(task, requirements,  log=False):
    if log:
        print("Generating answer...")
    response = client.chat.completions.create(
                model="deepseek/deepseek-chat-v3-0324:free",
                messages=[PROMPT_ROLE, PROMPT_FOR_TASK(requirements), {"role": "user","content": task}],
                temperature=1)
    if log:
        print("Answer generated")
    return get_str_interval(response.choices[0].message.content, "```python", "```").strip()

if __name__ == "__main__":
    task = "Напишите программу, которая из списка заявок выбирает максимальное количество совместных друг с другом используя жадную стратегию. Заявки задаются строкой вида “1,2 2,6 2,3 4,6”, где a,b – обозначают время начала и окончания заявки (целые положительные числа).Вход: строка со списком заявокВыход: количество и список заявок (в виде кортежей)% python3 tasks.py '1,2 2,6 2,3 4,6'3 [(1, 2), (2, 3), (4, 6)]"
    req = ""
    answer = make_answer_string(task, req)
    print(answer)
