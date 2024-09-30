from queue import Queue

#Створити чергу заявок
queue = Queue()

def generate_request():
    request = f"Request {queue.qsize() + 1}"
    queue.put(request)
    print(f"Заявку {request} додано до черги")

def process_request():
     if not queue.empty():
        request = queue.get()
        print(f"Заявку {request} оброблено")
     else:
        print("Черга пуста")


while True:
    while not queue.empty():
        generate_request() #для створення нових заявок
        process_request() #для обробки заявок
