from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = "registration/login.html"

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # Session will expire when browser is closed
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)
