from django.contrib import messages, auth
from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DetailView, RedirectView, View , UpdateView , ListView, TemplateView, FormView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.utils.decorators import method_decorator

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from account.forms import *
from django.conf import settings
User= settings.AUTH_USER_MODEL

class RegisterView(CreateView):
    """
        Provides the ability to Register as a Instructor
    """
    model = User
    form_class = RegistrationForm
    template_name = "site/pages/register.html"


    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('newspaper:home')
        return super().dispatch(self.request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,'Registration Successfull')
            return redirect('account:login')
        else:
            context={
                'form':form
            }
            return render(request, self.template_name ,context)

class LogInView(FormView):
    """
        Provides the ability to login as a user with an email/username and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'site/pages/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        messages.success(self.request, 'You are Successfully logged In')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, 'Login Faild ! Try Again')
        
        return self.render_to_response(self.get_context_data(form=form))    


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/accounts/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(self.request, 'You are Successfully logged Out')
        return super(LogoutView, self).get(request, *args, **kwargs)


class ProfileView(DetailView):
    model = User
    context_object_name = 'profile'
    pk_url_kwarg = 'id'
    template_name = 'mainsite/accounts/profile.html'


    def get_course(self):               
        return Course.objects.filter(instructor=self.object.id)
        # return Lesson.objects.filter(course=self.object.id).values('video_link').count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_courses'] = self.get_course()
        context['total'] = self.get_course().count()

        return context


@login_required
def EditProfileView(request):
    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect(reverse("accounts:profile", kwargs={
                'id': request.user.id
                }))
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = ProfileUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.profile)
    return render(request, 'mainsite/accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




@method_decorator(login_required(), name='dispatch')
class SettingView(TemplateView):
    template_name = 'mainsite/accounts/settings.html'

@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'mainsite/accounts/change_password.html', {
        'form': form
    })