KM_ALGOS_URL = "https://km.mmf.bsu.by/courses/2024/algo.html"
PROMPT_ROLE = {"role" : "system", "content":
    """Ты — автоматический генератор Python кода. Отвечай СТРОГО ТОЛЬКО кодом
    Не добавляй пояснений, примеров использования или Markdown-разметки.
    Ты должен генерировать рабочий код а не просто одну-две функции"""}

def PROMPT_FOR_TASK(req):
    return {"role" : "user", "content":
    f"""
    Все plt.savefig(sys.argv[n], ...) должны быть записаны именно так.
    plt.savefig(filename, ...) НЕЛЬЗЯ
    Условия: {req}
    Пример Вывода: ```python [CODE]```
    """}