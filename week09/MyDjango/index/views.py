from django.shortcuts import render
from django.shortcuts import redirect
###  从models取数据传给template  ###
from .models import Tb2
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def movies(request):
    ###  从models取数据传给template  ###
    n = Tb2.objects.all()
    return render(request, 'movieslist.html', locals())

def form1(request):
  return render(request, 'form1.html')

def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)  
                #return HttpResponse('登录成功')
                return redirect('movies/')
            else:
                #return HttpResponse('登录失败')
                return redirect('form/')

    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})
