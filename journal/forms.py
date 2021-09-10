from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import CheckboxSelectMultiple, Widget
from journal.models import ContactsResource, JournalResource, Resource, TagsResource
from django import forms

class JournalResourceForm(ModelForm):
       class Meta:
              model = JournalResource
              fields = ['journalName', 'journalUrl', 'tagNames', 'contactNames']

       tagNames = forms.ModelMultipleChoiceField(
              queryset = TagsResource.objects.all(),
              widget = forms.CheckboxSelectMultiple
       )

       contactNames = forms.ModelMultipleChoiceField(
              queryset = ContactsResource.objects.all(),
              widget = forms.CheckboxSelectMultiple
       )


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