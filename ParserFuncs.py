
import requests
from bs4 import BeautifulSoup
from Config import KM_ALGOS_URL
from utilits import get_str_interval


def url_parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    text = soup.get_text(separator=" ", strip=True).split("Требования к сдаче работы")[1]
    return text

def make_requirements(text, log=False):
    requirements = get_str_interval(text,'совпадать с указанным в задании', " (0 баллов)")
    return requirements

def make_tasks(text, log=False):
    text_len = len(text)
    tasks_list = text.split("Задача:")
    tasks_dict = {}

    for block in tasks_list:
        if len(block) > 0.3 * text_len:
            continue
        name = ""
        for word in block.split(" "):
            if ".py" in word:
                name = word
                break
        tasks_dict[name] = block
    return tasks_dict

def get_urls():
    response = requests.get(KM_ALGOS_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    wrap = soup.find_all(id='wrap')[0]
    container = wrap.find_all(class_='container')[0]
    urls = container.find_all('a')
    res = {}
    lbnum = 0
    for url in urls:
        if "docs" in url['href']:
            lbnum += 1
            res[lbnum] = url['href']
    return res


if __name__ == "__main__":
    with open('LB1TXT.txt', 'r', encoding="utf-8") as lb1:
        text = lb1.read()
    print("text:", text)
    req = make_requirements(text)
    print(req)
    print("))))))))))))))))))))))")
    tasks = make_tasks(text)
    for name, task in tasks.items():
        print(name + ": " + task)
