import Grafo
import BDAEstrela
import tkinter as tk
from tkinter import *
import customtkinter as ctk


#Classe Nó
class Nó:
    def __init__ (self):
        self.cidade = self.bd.ciudades 
        self.visitado = False
        self.linha_reta = self.bd.heuristicasCuritiba #heurística da distância para o objetivo
        self.adjacentes = []

    def insere_adjacentes(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.nó.cidade, i.custo)


#Classe Adjacentes
class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo #Atributo da distância de nó a nó pela estrada

        #Atributo que representa a soma das distâncias da estrada(nó a nó) e a distância em linha reta de um nó ao objetivo.
        self.distancia_aestrela = vertice.linha_reta + self.custo




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1000x500")
        self.title("Mapa Sul")

        self.bd = BDAEstrela.BD()
        #self.grafo = Grafo.Grafo()

        #Criando o frame izquerdo
        self.left_frame = ctk.CTkFrame(self, fg_color="light gray")
        self.left_frame.pack(side="left", fill="both", expand=True)

        #Criando o frame direito
        self.frame_mapa = ctk.CTkFrame(self, fg_color='dark gray')
        self.frame_mapa.pack(side="right", fill="both", expand=True)

        #BPointer = ctk.CTkImage(file="\imagenes\BlackPointer.png")
        self.Bpointer = PhotoImage(file="imagenes\BlackPointer.png")

        #RPointer no mapa
        self.RPointer = PhotoImage(file="imagenes\RedPointer.png")

        #Canvas base para o nosso mapa
        self.canvas = tk.Canvas(master=self.frame_mapa, bg = 'white')
        self.canvas.pack(side="right", fill="both", expand=True)

        #Custos das cidades adjacentes:

        #Porto União - Paulo Frontin
        self.canvas.create_line(85,205,105,105, fill='dark gray', width=2)
        #Palmeira - Campo Largo
        self.canvas.create_line(225,75,355,75, fill='dark gray', width=2) 
        #Paulo Frontin - Irati
        self.canvas.create_line(105,105,155,75, fill='dark gray', width=2)
        #Irati - Palmeira
        self.canvas.create_line(155,75,225,75, fill='dark gray', width=2)
        #Porto União - Canoinhas
        self.canvas.create_line(85,205,135,305, fill='dark gray', width=2)
        #Porto União - São Mateus
        self.canvas.create_line(85,205,165,205, fill='dark gray', width=2)
        #São Mateus - Irati
        self.canvas.create_line(165,205,155,75, fill='dark gray', width=2)
        #São Mateus - Palmeira
        self.canvas.create_line(165,205,225,75, fill='dark gray', width=2)
        #Canoinhas - Três Barras
        self.canvas.create_line(135,305,215,255, fill='dark gray', width=2)
        #São Mateus - Três Barras
        self.canvas.create_line(165,205,215,255, fill='dark gray', width=2)
        #Canoinhas - Mafra
        self.canvas.create_line(135,305,265,305, fill='dark gray', width=2)
        #Mafra - Tijucas do Sul
        self.canvas.create_line(265,305,335,305, fill='dark gray', width=2)
        #Tijucas do Sul - SJP
        self.canvas.create_line(335,305,385,220, fill='dark gray', width=2)
        #São Mateus - Lapa
        self.canvas.create_line(165,205,260,210, fill='dark gray', width=2)
        #Lapa - Mafra
        self.canvas.create_line(260,210,265,305, fill='dark gray', width=2)
        #Lapa - Contenda
        self.canvas.create_line(260,210,300,150, fill='dark gray', width=2)
        #Balsa Nova - Campo Largo 
        self.canvas.create_line(320,110,355,75, fill='dark gray', width=2)
        #Contenda - Balsa Nova
        self.canvas.create_line(300,150,320,110, fill='dark gray', width=2)
        #Contenda - Araucária
        self.canvas.create_line(300,150,340,190, fill='dark gray', width=2)
        #Araucária - Curutiba
        self.canvas.create_line(340,190,400,145, fill='dark gray', width=2)
        #Balsa Nova - Curitiba
        self.canvas.create_line(320,110,400,145, fill='dark gray', width=2)
        #Campo Largo - Curitiba
        self.canvas.create_line(355,75,400,145, fill='dark gray', width=2)
        #SJP - Curitiba
        self.canvas.create_line(385,220,400,145, fill='dark gray', width=2)


        #Cidades:

        #Porto União
        #self.Porto = self.grafo.Porto_União #Valor conectado ao bd
        self.lbl_Porto = ctk.CTkLabel(self.canvas, text="Porto U.",fg_color="light gray", text_color="black")
        self.lbl_Porto.place(x=80,y=200,anchor="se")
        self.canvas.create_image(85,205,anchor="center",image=self.Bpointer)

        #Paulo Frontin
        #self.Paulo = self.grafo.Paulo_Frontin #Valor conectado ao bd
        self.lbl_Paulo = ctk.CTkLabel(self.canvas, text="Paulo F.",fg_color="light gray", text_color="black")
        self.lbl_Paulo.place(x=100,y=100,anchor="se")
        self.canvas.create_image(105,105,anchor="center",image=self.Bpointer)

        #Irati
        #self.Irati = self.grafo.Irati #Valor conectado ao bd
        self.lbl_Irati = ctk.CTkLabel(self.canvas, text="Irati",fg_color="light gray", text_color="black")
        self.lbl_Irati.place(x=150,y=70,anchor="se")
        self.canvas.create_image(155,75,anchor="center",image=self.Bpointer)

        #Palmeira
        #self.Palmeira = self.grafo.Palmeira #Valor conectado ao bd
        self.lbl_Palmeira = ctk.CTkLabel(self.canvas, text="Palmeira",fg_color="light gray", text_color="black")
        self.lbl_Palmeira.place(x=220,y=70,anchor="se")
        self.canvas.create_image(225,75,anchor="center",image=self.Bpointer)

        #Campo Largo
        #self.Campo = self.grafo.Campo_Largo #Valor conectado ao bd
        self.lbl_Campo = ctk.CTkLabel(self.canvas, text="Campo L.",fg_color="light gray", text_color="black")
        self.lbl_Campo.place(x=350,y=70,anchor="se")
        self.canvas.create_image(355,75,anchor="center",image=self.Bpointer)

        #Canoinhas
        #self.Canoinhas = self.grafo.Canoinhas #Valor conectado ao bd
        self.lbl_Canoinhas = ctk.CTkLabel(self.canvas, text="Canoinhas",fg_color="light gray", text_color="black")
        self.lbl_Canoinhas.place(x=130,y=310,anchor="ne")
        self.canvas.create_image(135,305,anchor="center",image=self.Bpointer)

        #São Mateus 
        #self.SMateus = self.grafo.São_Mateus #Valor conectado ao bd
        self.lbl_SMateus = ctk.CTkLabel(self.canvas, text="São Mat.",fg_color="light gray", text_color="black")
        self.lbl_SMateus.place(x=160,y=200,anchor="se")
        self.canvas.create_image(165,205,anchor="center",image=self.Bpointer)

        #Três Barras
        #self.Tres = self.grafo.Três_Barras #Valor conectado ao bd
        self.lbl_Tres = ctk.CTkLabel(self.canvas, text="Três B.",fg_color="light gray", text_color="black")
        self.lbl_Tres.place(x=200,y=250,anchor="e")
        self.canvas.create_image(215,255,anchor="center",image=self.Bpointer)

        #Mafra
        #self.Mafra = self.grafo.Mafra #Valor conectado ao bd
        self.lbl_Mafra = ctk.CTkLabel(self.canvas, text="Mafra",fg_color="light gray", text_color="black")
        self.lbl_Mafra.place(x=260,y=310,anchor="ne")
        self.canvas.create_image(265,305,anchor="center",image=self.Bpointer)

        #Tijucas do Sul
        #self.Tijucas = self.grafo.Tijucas_do_Sul #Valor conectado ao bd
        self.lbl_Tijucas = ctk.CTkLabel(self.canvas, text="Tijucas",fg_color="light gray", text_color="black")
        self.lbl_Tijucas.place(x=330,y=310,anchor="nw")
        self.canvas.create_image(335,305,anchor="center",image=self.Bpointer)

        #São José dos Pinhais
        #self.SJP = self.grafo.São_José_dos_Pinhais #Valor conectado ao bd
        self.lbl_SJP = ctk.CTkLabel(self.canvas, text="São José dos P.",fg_color="light gray", text_color="black")
        self.lbl_SJP.place(x=380,y=235,anchor="nw")
        self.canvas.create_image(385,220,anchor="center",image=self.Bpointer)

        #Lapa
        #self.Lapa = self.grafo.Lapa #Valor conectado ao bd
        self.lbl_Lapa = ctk.CTkLabel(self.canvas, text="Lapa",fg_color="light gray", text_color="black")
        self.lbl_Lapa.place(x=255,y=175,anchor="ne")
        self.canvas.create_image(260,210,anchor="center",image=self.Bpointer)

        #Contenda
        #self.Contenda = self.grafo.Contenda
        self.lbl_Contenda = ctk.CTkLabel(self.canvas, text="Contenda",fg_color="light gray", text_color="black")
        self.lbl_Contenda.place(x=295,y=145,anchor="se")
        self.canvas.create_image(300,150,anchor="center",image=self.Bpointer)

        #Balsa Nova
        #self.Balsa = self.grafo.Balsa_Nova #Valor conectado ao bd
        self.lbl_Balsa = ctk.CTkLabel(self.canvas, text="Balsa N.",fg_color="light gray", text_color="black")
        self.lbl_Balsa.place(x=315,y=105,anchor="se")
        self.canvas.create_image(320,110,anchor="center",image=self.Bpointer)

        #Araucária
        #self.Araucaria = self.grafo.Araucária #Valor conectado ao bd
        self.lbl_Araucaria = ctk.CTkLabel(self.canvas, text="Araucária",fg_color="light gray", text_color="black")
        self.lbl_Araucaria.place(x=335,y=225,anchor="se")
        self.canvas.create_image(340,190,anchor="center",image=self.Bpointer)

        #Curitiba 
        #self.Curitiba = self.grafo.Curitiba #Valor conectado ao bd
        self.lbl_Curitiba = ctk.CTkLabel(self.canvas, text="Curitiba",fg_color="light gray", text_color="black")
        self.lbl_Curitiba.place(x=410,y=150,anchor="sw")
        self.canvas.create_image(400,145,anchor="center",image=self.Bpointer)


        #Criando as 5 opções possíveis para o nosso método de pesquisa
        self.ObjCuritiba = self.bd.ObjCuritiba
        self.ObjPalmeira = self.bd.ObjPalmeira
        self.ObjLapa = self.bd.ObjLapa
        self.ObjSJP = self.bd.ObjSJP
        self.ObjContenda = self.bd.ObjContenda

        

        self.objetivos = [str(self.ObjCuritiba), str(self.ObjPalmeira), str(self.ObjLapa), str(self.ObjSJP), str(self.ObjContenda)]
        
        self.cidades = BDAEstrela.BD.ciudades
        
        self.partida = ctk.CTkComboBox(master=self.left_frame,
                                values=self.cidades,
                                width=350,
                                height=50,
                                font=("helvetica",18),
                                dropdown_font=("helvetica",18),
                                corner_radius=50)
        self.partida.set('Selecione um ponto de partida')
        self.partida.pack(pady=50)
        
        def ObjSelected(objetivo):
            for objetivo in self.cbobj:
                if objetivo == objetivo:

                    pass

        self.cbobj = ctk.CTkComboBox(master=self.left_frame,
                        values=self.objetivos,
                        width=350,
                        height=50,
                        font=("helvetica",18),
                        dropdown_font=("helvetica",18),
                        corner_radius=50,
                        command=ObjSelected
                        )
        self.cbobj.set('Selecione um destino')
        self.cbobj.pack(pady=50)

        def procurar():
            pass

        #Botão de busqueda
        self.search_btn = ctk.CTkButton(master=self.left_frame,
                                    width=250,
                                    height=50,
                                    font=("helvetica",18),
                                    corner_radius=50,
                                    text='Buscar',
                                    fg_color='dark gray',
                                    text_color='black',
                                    command=procurar)
        self.search_btn.pack(pady = 50)





app = App()
app.mainloop()