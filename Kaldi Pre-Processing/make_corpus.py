import os
from os import listdir
from os.path import isfile, join
import gzip

# Mido package
from mido import MidiFile


"""
String together notes from the midi files in the database to create of
corpus of note sequences for training the language model.
"""
def make_corpus(src_dir, out_dir, corpus_file_name):

    if not os.path.exists(out_dir):
        os.makedirs(join(out_dir))

    with gzip.open(join(out_dir, corpus_file_name), 'wb') as corpus_file:

        for i, midi_file in enumerate(sorted(listdir(src_dir))):

            if midi_file == '.DS_Store':
                continue

            mid = MidiFile(join(src_dir, midi_file))

            for i, track in enumerate(mid.tracks):

                for msg in track:
                    if msg.type == 'note_on':
                        corpus_file.write(str(msg.note) + ' ')

            corpus_file.write('\n')


if __name__ == '__main__':

    src_dir = 'midi_files'
    corpus_file_name = 'corpus.en.gz'
    out_dir = 'db/TEDLIUM_release2/LM'

    make_corpus(src_dir, out_dir, corpus_file_name)

