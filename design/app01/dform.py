from django import forms
from django.forms import widgets
from app01 import models
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    # User类中加str方法
    # usertype = forms.ModelChoiceField(queryset=models.User.objects.values_list("id","caption"),
    #                                   empty_label="请选择用户类型",
    #                                   to_field_name="id")不用重写init方法 也可以刷新后更新内容,to_field_name:select value=

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

    # def clean_username(self):
    #     value = self.cleaned_data["username"]
    #     if value == "root":
    #         return value
    #     else:
    #         raise ValidationError("你不是我")

    def _post_clean(self):
        v1 = self.cleaned_data["username"]
        v2 = self.cleaned_data["password"]
        if v1 == "root" and v2 == "1234":
            pass
        else:
            self.add_error("__all__", ValidationError('用户名或者密码错误'))

    #此方法取值要把obj.clean()换成obj.cleaned_data
    # def clean(self):
    #     v1 = self.cleaned_data["username"]
    #     v2 = self.cleaned_data["password"]
    #     if v1 == "root" and v2 == "1234":
    #         pass
    #     else:
    #         raise ValidationError('用户名或者密码错误')
    #     return self.cleaned_data



