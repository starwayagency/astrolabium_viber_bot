
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import logging
from django.http import HttpResponse
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest


# сюда нужно вставить инфу со своего бота
viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='https://st.depositphotos.com/1288351/3081/i/600/depositphotos_30815063-stock-photo-paint-smears.jpg',
    auth_token='4e2cbddffca7e23a-177120b28983c523-2a880a9cda9967cf'
))

viber.set_webhook('https://astrolabiumviberbot.starway.agency/incoming/')


def incoming(request):
    print("received request. post data: {0}".format(request.POST))
    # every viber message is signed, you can verify the signature using this method
    # if not viber.verify_signature(request.POST, request.headers.get('X-Viber-Content-Signature')):
    #     return HttpResponse(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.POST)

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        # lets echo back
        viber.send_messages(viber_request.sender.id, [
            message
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        print("client failed receiving message. failure: {0}".format(viber_request))

    return HttpResponse(status=200)


def test_view(request):
    return HttpResponse('asdasdasda')


# http://starway.agency:8010/incoming/