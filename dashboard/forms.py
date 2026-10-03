from django import forms
from django.contrib.auth.forms import AuthenticationForm

from projects.models import Project, TechStack


class AdminLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_superuser:
            raise self.get_invalid_login_error()


class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Python'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if TechStack.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('This tech stack already exists.')
        return name


class ProjectForm(forms.ModelForm):
    tech_stack = forms.ModelChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None,
        error_messages={'required': 'Please choose a tech stack.'},
    )

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].required = True

    def save(self, commit=True):
        project = super().save(commit=commit)
        if commit:
            project.tech_stacks.set([self.cleaned_data['tech_stack']])
        return project