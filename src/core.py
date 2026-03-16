
from .llm_client import KMSolver
from .file_manager import KMFileSaver
from .parser import KMParser


class KMCore:
    def __init__(self, last_name: str, year= "2025"):
        self.last_name = last_name
        self.solver = KMSolver()
        self.saver = KMFileSaver(last_name)
        self.parser = KMParser(year)

    def run(self, target_nums: list[int]):
        """
        Если target_nums пустой решаем все
        """
        all_labs = self.parser.get_all_labs_data()

        for lab in all_labs.labs:
            # Если указаны конкретные номера пропускаем всё остальное
            if target_nums and lab.number not in target_nums:
                continue

            # Собираем только те задачи которые еще не решены
            to_do = [t for t in lab.tasks if not self.saver.is_task_solved(lab.number, t.name)]

            if not to_do:
                print(f"All Tasks in {lab.number} Complete.")
                continue

            print(f"Task amount in Lab {lab.number} - {len(to_do)}")
            for task in to_do:
                print(f"    Solving {task.name}...")
                solved_task = self.solver.solve_task(task)
                self.saver.save_task(lab.number, solved_task)
                print(f"    Task {solved_task.name} solved.")

        print("\n Done.")
