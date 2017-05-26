from django.db import models

class ToolType(models.Model):
    tool_type = models.CharField(max_length=100)

class Tool(models.Model):
    tool_type = models.ForeignKey(ToolType, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    status = models.BooleanField()
