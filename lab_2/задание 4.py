import re
def extract_emails(text): "Извлекает email-адреса"
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def extract_phones(text): "Извлекает номера телефонов +7-XXX-XXX-XX-XX."
    pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
    return re.findall(pattern, text)

def extract_capital_words(text): "Извлекает слова, начинающ. с заглавной буквы"
    pattern = r'\b[A-ZА-ЯЁ][a-zа-яё]*\b'
    return re.findall(pattern, text)

def save_to_file(filename, data): "Сохраняет данные в файл, каждое значение с новой строки."
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item}\n")

def main():
    try:
        with open('text.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        emails = extract_emails(text)
        phones = extract_phones(text)
        capital_words = extract_capital_words(text)

        save_to_file('emails.txt', emails)
        save_to_file('phones.txt', phones)
        save_to_file('capital_words.txt', capital_words)

        print("Данные успешно извлечены и сохранены в файлы:")
        print(f"- emails.txt: {len(emails)} email-адресов")
        print(f"- phones.txt: {len(phones)} номеров телефонов")
        print(f"- capital_words.txt: {len(capital_words)} слов с заглавной буквы")

    except FileNotFoundError:
        print("Ошибка: Файл 'text.txt' не найден.")

if name == "main":
    main()
