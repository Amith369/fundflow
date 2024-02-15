from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Transaction(models.Model):
    title=models.CharField(max_length=200)
    amount=models.PositiveIntegerField()
    options=(
        ("expense","expense"),
        ("income","income")
    )
    type=models.CharField(max_length=200,choices=options,default="expense")
    cat_options=(
        ("fuel","fuel"),
        ("food","food"),
        ("entertainment","entertainment"),
        ("emi","emi"),
        ("bills","bills"),
        ("miscellaneous","miscellaneous")
    )
    category=models.CharField(max_length=200,choices=cat_options,default="miscellaneous")
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    user_object=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title