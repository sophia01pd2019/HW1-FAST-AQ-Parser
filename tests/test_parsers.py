# write tests for parsers
import pytest
from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True 


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # empty file
    with pytest.raises(ValueError):
        empty_parser = FastaParser("./blank.fa")
        list(empty_parser)

    # corrupted file
    with pytest.raises(ValueError):
        bad_parser = FastaParser("./bad.fa")
        list(bad_parser)

    # valid file
    fastq_parser = FastqParser("../data/test.fa")  
    sequences = list(fastq_parser)
    assert len(sequences) > 0, "FASTA file should yield valid sequences."


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """

    # Test reading a FASTA file with FastaParser
    fasta_parser = FastaParser("../data/test.fa")  
    first_sequence = next(iter(fasta_parser), None)
    assert first_sequence is not None, "FASTA file should yield valid sequences."


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # empty file
    with pytest.raises(ValueError):
        empty_parser = FastaParser("./blank.fq")
        list(empty_parser)

    # valid file
    fastq_parser = FastqParser("../data/test.fq")  
    sequences = list(fastq_parser)
    assert len(sequences) > 0, "FASTQ file should yield valid sequences."

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fasta_parser = FastaParser("../data/test.fq")  
    first_sequence = next(iter(fasta_parser), None)
    assert first_sequence is not None, "FASTQ file should yield valid sequences."
