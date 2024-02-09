import socket

PORT = 5555
MAX_TASK_LENGTH = 256

def send_data(socket, data):
    socket.send(data.encode('utf-8'))

def receive_data(socket):
    data = socket.recv(MAX_TASK_LENGTH).decode('utf-8')
    print(data)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', PORT))
    
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            data = f"ADD {task}"
            send_data(client_socket, data)
        elif choice == '2':
            send_data(client_socket, "LIST")
            receive_data(client_socket)
        elif choice == '3':
            client_socket.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
