Python bindings to UCSC genome browser tables
=============================================

pyucsc provides a way of accessing UCSC genome browser SQL tables and FASTA files.
It provides the following features: 

* SQL table access via SqlAlchemy 
* FASTA file access via pyfasta & fastinterval
* Python models and mappers that link together database information into 
python classes


Example
-------

A really simple example session::

    >>> from ucsc import use
    >>> from ucsc.model import KnownGene
    >>> session, genome = ucsc.use('hg19') 
    >>> vhl = session.query(KnownGene).filter(KnownGene.geneSymbol=='VHL').one()
    >>> vhl 
    KnownGene(VHL, uc003bvc.2, chr3:10183318-10193744)
     >>> vhl.transcript
    Interval(10183318, 10193744)
    >>> vhl.transcript.sequence
    'CCTCGCCTCCGTTACAACGGCCTACGGTGCTG...'




