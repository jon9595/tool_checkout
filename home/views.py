from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from tools.models import Tool, ToolType, ToolForm

def index(request):
    return redirect('accounts/login')
@login_required
def dashboard(request):
    if request.method == 'GET':
        tools = {'tools': Tool.objects.all()}
        return render(request, 'home/index.html', tools)
    if request.method == 'POST':
        tool = Tool.objects.get(id=request.POST.get('tool',))
        if tool.status == True:
            tool.status = False
            tool.user = None
            tool.save()
            tools = {'tools': Tool.objects.all(), 'status':'in'}
            return render(request, 'home/index.html', tools)
        if tool.status == False:
            tool.status = True
            tool.user = request.user
            tool.save()
            tools = {'tools': Tool.objects.all(), 'status':'out'}
            return render(request, 'home/index.html', tools)
