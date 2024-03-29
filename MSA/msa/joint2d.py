# -*- coding: UTF-8 -*-

from pylab import *

class Joint():
    def __init__(self, X, Y, FX, FY, MZ, type = "rj"):
        """ Define un nudo de la estructura a partir de sus coordenadas y tipo """

        # Coordenadas en el sistema de referencia absoluto
        self.X = X # Horizontal
        self.Y = Y # Vertical

        # Tipo de nudo o apoyo
        self.type = type # type: {fs, hs, rs, rj, hj}
        
        # Cargas en el nudo
        self.FX = FX
        self.FY = FY
        self.MZ = MZ

        # Desplazamientos y giro
        self.dX = 0
        self.dY = 0
        self.gZ = 0

        # Reacciones
        self.RX = 0
        self.RY = 0
        self.RMZ = 0

    def set_loads(self, FX, FY, MZ):
        """ Establece las cargas en el nudo según los ejes globales """
        (self.FX, self.FY, self.MZ) = (FX, FY, MZ)

    def get_loads(self):
        """ Devuelve la lista de cargas del nudo """
        return [self.FX, self.FY, self.MZ]

    def set_displacements(self, dX, dY, gZ):
        """ Establece los desplazamientos y el giro del nudo en los ejes globales """
        (self.dX, self.dY, self.gZ) = (dX, dY, gZ)

    def set_reactions(self, RX, RY, RMZ):
        """ Establece las reacciones del apoyo en los ejes globales """
        (self.RX, self.RY, self.RMZ) = (RX, RY, RMZ)
        
    def draw_joint(self):
        """ Representa el nudo o apoyo """        
        if self.type == "fs" : # fixed support
            text(self.X, self.Y, "$\\bot$\n", va='top', ha='center', fontsize=20, color='black')
        else :
            if self.type == "hj" :
                text(self.X, self.Y, "o", va='center', ha='center', fontsize=10, color='black') # hinge joint
            if self.type == "hs" : # hinge support
                text(self.X, self.Y, "$\\bigtriangleup$\n", va='top', ha='center', fontsize=20, color='black')
            elif self.type == "rs" : # roller support
                text(self.X, self.Y, "$\\triangleq$\n", va='top', ha='center', fontsize=20, color='black')

    def draw_loads(self):
        """ Dibuja las cargas sobre el nudo """
        self.draw_forces(self.FX, self.FY, self.MZ)

    def draw_reactions(self):
        """ Dibuja las reacciones en los apoyos """
        self.draw_forces(round(self.RX, 1), round(self.RY, 1), round(self.RMZ, 1))

    def draw_forces(self, fX, fY, mZ):
        """ Dibuja las fuerzas actuantes sobre un nudo y sus valores correspondientes """
        if fX > 0:
            text(self.X, self.Y, "$\\rightarrow$", va='center', ha='right', fontsize=20, color='black')
            txt = "%.1f     \n" %fX
            text(self.X, self.Y, txt, va='bottom', ha='right', fontsize=10, color='red')
        elif fX < 0:
            text(self.X, self.Y, "$\\leftarrow$", va='center', ha='left', fontsize=20, color='black')
            txt = "\n    %.1f" %fX
            text(self.X, self.Y, txt, va='top', ha='left', fontsize=10, color='red')
        if fY > 0:
            text(self.X, self.Y, "$\\uparrow$", va='top', ha='center', fontsize=20, color='black')
            txt = "\n\n\n %.1f" %fY
            text(self.X, self.Y, txt, va='top', ha='center', fontsize=10, color='green')
        elif fY < 0:
            text(self.X, self.Y, "$\\downarrow$", va='bottom', ha='center', fontsize=20, color='black')
            txt = "%.1f \n\n" %fY
            text(self.X, self.Y, txt, va='bottom', ha='center', fontsize=10, color='green')
        if mZ > 0:
            text(self.X, self.Y, "$\\circlearrowleft$", va='center', ha='center', fontsize=20, color='black')
            txt = "\n\n %.1f" %mZ
            text(self.X, self.Y, txt, va='top', ha='right', fontsize=10, color='blue')
        elif mZ < 0:
            text(self.X, self.Y, "$\\circlearrowright$", va='center', ha='center', fontsize=20, color='black')
            txt = "  %.1f \n" %mZ
            text(self.X, self.Y, txt, va='bottom', ha='left', fontsize=10, color='blue')
