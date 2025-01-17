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
    fasta_content = """>Sequence1
    ATCGATCGATCG
    >Sequence2
    GCTAGCTAGCTA
    """
    with open("./test_fasta.fa", "w") as fasta_file:
        fasta_file.write(fasta_content)
    
    # Test reading a FASTA file with FastaParser
    fasta_parser = FastaParser("./test_fasta.fa")  # Assuming a valid FASTA file with headers
    first_sequence = next(iter(fasta_parser), None)
    assert first_sequence is not None, "FASTA file should yield valid sequences when read by FastaParser."

    # Test reading a FASTA file with FastqParser
    with pytest.raises(ValueError, match="FASTQ format expected"):
        fastq_parser = FastqParser("./test_fasta.fa")
        list(fastq_parser)

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

    # corrupted file
    with pytest.raises(ValueError):
        bad_parser = FastaParser("./bad.fq")
        list(bad_parser)

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fasta_parser = FastaParser("./blank.fq")  # Assuming a valid FASTQ file with headers
    first_sequence = next(iter(fasta_parser), None)
    assert first_sequence is not None, "FASTQ file should yield valid sequences when read by FastaParser."

    with pytest.raises(ValueError, match="FASTA format expected"):
        fastq_parser = FastqParser("./blank.fq")
        list(fastq_parser)