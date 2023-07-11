import csv
import json

arquivo_resultado_bert = "/home/vini/ufsc/resultado2.json"
arquivo_candidatos_2022 = "/home/vini/ufsc/consulta_cand_2022_BRASIL.csv"
arquivo = open(arquivo_resultado_bert)
dados = json.load(arquivo)

resultado_bert = []
todos_politicos = []



for item in dados[0]['entities']:
    if "PESSOA/CARGO" in item['class'] :
        resultado_bert.append({
            "nome": item['text'],
            "cargo":  item['class']
        })



with open(arquivo_candidatos_2022, 'r',  encoding='utf-8') as csvfile:
    columns = csv.DictReader(csvfile)
    for item in columns:
        for um_resultado_bert in resultado_bert:
            if item['NM_URNA_CANDIDATO'] in um_resultado_bert['nome'] or item['NM_CANDIDATO'] in um_resultado_bert['nome']:
                todos_politicos.append({
                    "nome_candidato_urna": item['NM_CANDIDATO'],
                    "cargo": item['DS_CARGO']
                })


with open("acerto_bert_resultado_acerto_cargo.json", 'w', encoding="utf-8") as output_file:
    output_file.write('')
    json.dump(resultado_bert, output_file,ensure_ascii=False)



'''
print(todos_politicos)
acerto_bert = []
erro_bert = []
for item in todos_politicos:
    cargo = item.split()
    for item in cargo:
        if item.title() in resultado_bert:
            acerto_bert.append(item.title())
'''
        
#teste = set(resultado_bert) - set(acerto_bert)

