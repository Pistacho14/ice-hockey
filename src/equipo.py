class Equipo:
    def __init__(self, nombre, ciudad = None):

        self.nombre = nombre
        self.ciudad = ciudad
        self.jugadores = {}

    def añadir_jugador(self, jugador):

        self.jugadores[jugador.dorsal] = jugador

    def listar_jugadores(self):

        print(
            "================================"
            + "\n"
            + "ROSTER - "
            + self.nombre.upper()
            + "\n"
            + "================================"
            + "\n"
        )

        for jugador in self.jugadores.values():
            print(jugador)

        print("================================" + "\n")

    def obtener_jugador(self, dorsal):

        return self.jugadores.get(dorsal)
    
    def total_goles(self):
        goles = 0
        for jugador in self.jugadores.values():
            goles += jugador.get_goles()
        return goles

    def jugadores_activos(self):
        jugadores_en_juego = []
        
        for jugador in self.jugadores.values():
            if jugador.estado == "[ACTIVA]":
                jugadores_en_juego.append(jugador)
        
        return jugadores_en_juego
        