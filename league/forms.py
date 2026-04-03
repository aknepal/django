from django import forms
from .models import Team, Manager, Player

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'