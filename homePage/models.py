from django.db import models
from django.contrib.auth.models import User
from django.forms import TextInput
from datetime import datetime
from django.db.models.signals import post_save
import uuid



#-- User Database --
class Member(models.Model):
    MobileNo = models.CharField("User's Mobile Number", max_length=10,blank=True)
    category = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usn = models.CharField("Student User's Mobile Number", null=True,blank=True,max_length=10)
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    uniqueID = models.CharField("Unique Reg ID", null=True,blank=True,max_length=64)

    def __str__(self):
        return self.user.first_name

def create_member(sender,**kwargs):
    if kwargs["created"]:
        new_member=Member.objects.create(user=kwargs["instance"])

post_save.connect(create_member,sender=User)


#-- Payment Database --


#--NewsFeed Database--
class NewsFeed(models.Model):

    Title = models.CharField("Title", max_length=50)
    Content = models.CharField("Content", max_length=1000)
    #Image = models.ImageField(upload_to=None, height_field=50, width_field=50, max_length=100)
    Category = models.CharField("Category", max_length=50)
    CreatedBy = models.CharField("CreatedBy User ID", max_length=10)
    CreatedOn = datetime.now()
    UpdatedBy = models.CharField("UpdatedBy User ID", max_length=10, null=True)
    UpdatedOn = models.DateField(null=True)
    Priority = models.IntegerField(default=1)

#--Events Database--
class Events(models.Model):

    EventName = models.CharField("Event Name", max_length=50)
    Description = models.CharField("Event Description", max_length=1000)
    #Image = models.ImageField(upload_to=None, height_field=50, width_field=50, max_length=100)
    Organiser1 = models.CharField("Organisers1 Name", max_length=50)
    Organiser2 = models.CharField("Organisers2 Name", max_length=50)
    Organiser3 = models.CharField("Organisers3 Name", max_length=50)
    MobileNo1 = models.CharField("Organiser1's Mobile Number", max_length=10)
    MobileNo2 = models.CharField("Organiser2's Mobile Number", max_length=10)
    MobileNo3 = models.CharField("Organiser3's Mobile Number", max_length=10)
    IsActive = models.BooleanField()


# --Donation Database--
'''class Donation(models.Model):
    DonationID = models.AutoField(primary_key=True)
    TransactionID = models.CharField("Transaction ID", max_length=50,unique=True)
    EmailID = models.ForeignKey('User',on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Status = models.IntegerField()
    TransactionDateTime = datetime.now()'''

#--FeedBack Database--
class Feedback(models.Model):

    Name = models.CharField("Name", max_length=100)
    EmailID = models.EmailField("Email Id", max_length=254)
    Comment = models.CharField("Feedback....", max_length=1000)



# Create your models here.
