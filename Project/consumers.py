import json
from channels import Channel
from channels import Group
from channels.sessions import enforce_ordering
from whiteboard.models import Group, Member
from user_profile.models import Users

from .views import respond_to_websockets

subs = []
@enforce_ordering
def ws_connect(message):
    message.reply_channel.send({
        'accept': True
    })
    subs.append({'id': message.reply_channel, 'room': 1})


@enforce_ordering
def ws_receive(message):

    msg = message['text']
    command = msg[msg.find("command") + len("command") + 3: (msg.find("command") + len("command") + 3) + len("send")]
    txt = msg[msg.find("text") + len("text") + 3: (msg.find("text") + len("text") + 3) + len("chat")]
    # room = msg[msg.find("room") + len("room") + 3: (msg.find("text") + len("text") + 3) + len("chat")]

    print("####################################### " + txt)
    print(message['text'])
    if command == "send":
        for reply_channel in subs:
            #print(reply_channel['room']) if reply_channel['room'] == client.room
            reply_channel['id'].send({
                'text': json.dumps({
                'text': message['text'],
                'type': 'text',
                'source': txt
                })
                    })
    # print(message.channel_session)
    # payload = json.loads(message['text'])
    # payload['reply_channel'] = message.content['reply_channel']
    # print(payload);
    # Channel("chat.receive").send(payload)

@enforce_ordering
def ws_disconnect(message):
    pass


# Chat channel handling ###

def chat_start(message):
    pass


def chat_leave(message):
    pass


def chat_send(message):
    message_to_send_content = {
        'text': message['text'],
        'type': 'text',
        'source': 'SENDER'
    }

    response = respond_to_websockets(
        message
    )
