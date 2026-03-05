class EstadoJugador:
    def registrar_gol(self, jugadora):
        pass

    def registrar_asisencia(self, jugadora):
        pass

    def __str__(self):
        return self.__class__.__name__


class JugadorActivo(EstadoJugador):
    def registrar_gol(self, jugadora):
        jugadora.goles += 1

    def registrar_asisencia(self, jugadora):
        jugadora.asistencias += 1

    def __str__(self):
        return "[ACTIVA]"


class JugadorSancionado(EstadoJugador):
    def registrar_gol(self, jugadora):
        print(
            "[AVISO] "
            + jugadora.nombre
            + " está en la penalty box y no puede marcar goles."
        )

    def registrar_asisencia(self, jugadora):
        print(
            "[AVISO] "
            + jugadora.nombre
            + " está en la penalty box y no puede dar asistencias."
        )

    def __str__(self):
        return "[SANCIONADA]"
