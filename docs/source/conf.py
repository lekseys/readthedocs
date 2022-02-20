# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'РЛЭ аэростат тепловой'
#copyright = '2021, Graziella'
#author = 'Graziella'

release = '0.1'
version = '0.1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

'fontpkg': r"""
\PassOptionsToPackage{bookmarksnumbered}{hyperref}

""",

# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{setspace}
""",

'footer': r"""
""",

'maketitle': r'''
\pagenumbering{arabic}
''',
}
