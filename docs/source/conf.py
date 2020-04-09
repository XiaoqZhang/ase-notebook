"""Configuration for Sphinx documentation."""
# -*- coding: utf-8 -*-
#
# ase-notebook documentation build configuration file
#
# This file is ``execfile()``d with the current directory set to its
# containing dir.

import os
import subprocess
import sys

import ase_notebook

# -- General configuration ------------------------------------------------

needs_sphinx = "1.6"

if os.environ.get("READTHEDOCS", None) != "True":
    try:
        import sphinx_rtd_theme  # noqa: F401

        html_theme = "sphinx_rtd_theme"
    except ImportError:
        pass

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "ipypublish.sphinx.notebook",
]

templates_path = []
exclude_patterns = ["_build", "**/.ipynb_checkpoints", "**/example_nbs"]

master_doc = "index"
source_suffix = ".rst"

# General information about the project.
project = u"ase-notebook"
copyright = u"2019, Chris Sewell"  # noqa: A001
author = u"Chris Sewell"
# The full version, including alpha/beta/rc tags, will replace |release|
release = ase_notebook.__version__
# The short X.Y version, will replace |version|
version = ".".join(release.split(".")[:2])

# ipysphinx_export_config = "sphinx_ipypublish_all.ext.noexec"
ipysphinx_show_prompts = True
# ipysphinx_input_prompt = "In:"
# ipysphinx_output_prompt = "Out:"

git_commands = ["git", "rev-parse", "HEAD"]
try:
    git_commit = subprocess.check_output(git_commands).decode("utf8").strip()
    binderpath = "master"
except subprocess.CalledProcessError:
    git_commit = binderpath = "v{}".format(ase_notebook.__version__)

ipysphinx_prolog = r"""
{{% set docname = env.doc2path(env.docname, base='docs/source') %}}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        | This page was generated from `{{{{ docname }}}}`__.
        | Interactive online version:
          :raw-html:`<a href="https://mybinder.org/v2/gh/chrisjsewell/ase-notebook/{binderpath}?filepath={{{{ docname }}}}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/chrisjsewell/ase-notebook/blob/{git_commit}/{{{{ docname }}}}

""".format(  # noqa: E501
    git_commit=git_commit, binderpath=binderpath
)

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.6", None),
    "ase": ("https://wiki.fysik.dtu.dk/ase/", None),
    "attr": ("http://www.attrs.org/en/stable/", None),
    "ipywidgets": ("https://ipywidgets.readthedocs.io/en/stable/", None),
    "pythreejs": ("https://pythreejs.readthedocs.io/en/stable/", None),
    "svgwrite": ("https://svgwrite.readthedocs.io/en/stable/", None),
}

intersphinx_aliases = {
    ("py:class", "List"): ("py:class", "list"),
    ("py:class", "Sequence"): ("py:class", "list"),
    ("py:class", "Mapping"): ("py:class", "dict"),
    ("py:class", "Tuple"): ("py:class", "tuple"),
    ("py:class", "Callable"): ("py:class", "collections.abc.Callable"),
    ("py:class", "callable"): ("py:class", "collections.abc.Callable"),
    ("py:class", "json.encoder.JSONEncoder"): ("py:class", "json.JSONEncoder"),
}

nitpick_ignore = [
    ("py:class", "NoneType"),
    ("py:class", "attr.ib"),
    ("py:class", "attr.s"),
    ("py:class", "numpy.array"),
    ("py:class", "ase.gui.gui.GUI"),
    ("py:class", "ase.gui.images.Images"),
    ("py:class", "ipywidgets.GridspecLayout"),
    ("py:class", "pythreejs.Renderer"),
    ("py:class", "tkinter.Canvas"),
    ("py:class", "svgutils.compose.Figure"),
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "ase-notebookdoc"


# -- Options for other outputs ---------------------------------------

latex_documents = [
    (
        master_doc,
        "ase-notebook.tex",
        u"ase-notebook Documentation",
        u"Chris Sewell",
        "manual",
    )
]
# latex_logo = None
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

man_pages = [(master_doc, "ase-notebook", u"ase-notebook Documentation", [author], 1)]

texinfo_documents = [
    (
        master_doc,
        "ase-notebook",
        u"ase-notebook Documentation",
        author,
        "ase-notebook",
        (
            "Highly configurable 2D (SVG) & 3D (threejs) visualisations "
            "for ASE/Pymatgen structures, within the Jupyter Notebook"
        ),
        "Miscellaneous",
    )
]

# -- Sphinx setup for other outputs ---------------------------------------


def run_apidoc(_):
    """Run sphinx-apidoc when building the documentation.

    Needs to be done in conf.py in order to include the APIdoc in the
    build on readthedocs.
    See also https://github.com/rtfd/readthedocs.org/issues/1139
    """
    source_dir = os.path.abspath(os.path.dirname(__file__))
    apidoc_dir = os.path.join(source_dir, "apidoc")
    package_dir = os.path.join(source_dir, os.pardir, os.pardir, "ase_notebook")

    # In #1139, they suggest the route below, but this ended up
    # calling sphinx-build, not sphinx-apidoc
    # from sphinx.apidoc import main
    # main([None, '-e', '-o', apidoc_dir, package_dir, '--force'])

    cmd_path = "sphinx-apidoc"
    if hasattr(sys, "real_prefix"):  # Check to see if we are in a virtualenv
        # If we are, assemble the path manually
        cmd_path = os.path.abspath(os.path.join(sys.prefix, "bin", "sphinx-apidoc"))

    options = [
        "-o",
        apidoc_dir,
        package_dir,
        "--private",
        "--force",
        "--no-toc",
        "--separate",
    ]

    # See https://stackoverflow.com/a/30144019
    env = os.environ.copy()
    env["SPHINX_APIDOC_OPTIONS"] = "members,undoc-members,show-inheritance"
    subprocess.check_call([cmd_path] + options, env=env)


def add_intersphinx_aliases_to_inv(app):
    """Add type aliases for intersphinx.

    see https://github.com/sphinx-doc/sphinx/issues/5603
    """
    from sphinx.ext.intersphinx import InventoryAdapter

    inventories = InventoryAdapter(app.builder.env)

    for alias, target in app.config.intersphinx_aliases.items():
        alias_domain, alias_name = alias
        target_domain, target_name = target
        try:
            found = inventories.main_inventory[target_domain][target_name]
            try:
                inventories.main_inventory[alias_domain][alias_name] = found
            except KeyError:
                continue
        except KeyError:
            continue


def setup(app):
    """Add functions to the Sphinx setup."""
    app.connect("builder-inited", run_apidoc)
    app.add_config_value("intersphinx_aliases", {}, "env")
    app.connect("builder-inited", add_intersphinx_aliases_to_inv)
