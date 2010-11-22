#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This work was created by participants in the DataONE project, and is
# jointly copyrighted by participating institutions in DataONE. For
# more information on DataONE, see our web site at http://dataone.org.
#
#   Copyright ${year}
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# DataONE Architecture documentation build configuration file, created by
# sphinx-quickstart on Sun Nov  8 12:43:25 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.append( os.path.abspath('../sphinx-ext') )

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 
              'sphinx.ext.todo', 
              'sphinx.ext.pngmath', 
              'sphinx.ext.ifconfig',
              'sphinx.ext.graphviz',
              'rst2pdf.pdfbuilder', 
              #'sphinx.ext.todo',
              'sphinx.ext.inheritance_diagram',
              'plantuml',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

plantuml = 'plantuml'

# The suffix of source filenames.
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'DataONE Architecture'
copyright = u'2010, DataONE'
#copyright = u'''- INTEROP: Creation of an International Virtual Data Center for the Biodiversity, 
#Ecological and Environmental Sciences (NSF Award 0753138); 
#
#- DataNet Full Proposal: DataNetONE (Observation Network for Earth) (NSF Award 0830944)'''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.5.0'
# The full version, including alpha/beta/rc tags.
release = '0.5'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = '2010-April-04'
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d'

# List of documents that shouldn't be included in the build.
unused_docs = ['UseCases/uc_template', 
               'MN_APIs_v0_3', 
               'CN_APIs_v0_3',
               'REST_overview',
               'REST_object',
               'REST_meta',
               'REST_resolve',
               'REST_reserve',
               'REST_log',
               'REST_account',
               'REST_nodes',
               'REST_monitor']

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['generated', ]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

todo_include_todos = True

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'sphinxdoc'
html_theme = 'dataone'
#html_theme = 'nose'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {}
#html_theme_options = {'rightsidebar':'true'}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
html_theme_path = ['../themes', ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/dataone_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%b-%d'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'DataONEArchitecturedoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
dv_latex_author = u'''Produced by:\\\\INTEROP: Creation of an International Virtual Data Center for the Biodiversity, 
Ecological and Environmental Sciences (NSF Award 0753138)\\\\and\\\\DataNet Full Proposal: DataNetONE (Observation Network for Earth) (NSF Award 0830944)'''
latex_documents = [
  ('index', 'DataONEArchitecture.tex', project,
   dv_latex_author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = True
latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_preamble = '\\usepackage{pdflscape}'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

pdf_documents = [
  ('index', 'DataONEArchitecture_0_0_4', u'DataONE Architecture Documentation',
   u'VDC Project, DataONE CCIT', 'manual'),
  #('MN_APIs_v0_3', 'MN_APIs_v0_3', u'MN API 0.3',
  #u'VDC Project, DataONE CCIT', 'manual'),
]

#pdf_default_dpi = 400

pdf_stylesheets = ['sphinx', ]

pdf_fit_mode = "shrink"

pdf_break_level = 1

pdf_breakside = 'any'

pdf_use_index = True

pdf_use_modindex = True

pdf_use_coverpage = False

pdf_splittables = False

pdf_page_template = 'cutePage'

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = dv_latex_author
epub_publisher = u'DataONE.org'
epub_copyright = copyright

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3
