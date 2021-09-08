from django.forms import ModelForm
from journal.models import Resource

class ResourceForm(ModelForm):
         class Meta:
            model = Resource
            fields = ['name', 'url'] #Or 'All'

# # Creating a form to add an article.
# form = ArticleForm()

# # Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)