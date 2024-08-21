# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import LuggageForm  # 如果你有表单类，可以导入它
from .models import Luggage, Image, Locker


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def home(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/home.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def storage(request):
    if request.method == 'POST':
        form = LuggageForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            luggage = form.save(commit=False)  # 先保存行李对象，不保存 ManyToManyField

            # 保存行李对象
            luggage.save()

            # 处理图片上传
            image_files = request.FILES.getlist('images')
            for image_file in image_files:
                image = Image(image=image_file)
                image.save()  # 保存图片对象

                # 将图片添加到行李对象的图片字段
                luggage.images.add(image)

            # 提交保存图片数据
            luggage.save()

            return redirect('storage_success')  # 确保这里的名称与 urls.py 中的名称匹配
    else:
        form = LuggageForm(user=request.user)

    return render(request, 'home/storage.html', {'form': form})


@login_required(login_url="/login/")
def storage_success(request):
    return render(request, 'home/storage_success.html')


@login_required(login_url="/login/")
def mine(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/mine.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def mine_luggage(request):
    luggage_list = Luggage.objects.filter(user=request.user)
    return render(request, 'home/mine_luggage.html', {'luggage_list': luggage_list})


@login_required(login_url="/login/")
def manage_todo(request):
    luggage_list = Luggage.objects.filter(status='0')
    lockers = Locker.objects.all()
    return render(request, 'home/manage_todo.html', {'luggage_list': luggage_list, 'lockers': lockers})


@csrf_exempt
@require_POST
def select_locker(request):
    luggage_id = request.POST.get('luggage_id')
    locker_id = request.POST.get('locker_id')

    try:
        luggage = Luggage.objects.get(id=luggage_id)
        locker = Locker.objects.get(id=locker_id)

        # Update luggage and locker status to 1
        luggage.status = '1'
        locker.status = '1'
        luggage.save()
        locker.save()

        return JsonResponse({'success': True})
    except Luggage.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Luggage not found.'})
    except Locker.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Locker not found.'})


@login_required(login_url="/login/")
def manage_saved(request):
    luggage_list = Luggage.objects.filter(status='1')
    return render(request, 'home/manage_saved.html', {'luggage_list': luggage_list})


@login_required(login_url="/login/")
def manage_done(request):
    luggage_list = Luggage.objects.filter(status='2')
    return render(request, 'home/manage_done.html', {'luggage_list': luggage_list})


@login_required(login_url="/login/")
def manage_lockers(request):
    lockers = Locker.objects.all()
    return render(request, 'home/manage_lockers.html', {'lockers': lockers})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
