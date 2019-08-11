from django import forms
from django.db import models
from django.forms import widgets
from django.utils.timezone import timedelta


class DurationInput(widgets.Input):
    input_type = 'number'
    template_name = 'duration_input.html'
    label_attr_key = 'label'

    def __init__(self, attrs=None, label=""):

        if attrs is not None:
            attrs[self.label_attr_key] = label
        else:
            attrs = {self.label_attr_key: label}
        super().__init__(attrs)


class SplitDurationWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets_list = (DurationInput(attrs, "Days"),
                        DurationInput(attrs, "Hours"),
                        DurationInput(attrs, "Minutes"),
                        )
        super(SplitDurationWidget, self).__init__(widgets_list, attrs)

    def decompress(self, value):
        if value:
            hours = value.seconds // 3600
            minutes = (value.seconds % 3600) // 60
            return [int(value.days), int(hours), int(minutes)]
        return [0, 0, 0]


class MultiValueDurationField(forms.MultiValueField):
    widget = SplitDurationWidget

    def __init__(self, **kwargs):
        fields = (
            forms.IntegerField(min_value=0),
            forms.IntegerField(min_value=0, max_value=24),
            forms.IntegerField(min_value=0, max_value=60),
        )
        super(MultiValueDurationField, self).__init__(fields=fields, require_all_fields=True, **kwargs)

    def compress(self, data_list):
        if len(data_list) == 3:
            return timedelta(days=int(data_list[0]),
                             hours=int(data_list[1]),
                             minutes=int(data_list[2]),
                             )
        else:
            return timedelta(0)


class Duration(models.DurationField):

    def formfield(self, **kwargs):
        return super().formfield(form_class=MultiValueDurationField, **kwargs)
