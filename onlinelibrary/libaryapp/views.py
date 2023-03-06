from django.shortcuts import render
from .models import *

# Создание функции, которая отвечает за отображение книг на сайте
def show_books(request):
    # Если метод запроса - POST
    if request.method == 'POST':
        # Создание пустого словаря
        context = {}
        # Если выполнен поиск по названию книги
        if 'bookname' in request.POST:
            # Получение запроса от пользователя сайта
            bookname = request.POST.get('bookname')
            # Фильтрация объектов класса Book по строке, которую ввёл пользователь сайта
            books = Book.objects.filter(title__icontains=bookname)
            # Добавление отфильтрованных объектов в словарь
            context['books'] = books
            # Вывод объектов на экране, которые отфильтровал пользователь
            context['bookselection'] = f'Усі збіги за іменем книжки "{bookname}"'
        # Если выполнен поиск по имени автора
        elif 'authorname' in request.POST:
            # Получение запроса от пользователя сайта
            authorname = request.POST.get('authorname')
            # Фильтрация объектов класса Author по строке, которую ввёл пользователь сайта
            authors = Author.objects.filter(name__icontains = authorname)
            # Создание пустого списка
            list_books = []
            # 
            for author in authors:
                # 
                list_books += Book.objects.filter(author_id = author.id)
            # Добавление отфильтрованных авторов в словарь
            context['books'] = list_books
            # Вывод объектов на экране, которые отфильтровал пользователь
            context['bookselection'] = f'Усі збіги за іменем автора "{authorname}"'
    else:
        # Выбор всех объектов класса Book
        books = Book.objects.all()
        # Вывод всех объектов на экране
        context = {'books': books, 'bookselection': 'Усі Книжки'}
    return render(request, 'books.html', context)