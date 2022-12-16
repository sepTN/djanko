#Create a fake ko-fi request and have it 'hooks' your endpoint

from faker import Faker
import os, requests, urllib, json, random, uuid

webhook_url = 'http://0.0.0.0:3000/kofi/webhook/'

locale = random.choice(['it_IT', 'en_US', 'es_ES', 'de_DE', 'fr_FR'])
fake = Faker(locale)
txid = str(uuid.uuid4())
data = {
    "verification_token": os.environ['KOFI_VERIFICATION_TOKEN'],
    "message_id": str(uuid.uuid4()),
    "timestamp": fake.date_time_this_year(),
    "type": "Donation",
    "is_public": True,
    "from_name": fake.name(),
    "message": fake.paragraph(nb_sentences=5, variable_nb_sentences=True),
    "amount": str(random.randint(1, 99)),
    "url": "https://ko-fi.com/Home/CoffeeShop?txid=" + txid,
    "email": fake.email(),
    "currency": "USD",
    "is_subscription_payment": True,
    "is_first_subscription_payment": True,
    "kofi_transaction_id": txid,
    "shop_items": None,
    "tier_name": None,
    "shipping": None
}

data_json = json.dumps(data, default=str)
data_url = 'data=' + urllib.parse.quote_plus(data_json)

request = requests.post(
    webhook_url,
    data=data_url,
    headers={"Content-Type": "application/x-www-form-urlencoded"})
