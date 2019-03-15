django CMS Twitter plugin
=========================


.. image:: https://badge.fury.io/py/djangocms-twitter.png
    :target: http://badge.fury.io/py/djangocms-twitter

.. image:: https://pypip.in/d/djangocms-twitter/badge.png
        :target: https://crate.io/packages/djangocms-twitter?version=latest



``djangocms-twitter`` is a upgrade-friendly plugin, mostly derived from original
implementation in **django CMS** core.

**Substantive Changes**
-----------------------

The method of embedding tweets has now been changed to use the new Twitter publication method.
See: https://publish.twitter.com

See this URL for details: https://twittercommunity.com/t/deprecating-widget-settings/102295

 "In June 2016 we announced that we would be making it much easier for developers to create embedded timelines on their sites, by no longer requiring the timelines to be registered under widget settings 2.9k. We launched publish.twitter.com 14.7k to make it much easier to create timeline widgets without requiring you to make changes to your account settings, and to make the embedded timelines more flexible."

Also the **Embedded Search has been removed**

 "Embedded Search timelines have been deprecated"

The following changes have been made to the plugin:
###################################################
#. Renamed Twitter Recent Entries to Twitter Timeline
#. Removed Twitter Search
#. Added migrations to remove deprecated fields:
    - link_hint
    - twitter_id
#. Added fields to simplify user customisations:
    - tweet_limit
    - width
    - height
    - theme
    - link_color
    - chrome
    - show_replies
#. Replaced the userid with the flexible Twitter URL
    - twitter_url


Installation
------------

First-time installation
#######################

#. Install from pypi::

    $ pip install djangocms-twitter

#. Add ``djangocms_twitter`` to ``INSTALLED_APPS``
#. Apply migrations::

    $ python manage.py migrate djangocms_twitter

#. Insert the plugin into the page and configure as stated in Usage_.

Upgrade from the existing plugin
################################

#. Apply migrations::

    $ python manage.py migrate djangocms_twitter

#. Remove orphaned plugins carefully! i.e. Twitter Search::

    $ python manage.py cms delete-orphaned-plugins

#. Modify the plugin instances according to Usage_.
#. Check your Templates_.

.. _Usage:

Usage
-----

TwitterTimelinePlugin
##########################

#. Enter the optional Title, this will be displayed above embedded tweets.
#. Enter a Twitter URL, see the guidance at https://publish.twitter.com For example:
    - A collection: https://twitter.com/TwitterDev/timelines/539487832448843776
    - A tweet: https://twitter.com/Interior/status/463440424141459456
    - A profile: https://twitter.com/TwitterDev
    - A list: https://twitter.com/TwitterDev/lists/national-parks
    - A moment: https://twitter.com/i/moments/625792726546558977
    - A likes timeline: https://twitter.com/TwitterDev/likes

#. Set the following values as required, see further guidance here: https://developer.twitter.com/en/docs/twitter-for-websites/timelines/overview.html:
    - tweet_limit - number of tweets to display
    - width - number in pixels (else 100% of parent)
    - height - number in pixels (else 100% of parent)
    - theme - light/dark
    - link_color - use built-in colour selector
    - chrome - set the borders
    - show_replies - true/false

.. _Templates:

Templates
---------

A limited set of client-side options exists to configure the widgets; see
https://developer.twitter.com/en/docs/twitter-for-websites/timelines/overview.html for further info.

To apply them you need to apply the plugin settings above or modify the plugin templates:

- ``djangocms_twitter/twitter_timeline.html``: for ``TwitterTimelinePlugin``


