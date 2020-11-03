# -*- coding: utf-8 -*-
from DateTime import DateTime
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


    def cuContents(self):
        return self.getContents()

    def ucContents(self):
        foo = {
            'getURL': 'http://localhost:8080/infomatem/seminarios/representaciones/actividades/tba-7',
            'pretty_title_or_id': 'PRETTY',
            'start': DateTime('2020/11/03 10:00:00 US/Central'),
            'location': 'https://paginas.matem.unam.mx/ocas/',
            'Subject': ('Seminario de Representaciones de \xc3\x81lgebras',),
            'getSpeaker': u'Karin Baur',
            'getEventInstitution': u'University of Graz & University of Leeds',
            'isCanceled': False
        }
        return [foo]

    def ujContents(self):
        return []

    def uoContents(self):
        return []





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
