# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FUSION'
copyright = 'Fusion,' \
    'TingYuan,' \
    'Steven_Zhang,' \
    'FeiYu,' \
    'Xiaojun Chen,' \
    'Zitai XuYang,' \
    'Qianguang Zhao,' \
    'S.K.Park,' \
    'QuanCui,' \
    'Hanjin Liu' \

author = 'Fusion'

release = '0.1'
version = '0.0'


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
