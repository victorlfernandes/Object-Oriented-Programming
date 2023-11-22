import scrapper
from interface import Interface
from movie import Movie

if __name__ == '__main__':
    # filmes = dados dos filmes
    # filme[0] = titulos
    # filme[1] = descrição
    # filme[2] = avaliação
    # filme[3] = thumbnail
    data = scrapper.get_filmes()

    films = []

    
    for i in range(len(data[0])):         
        films.append(Movie())
        films[i].setName(data[0][i])
        films[i].setDescription(data[1][i])
        films[i].setGrade(data[2][i])
        films[i].setImageLink(data[3][i])
        print(films[i])


    tela = Interface(films)
    tela.execute()


    #limpar imagens
    scrapper.clean_imagens()