# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django import forms
from django.utils.translation import ugettext_lazy as _

from edw_fluent.models.related import EntityImage
from edw_fluent.plugins.block.models import BlockItem


class PublicationImageInlineForm(forms.ModelForm):

    AVAILABLE_CHOICES = (
        (None, _("Default")),
        (EntityImage.THUMBNAIL_KEY, _("Thumbnail"))
    )

    key = forms.ChoiceField(label=_("Info block"), required=False, choices=AVAILABLE_CHOICES)

    image_author = forms.CharField(label=_("Author"), required=False, max_length=255)

    image_caption = forms.CharField(label=_("Title"), required=False, max_length=255)

    def __init__(self, *args, **kwargs):
        super(PublicationImageInlineForm, self).__init__(*args, **kwargs)
        publication = getattr(self, 'publication', None)
        available_choices = list(self.AVAILABLE_CHOICES)
        if publication:
            for block in publication.content.contentitems.filter(instance_of=BlockItem):
                available_choices.append((int(block.pk), str(block.__str__())))
        self.fields['key'].choices = available_choices

    def clean(self):
        cleaned_data = super(PublicationImageInlineForm, self).clean()
        key = cleaned_data['key']
        if key == '':
            cleaned_data['key'] = None
        return cleaned_data