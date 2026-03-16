from pathlib import Path

from src.objects import SolvedTask


class KMFileSaver:
    def __init__(self, last_name: str):
        self.last_name = last_name
        # /data/All_Labs_Фамилия
        self.base_path = Path(__file__).parent.parent / "data" / f"All_Labs_{self.last_name}"
        self.base_path.mkdir(parents=True, exist_ok=True)

    def get_lab_path(self, lab_number: int) -> Path:
        """Возвращает путь к папке конкретной лабы: 1_Yurenko"""
        return self.base_path / f"{lab_number}_{self.last_name}"

    def is_task_solved(self, lab_number: int, task_name: str) -> bool:
        """Проверяет, существует ли уже файл с решением"""
        clean_name = task_name.replace(',', '').strip()
        file_path = self.get_lab_path(lab_number) / clean_name
        return file_path.exists()

    def save_task(self, lab_number: int, solved_task:SolvedTask):
        """Сохраняет одно конкретное задание"""
        lab_dir = self.get_lab_path(lab_number)
        lab_dir.mkdir(parents=True, exist_ok=True)

        file_path = lab_dir / solved_task.name
        file_path.write_text(solved_task.code, encoding='utf-8')



