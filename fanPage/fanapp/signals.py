from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.core.mail import send_mail
from .models import Reply, UsersReplys, Ad


@receiver(post_save, sender = Reply)
def send_tracking_email(sender, instance, created, **kwargs):
    if created:
        print("-----------------------------------------------------------")
        adAuthor = Ad.objects.get(id = instance.ad.id).author.email
        replyAuthor = instance.user.username
        recipient =[adAuthor]
        send_mail( 
            subject = f'На вашем объявлении новый отклик от {replyAuthor}' ,
            message = f'Вы можете прочитать новый отклик в своем личном кабинете, а также принять или сохранить', 
            from_email = 'linkamal1nka@yandex.ru', 
            recipient_list = recipient
        )


@receiver(post_save, sender = UsersReplys)
def send_tracking_email(sender, instance, created, **kwargs):
    if created:
        print("-----------------------------------------------------------")
        replyReciver = instance.reciever.username
        acceptedReply = instance.reply
        replyAuthor = Reply.objects.get(id=acceptedReply.id).user.email
        recipient =[replyAuthor]
        send_mail( 
            subject = f'Ваш отклик приняли!' ,
            message = f'Пользователь {replyReciver} принял ваш отклик!', 
            from_email = 'linkamal1nka@yandex.ru', 
            recipient_list = recipient
        )