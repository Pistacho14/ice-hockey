from .posicion import Posicion
from. estado_jugador import EstadoJugador, JugadorActivo, JugadorSancionado


class Jugadora:
    def __init__(self, dorsal, nombre, posicion):

        self.dorsal = dorsal
        self.nombre = nombre
        self.posicion = Posicion(posicion)
        self.goles = 0
        self.asistencias = 0
        self.estado = JugadorActivo()
        
    def get_dorsal(self):
        return self.dorsal
    
    def get_nombre(self):
        return self.nombre
    
    def get_posicion(self):
        return self.posicion    
    
    def get_goles(self):
        return self.goles
    
    def get_asistencias(self):
        return self.asistencias
        
    def registrar_gol(self):
        
            self.estado.registrar_gol()
        
    def registrar_asistencia(self):
        self.estado.registrar_asisencia()
        
    def sancionar(self, minutos):
        self.estado = JugadorSancionado()

    def liberar(self):
        self.estado = JugadorActivo()

    def __repr__(self):
        return (
            "# "
            + str(self.dorsal)
            + "\t"
            + self.nombre
            + "\t\t\t"
            + self.posicion.value
            + "\t G: "
            + str(self.goles)
            + "   A: "
            + str(self.asistencias)
            + "  "
            + str(self.estado)
        )
