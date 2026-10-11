from queue import Queue

requests = Queue()


def generate_request():
    request = "new request"
    requests.put(request)
    print("request added")


def process_request():
    if not requests.empty():
        request = requests.get()
        print(f"processing: {request}")
    else:
        print("no requests to process")


while True:
    command = input("press ENTER to continue or type E to exit: ")

    if command.lower() == "e":
        break

    generate_request()
    process_request()