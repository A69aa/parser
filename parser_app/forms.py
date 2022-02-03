from django import forms
from parser_app import models
from parser_app.parser import parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ("Books", "Books"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class meta:
        fields = [
            "media_type",
        ]


    def parser_data(self):
        if self.data["media_type"] == "Anime":
            anime_data = parser()
            for i in anime_data:
                models.Anime.objects.create(**i)

        elif self.data["media_type"] == "Books":
            books_data = parser()
            for i in books_data:
                models.Novel.objects.create(**i)
