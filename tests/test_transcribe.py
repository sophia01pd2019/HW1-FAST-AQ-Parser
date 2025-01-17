# write tests for transcribe functions

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
    # Test a valid DNA sequence
    dna_sequence = "ATCG"
    expected_rna = "UAGC"
    assert transcribe(dna_sequence) == expected_rna, "Transcription failed for a valid DNA sequence."

    # Test an empty DNA sequence
    dna_sequence = ""
    expected_rna = ""
    assert transcribe(dna_sequence) == expected_rna, "Transcription failed for an empty DNA sequence."

    # Test invalid characters in DNA sequence
    with pytest.raises(ValueError):
        transcribe("ATXG")


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # Test a valid DNA sequence
    dna_sequence = "ATCG"
    expected_rna = "CGAU"  # Reverse of "UAGC"
    assert reverse_transcribe(dna_sequence) == expected_rna, "Reverse transcription failed for a valid DNA sequence."

    # Test an empty DNA sequence
    dna_sequence = ""
    expected_rna = ""
    assert reverse_transcribe(dna_sequence) == expected_rna, "Reverse transcription failed for an empty DNA sequence."

    # Test invalid characters in DNA sequence
    with pytest.raises(ValueError):
        reverse_transcribe("ATXG")
