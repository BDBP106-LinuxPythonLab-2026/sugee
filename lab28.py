# #Q1
# from Bio.Seq import Seq
# from Bio.SeqUtils import gc_fraction
#
# thrL = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
#
# print(f"Length: {len(thrL)}")
# print(f"GC content: {gc_fraction(thrL) * 100:.2f}%")
# print(f"Translation (to_stop=True): {thrL.translate(to_stop=True)}")
# print(f"Translation (to_stop=False): {thrL.translate(to_stop=False)}")
# print(f"ACC Count: {thrL.count('ACC')}")
# print(f"Last Codon: {thrL[-3:]}")
# print(f"First 12 bases of RC: {thrL.reverse_complement()[:12]}")

#Q2
# from Bio import SeqIO
# from Bio.SeqUtils import gc_fraction
#
# # 1. Read lab_genes.fasta into a list and print the record count
# records = list(SeqIO.parse("lab_genes.fasta", "fasta"))
# print(f"Total records read: {len(records)}\n")
#
# # 2. Print a table of ID, length, GC %, and protein (up to the first stop codon)
# print(f"{'ID':<15} | {'Length':<6} | {'GC %':<6} | {'Protein (to stop)'}")
# print("-" * 65)
#
# for record in records:
#     length = len(record.seq)
#     gc_pct = gc_fraction(record.seq) * 100
#     protein = record.seq.translate(to_stop=True)
#
#     print(f"{record.id:<15} | {length:<6} | {gc_pct:<6.1f} | {protein}")
# print()
#
# # 3. Write genes with GC content >= 50% to a new file and print the count
# high_gc_records = [rec for rec in records if gc_fraction(rec.seq) * 100 >= 50]
#
# count_written = SeqIO.write(high_gc_records, "lab_high_gc.fasta", "fasta")
# print(f"Number of high GC records written: {count_written}\n")
#
# # 4. Print the IDs sorted from highest to lowest GC content using a lambda function
# sorted_records = sorted(records, key=lambda rec: gc_fraction(rec.seq), reverse=True)
#
# print("IDs sorted by GC content (Highest to Lowest):")
# for rec in sorted_records:
#     gc_pct = gc_fraction(rec.seq) * 100
#     print(f"- {rec.id} ({gc_pct:.1f}%)")
#
# import os
# from Bio import SeqIO
# from Bio.SeqUtils import gc_fraction
#
# # Find the directory where lab28.py is located
# script_dir = os.path.dirname(os.path.abspath(__file__))
# fasta_path = os.path.join(script_dir, "lab_genes.fasta")
#
# # Now read the file using the calculated path
# records = list(SeqIO.parse(fasta_path, "fasta"))
#


# #Q3
# import re
# from Bio.Seq import Seq
#
# mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")
#
# # 1. Generate and translate all 6 frames (trimming to multiples of 3)
# frames = {}
# fwd, rev = mystery, mystery.reverse_complement()
#
# for i in range(3):
#     frames[f"+{i+1}"] = str(fwd[i : len(fwd) - (len(fwd) - i) % 3].translate())
#     frames[f"-{i+1}"] = str(rev[i : len(rev) - (len(rev) - i) % 3].translate())
#
# print("--- Six Reading Frame Translations ---")
# for name, prot in frames.items():
#     print(f"Frame {name}: {prot}")
# print("\n" + "="*40 + "\n")
#
# # 2. Use Regex to find the longest ORF starting with M and ending with *
# longest_orf = ""
# longest_frame = ""
#
# # Regex pattern: 'M', followed by zero or more non-stop characters, ending with '*'
# # We use a lazy match (.*?) to find the immediate next stop codon
# orf_pattern = re.compile(r"M.*?\*")
#
# for name, prot in frames.items():
#     # findall finds non-overlapping matches; finditer tracks cross-overlaps if needed
#     matches = orf_pattern.findall(prot)
#     for orf in matches:
#         if len(orf) > len(longest_orf):
#             longest_orf = orf
#             longest_frame = name
#
# print("--- Longest Open Reading Frame Found ---")
# if longest_orf:
#     print(f"Found in Frame: {longest_frame}")
#     print(f"Protein Sequence: {longest_orf}")
#     print(f"Length (in amino acids): {len(longest_orf)}")
# else:
#     print("No valid ORF found (M...*).")
#
#
# #Q4
# from Bio import SeqIO
# from Bio.Seq import Seq
# from Bio.SeqRecord import SeqRecord
# from Bio.SeqFeature import SeqFeature, FeatureLocation
#
# # Initial sequence
# plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")
#
# # =====================================================================
# # 1. Create a SeqRecord and add annotations/features
# # =====================================================================
# record = SeqRecord(
#     plasmid_seq,
#     id="PLAB001",
#     name="PLAB001",
#     description="Cloning construct with BamHI, coding sequence, and EcoRI sites"
# )
#
# # Set the mandatory GenBank molecule type annotation
# record.annotations["molecule_type"] = "DNA"
#
# # Define the features using Python-style 0-indexed coordinates
# features_to_add = [
#     SeqFeature(
#         FeatureLocation(0, 6),
#         type="misc_feature",
#         qualifiers={"note": ["BamHI site"]}
#     ),
#     SeqFeature(
#         FeatureLocation(8, 41),
#         type="CDS",
#         qualifiers={"gene": ["labA"], "translation": ["MASKGEELFT"]}
#     ),
#     SeqFeature(
#         FeatureLocation(41, 47),
#         type="misc_feature",
#         qualifiers={"note": ["EcoRI site"]}
#     )
# ]
#
# record.features = features_to_add
#
# # =====================================================================
# # 2. Write it to lab_construct.gb in GenBank format
# # =====================================================================
# filename = "lab_construct.gb"
# SeqIO.write(record, filename, "genbank")
# print(f"Successfully wrote the GenBank file to '{filename}'.\n")
#
# # =====================================================================
# # 3. Read it back with SeqIO.read() and list details (1-based format)
# # =====================================================================
# imported_record = SeqIO.read(filename, "genbank")
#
# print("--- Parsed Features Table (1-Based Coordinates) ---")
# for feature in imported_record.features:
#     # Biopython automatically formats .start and .end as 1-based when printing,
#     # or we can display them explicitly. Note: internally they stay 0-based.
#     start_1based = int(feature.location.start) + 1
#     end_1based = int(feature.location.end)
#
#     # Safely look for gene name or note qualifier
#     gene_or_note = ""
#     if "gene" in feature.qualifiers:
#         gene_or_note = f"gene={feature.qualifiers['gene'][0]}"
#     elif "note" in feature.qualifiers:
#         gene_or_note = f"note={feature.qualifiers['note'][0]}"
#
#     print(f"Type: {feature.type:<12} | Start: {start_1based:<2} | End: {end_1based:<2} | Info: {gene_or_note}")
# print("\n" + "=" * 60 + "\n")
#
# # =====================================================================
# # 4. Extract the CDS, translate it, and check against stored qualifier
# # =====================================================================
# print("--- Verifying Translation Alignment ---")
# for feature in imported_record.features:
#     if feature.type == "CDS":
#         # Extract the sequence using the feature's location mapping
#         cds_seq = feature.extract(imported_record.seq)
#
#         # Translate to protein (stopping right before the stop codon if any)
#         calculated_translation = str(cds_seq.translate(to_stop=True))
#         stored_translation = feature.qualifiers["translation"][0]
#
#         print(f"Extracted CDS Sequence: {cds_seq}")
#         print(f"Calculated Translation: {calculated_translation}")
#         print(f"Stored GenBank Value:   {stored_translation}")
#
#         # Validation check
#         if calculated_translation == stored_translation:
#             print("Verification Result: SUCCESS - Translations match exactly!")
#         else:
#             print("Verification Result: FAILED - Discrepancy found.")
