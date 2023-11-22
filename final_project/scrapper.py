import scrapy
import urllib.request
from scrapy.crawler import CrawlerProcess
from PIL import Image
import validators
import os

info = [[], [], [], []]


class CineSpider(scrapy.Spider):
    name = 'cine'
    #allowed_domains = ['cine.com']
    start_urls = ['https://www.adorocinema.com/filmes/numero-cinemas/']
    pag_atual = 1

    def parse(self, response):
        total = len(response.css('.pagination-item-holder .button::text').getall())

        # coletar titulos
        titulo = response.css('.entity-card-list .meta-title-link::text').getall()
        # coletar descração
        descricao = response.css('.content-txt::text').getall()

        # coletar verificação pra cada nota
        nota_ver = response.css('.card.entity-card').getall()
        # coletar avaliação
        nota_aux = response.css('.rating-item:nth-child(1) .stareval-note::text').getall()
        
        #avaliação final
        nota = []
        j = 0
        for i in range(0, len(nota_ver)):
            if "rating-item" in nota_ver[i]:
                nota.append(nota_aux[j])
                j += 1
            else:
                #caso não contenha "rating-item" adicionar avaliação como 0
                nota.append("0,0")

        # coletar link das imagens
        imagem_link = []
        imagens = []

        imgData = response.css('.entity-card-list .thumbnail-img::attr(data-src)').extract()
        imgSrc = response.css('.entity-card-list .thumbnail-img::attr(src)').extract()

        for i in imgSrc:
            # alguns link não são validos, apartir disso utilizar links relacionadas a (data-src)
            if validators.url(i):
                imagem_link.append(i)
            else:
                break

        imagem_link += imgData

        # baixar imagens e adicionar a lista de imagens
        for i in range(0, len(imagem_link)):
            urllib.request.urlretrieve(imagem_link[i], titulo[i] + ".jpg")
            imagens.append(Image.open(titulo[i] + ".jpg"))

        # adicionar tudo a variavel global
        global info
        info[0] += titulo
        info[1] += descricao
        info[2] += nota
        info[3] += imagens

        # verificar se o botão prox está desabilidado
        var = response.css(".button-right.button-disabled").extract()

        self.pag_atual += 1
        next_page = 'https://www.adorocinema.com/filmes/numero-cinemas/?page={}'.format(self.pag_atual)

        # caso não esteja continua pra proxima pagina
        if len(var) == 0:
            yield scrapy.Request(next_page, callback=self.parse)


# start no scrapper e retorna info
def get_filmes():
    process = CrawlerProcess()
    process.crawl(CineSpider)
    process.start()
    return info


# limpar imagens do diretorio
def clean_imagens():
    for i in info[3]:
        i.close()

    for file in os.listdir(os.getcwd()):
        if file.endswith('.jpg'):
            os.remove(file)