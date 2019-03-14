from django import forms

TWITTER_CHROME = (('noheader', 'noheader'),
                  ('nofooter', 'nofooter'),
                  ('noborders', 'noborders'),
                  ('noscrollbar', 'noscrollbar'),
                  ('transparent', 'transparent'),)

class TwitterForm(forms.ModelForm):
    chrome = forms.MultipleChoiceField(choices=TWITTER_CHROME, widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        super(TwitterForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.chrome:
            self.initial['chrome'] = eval(self.instance.chrome)