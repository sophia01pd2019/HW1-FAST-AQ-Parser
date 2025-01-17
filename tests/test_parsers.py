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
    with pytest.raises(ValueError, match="0 lines"):
        fasta_parser = FastaParser("./blank.fa")
        list(fasta_parser)

    # Test with a corrupted Fasta file - Expect ValueError
    with pytest.raises(ValueError, match="corrupted"):
        FastaParser("./bad.fa")

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # Test with an empty Fastq file - Expect ValueError
    with pytest.raises(ValueError, match="0 lines"):
        fastq_parser = FastqParser("./blank.fa")
        list(fastq_parser)

    # Test with a valid Fastq file (if available)
    # Assuming you have a valid file called `valid.fastq`
    valid_parser = FastqParser("./valid.fastq")
    sequences = list(valid_parser)
    assert len(sequences) > 0, "Valid Fastq file should return sequences."


def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Test reading a FASTA file with FastqParser should raise ValueError
    # Test reading a FASTA file with FastqParser should raise ValueError
    with pytest.raises(ValueError, match="invalid format"):
        fastq_parser = FastqParser("./bad.fa")
        list(fastq_parser)

    # Test reading a blank Fastq file - Expect ValueError
    with pytest.raises(ValueError, match="0 lines"):
        FastqParser("./blank.fa")