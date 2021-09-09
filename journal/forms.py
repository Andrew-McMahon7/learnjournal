from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from journal.models import ContactsResource, JournalResource, Resource, TagsResource


class JournalResourceForm(ModelForm):
       class Meta:
              model = JournalResource
              fields = '__all__'


class TagResourceForm(ModelForm):
       class Meta:
              model = TagsResource
              fields = '__all__'


class ContactResourceForm(ModelForm):
       class Meta:
              model = ContactsResource
              fields = '__all__'

# # Creating a form to add an article.
# form = ArticleForm()

# # Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)