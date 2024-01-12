from typing import Iterable


class Seq:
    def __init__(self, generator):
        self.generator = generator

    @staticmethod
    def of(*args):
        if len(args) == 1 and isinstance(args[0], Iterable):
            iterable = args[0]
        else:
            iterable = args

        def generator():
            for x in iterable:
                yield x

        return Seq(generator())

    def take(self, n):
        """
        take first n elements
        :param n:
        :return:
        """

        def generator():
            for x in range(n):
                yield next(self.generator)

        return Seq(generator())

    def drop(self, n):
        """
        drop first n elements
        :param n:
        :return:
        """

        def generator():
            for x in range(n):
                next(self.generator)
            for x in self.generator:
                yield x

        return Seq(generator())

    def flat_map(self, f):
        def generator():
            for x in self.generator:
                yield from f(x)

        return Seq(generator())

    def map(self, f):
        def generator():
            for x in self.generator:
                yield f(x)

        return Seq(generator())

    def filter(self, f):
        def generator():
            for x in self.generator:
                if f(x):
                    yield x

        return Seq(generator())

    def subscribe(self, f):
        for x in self.generator:
            f(x)

    def join(self, sep, to_str=lambda x: str(x)):
        def generator():
            for x in self.generator:
                yield to_str(x)

        return sep.join(generator())

    def reduce(self, f, init):
        for x in self.generator:
            init = f(init, x)
        return init
