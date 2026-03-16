import re
import logging
import requests
from bs4 import BeautifulSoup
from typing import List, Optional
from .objects import Task, LabTasks, AllLabTasks

# Настройка логирования
logger = logging.getLogger(__name__)


class KMParser:
    def __init__(self, year: str = 2025):
        self.base_url = f"https://km.mmf.bsu.by/courses/{year}/algo.html"
        self._cache = self.get_all_labs_data()

    def _fetch_lab_links(self) -> List[str]:
        logger.info(f"Parsing lab links from the site {self.base_url}")

        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, "lxml", from_encoding="utf-8")

        res_links = []

        start_phrase = "<h2>Лабораторные работы</h2>"
        end_phrase = "<h2>Контрольные работы</h2>"

        search_field = re.search(rf"{re.escape(start_phrase)}(.*?){re.escape(end_phrase)}", str(soup),
                                 re.DOTALL | re.IGNORECASE).group(1).strip()
        all_links = re.findall(r'href="(https?://docs\.google\.com/[^"]+)"', search_field)

        for link in all_links:
            if "doc" in link:
                res_links.append(link)

        return res_links

    def _parse_single_lab(self, lab_url: str) -> LabTasks:

        response = requests.get(lab_url)
        soup = BeautifulSoup(response.content, "lxml", from_encoding="utf-8")

        title_text = soup.title.string
        lab_num = re.search(r"(?<=-)\d+(?=\.)", title_text).group()

        parts = re.split(r'<h1.*?>.*?</h1>', str(soup))



        last_part = parts[-1]
        penult_part = parts[-2]
        if last_part.count(".py") < penult_part.count(".py"):
            tasks_string_xml = penult_part + last_part
        else:
            tasks_string_xml = last_part

        task_soup = BeautifulSoup(tasks_string_xml, "lxml")
        tasks_clean_text = task_soup.get_text()
        tasks = tasks_clean_text.split("Напишите программ")

        tasks_req = tasks[0]
        tasks = tasks[1::]

        res = LabTasks(int(lab_num), [])
        tasks_dict = {}
        for task_description in tasks:
            task_name = re.search(r'\S+\.py\S*', task_description).group()
            tasks_dict[task_name.strip(",")] = task_description

        for k, v in tasks_dict.items():
            res.tasks.append(Task(k, v, tasks_req))

        return res

    def get_all_labs_data(self) -> AllLabTasks:
        all_links = self._fetch_lab_links()
        result = AllLabTasks([])
        for link in all_links:
            result.labs.append(self._parse_single_lab(link))
        return result

    def get_lab_by_number(self, number: int) -> Optional[LabTasks]:
        for lab in self._cache.labs:
            if lab.number == number:
                return lab
        return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    parser = KMParser()
    r = parser.get_all_labs_data()
    for lb in r.labs:
        print()
        print("TASKS for lab number", lb.number)
        for task in lb.tasks:
            print(f"|{task.name}| {task.description}")
        print()
