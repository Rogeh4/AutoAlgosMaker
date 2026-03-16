import sys
from src.core import KMCore

def main():



    last_name = input("Enter your surname: ").strip()
    year = input("Enter your year (at the start of your course ").strip() or "2025"


    #загрузятся конфиги, промпты и создастся папка data/All_Labs_фамилия
    try:
        core = KMCore(last_name=last_name, year=year)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print("\nModes:")
    print(" - enter 'All' to Solve All labs")
    print(" - enter numbers thro space (for example, '1 6'), to solve chosen labs.")

    choice = input("\nYour choice: ").strip().lower()

    target_nums = []
    if choice != 'all' and choice != '':
        # Парсим строку '1 2 6' -> [1, 2, 6]
        target_nums = [int(n) for n in choice.split() if n.isdigit()]
        if not target_nums:
            print("Wrong Labs numbers")
            return

    print(f"\nSolving labs for {last_name} year: {year}...")
    core.run(target_nums)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
        sys.exit(0)