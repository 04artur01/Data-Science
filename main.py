from lib import generate_urls

import requests
from bs4 import BeautifulSoup


def get_text(url, elements):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all(f"{elements}")
        text = "\n".join([i.text.strip() for i in paragraphs])
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch content from {url}. Reason: {e}")
        return None


def main():
    url = input("Enter URL (or 'q' to quit): ")
    if url.lower() == "q":
        return
    print("How many pages do you want to explore? (Enter the number): ")
    print("1. Just one")
    print("2. More than one")
    print("q. Quit")
    pattern = None
    choice = input()
    if choice == '1':
        pattern = None
    elif choice == '2':
        pattern = input("Enter page index search pattern (or 'q' to quit):  ")
    elif choice == 'q':
        return
    else:
        print("Invalid input")

    searched_elements = input("Enter search elements from HTML: ")

    domain = input('Enter the domain for the name of the link file: ')
    if not domain:
        print("Domain cannot be empty. Exiting.")
        return

    urls = generate_urls(url, pattern)
    print(urls)

    with open(f'({domain})urls.txt', 'w') as out:
        for i, generated_url in enumerate(urls, 1):
            out.write(f'URL #{i}: {generated_url}\n')

    with open(f'({domain})responses.txt', 'w') as out:
        tmp = 1
        for generated_url in urls:
            tmp += 1
            text = get_text(generated_url, searched_elements)
            if text:
                out.write(f'\n{text}\n')
            else:
                out.write(f'No text found on the url #{tmp} \n')


if __name__ == "__main__":
    main()
