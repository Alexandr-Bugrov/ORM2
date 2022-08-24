from django.contrib import admin
from .models import Article, Tag, Scopes
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class Article_TagFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                i += 1
            if i > 1:
                raise ValidationError('Основной тег только однин')
        if i == 0:
            raise ValidationError('Укажите основной тег')
        elif i == 1:
            return super().clean()


class Article_Tag(admin.TabularInline):
    model = Scopes
    formset = Article_TagFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [Article_Tag]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [Article_Tag]