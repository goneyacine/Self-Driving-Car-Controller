import socket
import threading
import json
import policy_gradient
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),2183))


def data_to_state(data):
    data = json.loads(data)
    state = [data['angle']]
    for point in data['points']:
        state.append(point[0])
        state.append(point[1])
    return state

def handle_client(client_socket):
    model = policy_gradient.model()
    steps_data = []
    predictions = []
    while True:
        data = client_socket.recv(1024)
        if not data:
          break  # If the client disconnects, exit the loop
        message = data.decode('utf-8')
        state = data_to_state(message)
        steps_data.append(state)
        prediction = model.predict(state=state)
        predictions.append(prediction)
        client_socket.send(bytes(str(prediction),'utf-8'))
        if(len(predictions) == 100):
            predictions = []
            steps_data = []       

s.listen(1)
while True:
  client_socket, client_address = s.accept()
  print(f"Accepted connection from {client_address}") 
  client_handler = threading.Thread(target=handle_client, args=(client_socket,))
  client_handler.start()