# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


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

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Test with an empty Fasta file
    fasta_parser = FastaParser("./blank.fa")
    first_sequence = next(iter(fasta_parser), None)
    assert first_sequence is None, "Empty Fasta file should not yield valid sequences."

    # Test with a corrupted Fasta file
    with pytest.raises(ValueError):
        corrupted_parser = FastaParser("./bad.fa")
        list(corrupted_parser)

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    empty_parser = FastqParser("./blank.fa")
    empty_sequences = list(empty_parser)
    assert len(empty_sequences) == 0, "Empty Fastq file should return no sequences."

    # Test with a corrupted Fastq file
    with pytest.raises(ValueError):
        corrupted_parser = FastqParser("./bad.fa")
        list(corrupted_parser)

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    with pytest.raises(ValueError):
        fasta_with_fastq_parser = FastqParser("./bad.fa")
        list(fasta_with_fastq_parser)

    # Test reading a blank Fastq file
    blank_fastq_parser = FastqParser("./blank.fa")
    first_sequence = next(iter(blank_fastq_parser), None)
    assert first_sequence is None, "Blank Fastq file should not yield valid sequences."