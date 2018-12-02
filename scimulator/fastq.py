import numpy as np
from numpy.random import choice
from scimulator.utils import rgamma
from textwrap import wrap


def generate_reads(position, counts, mu, sd, readLength=100, seq="".join(choice(list("ACGT"), size=5000))):

    if not len(position) == len(counts) == len(mu) == len(sd):
        raise ValueError("Argument lengths must be identical! Found: %d, %d, %d, %d" % \
                         (len(position), len(counts), len(mu), len(sd)))

    if not (isinstance(readLength, int) and readLength > 0):
        raise ValueError("`readLength` must be positive integer! Found: %s" % readLength)

    # work with reversed transcripts, i.e., coords are distance from 3' end
    txs_rev = [seq[::-1][pos:] for pos in position]

    # generate random distances from 3' end
    xss = (rgamma(mu=m, sd=s, size=n).astype(np.integer) for m, s, n in zip(mu, sd, counts))

    # extract corresponding sequences
    reads = [[tx[max(0, x - readLength):x][::-1] for x in xs] for tx, xs in zip(txs_rev, xss)]

    return reads, [tx[::-1] for tx in txs_rev]


def reads_to_fastq(reads, filename):
    """
    Outputs reads in FASTQ format, with names indexed by UTR.

    :param reads: list of string lists, each list corresponds to reads originated from a different UTR
    :param filename: FASTQ file
    :return: None
    """

    with open(filename, 'w') as fq:
        for i, utr in enumerate(reads):
            for j, read in enumerate(utr):
                fq.writelines([
                    "@UTR%d.%d\n" % (i, j),
                    read, "\n",
                    "+\n",
                    "I"*len(read), "\n"
                ])

    fq.close()


def txs_to_fasta(txs, filename, truncate=0):
    """
    Write reads to file in FASTQ format, with names indexed by UTR.

    :param txs: list of strings representing transcripts with alternative 3' UTRs
    :param filename: FASTA file
    :param truncate: size of output transcripts, measured from 3' end
    :return: None
    """

    with open(filename, 'w') as fa:
        for i, tx in enumerate(txs):
            fa.write(">UTR%d\n" % i)
            fa.writelines(["\n".join(wrap(tx[-truncate:], 80)), "\n"])

    fa.close()


if __name__ == '__main__':
    from os import makedirs
    reads, txs = generate_reads([0, 100], [100, 100], [300, 300], [100, 100])

    makedirs("tmp", exist_ok=True)

    txs_to_fasta(txs, "tmp/txs.d100.w500.fa", truncate=500)
    reads_to_fastq(reads, "tmp/reads.d100.fq")

