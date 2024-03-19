# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
#
# Given:
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Expected Outcome:
# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]


items = [11, 45, 8, 23, 14, 12, 78, 45, 89, 67]

chunk_length = int(len(items)/3)

first_chunk = items[:chunk_length]
first_chunk.reverse()

second_chunk = items[chunk_length: 2*chunk_length]
second_chunk.reverse()

third_chunk = items[-chunk_length:]
third_chunk.reverse()

print(f"Reversed 1st chunk: {first_chunk}")
print(f"Reversed 2nd chunk: {second_chunk}")
print(f"Reversed 3rd chunk: {third_chunk}")
