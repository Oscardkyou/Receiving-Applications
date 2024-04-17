from django import forms

from .models import Delivery, Schedule_of_road_transport, Support


class UnifiedDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'product_name', 'weight', 'volume', 'quantity', 'document',
            'address_line', 'delivery_address', 'additional_info',
            'insurance_needed', 'storage', 'customs_clearance', 'packaging', 'special_requirements',
            'full_name', 'company_name', 'phone_number', 'email',
            'desired_departure_date', 'delivery_deadline'
        ]
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control additional-class'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control additional-class'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control additional-class'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control additional-class'}),
            'document': forms.FileInput(attrs={'class': 'form-control-file additional-class'}),
            'address_line': forms.Textarea(attrs={'class': 'form-control additional-class', 'rows':  3}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control additional-class', 'rows':  3}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control additional-class', 'rows':  3}),
            'insurance_needed': forms.Select(attrs={'class': 'form-control additional-class'}),
            'special_requirements': forms.Textarea(attrs={'class': 'form-control additional-class', 'rows':  3}),
            'storage': forms.CheckboxInput(attrs={'class': 'form-check-input additional-class'}),
            'customs_clearance': forms.CheckboxInput(attrs={'class': 'form-check-input additional-class'}),
            'packaging': forms.CheckboxInput(attrs={'class': 'form-check-input additional-class'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control additional-class'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control additional-class'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control additional-class'}),
            'email': forms.EmailInput(attrs={'class': 'form-control additional-class'}),
            'desired_departure_date': forms.DateInput(attrs={'class': 'form-control additional-class', 'type': 'date'}),
            'delivery_deadline': forms.DateInput(attrs={'class': 'form-control additional-class', 'type': 'date'}),
        }


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule_of_road_transport
        fields = ['recipient', 'application', 'data', 'additional_info', 'file_and_photo']
        widgets = {
            'recipient': forms.Select(attrs={'class': 'form-control'}),
            'application': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'file_and_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }