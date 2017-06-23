from django.shortcuts import render
from django.db import models
from django.http import JsonResponse
from django.core.mail import send_mail
from . import models

def index(request):
    return JsonResponse({'Status': 'OK'})

def email(request):
    tool_list = models.Tool.objects.all()
    email_list = models.EmailList.objects.all()

    staff_list = []
    for user in email_list:
        staff_list.append(user.recipient.email)

    print(staff_list)
    for tool in tool_list:
        if(tool.status == True):
            staff_list.append(tool.user.email)
            send_mail(
                'Overdue Tool Alert',
                'Hello ' + tool.user.first_name + ',' + '\n\nOur records show that you have checked out a ' + tool.description + ' ' + tool.tool_type.tool_type + ' and have not returned it. Please check it back in at your earliest convenience.\n\nThank you,\nMaintenance & Repair Crew',
                'murecservicesit@missouri.edu',
                staff_list,
                fail_silently=False,
            )
    return JsonResponse({'list':'yes'})
