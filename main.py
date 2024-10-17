import json 
import requests
from bs4 import BeautifulSoup
import re

author_list_g = ['Albert Einstein', 'Alexandre Dumas fils', 'Alfred Tennyson', 'Allen Saunders', 'André Gide', 'Ayn Rand', 'Bob Marley', 'C.S. Lewis', 'Charles Bukowski', 'Charles M. Schulz', 'Douglas Adams', 'Dr. Seuss', 'E.E. Cummings', 'Eleanor Roosevelt', 'Elie Wiesel', 'Ernest Hemingway', 'Friedrich Nietzsche', 'Garrison Keillor', 'George Bernard Shaw', 'George Carlin', 'George Eliot', 'George R.R. Martin', 'Harper Lee', 'Haruki Murakami', 'Helen Keller', 'J.D. Salinger', 'J.K. Rowling', 'J.M. Barrie', 'J.R.R. Tolkien', 'James Baldwin', 'Jane Austen', 'Jim Henson', 'Jimi Hendrix', 'John Lennon', 'Jorge Luis Borges', 'Khaled Hosseini', "Madeleine L'Engle", 'Marilyn Monroe', 'Mark Twain', 'Martin Luther King Jr.', 'Mother Teresa', 'Pablo Neruda', 'Ralph Waldo Emerson', 'Stephenie Meyer', 'Steve Martin', 'Suzanne Collins', 'Terry Pratchett', 'Thomas A. Edison', 'W.C. Fields', 'William Nicholson']

def machen_authors():     
    authors_list = []   

    for i in author_list_g:
        # Об'єднана заміна пробілів і крапок
        result = re.sub(r'[ .]+', '-', i)
        
        url = f'https://quotes.toscrape.com/author/{result}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Перевірка наявності елементів
        born_date = soup.find('span', class_='author-born-date')
        born_location = soup.find('span', class_='author-born-location')
        description = soup.find('div', class_='author-description')

        if born_date and born_location and description:
            authors_list.append({
                "fullname": i, 
                "born_date": born_date.text.strip(), 
                "born_location": born_location.text.strip(), 
                "description": description.text.strip()
            })
    
    return authors_list

def machen_qoutes():
    qoutes_list = []
   
    for e in range(1, 11):
        url = f'https://quotes.toscrape.com/page/{e}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        tags = soup.find_all('div', class_='tags')
        
        for i in range(len(quotes)):
            tags_list = [tag.text for tag in tags[i].find_all('a', class_='tag')]

            qoutes_list.append({
                'tags': tags_list, 
                'author': authors[i].text, 
                'quote': quotes[i].text
            })
            
    return qoutes_list

def json_machen():
    qoutes_list = machen_qoutes()
    authors_list = machen_authors()
    
    with open('qoutes.json', 'w', encoding='utf-8') as json_file:
        json.dump(qoutes_list, json_file, indent=4, ensure_ascii=False)   
    print('Die Datei qoutes.json wurde erfolgreich erstellt')
    
    with open('authors.json', 'w', encoding='utf-8') as json_file:
        json.dump(authors_list, json_file, indent=4, ensure_ascii=False)  
    print('Die Datei authors.json wurde erfolgreich erstellt')


if __name__ == '__main__':
    json_machen()

    

