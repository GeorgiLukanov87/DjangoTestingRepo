from django import forms

from DjangoTesting.my_web.models import Professor


class BaseProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class ProfessorCreateForm(BaseProfessorForm):
    pass


class ProfessorEditForm(BaseProfessorForm):
    pass


class ProfessorDeleteForm(BaseProfessorForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
