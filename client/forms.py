from django.forms import ModelForm, CharField, ValidationError
from client.models import Client


class ClientAdminForm(ModelForm):
    class Meta:
        model = Client
        fields = ['FIO', 'phone_number']

    FIO = CharField(label="Ф.И.О")
    phone_number = CharField(label="Номер телефона")

    def clean(self):
        cleaned_data = super().clean()
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) != 9:
            raise ValidationError("Номер телефона не должен содержать менее 9 цифр. (например: 999961516)")
        return cleaned_data
