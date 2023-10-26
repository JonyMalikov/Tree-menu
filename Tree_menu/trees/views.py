from django.shortcuts import render


def index(request, id=None):
    """
    Отображает шаблон index.html с заданным запросом и id.

    Аргументы:
        request: Объект HTTP-запроса.
        id: ID, передаваемый в шаблон.

    Возвращает:
        Отображенный шаблон index.html.
    """
    context = {
        "id": id,
    }

    # Отображение шаблона index.html с контекстом
    return render(request, "trees/index.html", context)
