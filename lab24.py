class InvalidDNASequence(Exception):
    pass


class DNASequence:

    def __init__(self, seq_id, sequence):
        self.seq_id = seq_id
        self.sequence = sequence.upper()

        if any(base not in "ATGC" for base in self.sequence):
            raise InvalidDNASequence("Invalid DNA sequence")

    # 1. Complement
    def complement(self):
        mapping = {
            "A": "T",
            "T": "A",
            "G": "C",
            "C": "G"
        }

        new_sequence = "".join(
            mapping[base] for base in self.sequence
        )

        return DNASequence(
            self.seq_id + "_comp",
            new_sequence
        )

    # 2. Reverse complement
    def reverse_complement(self):
        comp = self.complement()
        new_sequence = comp.sequence[::-1]

        return DNASequence(
            self.seq_id + "_revcomp",
            new_sequence
        )

    # 3. Transcription
    def transcribe(self):
        return self.sequence.replace("T", "U")

    # 4. Find restriction site
    def find_site(self, site):
        positions = []
        start = 0

        site = site.upper()

        while True:
            index = self.sequence.find(site, start)

            if index == -1:
                break

            positions.append(index + 1)
            start = index + 1

        return positions


# Test code
s2 = DNASequence("seq2", "ATGGAATTCTAG")

print("Original:", s2.sequence)
print("Complement:", s2.complement().sequence)
print("Reverse complement:", s2.reverse_complement().sequence)
print("mRNA:", s2.transcribe())
print("GAATTC at:", s2.find_site("GAATTC"))
print("TTT at:", s2.find_site("TTT"))

