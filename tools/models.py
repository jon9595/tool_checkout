from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class ToolType(models.Model):
    tool_type = models.CharField(max_length=100)

    def __str__(self):
        return self.tool_type

class Tool(models.Model):
    tool_type = models.ForeignKey(ToolType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True)
    description = models.CharField(max_length=200)
    status = models.BooleanField()

    def __str__(self):
        return self.description

class EmailList(models.Model):
    recipient = models.ForeignKey(User)

    def __str__(self):
        return self.recipient.first_name + ' ' + self.recipient.last_name

class ToolForm(ModelForm):
    class Meta:
        model = Tool
        fields = ['id',]
