from src.jugadora import Jugadora
from src.posicion import Posicion

def test_registrar_gol():
    delantero = Jugadora(11, "Fernando Torres", Posicion.GOALIE)
    
    for _ in range(10):
        delantero.registrar_gol()
    assert delantero.goles == 10
    
    
    
def test_registrar_asistencia():
    delantero = Jugadora(11, "Fernando Torres", Posicion.GOALIE)
    for _ in range(8):
        delantero.registrar_asistencia()
    assert delantero.asistencias == 8