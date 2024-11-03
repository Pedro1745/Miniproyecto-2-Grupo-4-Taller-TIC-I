from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from MascaraFinal import Ui_MainWindow
#from gpiozero import RGBLED, Button, Buzzer
import sys
import os
import random
#led_boton = RGBLED(red = 16,green = 19,blue = 13)
#led_slider = RGBLED(red = 21,green = 20,blue = 26)
class MascaraFinal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MascaraFinal, self).__init__(*args, **kwargs)
        self.setupUi(self)
        '''#leds
        self.encendido=0
        self.pushButton_2.clicked.connect(self.led_on)
        self.horizontalSlider.valueChanged.connect(self.led_lum)'''
        #imagenes
        self.nombres = ["Palkia", "Dialga", "Giratina", "Reshiram", "Zekrom", "Kyurem", "Tornadus", "Thundurus", "Landorus", "Enamorus"]
        base_dir = os.path.expanduser("~") + "/Desktop/MP2/ITEM2/fotosMP2/"
        self.imagenes = [
            base_dir + "Palkia.png", base_dir + "Dialga.png", base_dir + "Giratina.png", 
            base_dir + "Reshiram.png", base_dir + "Zekrom.png", base_dir + "Kyurem.png", 
            base_dir + "Tornadus.png", base_dir + "Thundurus.png", base_dir + "Landorus.png", 
            base_dir + "Enamorus.png"
        ]
        self.textos = ["Se trata de un gran Pokémon dragón creado por Arceus para la existencia del espacio. Según leyendas y mitología de Sinnoh y Hisui, este Pokémon es considerado una deidad. Tiene la habilidad de distorsionar el espacio, controlar las conexiones de este abriendo portales y así poder viajar entre dimensiones a su total antojo. Se dice que el espacio se vuelve más estable con cada respiración suya. En su creación, hizo que se cayera un gran muro que confinaba al mundo terrenal, dando paso a un cielo que se extiende al infinito. Si Palkia y Dialga se encuentran en una grieta del espacio-tiempo y usan sus poderes en un combate, se desatará un enorme cataclismo entre sus dimensiones que desencadenaría la destrucción del universo",
                        "Se trata de un gran Pokémon dragón creado por Arceus para la existencia del tiempo. Según la mitología local de Sinnoh y Hisui, después de que Arceus creara a Dialga, empezó a correr el tiempo en el mundo terrenal, como las aguas de un río caudaloso, y continúa avanzando con cada latido de su corazón. Se trata de un Pokémon hablado en antiguas leyendas y mitos, donde es considerado como una antigua deidad. Tiene la capacidad de controlar el transcurso del tiempo y de viajar libremente por el tiempo, al pasado y al futuro. Con el diamante que tiene en el pecho dispara su potente ataque distorsión, ataque que puede alterar el tiempo. Si Dialga y Palkia se encuentran en una grieta del espacio-tiempo y usan sus poderes en un combate, se desatará un enorme cataclismo entre sus dimensiones que desencadenaría la destrucción del universo",
                        "Las viejas leyendas dicen que Giratina vive en un universo paralelo, del que es guardián. Este sitio se trata del Mundo Distorsión, un lugar opuesto al mundo real, en donde las leyes desafían al sentido común y no hay distinción entre cielo y tierra. Este Pokémon legendario fue desterrado a este otro mundo por su comportamiento violento, aunque desde allí se dedica a observar el mundo real en silencio. En Hisui existe un dicho: 'Cuanto mayor sea la luz, mayor será la oscuridad que esta engendre'. Muchos creen que este dicho se refiere a este Pokémon", 
                        "Reshiram es capaz de generar llamas en el interior de su cola. La intensidad de estas llamas es tal que alteran la atmósfera, y el tiempo meteorológico cambia. Si algo se pone por delante de estas llamaradas será consumido por el fuego prácticamente al instante. Para desplazarse por el cielo lo hace de forma similar a un cohete a reacción, expulsando llamas por la cola con gran intensidad dejando una estela tras de sí. Según las leyendas, sus llamas reducirán a cenizas aquellos países cuyos habitantes desprecien la verdad y estén mancilladas por la codicia. Se cree que puede abrasar al mundo entero con sus llamas y reducirlo a cenizas. También aparece en los mitos de antaño ayudando a aquellas personas cuyas convicciones les llevan a perseguir un mundo veraz",
                        "Zekrom es capaz de generar electricidad haciendo girar el interior de su cola como si fuera una turbina, ya que se trata de un enorme generador. La intensidad de esta electricidad es tal que le permiten descargar rayos que destruyen todo a su alrededor, dejándolo todo completamente chamuscado. Para desplazarse por el cielo suele envolverse en nubes de rayos que ocultan su presencia, simulando ser una tormenta eléctrica, aunque de gran intensidad. Según las leyendas, la furia de sus rayos fulminará aquellos países cuyos habitantes hayan perdido el sentido de la justicia. También aparece en los mitos de antaño ayudando a aquellas personas cuyas convicciones les llevan a perseguir un mundo de ideales", 
                        "Este Pokémon legendario produce en su interior una intensa energía gélida que puede crear corrientes de aire tremendamente frías. En consecuencia, cualquier fuga de esta energía que tenga su cuerpo, hace que este termine congelándose. Es tan poderoso, que su poder supera al de Zekrom o Reshiram, pero este poder permanece sellado por el frío extremo que genera. La congelación de su cuerpo también le ayuda a estabilizar su estructura celular. Aguarda pacientemente en sitios congelados a aquel héroe que compense el vacío de su cuerpo con verdad e ideales.", 
                        "Su parte inferior está envuelta en una nube, y lo envuelve como un cuerpo de energía. Vuela por el cielo a una velocidad promedio de 300 km/h. La energía que fluye desde la cola de Tornadus despierta grandes tormentas, las cuales pueden llegar a crear hasta grandes ciclones. A Tornadus le gusta volar de un lugar a otro a medida que crea tempestades tan fuertes que pueden echar abajo las casas. Se dice que altera la atmósfera y propicia el cambio de estaciones. Algunos investigadores como el profesor Lavender sospechan que su forma antropomórfica no es la real. Desde tiempos inmemorables mantiene una fuerte rivalidad con Thundurus.", 
                        "Se dice que las tierras por las que Thundurus pasa quedan con incontables cicatrices y marcas provocadas por la caída de sus rayos, esto ayuda a enriquecer las tierras horadadas. La energía eléctrica que está cargada en las púas de la cola de Thundurus genera grandes lluvias, las cuales pueden despertar grandes tormentas cargadas de truenos. Es un Pokémon muy agresivo ya que lanza rayos sin más, provocando incendios forestales por diversión, esto le ha generado poca simpatía entre las personas. Sobrevuela la región de Teselia provocando rayos, camuflándose en su propia nube para que no sea distinguido por las personas. Desde tiempos inmemorables ha tenido una rivalidad contra Tornadus, su némesis, contra el que combate blandiendo rayos.", 
                        "Las tierras que Landorus visita generan grandes cosechas, por lo que se le considera el señor de la agricultura. Utiliza energía que obtiene del viento y del relámpago para enriquecer de nutrientes la tierra y generar abundantes cosechas. Esta energía la libera a través de su cola. Es el único capaz de parar a Thundurus y Tornadus cuando estos se pelean, así que se le podría considerar como el mediador de los dos, una vez apaciguados el trueno y las tormentas se auguran tierras fértiles y buenas cosechas.",
                        "A Enamorus se le conoce como el 'Heraldo de la Primavera', ya que su llegada desde el mar a la región de Hisui anuncia el fin del duro invierno. Al contrario que el resto de las Fuerzas de la naturaleza, Enamorus no es propenso a cometer fechorías ni bromas. Sin embargo, si alguien menosprecia el don de la vida, este Pokémon surge de entre las nubes rabioso y desata toda su furia para castigarlo. De acuerdo con el folclore, su amor siempre trae consigo un soplo de vida nueva a las regiones que visita"
                        ]
        self.timer = QtCore.QTimer(self)
        self.pushButton.clicked.connect(self.controlador_timer)
        self.timer.timeout.connect(self.mostrar_contenido)
        self.timer_is_running = False 
        self.mostrar_contenido()
    #leds
    '''def led_on(self):
        if self.encendido==0:
            led_boton.color = (1,1,1)
            self.encendido=1
        else:
            led_boton.color = (0,0,0)
            self.encendido=0
    def led_lum(self,valor):
        v = valor/100
        led_slider.color = (v,v,v)
        self.lcdNumber.display(v*100)'''
    #imagenes
    def mostrar_contenido(self):
        n = random.randint(0,9)
        imagen = self.imagenes[n]
        texto = self.textos[n]
        nombre = self.nombres[n]
        pixmap = QPixmap(imagen)
        if pixmap.isNull():
            print(f"Error al cargar la imagen: {imagen}")
        else:
            self.label_2.setPixmap(pixmap)
        self.label.setText(texto)
        self.label_7.setText(nombre)
    def controlador_timer(self):
        if self.timer_is_running:
            self.timer.stop()
            self.pushButton.setText("Iniciar Timer")
        else:
            self.timer.start(5000)
            self.pushButton.setText("Detener Timer")
        self.timer_is_running = not self.timer_is_running

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MascaraFinal()
    window.show()
    app.exec()
