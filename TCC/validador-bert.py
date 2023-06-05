import csv
import json

arquivo_resultado_bert = "/home/vini/ufsc/resultado.json"
arquivo_candidatos_2022 = "/home/vini/ufsc/consulta_cand_2022_BRASIL.csv"
arquivo = open(arquivo_resultado_bert)
dados = json.load(arquivo)

resultado_bert = {}
todos_candidatos = []


for item in dados[0]['entities']:
    resultado_bert.update({
        item['text']: item['class']
    })


with open(arquivo_candidatos_2022, 'r',  encoding='utf-8') as csvfile:
    columns = csv.DictReader(csvfile)
    for item in columns:
        todos_candidatos.append({
            "cargo": item['DS_CARGO'],
            "nome": item['NM_CANDIDATO'],
            "nome_na_urna": item['NM_URNA_CANDIDATO'],
            "estado": item['SG_UF']
        })

acerto_bert = {}
erro_bert = []
for item in todos_candidatos:
    nome = item['nome'].title()
    nome_na_urna = item['nome_na_urna'].title()
    if nome in resultado_bert:
        acerto_bert.update({nome: resultado_bert[nome]})
        continue
    if nome_na_urna in resultado_bert:
        acerto_bert.update({nome: resultado_bert[nome_na_urna]})
        
teste = set(resultado_bert) - set(acerto_bert)


with open("acerto_bert_resultado.json", 'w', encoding="utf-8") as output_file:
    output_file.write('')
    json.dump(acerto_bert, output_file,ensure_ascii=False)


with open("erro_bert_resultado1.json", 'w', encoding="utf-8") as output_file:
    output_file.write('')
    json.dump(erro_bert, output_file,ensure_ascii=False)
