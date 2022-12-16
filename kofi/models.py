from django.db import models


# Create your models here.
class Hook(models.Model):
    message_id = models.CharField(primary_key=True, max_length=255)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)
    from_name = models.CharField(max_length=255)
    message = models.TextField()
    amount = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    currency = models.CharField(max_length=9)
    is_subscription_payment = models.BooleanField(default=False)
    is_first_subscription_payment = models.BooleanField(default=False)
    kofi_transaction_id = models.CharField(max_length=255)
    shop_items = models.TextField(null=True)
    tier_name = models.CharField(null=True, max_length=255)
    shipping = models.TextField(null=True)

    def __str__(self):
        return f'{self.message_id} [{self.email}]'