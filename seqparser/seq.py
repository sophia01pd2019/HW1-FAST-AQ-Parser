# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # Ensure all characters in the sequence are valid nucleotides
    if not all(nuc in ALLOWED_NUC for nuc in seq):
        raise ValueError("Sequence contains invalid nucleotides.")

    # Transcribe the sequence using TRANSCRIPTION_MAPPING
    rna_seq = ''.join(TRANSCRIPTION_MAPPING[nuc] for nuc in seq)

    # Reverse the sequence if required
    if reverse:
        rna_seq = rna_seq[::-1]

    return rna_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    return transcribe(seq, reverse=True)

# Example usage:
if __name__ == "__main__":
    dna_seq = "ATCG"
    print("Transcribed RNA:", transcribe(dna_seq))
    print("Reversed Transcribed RNA:", reverse_transcribe(dna_seq))