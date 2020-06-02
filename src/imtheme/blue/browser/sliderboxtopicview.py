# -*- coding: utf-8 -*-

from Products.Collage.browser.views import BaseTopicView


class SliderBoxTopicView(BaseTopicView):

    def hasImage(self, obj):
        if obj.getImage():
            return True
        return False
