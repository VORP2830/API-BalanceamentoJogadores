from flask import Flask, request
import copy
import json
import os

app = Flask(__name__)

def balanceamento(pessoasOrdenadas, quantidadePessoasTimes):
    quantidadeTotal = len(pessoasOrdenadas)
    quantidadeTimes = quantidadeTotal // quantidadePessoasTimes
    quantidadeExcedentes = quantidadeTotal % quantidadePessoasTimes

    if (quantidadeExcedentes):
        return f'Não é possivel fazer esse balanceamento pois temos {quantidadeExcedentes} jogadores excedente. Adicione mais {quantidadePessoasTimes - quantidadeExcedentes} jogador(es) para fazer o balanceamento'
    
    times = [[] for i in range(quantidadeTimes)]

    for i in range(quantidadePessoasTimes):
        for j in range(quantidadeTimes):
            if pessoasOrdenadas:
                if(len(times[j]) > 0):
                    times[j].append(pessoasOrdenadas.pop(len(pessoasOrdenadas)-1))
                else:
                    times[j].append(pessoasOrdenadas.pop(0))

    return json.dumps(times)

@app.route('/')
def index():
    return '<h1 style="text-align: center;">Bem vindo à API</h1>'

@app.route('/', methods=['POST'])
def postBalanceamento():
    jogadores = request.json
    pessoasOrdenadas = sorted(jogadores['Pessoas'], key=lambda x: x["media"], reverse=True)
    quantidadePessoasTimes = jogadores['PessoasPorTime']
    return balanceamento(pessoasOrdenadas, quantidadePessoasTimes)

if __name__ == "__main__":
    app.run(host='0.0.0.0')