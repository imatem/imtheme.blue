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
* En Collage crear página con:
        sevicios-container
        <div class="sevicios-container standard-topic">
            <h2>SERVICIOS AL PÚBLICO</h2>
            <ul>
                <li><a class="internal-link" href="resolveuid/f10548cc791cd1e2c053bc871ee3ac01" target="_self" title="">Becas de lugar en el IM</a></li>
                <li><a class="external-link" href="http://biblioteca.matem.unam.mx/" target="_self" title="">Biblioteca Sotero Prieto</a></li>
                <li><a class="external-link" href="http://im-c.bibliotecas.unam.mx/" target="_self" title="">Biblioteca Solomon Lefchetz Cuernavaca</a></li>
                <li><a class="external-link" href="http://papirhos.matem.unam.mx/" target="_self" title="">Publicaciones/Papirhos</a></li>
                <li><a class="internal-link" href="resolveuid/07ea4b7915a4bf3365d53e2b75c312a5" target="_self" title="">Comunicación</a></li>
                <li><a>Prensa</a></li>
                <li><a>Formatos autorización uso de imagen IMUNAM (foto, video)</a></li>
                <li><a class="internal-link" href="resolveuid/93d8b350d3210b1d59e5c701ba3b96f3" target="_self" title="">Enlaces de interés</a></li>
            </ul>
        </div>
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
* Sección de Seminarios mover de Actividades
* Revisar links de la principal
* Dentro de sección ORGANIZACIÓN INTERNA hay que agregar sección de DIRECTORIO antes de ORGANIGRAMA
* Dentro de sección ORGANIZACIÓN INTERNA / COMISIONES, no te envía a COMISIONES sino que te regresa a la entrada de Organización Interna: deben aparecer los enlaces de Comisión Dictaminadora, Comisión Evaluadora, Comisiones Académicas

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
