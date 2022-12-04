from django.db import models
choices=[
     ('Male','MALE'),
     ('Female','FEMALE'),
     ('Others','OTHERS'),

]
# Create your models here.
class Childdetails(models.Model):
    Sno=models.IntegerField(verbose_name="Sno")
    Child_Name=models.CharField(verbose_name="Child_Name",max_length=30)
    Child_UIDNo=models.IntegerField(verbose_name="Child_UIDNo")
    Gender=models.CharField(verbose_name="Gender",max_length=30)
    Mother_Name = models.CharField(verbose_name="Mother_Name",max_length=30)
    Mother_UIDNo = models.IntegerField(verbose_name="Mother_UIDNo")
    Father_Name = models.CharField(verbose_name="Father_Name",max_length=30)
    Father_UIDNo = models.IntegerField(verbose_name="Father_UIDNo")
    Ration_CardNo = models.IntegerField(verbose_name="Ration_CardNo")
    Mobile_No = models.IntegerField(verbose_name="Mobile_No")
#
#
# class DataModel(models.Model):
#
#

