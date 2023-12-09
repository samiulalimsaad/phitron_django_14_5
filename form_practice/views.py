from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from form_practice.form import InputForm, TestForm


def index(req: HttpRequest) -> HttpResponse:
    return redirect("/test")


def form(req: HttpRequest) -> HttpResponse:
    form = InputForm(req.POST)

    if req.method == "POST" and form.is_valid():
        print(form.cleaned_data)

    return render(req, "index.html", {"form": form})


def test_form(req):
    form = TestForm(req.POST)

    return render(req, "index.html", {"form": form})
