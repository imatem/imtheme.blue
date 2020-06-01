# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase


class SliderViewlet(ViewletBase):

    def update(self):
        self.sliders = self.get_sliders()

    def get_sliders(self):
        headers = []
        brains = api.content.find(
            portal_type='SliderContent',
            path='/infomatem/actividades/headers/',
            review_state='front-page',
            sort_on='start'
        )
        for b in brains:
            obj = b.getObject()
            image = obj.image
            if image:
                data = {}
                data['url'] = obj.urlevent
                data['urlimage'] = obj.absolute_url() + '/@@images/image'
                headers.append(data)
        return headers

    def render(self):
        return super(SliderViewlet, self).render()
