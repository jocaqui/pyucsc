from ucsc import use_genome, create_session

def setup_package():
    use_genome('hg19')
    create_session('hg19')
    