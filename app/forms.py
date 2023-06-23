from django.forms import ModelForm

from app.models import TODOS_LIST
class TODOForm(ModelForm):
    class Meta:
        model = TODOS_LIST
        fields = ['title','status','priority']