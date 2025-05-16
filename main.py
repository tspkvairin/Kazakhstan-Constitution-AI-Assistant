import subprocess

def ask_ollama(question, context):
    prompt = f"Ответь на основе следующего текста Конституции Казахстана:\n\n{context}\n\nВопрос: {question}\nОтвет:"
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        capture_output=True,
    )
    return result.stdout.decode()

def main():
    with open("constitution.txt", "r", encoding="utf-8") as f:
        context = f.read()

    print("🇰🇿 AI Assistant: Конституция Республики Казахстан")
    print("Введите вопрос (или 'выход' для завершения):")

    while True:
        question = input("Вопрос: ")
        if question.lower() in ["выход", "exit", "quit"]:
            break
        answer = ask_ollama(question, context)
        print("\nОтвет:")
        print(answer.strip())
        print("-" * 50)

if __name__ == "__main__":
    main()
