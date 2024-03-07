import re


# Find page count in URL
def find_url_page_count(link, pattern):
    if pattern:
        page_count_pattern = rf'{pattern}(\d+)'
        match = re.search(page_count_pattern, link)
        if match:
            page_count = int(match.group(1))
            return page_count
    else:
        return


# Find page index in URL
def find_url_page_index(link, pattern):
    if pattern:
        page_index_pattern = rf'{pattern}(\d+)'
        match = re.search(page_index_pattern, link)
        if match:
            page_index = match.end()
            return page_index
    else:
        return


def count_of_numbers(num):
    count = 1
    if num >= 10:
        while num > 10:
            num /= 10
            count += 1
        return count
    else:
        return count


# Generate URL-s
def generate_urls(url, pattern):
    if pattern:
        page_last_index = find_url_page_index(url, pattern)
        page_count = find_url_page_count(url, pattern)
        page_first_index = (page_last_index - count_of_numbers(page_count))
        urls = []
        for get_page in range(1, (page_count + 1)):
            generated_url = url[:page_first_index] + str(get_page) + url[page_last_index:]
            urls.append(generated_url)
        return urls
    else:
        urls = [url]
        return urls
