from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()

from comment.form import CommentModelForm


def create_comment_View(request):
    """
    Provide the ability to create comment for post
    """
    form = CommentModelForm(request.POST or None)

    # user = get_object_or_404(User, id=request.user.id)
    
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user.id
            instance.save()
            # return redirect('/')
        else:
            print('no')
            form = CommentModelForm(request.POST or None)
            return redirect('/about')
