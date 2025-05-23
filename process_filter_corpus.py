import gzip
import csv

target_langs = {"quz", "quy", "qvi", "qug", "quw", "yua", "gug", "tzo", "aym", "mri"}

base_path = "/home/cw-lambda/Downloads/corpus_quechua"
input_langs = f"{base_path}/train.v1.lang"
input_sentences = f"{base_path}/train.v1.src.tok.gz"
output_file = "filtered_corpus.csv"

with open(input_langs, "r", encoding="utf-8") as f_langs, \
     gzip.open(input_sentences, "rt", encoding="utf-8") as f_texts, \
     open(output_file, "w", newline='', encoding="utf-8") as out:

    writer = csv.writer(out)
    writer.writerow(["ISO", "Sentence"])

    for lang, sentence in zip(f_langs, f_texts):
        lang = lang.strip().lower()
        sentence = sentence.strip().lower()
        if lang in target_langs:
            writer.writerow([lang, sentence])
