from django.db import models

# Create your models here.
class profile(models.Model):
    GENDER =(
        ('Male' , 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    RELIGIONS =(
        ('Islam', 'Islam'),
        ('HIndu', 'HIndu'),
        ('Others', 'Others')
    )
    BLOOD_GROOP =(
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-")
    )


    Name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='prof_pic/', default= "def.png.jpg")
    email = models.EmailField(max_length=20)
    phone_number = models.TextField(max_length=14)
    gender = models.CharField(choices=GENDER, max_length= 10, default="Male")
    address =models.TextField(max_length=40)
    religions=models.CharField(choices= RELIGIONS, max_length=10, default="Islam")
    blood_groop =models.CharField(choices= BLOOD_GROOP, max_length= 10, default="o+")
    date_of_birth =models.CharField(max_length=10)
    is_alive = models.BooleanField(default=True, null= True, blank=True)

    def __str__(self):
        return self.Name
