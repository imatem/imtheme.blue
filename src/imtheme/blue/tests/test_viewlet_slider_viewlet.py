# -*- coding: utf-8 -*-
from imtheme.blue.interfaces import IImthemeBlueLayer
from imtheme.blue.testing import IMTHEME_BLUE_FUNCTIONAL_TESTING
from imtheme.blue.testing import IMTHEME_BLUE_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.Five.browser import BrowserView
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.viewlet.interfaces import IViewletManager

import unittest


class ViewletIntegrationTest(unittest.TestCase):

    layer = IMTHEME_BLUE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Collage', 'main-collage')
        api.content.create(self.portal, 'News Item', 'newsitem')

    def test_slider_viewlet_is_registered(self):
        view = BrowserView(self.portal['main-collage'], self.request)
        manager_name = 'plone.portalheader'
        alsoProvides(self.request, IImthemeBlueLayer)
        manager = queryMultiAdapter(
            (self.portal['main-collage'], self.request, view),
            IViewletManager,
            manager_name,
            default=None
        )
        self.assertIsNotNone(manager)
        manager.update()
        my_viewlet = [v for v in manager.viewlets if v.__name__ == 'slider-viewlet']  # NOQA: E501
        self.assertEqual(len(my_viewlet), 1)

    def test_slider_viewlet_is_not_available_on_newsitem(self):
        view = BrowserView(self.portal['newsitem'], self.request)
        manager_name = 'plone.portalheader'
        alsoProvides(self.request, IImthemeBlueLayer)
        manager = queryMultiAdapter(
            (self.portal['newsitem'], self.request, view),
            IViewletManager,
            manager_name,
            default=None
        )
        self.assertIsNotNone(manager)
        manager.update()
        my_viewlet = [v for v in manager.viewlets if v.__name__ == 'slider-viewlet']  # NOQA: E501
        self.assertEqual(len(my_viewlet), 0)


class ViewletFunctionalTest(unittest.TestCase):

    layer = IMTHEME_BLUE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
