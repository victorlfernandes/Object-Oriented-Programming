import PySimpleGUI as sg
import scrapper
from PIL import Image
import movie
import io

'Implementa uma interface com várias páginas para a exibição dos filmes em cartaz'
class Interface:

    def __init__(self, films):

        sg.theme('DarkBlue')
        self.windows = []
        k = 0


        #Montagem das páginas (janelas) do programa
        for i in range(len(films)):

            posters_column = []
            information_column = []

            
            image = Image.open(str(films[k].getName()) + ".jpg")
            image.thumbnail((210,300))
            bio = io.BytesIO()
            image.save(bio, format="PNG")

            posters_column.append([sg.Image(key=k)])
            posters_column.append([sg.Text(" ")])
                
            
            
            information_column.append([sg.Text(films[k].getName(), font="Bold 15")])
            information_column.append([sg.Text("Avaliação: "), sg.Text(films[k].getGrade())])
            information_column.append([sg.Text(films[k].getDescription(), size=(50, 7))])
            information_column.append([sg.Text("_" * 115)])
                
            
            if i == 0:
                information_column.append([sg.Button("Página Anterior", visible=False), sg.Button("Próxima Página")])
            elif i == (len(films) - 1):
                information_column.append([sg.Button("Página Anterior"), sg.Button("Próxima Página", visible=False)])
            else:
                information_column.append([sg.Button("Página Anterior"), sg.Button("Próxima Página")])


            #Definição do Layout: coluna com os posters + coluna com as informações dos filmes
            layout = [
                [sg.Column(posters_column), sg.Column(information_column)]
            ]

            if i == 0:
                self.windows.append(sg.Window("Filmes em Cartaz", layout, size=(700,300), finalize=True))
            else:
                self.windows.append(sg.Window("Filmes em Cartaz", layout, size=(700,300), finalize=True))
                self.windows[i].hide()
            

            #Atualização das imagens (posters)
            self.windows[i][k].update(data=bio.getvalue())
            k += 1



    'Controla a execução da interface do programa com as suas diversas janelas'
    def execute(self):

        page = 0

        while True:

            window, events, values = sg.read_all_windows()

            #Quando a janela é fechada
            if events == sg.WIN_CLOSED:
                break

            #Navegação entre as janelas
            if window == self.windows[page] and events == "Próxima Página":
                self.windows[page+1].un_hide()
                self.windows[page].hide()
                page += 1
            if window == self.windows[page] and events == "Página Anterior":
                self.windows[page-1].un_hide()
                self.windows[page].hide()
                page -= 1
            
                
    