from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ArticleInlineFormset(BaseInlineFormSet):

    def clean(self):
        super().clean()

        main_scopes_count = sum(1 for form in self.forms if form.cleaned_data.get('is_main'))
        if main_scopes_count != 1:
            raise ValidationError("Должен быть указан один и только один основной раздел")

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']