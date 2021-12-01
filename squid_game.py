from ursina import *
from ursina.prefabs.first_person_controller \
  import FirstPersonController

#carga de menu
print("*************************************************************************************************")
print("************************* Programacion bajo plataformas abiertas ********************************")
print("******************************* Carlos Smith Ulloa - B36684 *************************************")
print("**********                                                                              *********")
print("**********        1 - Iniciar                                                           *********")
print("**********        2 - Invitar Amigos *                                                  *********")
print("**********        3 - Opciones       *                                                  *********")
print("**********        4 - Salir                                                             *********")
print("**********                                                                              *********")
print("*************************************************************************************************")
print("*************************************************************************************************")

#espera entrada de usuario
option = input("Option >> ")

#valida entrada
if option == '4':
  quit()
elif option != '1':
  print('Opción aun no implementada')
  quit()

#Entrada de Usuario
players1= input('Inserte el número de Jugadores :')
players = int(players1)
 
#Si la opcion es 1, inicia la aplicación.
app = Ursina()
window.fullscreen = False
window.color=color.black

player = FirstPersonController(
  speed=5,
  collider='box',
  jump_duration=0.3
)
player.cursor.visible=True

#Crear Plataforma de Inicio
ground = Entity(
  model='cube',
  collider='mesh',
  color=color.violet,
  scale=(10,0,10),
)

#Caida
Floor = Entity(
  texture='squid_game_vidrios2',
  collider='box',
  z=-3,y=-200,
  scale=(1920,1,1080),
)

#Crear Soportes
#El Tamaño del soporte es proporcional al número de vidrios
bracketsize =4*(players+1)
bracketposition = bracketsize/2

bracket1 = Entity(
  model='cube',
  color=color.pink,
  scale=(0.1,0.1,bracketsize),
  z=bracketposition+5,x=-0.6
)
bracket2 = duplicate(bracket1,
                  x=-3.5)
bracket3 = duplicate(bracket1,
                  x=0.6)
bracket4 = duplicate(bracket1,
                  x=3.6)
#Luz
PointLight(
  parent=camera,
  color=color.white,
  position=(10,10,-1.5)
)
AmbientLight(
  parent=camera,
  color=color.light_gray,
  texture="white_cube",
  collinder="box",
  scale=(100,1,100)
)
from random import randint
blocks = []
for i in range(players+1):
  block = Entity(
    model='cube',
    collider='box',
    color = color.white66,
    position=(2.05,0.1,6+i*4),
    scale=(3,0.1,2)
  )
  block2 = duplicate(block,
                     x=-2.05)
  blocks.append(
    (block,block2,randint(0,10)>7.5,
     randint(0,10)>7.5)
  )
Endground = Entity(
  color=color.violet,
  model='cube',
  scale=(12,0,12),
  position=(0,0,bracketsize+10)
)
pillar = Entity(
  color=color.brown,
  model='cube',
  z=58,
  scale=(1,15,1),y=8
)

#Entorno  
Sky(texture='squid_game_vidrios')

#Música Ambiente
music= Audio(
  'JuegoDelCalamar.mp3',
  loop= True,
  autoplay= True
  )

#yubication=player.position[2]
if player.position[2] <-1:
  Audio(
    'grito.mp3',
   loop= False,
   autoplay= False
  )
 


def update():
  for block1,block2,k,n in blocks:
    for x,y in [(block1,k),
                (block2,n)]:
      if x.intersects() and y:
        invoke(destroy,x,
               delay=0.1)
        x.fade_out(duration=0.1)

def input(key):
  if key =='q':
    quit()



app.run()