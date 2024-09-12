from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContentForm
from .models import Buyer, Game


# Create your views here.
def main_page(request):
    title = "Главная страница"
    link1 = "Главная"
    link2 = "Магазин"
    link3 = 'Корзина'
    context = {'title': title, 'link1': link1, 'link2': link2, 'link3': link3}
    return render(request, 'platform.html', context)


def store(request):
    title = 'Ассортимент'
    buy = 'Купить'
    games = Game.objects.all()
    back = 'Вернуться обратно'
    context = {'title': title, "buy": buy, 'games': games, 'back': back}
    return render(request, 'games.html', context)


def korzina(request):
    title = 'Корзина'
    back = 'Вернуться обратно'
    context = {'title': title, 'back': back}
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    info = {'error': []}
    i = 0
    users = []
    buyers = Buyer.objects.all()
    for buyer in buyers:
        users.append(buyer.name)
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in users and password == repeat_password and int(age) >= 18:
                users.append(username)
                return HttpResponse(f'Приветствуем {username}')

            elif username in users:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    'Этот логин уже занят', status=400, reason='repeated login')
                return HttpResponse('Этот логин уже занят',
                                    status=400, reason='repeated login')

            elif password != repeat_password:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    'Этот логин уже занят', status=400, reason='repeated login')
                return HttpResponse('Пароли не совпадают',
                                    status=400, reason='non-identical passwords')

            elif int(age) < 18:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    f'Регистрация разрешена с 18ти лет', status=400,
                    reason='insufficient age')

                return HttpResponse(
                    f'Регистрация разрешена с 18ти лет', status=400,
                    reason='insufficient age')
    else:

        form = ContentForm()
        context = {'info': info, 'form': form}
        return render(request, 'registration_page.html', context)
