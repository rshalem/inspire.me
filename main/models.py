from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Card(models.Model):
    index_no = models.CharField(max_length=10)
    content = models.TextField()
    said_by = models.CharField(max_length=50)
    likes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.content


class EmailStore(models.Model):
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.email

@receiver(post_save, sender=Card)
# sender to ensure receiver is only invoked when signal is sent by Card Model save
def post_card_save_email_send(sender, created, instance, **kwargs):
    if created:
        all_mailing_list = EmailStore.objects.all()
        subject = 'New post'
        quote = Card.objects.order_by('-id')[0]

        message = quote.content + ' by ' + quote.said_by 

        send_mail(subject=subject, message=message, from_email='hello@xyz.com', recipient_list=all_mailing_list, fail_silently=False)

    else:
        instance.save()