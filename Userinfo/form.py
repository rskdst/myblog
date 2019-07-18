from django import forms
from .models import *
from django.forms import widgets as wds
from  django.forms import fields
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import hashlib
def encrypt_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()


class RegisterForm(forms.Form):
    username = fields.CharField(label="用户名",strip=False,max_length=12,min_length=2,

                                error_messages={
                                    "max_length":"用户名不能超过12位",
                                    "min_length":"用户名不能低于两位",
                                    "required":"用户名不能为空"
                                },
                                validators=[RegexValidator(
                                    regex=r'^[\u4E00-\u9FA5A-Za-z0-9_]+$',
                                    message="用户名只能由汉字，数字，字母，下划线组成",
                                )],

                            )
    gender = fields.ChoiceField(label="性别",required=False,
                                choices=(
                                    ("男","男"),
                                    ("女","女")
                                ),
                                widget=wds.RadioSelect(attrs={

                                }),


                            )
    password1 = fields.CharField(label="密码",strip=False,max_length=20,min_length=8,widget=forms.PasswordInput,
                                 error_messages={
                                    "max_length":"密码不能超过20位",
                                    "min_length":"密码不能低于8位",
                                    "required":"密码不能为空"
                                }
                            )
    password2 = fields.CharField(label="确认密码",widget=forms.PasswordInput,
                                 error_messages={
                                    "required":""
                                }
                            )
    answer = fields.CharField(label="答案",max_length=50,
                              help_text ="可用于找回密码或修改密码",
                              error_messages={
                                    "max_length": "答案太长了",
                                    "required": "答案不能为空"
                            }

                        )
    def clean_password2(self):
        if self.errors:
            return self.errors
        else:
            if self.cleaned_data["password2"] != self.cleaned_data["password1"]:
                raise ValidationError("您输入的密码不一致，请重新输入")
            return self.cleaned_data
    def clean_username(self):
        username_tuple = UserInfo.objects.values_list("username").first()
        try:
            if self.cleaned_data["username"] in username_tuple:
                raise ValidationError("您输入的用户名已存在")
            else:
                return self.cleaned_data["username"]
        except:
            return self.cleaned_data["username"]


class LoginForm(forms.Form):
    username = fields.CharField(label="用户名",
                                error_messages={
                                    "required":"用户名不能为空"
                                },
                            )
    password = fields.CharField(label="密码",widget=forms.PasswordInput,
                                 error_messages={
                                    "required":"密码不能为空"
                                }
                            )
    def clean_username(self):
        try:
            username = UserInfo.objects.get(username=self.cleaned_data["username"])
            if username:
                return self.cleaned_data["username"]
            else:
                raise ValidationError("您输入的用户名或密码错误，请重新输入")
        except:
            raise ValidationError("您输入的用户名或密码错误，请重新输入")
    def clean_password(self):
        try:
            password = UserInfo.objects.filter(username=self.cleaned_data["username"]).first().password
            real_password  = encrypt_password(self.cleaned_data["password"])
            if real_password == password:
                return self.cleaned_data["password"]
            else:
                raise ValidationError("您输入的用户名或密码错误，请重新输入")
        except:
            raise ValidationError("您输入的用户名或密码错误，请重新输入")