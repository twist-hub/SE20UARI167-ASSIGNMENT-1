import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connection to server successful')

@sio.on('response')
def on_response(data):
    print(data['response'])
    sio.disconnect()

if __name__ == '__main__':
    message_to_send = input("Please input your message:- ")

    sio.connect('http://localhost:6954')
    sio.emit('send_message', {'message': message_to_send})
    sio.wait()