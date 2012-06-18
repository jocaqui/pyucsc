VERSION = 0.2

from db import create_session, tables
import config


def use(name):
    session = create_session(name)
    genome = config.use_genome(name)
    return session, genome


class HasInterval(object):
    """ Mix in for classes with the standard interval attributes """

    @property
    def interval(self):
        return config.genome.interval(self.start, self.end, chrom=self.chrom,
            strand=self.strand, value=self)


