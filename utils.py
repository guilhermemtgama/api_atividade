from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome = 'jose',idade = 27)
    print(pessoa, pessoa.idade)
    pessoa.save()


def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa =Pessoas.query.filter_by(nome = 'joao').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome = 'maria').first()
    pessoa.idade = 24
    pessoa.save()

if __name__ == '__main__':
    insere_pessoas()
    consulta()
    altera_pessoa()
