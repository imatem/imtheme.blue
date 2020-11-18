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
        if isinstance(loc, unicode):
            try:
                loc = loc.encode('utf-8')
            except:
                pass
        if v(loc) is 1:
            return True
        return False

    def getMinMax(self):
        query = self.context.buildQuery()
        end = query.get('end', {})
        return end.get('query', (DateTime(),DateTime()))

    def cuContents(self):
        return self.getContents()

    def ujContents(self, activities):
        minmax = self.getMinMax()
        # TODO: ojo con actividades de mas de un dia
        return [a for a in activities if minmax[0] < a.start and a.start < minmax[1]]

    def unidadContents(self, activities, campuscode):
        minmax = self.getMinMax()
        uc = []
        for act in activities:
            start = act['updated']
            if minmax[0] < start and start < minmax[1]:
                uc.append({
                    'getURL': act['url'],
                    'pretty_title_or_id': act['title'],
                    'start': start,
                    'location': act['location'],
                    'Subject': (act['seminarytitle'],),
                    'getSpeaker': act['speaker'],
                    'getEventInstitution': act['institution'],
                    'isCanceled': False,
                    'campus': campuscode,
                })
        return uc

    def getActivities(self, activities):
        """ see matem.event.browser.views.semanaryActivities
        """
        cu = [b for b in self.getContents()]
        uj = self.ujContents(activities['brainsjur'])
        cu.extend(uj)
        uc = self.unidadContents(activities['matcuerrss'], 'calendar-ucim')
        cu.extend(uc)
        uo = self.unidadContents(activities['oaxrss'], 'calendar-uoim')
        cu.extend(uo)
        return sorted(cu, key = lambda i: i['start'])

    def campus_class(self, item):
        cclass = item.get('campus', None)
        if cclass is not None:
            return cclass
        url = item.getURL()
        if '/juriquilla/' in url:
            return 'calendar-ujim'
        if '/oaxaca/' in url:
            return 'calendar-uoim'
        if 'cuernavaca' in url:
            return 'calendar-ucim'
        return 'calendar-im'


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
