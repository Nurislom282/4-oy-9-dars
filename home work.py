#1
import threading

def sum_digits_part(digits, result, index):
    result[index] = sum(int(digit) for digit in digits)
def sum_of_digits_multithreaded(number, num_threads=2):
    digits = str(number)
    length = len(digits)
    part_size = length // num_threads
    threads = []
    results = [0] * num_threads

    for i in range(num_threads):
        start_index = i * part_size
        end_index = (i + 1) * part_size if i != num_threads - 1 else length
        thread = threading.Thread(target=sum_digits_part, args=(digits[start_index:end_index], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return sum(results)

result = sum_of_digits_multithreaded(108, num_threads=2)
print(result)
#2
import threading

def convert_seconds(seconds):
    def calculate_days():
        nonlocal days
        days = seconds // 86400

    def calculate_hours():
        nonlocal hours
        hours = (seconds % 86400) // 3600

    def calculate_minutes():
        nonlocal minutes
        minutes = (seconds % 3600) // 60

    def calculate_remaining_seconds():
        nonlocal remaining_seconds
        remaining_seconds = seconds % 60

    days = hours = minutes = remaining_seconds = 0

    threads = [
        threading.Thread(target=calculate_days),
        threading.Thread(target=calculate_hours),
        threading.Thread(target=calculate_minutes),
        threading.Thread(target=calculate_remaining_seconds)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    return days, hours, minutes, remaining_seconds
seconds = 91000
days, hours, minutes, remaining_seconds = convert_seconds(seconds)
print(f"{seconds} sekund = {days} kun, {hours} soat, {minutes} minut, {remaining_seconds} sekund.")
#3
import threading

def capitalize_name(name, result, index):
    result[index] = name.capitalize()
def capitalize_names(names):
    threads = []
    result = [None] * len(names)
    for index, name in enumerate(names):
        thread = threading.Thread(target=capitalize_name, args=(name, result, index))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return result

names = ['alfred', 'tabitha', 'william', 'arla']
result = capitalize_names(names)
print(result)
#4
import threading
def filter_scores(scores, threshold, result, index):
    filtered = [score for score in scores if score > threshold]
    result[index] = filtered
def main():
    scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
    threshold = 75
    num_threads = 2
    chunk_size = len(scores) // num_threads
    threads = []
    results = [None] * num_threads
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = start_index + chunk_size if i != num_threads - 1 else len(scores)
        thread = threading.Thread(target=filter_scores, args=(scores[start_index:end_index], threshold, results, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    filtered_scores = [score for sublist in results for score in sublist]
    print(filtered_scores)
#5
import threading

def is_palindrome(word, results, index):
    word = word.lower()
    results[index] = word == word[::-1]
def find_palindromes(words):
    threads = []
    results = [None] * len(words)
    for index, word in enumerate(words):
        thread = threading.Thread(target=is_palindrome, args=(word, results, index))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    palindromes = [word for word, is_pal in zip(words, results) if is_pal]
    return palindromes

words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
result = find_palindromes(words)
print(result)
#6
import threading
def replace_e_with_3(text, start, end, result, index):
    modified_text = []
    for i in range(start, end):
        if text[i] == 'e':
            modified_text.append('3')
        else:
            modified_text.append(text[i])
    result[index] = ''.join(modified_text)
def main():
    user_input = input("Foydalanuvchidan matn kiriting: ")
    num_threads = 4
    length = len(user_input)
    chunk_size = length // num_threads
    threads = []
    result = [None] * num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else length
        thread = threading.Thread(target=replace_e_with_3, args=(user_input, start, end, result, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    final_result = ''.join(result)
    print("Natija:", final_result)
#7
import threading
def remove_spaces(text):
    while ' ' in text:
        text = text.replace(' ', '')
    return text
def process_text():
    user_input = input("Matn kiriting: ")
    updated_text = remove_spaces(user_input)
    print(f"Yangilangan matn: {updated_text}")

if __name__ == "__main__":
    thread = threading.Thread(target=process_text)
    thread.start()
    thread.join()
#8
import requests
import threading

API_KEY = '9fcd25b521763c53b9de15f96d26d27a'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

cities = ['London', 'New York', 'Tokyo', 'Paris', 'Moscow']

def fetch_weather(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C")
        else:
            print(f"Failed to get weather data for {city}: {data['message']}")
    except Exception as e:
        print(f"An error occurred for {city}: {e}")

def main():
    threads = []
    for city in cities:
        thread = threading.Thread(target=fetch_weather, args=(city,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
