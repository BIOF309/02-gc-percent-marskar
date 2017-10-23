seq_raw = input("Please enter sequence into GC calculator: ")

print("The sequence you enter is: " + seq_raw)

seq = seq_raw.upper()

# Count the number of "C"s in the above sequence

c_count = seq.count('C')

# Count the number of "G"s in the above sequence

g_count = seq.count('G')

# Add "C" and "G" counts together

gc_count = c_count + g_count

# Count the total number of nucleotides in the sequence

sequence_length = len(seq)

# Divide the total number of "C" and "G" nucleotides by the total number of nucleotides

gc_percentage = g_c_count / sequence_length * 100

# Print the percentage

print("The GC percentage of the sequence you entered is", gc_percentage)
