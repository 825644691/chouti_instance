from django import forms
from django.forms import widgets
from django.forms import fields
from django.core import validators
from app01 import models


class DetailForm(forms.Form):
    user1 = forms.CharField(widget=widgets.TextInput(
        attrs={"class": "c1",
               "placeholder": "用户名"}))
    user2 = forms.CharField(required=False,label="姓名", initial="lxl", disabled=False, error_messages={"required": "不能为空"})
    user3 = forms.CharField(initial=2,widget=widgets.Select(choices=[]))
    telephone = forms.CharField(validators=[validators.RegexValidator(r"^[0-9]+$", message='请输入正确格式的手机号码！')]) #第三个code参数
    user4 = forms.FileField()

    def __init__(self,*args,**kwargs):
        super(DetailForm,self).__init__(*args,**kwargs)
        self.fields["user3"].widget.choices = models.Place.objects.all().values_list("id", "place")


class InitialForm(forms.Form):
    username = fields.CharField()
    user_type = fields.IntegerField(
        widget=widgets.Select(choices=[])
    )

    def __init__(self, *args, **kwargs):
        # 执行父类的构造方法
        super(InitialForm, self).__init__(*args, **kwargs)

        self.fields['user_type'].widget.choices = models.Place.objects.all().values_list('id', 'place')

#CharField(strip=true)是否移除用户空白
#SlugField(CharField)只允许数字，字母，下划线，减号(连字符)
#GenericIPaddressField()
#protocol="both"   both,ipv4,ipv6支持的ip格式
#unpack_ipv4=false 解析ipv4地址，ps：只有both才能使用