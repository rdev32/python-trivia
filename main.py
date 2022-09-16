import time
import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[39m'

preguntas_general = [
    ('¿Cuál es el animal nacional de Australia?\n', 
    '\tA)Demonio de Tanzania\n\tB)Canguro\n\tC)Kiwi\n\tD)No tiene\n'),
    ('¿Cuál es la flor nacional de Japón?\n',
    '\tA)Flor de Cerezo\n\tB)Wasabi\n\tC)Flor de Loto\n\tD)Girasol\n'),
    ('¿Cuántas franjas tiene la bandera de Estados Unidos?\n',
    '\tA)9\n\tB)50\n\tC)23\n\tD)13\n'),
    ('¿Cuántas zonas horarias tiene en Rusia?\n',
    '\tA)9\n\tB)10\n\tC)11\n\tD)12\n'),
    ('¿Cómo se llamaba Istanbul antes de 1923?\n',
    '\tA)Constantinopla\n\tB)Etiopia\n\tC)Imperio Otomano\n\tD)Roma\n')
]
soluciones_general = ['b', 'a', 'd', 'c', 'a']

preguntas_geografia = [
    ('¿Qué país tiene la mayor cantidad de islas en el mundo?\n', 
    '\tA)Suecia\n\tB)Noruega\n\tC)Filipinas\n\tD)Grecia\n'),
    ('¿Cuál es el país más pequeño del mundo?\n',
    '\tA)San Marino\n\tB)Liechtenstein\n\tC)El Vaticano\n\tD)Monaco\n'),
    ('¿Cuál es la capital de Canadá?\n',
    '\tA)Yukon\n\tB)Quebec\n\tC)Vermont\n\tD)Ottawa\n'),
    ('Nombra la cordillera más larga (no más alta) del mundo?\n',
    '\tA)Cordillera artica\n\tB)Los Alpes\n\tC)Los Andes\n\tD)Himalayas\n'),
    ('¿Cuál es el río más largo del mundo?\n',
    '\tA)Rio Nilo\n\tB)Rio Amazonas\n\tC)Rio Missisipi\n\tD)Rio Congo\n')
]
soluciones_geografia = ['a', 'c', 'd', 'c', 'b']

preguntas_deportes = [
    ('¿Dónde se celebraron los primeros Juegos Olímpicos modernos?\n', 
    '\tA)Atenas\n\tB)Paris\n\tC)San Luis\n\tD)Londres\n'),
    ('¿Qué equipo de fútbol se le conoce como "The Red Devils"?\n',
    '\tA)Atletico de Madrid\n\tB)A.C Milan\n\tC)Manchester United\n\tD)Liverpool\n'),
    ('¿¿Quién ha ganado más campeonatos de ajedrez?\n',
    '\tA)Garry Kasparov\n\tB)Jose Raul Capablanca\n\tC)Hikaru Nakamura\n\tD)Magnus Carlsen\n'),
    ('¿Qué conductor de la Formula 1 ha ganado más campeonatos?\n',
    '\tA)Lewis Hamilton\n\tB)Michael Schumacher\n\tC)Niki Lauda\n\tD)Max Verstappen\n')
]
soluciones_deportes = ['a', 'c', 'd', 'b']

puntaje = 0
nivel = 0

categorias = [
    (f'{BLUE}Conocimiento General{RESET}', preguntas_general, soluciones_general), 
    (f'{YELLOW}Geografia{RESET}', preguntas_geografia, soluciones_geografia), 
    (f'{CYAN}Deportes{RESET}', preguntas_deportes, soluciones_deportes)
]

categoria = random.choice(categorias)

print('\n\t¡Bienvenido/a al juego Trivia!')
print('La categoria de tu trivia sera sobre.. ', end='')
time.sleep(2)
print(categoria[0])
print(RED, '\nSi deseas rendirte, presiona la tecla Q.', RESET)
print(YELLOW, '\nEscribe la letra de la opcion que consideres correcta.', RESET)

while True:
    print(CYAN, f'\nTu puntaje es de: {puntaje} {"punto." if puntaje == 1 else "puntos."}', RESET)
    print(categoria[1][nivel][0], categoria[1][nivel][1])
    rpta = input('>> ').lower()
    if rpta == 'q':
        break
    elif rpta not in ('a', 'b', 'c', 'd'):
        print('Error: Debes seleccionar entre las alternativas A, B, C y D.\n')
        continue
    else :
        if nivel == len(categoria[2]) -1:
            break
        if categoria[2][nivel] == rpta:
            print(GREEN, 'Correcto! Ahora aqui va la siguiente pregunta', RESET)
            time.sleep(1)
            puntaje += 1
        elif categoria[2][nivel] != rpta:
            print(YELLOW, 'Esa no es la respuesta, intenta nuevamente', RESET)
        nivel = (nivel + 1) if nivel < (len(categoria[2]) -1) else nivel
    
    
if puntaje > len(categoria[2]) * 0.75:
    print(GREEN, 'La trivia a terminado! Tu puntaje fue de: ', puntaje, RESET)
    time.sleep(1)
    print('Muy bueno, tu si sabes.')
elif puntaje > len(categoria[2]) * 0.50:
    print(YELLOW, 'La trivia a terminado! Tu puntaje fue de: ', puntaje, RESET)
    time.sleep(1)
    print('Podrias hacerlo mejor.')
else :
    print(RED, 'La trivia a terminado! Tu puntaje fue de: ', puntaje, RESET)
    time.sleep(1)
    print('Bastante mal... deberias repasar.')

print('¡Gracias por jugar!')