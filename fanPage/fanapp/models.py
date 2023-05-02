from django.db import models
from django.contrib.auth.models import User






    

class Ad(models.Model):
    tanks = 'TA'
    heel = 'HL'
    damagediller = 'DD'
    seller = 'SL'
    geeldmaster = 'GM'
    questgivers = 'QG'
    blacksmith = 'BS'
    leatherworker = 'LW'
    posion = 'PW'
    spellmaster = 'SM'

    CAT = [
        (tanks, 'Танки'),
        (heel, 'Хилы'),
        (damagediller, 'ДД'),
        (seller, 'Торговцы'),
        (geeldmaster, 'Гилдмастеры'),
        (questgivers, 'Квестгиверы'),
        (blacksmith, 'Кузнецы'),
        (leatherworker, 'Кожевники'),
        (posion, 'Зельевары'),
        (spellmaster, 'Мастера заклинаний'),
    ]

    header = models.CharField(max_length = 64, 
                                default = "")
    text = models.TextField()
    mediaImg = models.ImageField(upload_to='images/', blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 2, 
                            choices = CAT, 
                            default = None)
    


class Reply(models.Model):
    text = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    accept = models.CharField(max_length = 64, 
                                default = "")
    

    def changeReply(self):
        self.accept = 'yes'
        self.save()

class UsersReplys(models.Model):
    reciever = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete =models.CASCADE)
