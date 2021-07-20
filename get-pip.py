<!doctype html>
<html class="no-js">
  <head><meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <meta name="color-scheme" content="light dark"><meta name="generator" content="Docutils 0.17.1: http://docutils.sourceforge.net/" />
<link rel="search" title="Search" href="../search/" /><link rel="copyright" title="Copyright" href="../copyright/" /><link rel="next" title="User Guide" href="../user_guide/" /><link rel="prev" title="Getting Started" href="../getting-started/" />

    <meta name="generator" content="sphinx-3.2.1, furo 2021.06.18.beta36"/>
        <title>Installation - pip documentation v21.2.dev0</title>
      <link rel="stylesheet" href="../_static/styles/furo.css?digest=9b17055c4366e8b2949c66d6a9d8b0efe4dbaa60">
    <link rel="stylesheet" href="../_static/pygments.css">
    


<style>
  :root {
    --color-code-background: #f8f8f8;
  --color-code-foreground: black;
  
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --color-code-background: #202020;
  --color-code-foreground: #d0d0d0;
  
    }
  }

  /* For allowing end-user-specific overrides */
  .override-light {
    --color-code-background: #f8f8f8;
  --color-code-foreground: black;
  
  }
  .override-dark {
    --color-code-background: #202020;
  --color-code-foreground: #d0d0d0;
  
  }
</style><link rel="stylesheet" type="text/css" href="../_static/copybutton.css" />
    <link rel="stylesheet" type="text/css" href="../_static/tabs.css" />
    <link rel="stylesheet" type="text/css" href="https://assets.readthedocs.org/static/css/badge_only.css" />
    <link media="(prefers-color-scheme: dark)" rel="stylesheet" href="../_static/pygments_dark.css">
    <link rel="stylesheet" href="../_static/styles/furo-extensions.css?digest=ee12cdd73c4bbac24afec78d92c4afd7c2d8ea7f">
<!-- RTD Extra Head -->

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<script type="application/json" id="READTHEDOCS_DATA">{"ad_free": false, "api_host": "https://readthedocs.org", "build_date": "2021-07-17T04:20:57Z", "builder": "sphinx", "canonical_url": null, "commit": "76cd70ac", "docroot": "/docs/html/", "features": {"docsearch_disabled": false}, "global_analytics_code": "UA-17997319-1", "language": "en", "page": "installation", "programming_language": "py", "project": "pip", "proxied_api_host": "/_", "source_suffix": ".md", "subprojects": {}, "theme": "furo", "user_analytics_code": "", "version": "latest"}</script>

<!--
Using this variable directly instead of using `JSON.parse` is deprecated.
The READTHEDOCS_DATA global variable will be removed in the future.
-->
<script type="text/javascript">
READTHEDOCS_DATA = JSON.parse(document.getElementById('READTHEDOCS_DATA').innerHTML);
</script>

<script type="text/javascript" src="https://assets.readthedocs.org/static/javascript/readthedocs-analytics.js" async="async"></script>

<!-- end RTD <extrahead> -->
</head>
  <body dir="">
    
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
  <symbol id="svg-toc" viewBox="0 0 24 24">
    <title>Contents</title>
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
      stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <path stroke="none" d="M0 0h24v24H0z"/>
      <line x1="4" y1="6" x2="20" y2="6" />
      <line x1="10" y1="12" x2="20" y2="12" />
      <line x1="6" y1="18" x2="20" y2="18" />
    </svg>
  </symbol>
  <symbol id="svg-menu" viewBox="0 0 24 24">
    <title>Menu</title>
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
      stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
      class="feather feather-menu">
      <line x1="3" y1="12" x2="21" y2="12"></line>
      <line x1="3" y1="6" x2="21" y2="6"></line>
      <line x1="3" y1="18" x2="21" y2="18"></line>
    </svg>
  </symbol>
  <symbol id="svg-arrow-right" viewBox="0 0 24 24">
    <title>Expand</title>
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
      stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
      class="feather feather-chevron-right">
      <polyline points="9 18 15 12 9 6"></polyline>
    </svg>
  </symbol>
</svg>

<input type="checkbox" class="sidebar-toggle" name="__navigation" id="__navigation">
<input type="checkbox" class="sidebar-toggle" name="__toc" id="__toc">
<label class="overlay sidebar-overlay" for="__navigation"></label>
<label class="overlay toc-overlay" for="__toc"></label>



<div class="page">
  <header class="mobile-header">
    <div class="header-left">
      <label class="nav-overlay-icon" for="__navigation">
        <i class="icon"><svg><use href="#svg-menu"></use></svg></i>
      </label>
    </div>
    <div class="header-center">
      <a href="../"><div class="brand">pip documentation v21.2.dev0</div></a>
    </div>
    <div class="header-right">
      <label class="toc-overlay-icon toc-header-icon" for="__toc">
        <i class="icon"><svg><use href="#svg-toc"></use></svg></i>
      </label>
    </div>
  </header>
  <aside class="sidebar-drawer">
    <div class="sidebar-container">
      
      <div class="sidebar-sticky"><a class="sidebar-brand" href="../">
  
  
  <span class="sidebar-brand-text">pip documentation v21.2.dev0</span>
  
</a><form class="sidebar-search-container" method="get" action="../search/">
  <input class="sidebar-search" placeholder=Search name="q">
  <input type="hidden" name="check_keywords" value="yes">
  <input type="hidden" name="area" value="default">
</form><div class="sidebar-scroll"><div class="sidebar-tree">
  <ul class="current">
<li class="toctree-l1"><a class="reference internal" href="../getting-started/">Getting Started</a></li>
<li class="toctree-l1 current current-page"><a class="current reference internal" href="#">Installation</a></li>
<li class="toctree-l1"><a class="reference internal" href="../user_guide/">User Guide</a></li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../topics/">Topic Guides</a><input class="toctree-checkbox" id="toctree-checkbox-1" name="toctree-checkbox-1" type="checkbox"/><label for="toctree-checkbox-1"><i class="icon"><svg><use href="#svg-arrow-right"></use></svg></i></label><ul>
<li class="toctree-l2"><a class="reference internal" href="../topics/authentication/">Authentication</a></li>
<li class="toctree-l2"><a class="reference internal" href="../topics/caching/">Caching</a></li>
<li class="toctree-l2"><a class="reference internal" href="../topics/configuration/">Configuration</a></li>
<li class="toctree-l2"><a class="reference internal" href="../topics/dependency-resolution/">Dependency Resolution</a></li>
<li class="toctree-l2"><a class="reference internal" href="../topics/repeatable-installs/">Repeatable Installs</a></li>
<li class="toctree-l2"><a class="reference internal" href="../topics/vcs-support/">VCS Support</a></li>
</ul>
</li>
<li class="toctree-l1 has-children"><a class="reference internal" href="../cli/">Commands</a><input class="toctree-checkbox" id="toctree-checkbox-2" name="toctree-checkbox-2" type="checkbox"/><label for="toctree-checkbox-2"><i class="icon"><svg><use href="#svg-arrow-right"></use></svg></i></label><ul>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip/">pip</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_install/">pip install</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_uninstall/">pip uninstall</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_list/">pip list</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_show/">pip show</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_freeze/">pip freeze</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_check/">pip check</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_download/">pip download</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_wheel/">pip wheel</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_hash/">pip hash</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_search/">pip search</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_cache/">pip cache</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_config/">pip config</a></li>
<li class="toctree-l2"><a class="reference internal" href="../cli/pip_debug/">pip debug</a></li>
</ul>
</li>
</ul>
<p><span class="caption-text">Project</span></p>
<ul>
<li class="toctree-l1 has-children"><a class="reference internal" href="../development/">Development</a><input class="toctree-checkbox" id="toctree-checkbox-3" name="toctree-checkbox-3" type="checkbox"/><label for="toctree-checkbox-3"><i class="icon"><svg><use href="#svg-arrow-right"></use></svg></i></label><ul>
<li class="toctree-l2"><a class="reference internal" href="../development/getting-started/">Getting Started</a></li>
<li class="toctree-l2"><a class="reference internal" href="../development/contributing/">Contributing</a></li>
<li class="toctree-l2"><a class="reference internal" href="../development/ci/">Continuous Integration</a></li>
<li class="toctree-l2"><a class="reference internal" href="../development/issue-triage/">Issue Triage</a></li>
<li class="toctree-l2 has-children"><a class="reference internal" href="../development/architecture/">Architecture of pip’s internals</a><input class="toctree-checkbox" id="toctree-checkbox-4" name="toctree-checkbox-4" type="checkbox"/><label for="toctree-checkbox-4"><i class="icon"><svg><use href="#svg-arrow-right"></use></svg></i></label><ul>
<li class="toctree-l3"><a class="reference internal" href="../development/architecture/overview/">Broad functionality overview</a></li>
<li class="toctree-l3"><a class="reference internal" href="../development/architecture/anatomy/">Repository anatomy &amp; directory structure</a></li>
<li class="toctree-l3"><a class="reference internal" href="../development/architecture/configuration-files/">Configuration File Handling</a></li>
<li class="toctree-l3"><a class="reference internal" href="../development/architecture/package-finding/">Finding and choosing files (<code class="docutils literal notranslate"><span class="pre">index</span></code> and <code class="docutils literal notranslate"><span class="pre">PackageFinder</span></code>)</a></li>
<li class="toctree-l3"><a class="reference internal" href="../development/architecture/command-line-interface/">Command Line Interface</a></li>
<li class="toctree-l3"><a class="reference internal" href="../development/architecture/upgrade-options/">Options that control the installation process</a></li>
</ul>
</li>
<li class="toctree-l2"><a class="reference internal" href="../development/release-process/">Release process</a></li>
<li class="toctree-l2"><a class="reference internal" href="../development/vendoring-policy/">Vendoring Policy</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="../ux_research_design/">UX Research &amp; Design</a></li>
<li class="toctree-l1"><a class="reference internal" href="../news/">Changelog</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md">Code of Conduct</a></li>
<li class="toctree-l1"><a class="reference external" href="https://github.com/pypa/pip">GitHub</a></li>
</ul>

</div>

<div
  id="furo-sidebar-ad-placement"
  class="flat"
  data-ea-publisher="readthedocs"
  data-ea-type="readthedocs-sidebar"
  data-ea-manual="true"
></div>
</div>
      </div>
      
    </div>
  </aside>
  <main class="main">
    <div class="content">
      <article role="main">
        <label class="toc-overlay-icon toc-content-icon" for="__toc">
          <i class="icon"><svg><use href="#svg-toc"></use></svg></i>
        </label>
        <section class="tex2jax_ignore mathjax_ignore" id="installation">
<h1>Installation<a class="headerlink" href="#installation" title="Permalink to this headline">¶</a></h1>
<p>Usually, pip is automatically installed if you are:</p>
<ul class="simple">
<li><p>working in a
<a class="reference external" href="https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments" title="(in Python Packaging User Guide)"><span class="xref std std-ref">virtual environment</span></a></p></li>
<li><p>using Python downloaded from <a class="reference external" href="https://www.python.org">python.org</a></p></li>
<li><p>using Python that has not been modified by a redistributor to remove
<a class="reference external" href="https://docs.python.org/3/library/ensurepip.html#module-ensurepip" title="(in Python v3.9)"><code class="xref py py-mod docutils literal notranslate"><span class="pre">ensurepip</span></code></a></p></li>
</ul>
<section id="supported-methods">
<h2>Supported Methods<a class="headerlink" href="#supported-methods" title="Permalink to this headline">¶</a></h2>
<p>If your Python environment does not have pip installed, there are 2 mechanisms
to install pip supported directly by pip’s maintainers:</p>
<ul class="simple">
<li><p><a class="reference external" href="#ensurepip"><code class="docutils literal notranslate"><span class="pre">ensurepip</span></code></a></p></li>
<li><p><a class="reference external" href="#get-pip-py"><code class="docutils literal notranslate"><span class="pre">get-pip.py</span></code></a></p></li>
</ul>
<section id="ensurepip">
<h3><code class="docutils literal notranslate"><span class="pre">ensurepip</span></code><a class="headerlink" href="#ensurepip" title="Permalink to this headline">¶</a></h3>
<p>Python comes with an <a class="reference external" href="https://docs.python.org/3/library/ensurepip.html#module-ensurepip" title="(in Python v3.9)"><code class="xref py py-mod docutils literal notranslate"><span class="pre">ensurepip</span></code></a> module<a class="footnote-reference brackets" href="#python" id="id1">1</a>, which can install pip in
a Python environment.</p>
<p><div class="tab-set docutils container">
<input checked="True" class="tab-input" id="tab-set--0-input--1" name="tab-set--0" type="radio"/><label class="tab-label" for="tab-set--0-input--1">Linux</label><div class="tab-content docutils container">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python -m ensurepip --upgrade
</pre></div>
</div>
</div>
<input class="tab-input" id="tab-set--0-input--2" name="tab-set--0" type="radio"/><label class="tab-label" for="tab-set--0-input--2">MacOS</label><div class="tab-content docutils container">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python -m ensurepip --upgrade
</pre></div>
</div>
</div>
<input class="tab-input" id="tab-set--0-input--3" name="tab-set--0" type="radio"/><label class="tab-label" for="tab-set--0-input--3">Windows</label><div class="tab-content docutils container">
<div class="highlight-doscon notranslate"><div class="highlight"><pre><span></span><span class="gp">C:&gt;</span> py -m ensurepip --upgrade
</pre></div>
</div>
</div>
</div>
</p>
<p>More details about how <a class="reference external" href="https://docs.python.org/3/library/ensurepip.html#module-ensurepip" title="(in Python v3.9)"><code class="xref py py-mod docutils literal notranslate"><span class="pre">ensurepip</span></code></a> works and how it can be used, is
available in the standard library documentation.</p>
</section>
<section id="get-pip-py">
<h3><code class="docutils literal notranslate"><span class="pre">get-pip.py</span></code><a class="headerlink" href="#get-pip-py" title="Permalink to this headline">¶</a></h3>
<p>This is a Python script that uses some bootstrapping logic to install
pip.</p>
<ul>
<li><p>Download the script, from <a class="reference external" href="https://bootstrap.pypa.io/get-pip.py">https://bootstrap.pypa.io/get-pip.py</a>.</p></li>
<li><p>Open a terminal/command prompt, <code class="docutils literal notranslate"><span class="pre">cd</span></code> to the folder containing the
<code class="docutils literal notranslate"><span class="pre">get-pip.py</span></code> file and run:</p>
<p><div class="tab-set docutils container">
<input checked="True" class="tab-input" id="tab-set--1-input--1" name="tab-set--1" type="radio"/><label class="tab-label" for="tab-set--1-input--1">Linux</label><div class="tab-content docutils container">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python get-pip.py
</pre></div>
</div>
</div>
<input class="tab-input" id="tab-set--1-input--2" name="tab-set--1" type="radio"/><label class="tab-label" for="tab-set--1-input--2">MacOS</label><div class="tab-content docutils container">
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python get-pip.py
</pre></div>
</div>
</div>
<input class="tab-input" id="tab-set--1-input--3" name="tab-set--1" type="radio"/><label class="tab-label" for="tab-set--1-input--3">Windows</label><div class="tab-content docutils container">
<div class="highlight-doscon notranslate"><div class="highlight"><pre><span></span><span class="gp">C:&gt;</span> py get-pip.py
</pre></div>
</div>
</div>
</div>
</p>
</li>
</ul>
<p>More details about this script can be found in <a class="reference external" href="https://github.com/pypa/get-pip">pypa/get-pip</a>’s README.</p>
</section>
</section>
<section id="alternative-methods">
<h2>Alternative Methods<a class="headerlink" href="#alternative-methods" title="Permalink to this headline">¶</a></h2>
<p>Depending on how you installed Python, there might be other mechanisms
available to you for installing pip such as
<a class="reference external" href="https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers" title="(in Python Packaging User Guide)"><span class="xref std std-ref">using Linux package managers</span></a>.</p>
<p>These mechanisms are provided by redistributors of pip, who may have modified
pip to change its behaviour. This has been a frequent source of user confusion,
since it causes a mismatch between documented behaviour in this documentation
and how pip works after those modifications.</p>
<p>If you face issues when using Python and pip installed using these mechanisms,
it is recommended to request for support from the relevant provider (eg: Linux
distro community, cloud provider support channels, etc).</p>
</section>
<section id="compatibility">
<span id="compatibility-requirements"></span><h2>Compatibility<a class="headerlink" href="#compatibility" title="Permalink to this headline">¶</a></h2>
<p>The current version of pip works on:</p>
<ul class="simple">
<li><p>Windows, Linux and MacOS.</p></li>
<li><p>CPython 3.6, 3.7, 3.8, 3.9 and latest PyPy3.</p></li>
</ul>
<p>pip is tested to work on the latest patch version of the Python interpreter,
for each of the minor versions listed above. Previous patch versions are
supported on a best effort approach.</p>
<p>pip’s maintainers do not provide support for users on older versions of Python,
and these users should request for support from the relevant provider
(eg: Linux distro community, cloud provider support channels, etc).</p>
<hr class="footnotes docutils"/>
<dl class="footnote brackets">
<dt class="label" id="python"><span class="brackets"><a class="fn-backref" href="#id1">1</a></span></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">ensurepip</span></code> module was added to the Python standard library in Python 3.4.</p>
</dd>
</dl>
</section>
</section>

      </article>
      <footer>
        
        <div class="related-pages">
          <a class="next-page" href="../user_guide/">
              <div class="page-info">
                <div class="context">
                  <span>Next</span>
                </div>
                <div class="title">User Guide</div>
              </div>
              <svg><use href="#svg-arrow-right"></use></svg>
            </a>
          <a class="prev-page" href="../getting-started/">
              <svg><use href="#svg-arrow-right"></use></svg>
              <div class="page-info">
                <div class="context">
                  <span>Previous</span>
                </div>
                
                <div class="title">Getting Started</div>
                
              </div>
            </a>
        </div>

        <div class="related-information">
              <a href="../copyright/">Copyright</a> &#169; The pip developers.
            |
            Built with <a href="https://www.sphinx-doc.org/">Sphinx</a>
              and
              <a class="muted-link" href="https://pradyunsg.me">@pradyunsg</a>'s
              <a href="https://github.com/pradyunsg/furo">Furo theme</a>.
            |
            <a class="muted-link" href="../_sources/installation.md.txt"
               rel="nofollow">
              Show Source
            </a>
        </div>
        
      </footer>
    </div>
    <aside class="toc-drawer">
      
      
      <div class="toc-sticky toc-scroll">
        <div class="toc-title-container">
          <span class="toc-title">
            Contents
          </span>
        </div>
        <div class="toc-tree-container">
          <div class="toc-tree">
            <ul>
<li><a class="reference internal" href="#">Installation</a><ul>
<li><a class="reference internal" href="#supported-methods">Supported Methods</a><ul>
<li><a class="reference internal" href="#ensurepip"><code class="docutils literal notranslate"><span class="pre">ensurepip</span></code></a></li>
<li><a class="reference internal" href="#get-pip-py"><code class="docutils literal notranslate"><span class="pre">get-pip.py</span></code></a></li>
</ul>
</li>
<li><a class="reference internal" href="#alternative-methods">Alternative Methods</a></li>
<li><a class="reference internal" href="#compatibility">Compatibility</a></li>
</ul>
</li>
</ul>

          </div>
        </div>
      </div>
      
      
    </aside>
  </main>
</div>
    <script id="documentation_options" data-url_root="../" src="../_static/documentation_options.js"></script>
    <script src="../_static/jquery.js"></script>
    <script src="../_static/underscore.js"></script>
    <script src="../_static/doctools.js"></script>
    <script src="../_static/language_data.js"></script>
    <script src="../_static/clipboard.min.js"></script>
    <script src="../_static/copybutton.js"></script>
    <script src="../_static/tabs.js"></script>
    <script async="async" src="https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js"></script>
    <script src="../_static/scripts/main.js?digest=e931d09b2a40c1bb82b542effe772014573baf67"></script></body>
</html>