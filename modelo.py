class Programa:
    # para deixa uma variavel privada usamos 2s "__" neste caso vamos usar somente um "_", ele terá a mesma ideia de privacidade mas com a diferencia é poder compartilhar para as classes filhas
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - {self.likes} Likes')


# Definir minha classe mãe que é o "Programa", assim podemos compartilhar tudo q estiver na classe mãe para as outras classe que sejam filhas.
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração 🕒: {self.duracao} min - {self.likes} Likes 👍'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)  # chamar a Classe mãe
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - {self.likes} Likes 👍'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


# Lista de filmes e series
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

# dando likes nos filmes e series
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

listinha = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', listinha)

# percorrer o tamanho da lista (quantidade) e retornar uma resposta
for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')
