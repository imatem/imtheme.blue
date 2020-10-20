# -*- coding: utf-8 -*-
from collective.plonetruegallery.browser.views.galleryview import GalleryView
from Products.Collage.browser.views import BaseTopicView
from Products.validation import validation
# from matem.event.browser.rss_view import IMRSSFeed
from plone.app.portlets.portlets.rss import RSSFeed


class IMTopicsView(BaseTopicView):

    def isURL(self, loc):
        v = validation.validatorFor('isURL')
        if v(loc) is 1:
            return True
        return False

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

    def link(self, img):
        """ Take link from description
        """
        description = img.get('description')
        if description is None:
            link = img.get('link')
        try:
            href_index = description.index('href="')
            description = description[href_index + 6:]
            href_index = description.index('">')
            link = description[:href_index]
        except ValueError as error:
            link = img.get('link')
        target = '_blank'
        if 'www.matem.unam.mx' in link and '~' not in link:
            target = ''
        return {'href': link, 'target': target}
