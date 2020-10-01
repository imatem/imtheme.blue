# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone.app.layout.viewlets.common import SearchBoxViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SearchViewlet(SearchBoxViewlet):

    render = ViewPageTemplateFile("searchviewlet.pt")

    # def update(self):
    #     self.message = self.get_message()

    def get_message(self):
        return u'My message'

    # def render(self):
        # return super(SearchViewlet, self).render()

