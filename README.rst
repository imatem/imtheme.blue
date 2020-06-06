.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

============
imtheme.blue
============

Responsive Theme for IM, 2020

Features
--------

- Can be bullet points


Examples
--------

This Theme can be seen in action at the following sites:
- www.matem.unam.mx


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at https://github.com/collective/imtheme.blue/docs


Before Installation
-------------------

* Configuración del tema:
    * Desactivar Plone Theme: complex
* Desinstalar imtheme.complex
* Desinstalar IM responsivetheme
* En portal_view_customizations borrar:
    * zope.interface.interface-plone.colophon
    * zope.interface.interface-plone.footer
* En portal_skins borrar:
    * facebook.png
    * folder_congresos_view
    * main_template
    * twitter.png
    * ploneCustom.css
        * h1, h2, h3, h4, h5, h6 {
        * font-family:  'Open Sans Condensed', sans-serif;
        * letter-spacing: normal;
        * }
* En Collage borrar:
    * Unidades
    * Festivales
    * Galeria
* Theme
    * Señalar enlaces especiales
    * Mostrar iconos de tipo de contenido / Sólo para usuarios conectados
* Remover del buildout / borrar de src-git
* buildout
    * agregar imtheme.blue
    * actualizar matem.congresos a la rama themeblue (merge)

* Cambiar en index.html http://localhost:8080/infomatem por https://www.matem.unam.mx
* Instalar imtheme.blue
* En cada folder de congresos poner vista congresosfolder_view (ojo 2012)
* Quitar entrada NOTICIAS, Avisos, Visitantes de sección ACERCA DEL IM
* BIBLIOTECAS falta colocar enlace a ambas bibliotecas en esta nueva entrada
* En SERVICIOS INTERNOS quitar entrada de BIBLIOTECAS


Installation
------------

Install imtheme.blue by adding it to your buildout::

    [buildout]

    ...

    eggs =
        imtheme.blue


and then running ``bin/buildout``


Developmet
----------

.. code-block:: bash

    $ virtualenv-2.7 --no-setuptools --clear .
    $ ./bin/pip install -r requirements.txt
    $ ./bin/buildout


Contribute
----------

- Issue Tracker: https://github.com/collective/imtheme.blue/issues
- Source Code: https://github.com/collective/imtheme.blue
- Documentation: https://github.com/collective/imtheme.blue/docs


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: informatica.academica@matem.unam.mx


License
-------

The project is licensed under the GPLv2.
