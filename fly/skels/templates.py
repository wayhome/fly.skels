import sys
from paste.script.templates import Template

from fly.skels.base import var
from fly.skels.base import BaseTemplate


class Namespace(BaseTemplate):
    _template_dir = 'tmpl/namespace'
    summary = "A namespaced package"
    use_cheetah = True

    vars = [
        var('version', 'Version', default='0.1.0'),
        var('description', 'One-line description of the package'),
        var('author', 'Author name', default='Young King'),
        var('author_email', 'Author email', default='yanckin@gmail.com'),
        var('keywords', 'Space-separated keywords/tags'),
        var('url', 'URL of homepage', default='http://www.flyzen.com'),
        var('license_name', 'License name', default='BSD'),
        var('zip_safe', 'True/False: if the package can be distributed '
            'as a .zip file', default=False)]

    def check_vars(self, vars, cmd):
        if '.' not in vars['egg']:
            print "Error: The package name must contain the dot `.`"
            sys.exit(1)

        namespace, package = vars['egg'].split('.', 1)
        vars['namespace'] = namespace
        vars['python_package'] = package
        return super(Namespace, self).check_vars(vars, cmd)


class Buildout(BaseTemplate):

    _template_dir = 'tmpl/buildout'
    summary = "A buildout package"
    use_cheetah = True

    vars = [
        var('package', 'The package contained  package (like example)',
            default='example'),
        var('version', 'Version', default='0.1.0'),
        var('description', 'One-line description of the package'),
        var('author', 'Author name', default='Young King'),
        var('author_email', 'Author email', default='yanckin@gmail.com'),
        var('keywords', 'Space-separated keywords/tags'),
        var('url', 'URL of homepage', default='http://www.flyzen.com'),
        var('license_name', 'License name', default='BSD'),
        var('zip_safe', 'True/False: if the package can be distributed '
            'as a .zip file', default=False)]


class Full(Namespace):

    _template_dir = 'tmpl/full'
    summary = "A full package"
