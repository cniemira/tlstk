import os

import click
import x509.commands


@click.group()
@click.pass_context
@click.option('--debug', is_flag=True, default=False)
def tls(*args, **kwargs):
    if 'debug' in args:
        pass


@tls.command()
@click.argument('target')
@click.pass_context
def cert(ctx, target):
    if os.path.isfile(target):
        with open(target, 'rb') as fh:
            dat = fh.read()
        x509.commands.print_certificate_info(dat)

    else:
        raise NotImplementedError()


