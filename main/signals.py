# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import *


# @receiver(post_save, sender=Card)
# # sender to ensure receiver is only invoked when signal is sent by Card Model save
# def post_card_save_email_send(sender, created, instance, **kwargs):
#     if created:
#         all_mailing_list = EmailStore.objects.all()
#         subject = 'New post'
#         quote = Card.objects.order_by('-id')[0]

#         message = quote.content + "" + 'by' + "" + quote.said_by 

#         send_mail(subject=subject, message=message, from_email='hello@xyz.com', recipient_list=all_mailing_list, fail_silently=False)

#     else:
#         instance.save()


"""if you create a separate signals make sure to add it in AppConfig file inside ready function
and then use <app_name>.apps.<app_nameConfig> rather only app name in INSTALLED APPS
if u don't, then add default_app_config = '<app_name>.apps.<app_nameConfig>' in init.py"""