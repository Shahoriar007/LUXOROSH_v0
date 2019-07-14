from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.
class index(TemplateView):


    def get(self, request, *args, **kwargs):




        return render(request, template_name='user/index.html' )




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            if user is not None:
                if user.is_active:

                    login(request, user)
                    messages.success(request, 'Account !created successfully')
                    return redirect('product:index')#url to index page
                else:
                    messages.warning(request, 'user is not active')
                    return HttpResponse('Sorry,user is not active')
        else:
            for msg in form.error_messages:
                # print(form.error_messages[msg])
                messages.warning(request,form.error_messages[msg])

            return render(request = request,
                          template_name = "user/registerPage.html",
                          context={"form":form})

    else:
        form = CustomUserCreationForm()
    return render(request=request, template_name='user/registerPage.html', context={'form': form})
