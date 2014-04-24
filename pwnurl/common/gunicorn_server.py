import sys

from flask.ext.script import Command, Option

class GunicornServer(Command):

    """ Runs the Flask production gunicorn server """

    def __init__(self, host, port):
        self.host = host or '127.0.0.1'
        self.port = port

    def get_options(self):
        return (
            Option('--host', dest='host', default=self.host),
            Option('--port', dest='port', type=int, default=self.port),
            Option('--config', dest='config', type=str, default='setup.cfg'),
            Option('-d', '--daemon', default=False, action='store_true')
        )

    def handle(self, app, host, port, config, **kwargs):
        from ConfigParser import ConfigParser

        gc = ConfigParser()
        try:
            gc.readfp(open(config))
        except IOError, ex:
            print ex
            sys.exit(1)

        initopts = {'bind': '%s:%s' % (host, port)}
        initopts.update(kwargs)

        uniopts = dict(list(gc.items('gunicorn')))
        options = dict(uniopts, **initopts)

        from gunicorn import version_info

        if version_info >= (0, 9, 0):
            from gunicorn.app.base import Application

            class FlaskApplication(Application):

                def init(self, parser, opts, args):
                    return options

                def load(self):
                    return app

            sys.argv = sys.argv[:2]

            FlaskApplication().run()
