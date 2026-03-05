Examen 1º DAM Ice Skate
==================

Este examen ha sido realizado por Pablo González Temes alumno de 1º de DAM en el instituto IES Teis. El ejercicio consiste en realizar software que se pueda usar como marcador en una partida de Hockey sobre Hielo, un deporte dinámico que trata sobre dos equipos que deben marcar goles en la portería rival. En este deporte donde los jugadores o jugadoras pueden ser sancionados es importante tener en cuenta que jugadores en dicho estado tendrán sus goles anulados.

## Manual
### Requisitos

Los requisitos para el funcionamiento son
- [Python](https://www.python.org)
- [Git](https://git-scm.com/)
- [Uv](https://docs.astral.sh/uv/)

### Instalación

### Linux 

Para instalar los requisitos en Linux sigue los siguientes pasos:

Clona el repositorio de github (en caso de no tener [Git](https://git-scm.com/), debes instalarlo).

`git clone https://github.com/Pistacho14/Examen-DAM.git`

Instala Python:

`$ sudo apt install python3`

Instala uv:

`curl -LsSf https://astral.sh/uv/install.sh | less`

Instala las dependencias:

`uv sync --all-groups`

Inicia el entorno virtual:

`source venv/bin/activate`

### Windows

Para instalar los requisitos en Windows sigue los siguientes pasos:

Clona el repositorio de github (en caso de no tener [Git](https://git-scm.com/), debes instalarlo).

`git clone https://github.com/Pistacho14/Examen-DAM.git`

Para instalar Python puedes instalarlo desde la web de [<ins>*Python*</ins>](https://www.python.org/downloads/) y seguir los pasos de la instalación.

Instala uv:

`powershell -c "irm https://astral.sh/uv/install.ps1 | more"`

Instala las dependencias:

`uv sync --all-groups`

Instala el entorno virtual:

`.\.venv\Scripts\activate.ps1`


### Uso

Para utilizar este software el usuario debe introducir uno de estos dos comandos:

`uv run main.py`
