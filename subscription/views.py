from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages

from .forms import EmailForm

def email_sub(request):
    response_data = {}
    success_status = 'success'
    success_msg = 'Your Email Successfully Added'
    error_status = 'error'
    error_msg = 'Somthing went wrong. Please Try Again'

    if request.method =='POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            is_success = form.save()
            if is_success and request.is_ajax():
                response_data['status'] = success_status
                response_data['msg'] = success_msg

            elif is_success:
                messages.success(request, success_msg)

            else:
                response_data['status'] = error_status 
                response_data['msg'] = form.errors
            return JsonResponse(response_data, safe=False)

        else:
            response_data['status'] = error_status 
            response_data['msg'] = error_msg
            return JsonResponse(response_data, safe=False)

    return redirect('/')
