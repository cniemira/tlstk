# tlstk

*Pre-Alpha*

TLS ToolKit for Python and CLI

The goal for this project is to unify the various tools, scripts, and modules I've written into a single comprehensive open-source package that does 'all things TLS.' Aside from the underlying modules, the key components will be a general-purpose `tls` command line tool and a bunch of [iPython](https://ipython.org) magics for working interactively and [Jupyter](https://jupyter.org) support.

#### Features to include:

* Certificate inspection (a la nmap `ssl-certs` script)
* x509 dissection (a la `openssl x509`)
* Signature/trust validation
* Basic client (a la `openssl s_client`)
* Protocol diagnostics (port of unreleaed code)
* Protocol fuzzing
* Stress/torture test driver and analytics (port of unreleased code; `cypherlab`)
* Vulnerability assessor (port of unreleased code; `tlsreport`)
