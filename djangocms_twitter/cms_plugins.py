from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TwitterTimeline
from .forms import TwitterForm


class TwitterTimelinePlugin(CMSPluginBase):
    model = TwitterTimeline
    form = TwitterForm
    name = _("Twitter")
    render_template = "djangocms_twitter/twitter_timeline.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
        })
        return context


plugin_pool.register_plugin(TwitterTimelinePlugin)
