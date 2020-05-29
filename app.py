from flask import Flask, render_template, request
from Bio.Alpahabet import IUPAC
from Bio.Seq import Seq

app = Flask(__name__)


@app.route('/')
def web_pagina():
    seq = request.args.get("seq", '')
    check_seq(seq)
    return render_template("Afvink4.html", seq=seq)

def check_seq(seq):
    print(seq)
    my_seq = Seq("AGGAGG")
    my_seq






if __name__ == '__main__':
    app.run()
