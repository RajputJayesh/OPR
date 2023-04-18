from django.db import models

# Create your models here.

class Add(models.Model):
    CH1=((1,'Two Wheeler'),(2,'Four Wheeler'))
    CH2=((1,'Paid'),(2,'Not Paid'))
    token=models.CharField(max_length=5,verbose_name="Token Number")
    Name=models.CharField(max_length=50, verbose_name="Name")
    phone=models.CharField(max_length=11,verbose_name="Phone no")
    v_type=models.IntegerField(choices=CH1,verbose_name="Vehicle Type")
    v_number=models.CharField(max_length=50,verbose_name="Vehicle Number")
    payment=models.IntegerField(choices=CH2,verbose_name="Payment")
    v_park=models.CharField(max_length=50,verbose_name="Vehicle Prak By")
    Created_on=models.DateTimeField(verbose_name="Date Of Creation")
    uid=models.IntegerField()

    def __str__(self):
        return self.token

class Exit(models.Model):
    token=models.CharField(max_length=5)
    Name=models.CharField(max_length=50)
    phone=models.CharField(max_length=11)
    v_type=models.IntegerField()
    v_number=models.CharField(max_length=50)
    v_park=models.CharField(max_length=50,verbose_name="Vehicle Prak By")
    payment=models.IntegerField()
    Created_onn=models.DateTimeField()
    

    


class Feedback(models.Model):
    Name=models.CharField(max_length=50,verbose_name="Name")
    E_mail=models.CharField(max_length=50,verbose_name="E Mail")
    sub=models.CharField(max_length=50,verbose_name="Subject")
    msg=models.CharField(max_length=500,verbose_name="Message")
    Created_on=models.DateTimeField(verbose_name="Date of Creation")