from django.db import models

class login(models.Model):
    Username=models.CharField(max_length=150)
    Password=models.CharField(max_length=130)
    UserType=models.CharField(max_length=100)

    def __str__(self):
        return self.Username

class DeliveryPerson_Profile(models.Model):
    Username = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name,self.PhoneNo


class Delivery(models.Model):
    user_profile = models.ForeignKey(DeliveryPerson_Profile,default=1,on_delete=models.CASCADE)
    ticket_name = models.CharField(max_length=120)
    delivery_date=models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    delivery = models.ForeignKey(Delivery,default=1,on_delete=models.CASCADE)
    image_type = models.CharField(max_length=50)
    image_file = models.CharField(max_length=300)

    def __str__(self):
        return self.image_type



