from celery import shared_task
from django.core.mail import send_mail


@shared_task
def notify_order_saved(planreg_pk, name):
    # from time import sleep
    # sleep(3)

    send_mail(
        f"Planreg #{planreg_pk} saved",
        f"Here is the message. Planreg #{planreg_pk}, name: {name}",
        "from@example.com",
        ["to@example.com"],
        fail_silently=True,
    )