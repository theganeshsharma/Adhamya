from django.db import models
from django.contrib.auth.models import User
from django.forms import TextInput
from datetime import datetime
from django.db.models.signals import post_save
import uuid



#-- User Database --
class Member(models.Model):

    category = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usn = models.CharField("Student USN", null=True,blank=True,max_length=10)



    def __str__(self):
        return self.user.first_name

def create_member(sender,**kwargs):
    if kwargs["created"]:
        new_member=Member.objects.create(user=kwargs["instance"])

post_save.connect(create_member,sender=User)


#--Fest Tables--
class Fest(models.Model):
    name = models.CharField(max_length=50)
    organized_by = models.CharField(max_length=10)
    theme = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='static/imagess')

    def __str__(self):
        return self.name

#--NewsFeed Database--
class NewsFeed(models.Model):

    Title = models.CharField("Title", max_length=50)
    Content = models.CharField("Content", max_length=1000)
    Image = models.ImageField(upload_to='static/imagess')
    Category = models.CharField("Category", max_length=50)
    CreatedBy = models.CharField("CreatedBy User ID", max_length=10)
    CreatedOn = models.TimeField(default=datetime.now,editable=False)
    UpdatedBy = models.CharField("UpdatedBy User ID", max_length=10, null=True)
    UpdatedOn = models.DateField(null=True)
    Priority = models.IntegerField(default=1)

#--Events Database--
class Events(models.Model):
    FestName = models.ForeignKey(Fest,on_delete=models.CASCADE)
    EventName = models.CharField("Event Name", max_length=50)
    Description = models.CharField("Event Description", max_length=1000)
    Image = models.ImageField(upload_to='static/imagess')
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


class Subscribers(models.Model):
    email_id= models.CharField(max_length=50)

    def __str__(self):
        return str(self.email_id)
# Create your models here.

class Participation(models.Model):
    student = models.ForeignKey(Member,on_delete=models.CASCADE)
    activity = models.ForeignKey(Events,on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self):
        return str(self.student) + "'s registration to " + str(self.activity)
