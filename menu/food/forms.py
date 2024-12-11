from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["item_name", "item_desc", "item_price", "item_image"]

    def __init__(self, *args, **kwargs):
        # Flag to identify if this is an update or creation
        self.is_update = kwargs.pop('is_update', False)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        # If it's a create operation, ensure all fields are filled
        if not self.is_update:
            missing_fields = [field for field in self.fields if not cleaned_data.get(field)]
            if missing_fields:
                raise forms.ValidationError(
                    f"The following fields are required: {', '.join(missing_fields)}"
                )
        return cleaned_data
