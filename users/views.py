from django.shortcuts import redirect, render

from django.urls import reverse, reverse_lazy

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.sites.shortcuts import get_current_site

from conf.settings import EMAIL_HOST_USER

from users.form import LoginForm, RegisterForm

from users.token import email_verification_token

from django.utils.encoding import force_bytes

from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout


def verify_email(request, token, uidb64):
    uid = force_bytes(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    if user is not None and email_verification_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('users:login')
    else:
        return render(request, 'main/404/404.html')


def send_email_verification(request, user):
    token = email_verification_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_size = get_current_site(request)
    verification_url  = reverse(viewname='users:verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current_size}{verification_url}"

    text_content = render_to_string(
        template_name='main/auth/verify_email.html',
        context = {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject="Verification Email",
        body=text_content,
        from_email= EMAIL_HOST_USER,
        to=[user.email]
    )

    message.attach_alternative(text_content, "text/html")
    message.send()
 

def user_login_page_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data('email')
            password = form.cleaned_data('password')
            user = authenticate(request=request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                errors = form.errors
                return render(request, 'main/auth/login/login.html', {'errors': errors})
        else:
            return render(request, 'main/auth/login/login.html')
    else:
        return render(request, 'main/auth/login/login.html')


def user_register_page_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(raw_password=form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            send_email_verification(request, user)
            return redirect(reverse_lazy('users:login'))
        else:
            errors = form.errors
            return render(request, 'main/auth/register/register.html', {'errors': errors})
    else:
        return render(request, 'main/auth/register/register.html')


def product_checkout_page_view(request):
    logout(request('/'))
    return render(request, 'registration/product-checkout.html')


# def user_wishlist_page_view(request):
#     return render(request, 'registration/user-wishlist.html')


# def user_reset_password_page_view(request):
#     return render(request, 'registration/user-reset-password.html')
