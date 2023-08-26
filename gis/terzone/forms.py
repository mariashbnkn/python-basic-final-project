from django import forms

from .models import PlanRegulation, KindTerzone


class KindTerzoneForm(forms.ModelForm):
    class Meta:
        model = KindTerzone
        fields = "code", "name"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"
            if isinstance(field, forms.CharField):
                print(field.label, type(field.label))


class PlanregForm(forms.ModelForm):
    class Meta:
        model = PlanRegulation
        fields = "name", "kind_terzone", "note"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"
            if isinstance(field, forms.CharField):
                print(field.label, type(field.label))
