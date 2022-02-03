from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, FormView
from . import models, forms


class AnimeView(ListView):
    model = models.Anime
    template_name = "anime/anime_list.html"

    def get_queryset(self):
        return models.Anime.objects.all()


class ParserAnimeView(FormView):
    template_name = "anime/anime_parser.html"
    form_class = forms.ParserForm
    success_url = "/anime/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserAnimeView, self).post(request, *args, **kwargs)

########################################################################################################################

class NovelView(ListView):
    model = models.Novel
    template_name = "anime/books_list.html"

    def get_queryset(self):
        return models.Novel.objects.all()


class ParserNovelView(FormView):
    template_name = "anime/books_parser.html"
    form_class = forms.ParserForm
    success_url = "/books/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserNovelView, self).post(request, *args, **kwargs)