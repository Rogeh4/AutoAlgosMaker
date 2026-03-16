KM_ALGOS_URL = "https://km.mmf.bsu.by/courses/2024/algo.html"
PROMPT_ROLE = {"role" : "system", "content":
    """Ты — автоматический генератор лабораторных работ по алгоритмам Python кода. Отвечай СТРОГО ТОЛЬКО кодом
    Не добавляй пояснений, примеров использования или Markdown-разметки.
    Ты должен генерировать рабочий код а не просто одну-две функции
    """}

def PROMPT_FOR_TASK(description):
    return {"role" : "user", "content":
    f"""
    Все plt.savefig(sys.argv[n], ...) должны быть записаны именно так.
    plt.savefig(filename, ...) НЕЛЬЗЯ
    Так же не используй input, все только через argv если в условиях не сказано иначе
    Условия: {description}
    Пример Вывода: ```python [CODE]```
    """}