
import spacy
import json

nlp = spacy.load("pt_core_news_sm")

arquivo_resultado_bert = "/home/vini/ufsc/tcc-allison-vinicios/acerto_bert_resultado_pessoa-cargo.json"
arquivo = open(arquivo_resultado_bert)
dados = json.load(arquivo)
pessoa_cargo = ""
resultado_bert = []

for item in dados:
    pessoa_cargo += item['nome'] + ","

doc = nlp(pessoa_cargo)

nomes = []
for entidade in doc.ents:
    if entidade.label_ == "PER":
        nomes.append(entidade.text)


with open("/home/vini/ufsc/tcc-allison-vinicios/nome-de-pessoas-encontrados.json", 'w', encoding="utf-8") as output_file:
    output_file.write('')
    json.dump(nomes, output_file, ensure_ascii=False)
