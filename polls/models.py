from django.db import models

# Create your models here.
class HPmodel(models.Model):
    companyname = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    emailcheck = models.EmailField()
    Inquiry_Kind = (('1','ご依頼・ご相談'),('2', '廃墟について'),('3', 'ご意見・クレーム'),('4', 'その他お問い合わせ'))
    inquirykind = models.IntegerField(choices=Inquiry_Kind)
    number = models.IntegerField(null=True,blank=True)
    contents = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
