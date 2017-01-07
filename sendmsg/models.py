from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from sendsms.message import SmsMessage
from rest_framework.authtoken.models import Token

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True)

    REQUIRED_FIELDS = ['phone_number', 'email']

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


@receiver(post_save, sender=Token, dispatch_uid="send_sms_to_user")
def send_sms_signal(sender, instance, **kwargs):
    msg = SmsMessage(body=instance.key+" is the token", from_phone="Santosh", to=[instance.user.phone_number])
    msg.send()


