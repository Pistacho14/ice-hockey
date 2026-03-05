from src.equipo import Equipo
from src.jugadora import Jugadora
from src.posicion import Posicion

def test_total_goles():
    portugal = Equipo("Portugal")
    portugal.añadir_jugador(Jugadora(1, "Flavia", Posicion.CENTER))
    portugal.añadir_jugador(Jugadora(2, "Augusta", Posicion.GOALIE))
    goleadora = portugal.obtener_jugador(1)
    goleadora.registrar_gol()
    goleadora.registrar_gol()
    goleadora.registrar_gol()
    
    assert portugal.total_goles() == 3
    
    goleadora = portugal.obtener_jugador(2)
    goleadora.registrar_gol()
    goleadora.registrar_gol()
    
    assert portugal.total_goles() == 5
    