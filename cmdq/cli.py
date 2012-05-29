from argparse import ArgumentParser

from .queue import CommandQueue
from .resource import ResourcePool

def main():
    """Console script entry point

    """

    parser = ArgumentParser('cmdq')
    parser.add_argument('filename', help='Config filename.')
    parser.add_argument('--thread-count', type=int, default=8, help='Thread count.')
    args = parser.parse_args()

    with open(args.filename) as f:
        code = compile(f.read(), args.filename, 'exec')

    config = {'ResourcePool': ResourcePool}
    exec code in config
    if not 'cmdq' in config:
      raise Exception, 'Please provide a cmdq local in your config file.'

    CommandQueue(commands=config['cmdq'], thread_count=args.thread_count).run()

