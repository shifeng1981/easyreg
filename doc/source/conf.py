# -*- coding: utf-8 -*-
#
# pytorchRegistration documentation build configuration file, created by
# sphinx-quickstart on Sat Jul 29 08:41:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import glob
import shutil

from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList 
from docutils import nodes
import re
import sphinx_gallery

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class IncludeDirective(Directive):
    """Include source file without docstring at the top of file.

    Implementation just replaces the first docstring found in file
    with '' once.

    Example usage:

    .. includenodoc:: /beginner/examples_tensor/two_layer_net_tensor.py

    """

    # defines the parameter the directive expects
    # directives.unchanged means you get the raw value from RST
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False
    add_index = False

    docstring_pattern = r'"""(?P<docstring>(?:.|[\r\n])*?)"""\n'
    docstring_regex = re.compile(docstring_pattern)

    def run(self):
        document = self.state.document
        env = document.settings.env
        rel_filename, filename = env.relfn2path(self.arguments[0])

        try:
            text = open(filename).read()
            text_no_docstring = self.docstring_regex.sub('', text, count=1)

            code_block = nodes.literal_block(text=text_no_docstring)
            return [code_block]
        except FileNotFoundError as e:
            print(e)
            return []


class GalleryItemDirective(Directive):
    """
    Create a sphinx gallery thumbnail for insertion anywhere in docs.

    Optionally, you can specify the custom figure and intro/tooltip for the
    thumbnail.

    Example usage:

    .. galleryitem:: intermediate/char_rnn_generation_tutorial.py
        :figure: _static/img/char_rnn_generation.png
        :intro: Put your custom intro here.

    If figure is specified, a thumbnail will be made out of it and stored in
    _static/thumbs. Therefore, consider _static/thumbs as a 'built' directory.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'figure': directives.unchanged,
                   'intro': directives.unchanged}
    has_content = False
    add_index = False

    def run(self):
        args = self.arguments
        fname = args[-1]

        env = self.state.document.settings.env
        fname, abs_fname = env.relfn2path(fname)
        basename = os.path.basename(fname)
        dirname = os.path.dirname(fname)

        try:
            if 'intro' in self.options:
                intro = self.options['intro'][:195] + '...'
            else:
                _, blocks = sphinx_gallery.gen_rst.split_code_and_text_blocks(abs_fname)
                intro, _ = sphinx_gallery.gen_rst.extract_intro_and_title(abs_fname, blocks[0][1])

            thumbnail_rst = sphinx_gallery.backreferences._thumbnail_div(
                dirname, basename, intro)

            if 'figure' in self.options:
                rel_figname, figname = env.relfn2path(self.options['figure'])
                save_figname = os.path.join('_static/thumbs/',
                                            os.path.basename(figname))

                try:
                    os.makedirs('_static/thumbs')
                except OSError:
                    pass

                sphinx_gallery.gen_rst.scale_image(figname, save_figname,
                                                   400, 280)
                # replace figure in rst with simple regex
                thumbnail_rst = re.sub(r'..\sfigure::\s.*\.png',
                                       '.. figure:: /{}'.format(save_figname),
                                       thumbnail_rst)

            thumbnail = StringList(thumbnail_rst.split('\n'))
            thumb = nodes.paragraph()
            self.state.nested_parse(thumbnail, self.content_offset, thumb)

            return [thumb]
        except FileNotFoundError as e:
            print(e)
            return []


GALLERY_TEMPLATE = """
.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="{tooltip}">

.. only:: html

    .. figure:: {thumbnail}

        {description}

.. raw:: html

    </div>
"""


class CustomGalleryItemDirective(Directive):
    """Create a sphinx gallery style thumbnail.

    tooltip and figure are self explanatory. Description could be a link to
    a document like in below example. 

    Example usage:

    .. customgalleryitem::
        :tooltip: I am writing this tutorial to focus specifically on NLP for people who have never written code in any deep learning framework
        :figure: /_static/img/thumbnails/babel.jpg
        :description: :doc:`/beginner/deep_learning_nlp_tutorial`

    If figure is specified, a thumbnail will be made out of it and stored in
    _static/thumbs. Therefore, consider _static/thumbs as a 'built' directory.
    """

    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'tooltip': directives.unchanged,
                   'figure': directives.unchanged,
                   'description': directives.unchanged}

    has_content = False
    add_index = False

    def run(self):
        try:
            if 'tooltip' in self.options:
                tooltip = self.options['tooltip'][:195] + '...'
            else:
                raise ValueError('tooltip not found')

            if 'figure' in self.options:
                env = self.state.document.settings.env
                rel_figname, figname = env.relfn2path(self.options['figure'])
                thumbnail = os.path.join('_static/thumbs/', os.path.basename(figname))

                try:
                    os.makedirs('_static/thumbs')
                except FileExistsError:
                    pass

                sphinx_gallery.gen_rst.scale_image(figname, thumbnail, 400, 280)
            else:
                thumbnail = '_static/img/thumbnails/default.png'

            if 'description' in self.options:
                description = self.options['description']
            else:
                raise ValueError('description not doc found')

        except FileNotFoundError as e:
            print(e)
            return []
        except ValueError as e:
            print(e)
            raise
            return []

        thumbnail_rst = GALLERY_TEMPLATE.format(tooltip=tooltip,
                                                thumbnail=thumbnail,
                                                description=description)
        thumbnail = StringList(thumbnail_rst.split('\n'))
        thumb = nodes.paragraph()
        self.state.nested_parse(thumbnail, self.content_offset, thumb)
        return [thumb]



#from .custom_directives import IncludeDirective, GalleryItemDirective, CustomGalleryItemDirective


#sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0,os.path.abspath('../../easyreg'))
#sys.path.insert(0,os.path.abspath('../../easyreg/libraries'))
#sys.path.insert(0,os.path.abspath('../..'))

sys.path.insert(0,os.path.abspath('../..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.napoleon',
              'sphinx.ext.graphviz',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.doctest',
              'sphinx.ext.todo',
              'sphinx.ext.intersphinx',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'nbsphinx',
              #'sphinx_gallery.gen_gallery'
]

# generate autosummary even if no references
autosummary_generate = True
#
# sphinx_gallery_conf = {
#      'examples_dirs': ['../../demos', '../../jupyter'],   # path to your example scripts
#      'filename_pattern': '/example_',
#      # directory where function granular galleries are stored
#      'backreferences_dir': False,
#      'ignore_pattern': r'__init__\.py',
#      'gallery_dirs': ['auto_demos', 'auto_jupyter']  # path where to save gallery generated examples
# }
#
# for i in range(len(sphinx_gallery_conf['examples_dirs'])):
#     gallery_dir = sphinx_gallery_conf['gallery_dirs'][i]
#     source_dir = sphinx_gallery_conf['examples_dirs'][i]
#     # Create gallery dirs if it doesn't exist
#     try:
#         os.mkdir(gallery_dir)
#     except OSError:
#         pass
#
#     # Copy rst files from source dir to gallery dir
#     for f in glob.glob(os.path.join(source_dir, '*.rst')):
#         shutil.copy(f, gallery_dir)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'easyreg'
copyright = u'2018, Zhengyang Shen'
author = u'Zhengyang Shen'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u'0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

autodoc_member_order = 'bysource'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes',]
#html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
   'logo_only' : True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'easyregdoc'

html_logo = 'easyreg-logo.png'

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'xelatex'
latex_show_urls = 'footnote'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'easyreg.tex', u'easyreg Documentation',
     u'Marc Niethammer', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'easyreg', u'easyreg Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'easyreg', u'easyreg Documentation',
     author, 'easyreg', 'Image registration via automatic differentiation', 'Miscellaneous'),
]

autosectionlabel_prefix_document = True



def setup(app):
    # Custom CSS
    # app.add_stylesheet('css/pytorch_theme.css')
    # app.add_stylesheet('https://fonts.googleapis.com/css?family=Lato')
    # Custom directives
    app.add_directive('includenodoc', IncludeDirective)
    #app.add_directive('galleryitem', GalleryItemDirective)
    app.add_directive('customgalleryitem', CustomGalleryItemDirective)
    
