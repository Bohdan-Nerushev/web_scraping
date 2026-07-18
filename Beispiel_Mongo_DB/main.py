from models import Qoutes, Authors
import connect

# === ==== === #

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError, TypeError) as e:
            return str(e)
    return inner

# === ==== === #

@input_error
def name(key, value):
    quotes_list_1 = []
    author = Authors.objects(fullname=value).first()
    if author:
        quotes = Qoutes.objects(author=author)
        for quote in quotes:
            quotes_list_1.append(quote.quote.encode('utf-8').decode('utf-8'))
        return quotes_list_1
    else:
        return "Author not found."
    
@input_error
def tag(key, value):
    quotes_list_2 = []
    quotes = Qoutes.objects(tags=value)
    for quote in quotes:
        quotes_list_2.append(quote.quote.encode('utf-8').decode('utf-8'))
    return quotes_list_2

@input_error
def tags(key, value):
    quotes_list_3 = []
    tags = value.split(',')
    quotes = Qoutes.objects(tags__in=tags)
    for quote in quotes:
        quotes_list_3.append(quote.quote.encode('utf-8').decode('utf-8'))
    return quotes_list_3


# === ==== === #

def main():
    while True:
        try:
        
            command = input("Enter command: ").strip()
            if command.lower() in ['exit', 'close', 'stop']:
                break
            
            key, value = command.split(':')
            key, value = key.strip(), value.strip()
            
            if key == 'name':
                print(*name(key, value))
                    
            elif key == 'tag':
                print(*tag(key, value))
                    
            elif key == 'tags':
                print(*tags(key, value))
                    
            else:
                print("Unknown command. Try again.")
                
        except ValueError:
            print("Invalid command format. Try again.")
            
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()



    
