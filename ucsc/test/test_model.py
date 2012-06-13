# from ucsc import create_session
from ucsc.model import *
from ucsc.db import session
from ucsc import config

def test_gene_loading():
    g = session.query(KnownGene).limit(1).first()
    print g
    assert g

    c =  session.query(CcdsGene).limit(1).first()
    print c
    assert c

    r =  session.query(RefGene).limit(1).first()
    print r
    assert r


def test_snp_loading():
    g = session.query(KnownGene).limit(1).first()
    assert len(Snp.for_interval(g.transcript))
    # assert len(CommonSnp.for_interval(g.transcript))

def test_chainself():
    link = session.query(ChainSelfLink).first()
    print link
    print link.chain
    testint = config.genome.interval(10905, 11067, chrom='chr1')

    print ChainSelf.for_interval(testint)
    for link in ChainSelfLink.for_interval(testint):

        print link
        print link.source.sequence, link.source
        print link.dest.sequence, link.dest


def test_SNP_logic():

    print config.genome

    def get_snp(name):return session.query(CommonSnp).filter(CommonSnp.name==name).first()

    #### normal snp in + orientation
    snp  = get_snp('rs117577454')

    # check preconditions
    assert snp.strand == '+'
    assert snp.class_ == 'single'
    assert snp.refUCSC == 'C'
    assert snp.observed == 'C/G'

    # check derivations
    print snp.other_alleles()
    assert snp.other_alleles() == ['G']
    reg = snp.interval.add_border(1)
    print reg.sequence, snp.apply(reg)
    assert reg.sequence.upper() == 'TCG'
    assert snp.apply(reg)[0].upper() == 'TGG'


    #### normal snp in - orientation
    snp  = get_snp('rs67749660')

    # check preconditions
    assert snp.strand == '-'
    assert snp.class_ == 'single'
    assert snp.refUCSC == 'C'
    assert snp.observed == 'A/G'

    # check derivations

    # the other allelle here should be on the forward strand
    print snp.other_alleles()
    assert snp.other_alleles() == ['T']
    reg = snp.interval.add_border(1).copy(strand=None)
    print reg.sequence, snp.apply(reg)
    assert reg.sequence.upper() == 'GCG'
    assert snp.apply(reg)[0].upper() == 'GTG'

    #### insertion
    snp  = get_snp('rs67751522')

    # check preconditions
    assert snp.strand == '+'
    assert snp.class_ == 'insertion'
    assert snp.refUCSC == '-'
    assert snp.observed == '-/GTTTT'

    # check derivations

    # the other allelle here should be on the forward strand
    print snp.other_alleles()
    assert snp.other_alleles() == ['GTTTT']
    reg = snp.interval.add_border(1).copy(strand=None)
    print reg.sequence, snp.apply(reg)
    assert reg.sequence.upper() == 'TA'
    assert snp.apply(reg)[0].upper() == 'TGTTTTA'


    ### deletion
    snp  = get_snp('rs34628597')

    # check preconditions
    assert snp.strand == '-'
    assert snp.class_ == 'deletion'
    assert snp.refUCSC == 'AA'
    assert snp.observed == '-/TT'

    # check derivations

    # the other allelle here should be on the forward strand
    print snp.other_alleles()
    assert snp.other_alleles() == ['-']
    reg = snp.interval.add_border(1).copy(strand=None)
    print reg.sequence, snp.apply(reg)
    assert reg.sequence.upper() == 'AAAG'
    assert snp.apply(reg)[0].upper() == 'AG'

    ### MNP
    snp  = get_snp('rs71340016')

    # check preconditions
    assert snp.strand == '+'
    assert snp.class_ == 'mnp'
    assert snp.refUCSC == 'TG'
    assert snp.observed == 'CA/TG'

    # check derivations

    # the other allelle here should be on the forward strand
    print snp.other_alleles()
    assert snp.other_alleles() == ['CA']
    reg = snp.interval.add_border(1).copy(strand=None)
    print reg.sequence, snp.apply(reg)
    assert reg.sequence.upper() == 'CTGC'
    assert snp.apply(reg)[0].upper() == 'CCAC'




