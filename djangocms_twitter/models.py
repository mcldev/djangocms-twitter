from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from colorfield.fields import ColorField

TWITTER_THEMES = (('light', 'Light'),
                  ('dark', 'Dark'))


class TwitterTimeline(CMSPlugin):
    title = models.CharField(_('title'), max_length=75, null=True, blank=True)

    twitter_url = models.CharField(_('twitter url'), max_length=512,
                                   help_text=_('Enter a Twitter URL (see https://publish.twitter.com) e.g. <br><ol>'
                                               '<li>A collection: https://twitter.com/TwitterDev/timelines/539487832448843776</li>'
                                               '<li>A tweet: https://twitter.com/Interior/status/463440424141459456</li>'
                                               '<li>A profile: https://twitter.com/TwitterDev</li>'
                                               '<li>A list: https://twitter.com/TwitterDev/lists/national-parks</li>'
                                               '<li>A moment: https://twitter.com/i/moments/625792726546558977</li>'
                                               '<li>A likes timeline: https://twitter.com/TwitterDev/likes</li></ol>'))

    tweet_limit = models.PositiveSmallIntegerField(_('count'), blank=True, null=True, help_text=_('Number of entries to display'))
    width = models.PositiveSmallIntegerField(_('width'), blank=True, null=True, help_text=_('Width in pixels'))
    height = models.PositiveSmallIntegerField(_('height'), blank=True, null=True, help_text=_('Height in pixels'))
    theme = models.CharField(_('select theme'), max_length=50, choices=TWITTER_THEMES, default=TWITTER_THEMES[0][0])
    link_color = ColorField(default='#2B7BB9', blank=True, null=True)
    show_replies = models.BooleanField(_("Show Tweet Replies"), default=False)
    chrome = models.CharField(_('Control the frame around the linear timeline'), blank=True, null=True, max_length=512)

    def get_show_replies(self):
        return 'true' if self.show_replies else 'false'

    def get_url_text(self):
        return str(self.twitter_url).replace(r'https://twitter.com/', '')

    def get_chrome(self):
        if self.chrome:
            chrome_list = eval(self.chrome)
            return ' '.join(chrome_list)

    def __unicode__(self):
        return self.title


