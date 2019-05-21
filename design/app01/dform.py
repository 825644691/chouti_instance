from django import forms
from django.forms import widgets


class UserForm(forms.Form):
    username = forms.SlugField(min_length=9, label="用户名:", widget=widgets.TextInput(attrs={"placeholder": "请输入您的用户名"}),
                               error_messages={"required": "用户名不能为空",
                                               "min_length": "用户名不能少于8位",
                                               "invalid": "用户名要包含英文"})
    password = forms.SlugField(min_length=8, label="密码:", widget=widgets.PasswordInput(attrs={"placeholder": "请输入您的密码"}),
                               error_messages={"required": "密码不能为空",
                                               "min_length": "密码不能少于8位",
                                               "invalid": "密码要包含英文"}
                               )
    email = forms.CharField(widget=widgets.EmailInput(attrs={"placeholder": "请输入您的邮箱"}), label="邮箱:",
                            error_messages={"required": "邮箱不能为空",
                                            "invalid": "邮箱格式不对"}
                            )
