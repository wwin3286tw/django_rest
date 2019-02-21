from rest_framework import serializers
from joystick_api.models import User


class JAPI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        #fields = (username,gender,phone,email,userpass,uuid,birthday,fb_access_token,fb_userid,job,lastlogin,reg_datetime,token,account_status,share_code,registration_validation_email_token,share_ui_field,today_sned_reset_password_mail_count,reset_pass_token,reset_password_datetime)
        fields = ('username','email','userpass','user_uuid')
