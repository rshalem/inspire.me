from django.test import TestCase

# Create your tests here.


# user subsribes via mail
# after submit, an email is stored on the EmailStore
# send mail to subscribed mail list
# if first time, then welcome to inspire.me mail to new joinees
# now whenever a new motivation is saved into the database, using post_save signal, send email to all email objects
