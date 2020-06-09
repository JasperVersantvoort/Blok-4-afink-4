from flask import Flask, render_template, request
from Bio.Alphabet import IUPAC, generic_dna, generic_rna, generic_protein, \
    _get_base_alphabet
from Bio.Seq import Seq

app = Flask(__name__)


@app.route('/')
def web_pagina():
    seq = request.args.get("seq", '')
    seq = seq.upper()
    if check_dna(seq):
        bio_dna = Seq(seq, generic_dna)
        return render_template("Afvink4.html",
                               soort='DNA',
                               een=(bio_dna.transcribe()),
                               twee=(bio_dna.translate()))

    elif check_rna(seq):
        bio_rna = Seq(seq, generic_rna)
        return render_template("Afvink4.html",
                               soort='RNA',
                               een=(bio_rna.back_transcribe()),
                               twee=(bio_rna.translate()))

    elif check_eiwit(seq):
        bio_eiwit = Seq(seq, generic_rna)
        return render_template("Afvink4.html",
                               soort='Eiwit',
                               een="klik op de link en druk op blast",
                               twee="https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&QUERY=" + str(seq))

    else:

        return render_template("Afvink4.html",
                               soort = 'Geen DNA, RNA of eiwit',
                               een='',
                               twee='')


def check_dna(seq):
    for i in seq:
        if i not in ['A','C', 'G','T']:
            return False
    return True

def check_rna(seq):
    for i in seq:
        if i not in ['A', 'C', 'G', 'U']:
            return False
    return True

def check_eiwit(seq):
    amino = ["A",
             "R",
             "N",
             "D",
             "B",
             "C",
             "E",
             "Q",
             "Z",
             "G",
             "H",
             "I",
             "L",
             "K",
             "M",
             "F",
             "P",
             "S",
             "T",
             "W",
             "Y",
             "V",
             "X"]
    for i in seq:
        if i not in amino:
            return False
    return True



if __name__ == '__main__':
    seq = 'gggaaaggg'
    check_seq(seq)
    app.run()
