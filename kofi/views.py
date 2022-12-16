from django.http import HttpResponse
from .models import Hook
from django.views.decorators.csrf import csrf_exempt
import json, os


# Create your views here.
def index(request):
    return HttpResponse('kofi-index-ok')


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        strdata = request.POST.get("data")
        jsondata = json.loads(strdata)
        token = jsondata.get('verification_token')
        if token == os.environ['KOFI_VERIFICATION_TOKEN']:
            hook = Hook(
                message_id=jsondata.get('message_id'),
                timestamp=jsondata.get('timestamp'),
                type=jsondata.get('type'),
                is_public=jsondata.get('is_public'),
                from_name=jsondata.get('from_name'),
                message=jsondata.get('message'),
                amount=jsondata.get('amount'),
                url=jsondata.get('url'),
                email=jsondata.get('email'),
                currency=jsondata.get('currency'),
                is_subscription_payment=jsondata.get(
                    'is_subscription_payment'),
                is_first_subscription_payment=jsondata.get(
                    'is_first_subscription_payment'),
                kofi_transaction_id=jsondata.get('kofi_transaction_id'),
                shop_items=jsondata.get('shop_items'),
                tier_name=jsondata.get('tier_name'),
                shipping=jsondata.get('shipping'))
            hook.save()
            print(f'Hook Saved {hook.message_id}')
            return HttpResponse(status=200, content='kofi-webhook-ok')
        else:
            return HttpResponse(status=400,
                                content='Invalid verification token')
    else:
        return HttpResponse(status=400, content='Only POST is allowed')


@csrf_exempt
def supporter(request, limit):
    body = ''
    hooks = Hook.objects.all().order_by('-timestamp')[:limit]
    for hook in hooks:
        body += hook.from_name + "\n"
    return HttpResponse(status=200, content=body)


@csrf_exempt
def supporters(request):
    body = ''
    hooks = Hook.objects.all().order_by('-timestamp')
    for hook in hooks:
        body += hook.from_name + "\n"
    return HttpResponse(status=200, content=body)
