import requests
from bs4 import BeautifulSoup


def get_links(url, depth, max_depth, output_type):
    if depth > max_depth:
        return []

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a')]

        for link in links:
            if link.startswith("http://") or link.startswith("https://"):
                if output_type == 'console':
                    print(link)
                elif output_type == 'file':
                    with open('links.txt', 'a') as file:
                        file.write(link + '\n')
                get_links(link, depth + 1, max_depth, output_type)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: {e}")


def main():
    url = input("Введите URL: ")
    max_depth = int(input("Введите максимальную глубину поиска: "))
    output_type = input("Введите 'console' или 'file' для выбора типа вывода: ").lower()

    if output_type == 'file':
        with open('links.txt', 'w') as file:
            file.write(f"{url}\n")

    get_links(url, 1, max_depth, output_type)

if __name__ == "__main__":
    main()
