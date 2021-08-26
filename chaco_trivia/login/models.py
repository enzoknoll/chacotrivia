from django.db import models
from django.db.models.deletion import DO_NOTHING
 
# Create your models here
# class category(models.Model):
#     nombre = models.CharField(max_length=200,null=True)

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    # categoria = models.ForeignKey(category, on_delete=DO_NOTHING)

    
    def __str__(self):
        return self.question