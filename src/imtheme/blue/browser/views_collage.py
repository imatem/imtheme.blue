# -*- coding: utf-8 -*-
from collective.plonetruegallery.browser.views.galleryview import GalleryView
from Products.Collage.browser.views import BaseTopicView
# from matem.event.browser.rss_view import IMRSSFeed
from plone.app.portlets.portlets.rss import RSSFeed


class IMTopicsView(BaseTopicView):

    def cstyle(self, ptitle):
        if 'Juriquilla' in ptitle:
            return 'jurheader-color'
        return 'cuheader-color'

    def topicstyle(self, ptitle):
        if 'Juriquilla' in ptitle:
            return 'jurborder-color'
        return 'cuborder-color'

    def topicHome(self, ptitle):
        if 'Juriquilla' in ptitle:
            if 'juriquilla' in self.request['ACTUAL_URL']:
                # must be url activities
                return 'http://www.matem.unam.mx/juriquilla'
            else:
                return 'http://www.matem.unam.mx/juriquilla/actividades'
        if 'juriquilla' in self.request['ACTUAL_URL']:
            return 'http://www.matem.unam.mx'
        else:
            return 'http://www.matem.unam.mx/actividades/allactivitiesview'


class IMGalleryView(GalleryView):
    pass
