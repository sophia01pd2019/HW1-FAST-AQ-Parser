# write tests for transcribe functions
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # valid
    dna_sequence = "GTCA"
    expected_rna = "CAGU"
    assert transcribe(dna_sequence) == expected_rna, "Transcription failed for a valid DNA sequence."

    # empty
    dna_sequence = ""
    expected_rna = ""
    assert transcribe(dna_sequence) == expected_rna, "Transcription failed for an empty DNA sequence."

    # invalid
    with pytest.raises(ValueError):
        transcribe("XGPT")


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # valid
    dna_sequence = "GTCA"
    expected_rna = "UGAC"  
    assert reverse_transcribe(dna_sequence) == expected_rna, "Reverse transcription failed for a valid DNA sequence."

    # empty
    dna_sequence = ""
    expected_rna = ""
    assert reverse_transcribe(dna_sequence) == expected_rna, "Reverse transcription failed for an empty DNA sequence."

    # invalid
    with pytest.raises(ValueError):
        reverse_transcribe("ATXG")
