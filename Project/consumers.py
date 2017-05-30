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
    # Initialise their session
    message.reply_channel.send({
        'accept': True
    })
    print("-------------------------------------------------------------------------")
    subs.append({'id': message.reply_channel, 'room': 1})
    print(subs)
    # Channel("chat.receive").add(message.reply_channel)


# Unpacks the JSON in the received WebSocket frame and puts it onto a channel
# of its own with a few attributes extra so we can route it
# we preserve message.reply_channel (which that's based on)
@enforce_ordering
def ws_receive(message):

    msg = message['text']
    command = msg[msg.find("command") + len("command") + 3: (msg.find("command") + len("command") + 3) + len("send")]
    txt = msg[msg.find("text") + len("text") + 3: (msg.find("text") + len("text") + 3) + len("chat")]
    room = msg

    print("####################################### " + txt)
    print(message['text'])
    if command == "send":
        # if request.method == "POST":
        # username = request.POST.get('user', None)
        # group_id = request.POST.get('group', None)

        # print(group_id)
        # togroup = Group.objects.get(pk=group_id)
        # user = Users.objects.get(user__username=username)

        # # print(group);
        # newmember = Member(group=togroup, member=user)
        # newmember.save()

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
    # Unsubscribe from any connected rooms
    pass


# Chat channel handling ###

def chat_start(message):
    # Genearlly add them to a room, or do other things that should be
    # done when the chat is started
    # print("AT CHAT")
    # message.reply_channel.send({
    #     'accept': True
    # })
    pass


def chat_leave(message):
    # Reverse of join - remove them from everything.
    # if user logged in:
    #   find the current room with job id and user id
    #   remove the room_id from the list for this channel
    #   remove this reply_channel from the group associated with the room
    pass


def chat_send(message):
    # First send the candidate message in the right format for
    # chatbot to print it on the message channel
    print("****************************************************************")
    message_to_send_content = {
        'text': message['text'],
        'type': 'text',
        'source': 'SENDER'
    }
    # message.reply_channel.send({
    #     'text': json.dumps(message_to_send_content)
    # })

    #Call my view to actually construct the reseponse tothe query
    response = respond_to_websockets(
        message
    )

    # Reformat the reponse and send it to the html to print
    # response['source'] = 'BOT'
    # message.reply_channel.send({
    #     'text': json.dumps(response)
    # })
