from django import forms
from .models import Dancer, CastingGroup

class DancerForm(forms.ModelForm):
    class Meta:
        model = Dancer
        fields = (
            'semester',
            'name',
            'gender',
            'phone',
            'email',
        )

class CastingGroupForm(forms.ModelForm):

	class Meta:
		model = CastingGroup
		fields = (
			'semester',
			'video_link',
			'dancer_ids',
		)

class SearchById(forms.Form):
	dancer_id = forms.CharField()

class AddDancerForm(forms.Form):
	team_id = forms.CharField(required=False)
	dancer_id = forms.CharField(required=False)

class RemoveDancerForm(forms.Form):
	team_id = forms.CharField(required=False)
	dancer_id = forms.CharField(required=False)

class RandomizeForm(forms.Form):
	org = forms.CharField(required=False)

		# form = CastinGroupForm()
		# Something happens
		# casting_group = form.save()
		# --> form.is_valid()
		# dancer_ids = form.cleaned_data['dancer_ids']
		# dancer_ids = [int(dancer_id) for dancer_id in dancer_ids.split(',')]
		# for dancer_id in dancer_ids:
		# 	# fetch it
		# 	dancer = Dancer.objects.filter(id=dancer_id).first()
		#   if dancer is not None:
		#		dancer.casting_group = casting_group
		#       dancer.save()
