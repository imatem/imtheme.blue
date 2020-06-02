# -*- coding: utf-8 -*-
from imtheme.blue.testing import IMTHEME_BLUE_FUNCTIONAL_TESTING
from imtheme.blue.testing import IMTHEME_BLUE_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = IMTHEME_BLUE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'ATTopic', 'topic')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_sliderbox_is_registered(self):
        view = getMultiAdapter(
            (self.portal['topic'], self.portal.REQUEST),
            name='sliderbox'
        )
        self.assertTrue(view.__name__ == 'sliderbox')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in sliderbox'
        # )

    def test_sliderbox_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='sliderbox'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = IMTHEME_BLUE_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
