from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=32,verbose_name=u"使用者名稱")
    phone = models.TextField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    userpass = models.TextField(max_length=64)
    user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birthday = models.DateField(verbose_name=u"生日",default=u"1900-01-01")
    fb_access_token= models.TextField()
    fb_userid = models.TextField()
    lastlogin = models.DateTimeField(auto_now=True)
    job = models.IntegerField(null=True),
    reg_datetime =  models.DateTimeField(auto_now_add=True)
    gender_choices = (("male","男"),("female","女"))
    gender = models.CharField(max_length=6,choices = gender_choices,default=u"male")
    session_token = models.TextField(max_length=64)
    account_status = models.IntegerField(default=1)
    share_code = models.TextField(max_length=10)
    registration_validation_email_token = models.TextField(max_length=64)
    share_ui_field = models.TextField(max_length=16)
    today_sned_reset_password_mail_count = models.IntegerField(default=0)
    reset_pass_token = models.TextField(max_length=64)
    reset_password_datetime = models.DateTimeField(auto_now=True)

    class Meta:
       db_table = "user"
