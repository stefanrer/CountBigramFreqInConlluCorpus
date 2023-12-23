from collections import defaultdict
from nltk import bigrams, ngrams
import string
import gc
import os
import json

custom_punctuation = string.punctuation + '«»—„“‚‘--'
# Initialize a dictionary to store bigram frequencies
bigram_freq = defaultdict(int)
# Initialize a dictionary to store unigram frequencies
unigram_freq = defaultdict(int)
# Define the chunk size (e.g., 1GB)
chunk_size = 1024 * 1024 * 1024
# Define Texts directory
work_dir = 'Texts'
# Count files in work dir
file_count = sum(len(files) for _, _, files in os.walk(work_dir))

# Generator function to read file in chunks
def read_in_chunks(file_object, chunk_size):
    remainder = ''
    while True:
        chunk = file_object.read(chunk_size)
        if not chunk:
            break
        chunk = remainder + chunk
        last_newline_index = chunk.rfind('\n\n')
        if last_newline_index != -1:
            sentences, remainder = chunk[:last_newline_index], chunk[last_newline_index:]
        else:
            sentences = chunk
            remainder = ''
        yield sentences
    if remainder:
        yield remainder


# Function to process a chunk
def process_chunk(chunk):
    # Generator expression to create sentences of conllu lemmas , exclude punctuation
    sentences_gen = (
        [
            conllu_token.split("\t")[2]
            for conllu_token in conllu_sentence.split("\n")[1:]
            if conllu_token.split("\t")[2] not in custom_punctuation and conllu_token.split("\t")[3] != "PUNCT"
        ]
        for conllu_sentence in chunk.split("\n\n")
    )
    # Process each sentence from the generator
    for sentence in sentences_gen:
        # Update bigram frequencies
        for bigram in bigrams(sentence):
            bigram_freq[' '.join(bigram)] += 1
        # Update unigram frequencies
        for unigram in ngrams(sentence, 1):
            unigram_freq[unigram[0]] += 1


for root, dirs, files in os.walk(work_dir):
    i = 0
    for file in files:
        # Check if the file is a .conllu file
        if file.endswith('.conllu'):
            filename = os.path.join(root, file)
            with open(filename, 'r', encoding='UTF8') as conllu_file:
                for chunk in read_in_chunks(conllu_file, chunk_size=chunk_size):  # 1GB chunks
                    process_chunk(chunk)
                    gc.collect()
            i += 1
            print(f"Progress: {i}/{file_count}")

# Save the bigram frequencies as a JSON file
with open('bigram_freq.json', 'w', encoding="UTF8") as file:
    json.dump(bigram_freq, file, ensure_ascii=False)

# Save the unigram frequencies as a JSON file
with open('unigram_freq.json', 'w', encoding="UTF8") as file:
    json.dump(unigram_freq, file, ensure_ascii=False)


