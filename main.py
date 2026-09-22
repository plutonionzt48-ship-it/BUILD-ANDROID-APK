import os
import json
import shutil
import random

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle, Ellipse, Line, RoundedRectangle

from kivy.uix.screenmanager import (
    ScreenManager,
    Screen,
    FadeTransition,
    SlideTransition
)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image


try:
    from jnius import autoclass
except Exception:
    autoclass = None


# ============================================================
# CONFIGURACIÓN
# ============================================================

CONTRASENA = "27102024"

FONDO = (0.025, 0.008, 0.055, 1)
PANEL = (0.075, 0.018, 0.12, 0.96)

ROSA = (1.0, 0.08, 0.48, 1)
MAGENTA = (1.0, 0.0, 0.75, 1)
VIOLETA = (0.48, 0.08, 1.0, 1)
AZUL = (0.05, 0.45, 1.0, 1)
CIAN = (0.0, 0.95, 1.0, 1)
VERDE = (0.1, 1.0, 0.62, 1)
ORO = (1.0, 0.75, 0.08, 1)

ROSA_CLARO = (1.0, 0.65, 0.85, 1)
BLANCO = (1, 1, 1, 1)
GRIS = (0.72, 0.70, 0.78, 1)

Window.clearcolor = FONDO


def obtener_fuente():

    fuentes = [
        "/system/fonts/NotoSerif-Regular.ttf",
        "/system/fonts/NotoSerifDisplay-Regular.ttf",
        "/system/fonts/NotoSans-Regular.ttf",
        "/system/fonts/serif.ttf",
    ]

    for fuente in fuentes:

        if os.path.exists(fuente):
            return fuente

    return ""


FUENTE = obtener_fuente()


# ============================================================
# LAS 17 CARTAS
# ============================================================

CARTAS = [

    {
        "titulo": "Antes de nosotros",
        "texto": """Querida Marlys Julieth:

Antes de que existiéramos como “nosotros”, existíamos como dos personas que todavía no sabían lo que el otro iba a significar.

Tú tenías catorce años, y faltaban unos seis meses para que cumplieras quince. Yo todavía no sabía que aquella chica que había conocido en mi barrio terminaría ocupando un lugar tan importante en mi vida.

Recuerdo que, al principio, me parecías una chica tranquila. Había algo en ti que transmitía calma, aunque con el tiempo descubrí que detrás de esa tranquilidad había muchas cosas que cargabas sobre tus hombros, cosas que jamás habría imaginado para alguien tan joven.

Y quizá lo más curioso de todo es que tú te fijaste primero en mí.

Ninguno de los dos se atrevía a hablar demasiado. Mucho menos a reconocer lo que empezábamos a sentir. Era como si ambos supiéramos que había algo, pero ninguno quisiera ser el primero en ponerle nombre.

Ahora, mirando hacia atrás, me parece bonito pensar que nuestra historia comenzó precisamente así: sin prisas, sin saber qué hacer y sin imaginar hasta dónde nos llevaría.

Todavía no éramos novios.

Ni siquiera sabíamos si algún día lo seríamos.

Éramos simplemente dos personas que habían coincidido en el momento adecuado, aunque todavía no lo supiéramos.

Y si pudiera volver a aquel momento, no cambiaría nada.

Porque me gusta saber que, antes de que fueras mi novia, antes de que fueras mi persona favorita, simplemente fuiste aquella chica que apareció en mi vida sin avisar.

Y qué suerte tuve de encontrarte.

Con cariño,

De tu primer y gran amor:
Jesús Manuel"""
    },

    {
        "titulo": "La chica tranquila",
        "texto": """Para ti, que siempre has sido mucho más de lo que aparentabas.

Hay algo que todavía recuerdo de aquellos primeros momentos contigo.

Pensaba que eras una chica tranquila.

Y lo eras.

Pero no sabía todo lo que existía detrás de esa tranquilidad.

Con el tiempo fui descubriendo que habías tenido que cargar con cosas que, para alguien de tu edad, eran demasiado pesadas. Y creo que ahí empecé a mirarte de una manera diferente.

Porque una cosa es conocer a alguien.

Y otra muy distinta es empezar a conocer todo aquello que esa persona guarda cuando nadie está mirando.

Me gustaba tu tranquilidad, pero terminé admirando también tu fortaleza.

Admiré que, a pesar de todo lo que llevabas contigo, siguieras siendo tú. Que pudieras reír, querer, compartir y encontrar momentos bonitos incluso cuando tu vida no siempre había sido sencilla.

Quizá tú no te das cuenta de todas las cosas que he aprendido de ti.

Quizá tampoco sabes cuántas veces he pensado que eres mucho más fuerte de lo que tú misma crees.

Pero quiero que algún día, cuando leas esta carta otra vez, recuerdes algo:

Yo sí lo vi.

Vi a esa chica tranquila.

Pero también vi todo lo que había detrás de ella.

Y mientras más te conocía, más quería quedarme para descubrirlo.

Siempre tuyo,

Jesús Manuel"""
    },

    {
        "titulo": "Seis meses",
        "texto": """Hay distancias que terminan convirtiéndose en comienzos.

Después de conocernos, hubo un tiempo en el que dejamos de hablar.

Seis meses.

Dicho así parece poco.

Pero cuando pienso en nosotros, esos seis meses tienen un significado enorme, porque fueron la pausa que existió antes de que nuestra historia realmente comenzara.

Durante ese tiempo ninguno de los dos sabía qué iba a pasar.

Quizá incluso pensamos que aquello que había comenzado a surgir simplemente quedaría como una historia que nunca llegó a ser.

Pero la vida tiene formas extrañas de volver a juntar a las personas.

Y después de seis meses, volvimos a hablar.

El 27 de octubre.

En aquel momento probablemente ninguno de los dos imaginaba que algún día miraríamos esa fecha de una manera completamente diferente.

Para nosotros no sería solamente un día cualquiera.

Sería el día en que volvimos a encontrarnos.

El día que, sin saberlo, estábamos dando otra oportunidad a algo que todavía no habíamos terminado de entender.

A veces pienso que si hubiéramos hablado antes, quizá todo habría sido diferente.

Pero no quiero cambiarlo.

Porque esos seis meses también forman parte de nuestra historia.

Y quizá necesitábamos perdernos un poco para poder encontrarnos de verdad.

Con amor,

Jesús Manuel"""
    },

    {
        "titulo": "27 de octubre",
        "texto": """Para la fecha que terminó convirtiéndose en nosotros.

Si alguien me preguntara cuál fue el día en que empezó nuestra historia, probablemente podría decir muchas fechas.

Pero hay una que siempre tendría un lugar diferente.

27 de octubre.

Ese día volvimos a hablar después de seis meses.

Y aunque en ese momento no sabíamos lo que estábamos empezando, hoy puedo mirar atrás y entenderlo de otra manera.

A veces las historias importantes no comienzan con grandes declaraciones.

No hay música.

No hay una escena perfecta.

No hay una pregunta preparada.

A veces simplemente vuelves a hablar con alguien.

Y algo cambia.

Después de aquello empezamos a compartir nuestros primeros momentos juntos y ocurrió algo que todavía me cuesta explicar completamente.

Nos entendíamos.

Los dos sabíamos lo que el otro pensaba.

Los dos podíamos sentir lo que estaba pasando.

Era como si hubiera cosas que no necesitábamos decir porque ambos ya las conocíamos.

Y entonces, poco a poco, dejamos de ser simplemente dos personas que se gustaban.

Empezamos a ser nosotros.

Por eso el 27 de octubre significa tanto para mí.

No porque aquel día haya ocurrido algo espectacular.

Sino porque aquel día volviste a aparecer en mi vida.

Y esta vez, te quedaste.

Feliz cumpleaños, mi amor.

Jesús Manuel"""
    },

    {
        "titulo": "Tu mano",
        "texto": """Hay recuerdos que parecen pequeños hasta que uno se da cuenta de que los ha guardado durante mucho tiempo.

Este es uno de ellos.

La primera vez que me diste tu mano.

Puede parecer una cosa sencilla.

Una mano.

Un gesto.

Un instante.

Pero yo recuerdo lo bonito que se sintió.

Recuerdo mirarte y pensar que te veías linda, tranquila.

Y recuerdo algo más difícil de explicar.

Sentí que me estabas viendo de verdad.

Como si, de alguna manera, me reconocieras.

Como si en aquel momento hubiera algo entre nosotros que los dos entendíamos, incluso sin decirlo.

Yo todavía no sabía exactamente qué iba a pasar.

No sabía cuánto iba a quererte.

No sabía cuántos recuerdos íbamos a construir.

No sabía que algún día estaría escribiéndote diecisiete cartas para celebrar tus diecisiete años.

Solo sabía que tener tu mano junto a la mía se sentía bien.

Y quizá eso era suficiente.

Hoy, después de todo lo que ha pasado desde entonces, sigo pensando en aquel momento con cariño.

Porque algunas historias no empiezan con un “te quiero”.

Algunas empiezan simplemente con dos manos encontrándose.

Y la tuya fue la primera que quise sostener.

Jesús Manuel"""
    },

    {
        "titulo": "La ventana",
        "texto": """Hay primeros besos que parecen sacados de una película.

Y después está el nuestro.

El nuestro fue mucho más nosotros.

Fue en la ventana de la casa de mis abuelos.

Se suponía que debía ser yo quien te diera aquel primer beso.

Al menos, eso era lo que tenía en mente.

Pero parece que tú tenías otros planes.

Porque antes de que yo pudiera hacerlo, lo hiciste tú.

Un pico.

Rápido.

Sencillo.

Pero suficiente para que aquel momento se quedara guardado en mi memoria.

Y ahora que lo pienso, hasta me causa gracia.

Porque incluso en nuestro primer beso ya estabas demostrando esa forma tan tuya de hacer las cosas.

Yo creyendo que tenía que dar el primer paso...

Y tú simplemente te adelantaste.

Quizá debería haberme sorprendido.

Pero, sinceramente, me gusta que haya ocurrido así.

Porque si nuestro primer beso hubiera salido exactamente como yo lo había imaginado, probablemente no tendría la misma historia detrás.

Y nuestro primer beso no necesitaba ser perfecto.

Necesitaba ser nuestro.

Una ventana.

La casa de mis abuelos.

Un pequeño beso.

Y dos personas que todavía estaban descubriendo todo lo que iban a llegar a sentir.

Puede parecer un recuerdo pequeño.

Pero cuando pienso en aquella escena ahora, después de todo lo que hemos vivido, sonrío.

Porque ese pequeño pico fue uno de los primeros momentos en los que nuestra historia dejó de ser solamente miradas, conversaciones y sentimientos que ninguno se atrevía a nombrar.

Fue un pequeño paso más hacia nosotros.

Y aunque se suponía que debía hacerlo yo...

Gracias por haberte adelantado.

Creo que no podría haber imaginado un primer beso más nuestro.

Jesús Manuel"""
    },

    {
        "titulo": "La primera carta",
        "texto": """Hay primeras veces que uno recuerda por lo que ocurrió.

Y hay otras que recuerda por la persona con quien ocurrieron.

Tú fuiste mi primera carta.

Pero no solamente porque fuiste la primera persona que me escribió una.

También porque fuiste la primera persona a la que yo quise escribirle una.

Y eso, aunque pueda parecer algo pequeño, para mí significa mucho.

Porque antes de ti nunca había tenido una razón para sentarme frente a una hoja y tratar de convertir lo que sentía en palabras.

Llegaste tú.

Y de repente quise intentarlo.

Tú fuiste quien dio el primer paso.

Me escribiste antes.

Y quizá sin saberlo, hiciste que yo descubriera una manera diferente de decir lo que sentía.

Una carta no es como un mensaje cualquiera.

Cuando escribes una carta, tienes que detenerte.

Pensar.

Elegir las palabras.

Dejar un pedazo de ti en cada línea.

Y tú fuiste la primera persona por la que quise hacer eso.

Ahora me parece curioso pensar en aquella primera carta mientras estoy escribiendo estas diecisiete.

Porque aquella primera vez no sabía que algún día estaría aquí, escribiéndote una carta tras otra para celebrar tus diecisiete años.

No sabía que aquella primera hoja iba a terminar convirtiéndose en algo tan grande.

Pero quizá ahí comenzó otra parte de nuestra historia.

Primero fue tu carta.

Después fue la mía.

Y hoy son diecisiete.

Qué bonito pensar que, de alguna manera, todo esto comenzó con dos personas intentando decirse lo que sentían sin saber muy bien cómo hacerlo.

Y entre todas las personas del mundo, tú fuiste la primera.

La primera que me escribió.

La primera a la que le escribí.

Y probablemente por eso aquella primera carta siempre tendrá un lugar diferente.

Porque fue la primera vez que intenté poner en palabras algo que, contigo, cada vez se hacía más difícil esconder.

Lo que sentía por ti.

Jesús Manuel"""
    },

    {
        "titulo": "Sin preguntarlo",
        "texto": """Hay una parte de nuestra historia que siempre me ha parecido curiosa.

Nunca hubo realmente un momento perfecto en el que me arrodillara frente a ti, respirara profundo y dijera:

“¿Quieres ser mi novia?”

No pasó así.

Simplemente ocurrió.

Lo que sentíamos era tan mutuo que, de alguna manera, empezamos a ser pareja antes de ponerle oficialmente ese nombre.

Nos entendíamos.

Nos buscábamos.

Compartíamos momentos.

Y los dos sabíamos lo que había entre nosotros.

Tiempo después tú me lo recordaste.

Me dijiste que, en realidad, nunca te lo había pedido.

Y tenías razón.

Así que tuve que hacerlo.

Pero incluso entonces pensé que era curioso, porque para mí nuestra historia ya había empezado mucho antes de esa pregunta.

La pregunta solo puso palabras a algo que nosotros ya habíamos construido.

Y quizá eso es una de las cosas que más me gustan de nuestra historia.

Que no necesitó ser perfecta.

No siguió un guion.

Simplemente fue nuestra.

Dos personas que se encontraron, se alejaron, volvieron a encontrarse y terminaron eligiéndose.

Y si alguna vez me preguntaran cuál fue el momento exacto en que decidí que quería estar contigo, probablemente no sabría responder.

Porque no fue un momento.

Fueron muchos.

Y todavía siguen siendo muchos.

Te elegiría otra vez.

Jesús Manuel"""
    },

    {
        "titulo": "La primera vez que entendí",
        "texto": """Hay momentos en una relación que no tienen una fecha exacta.

No sabes cuándo ocurrieron exactamente, pero algún día miras hacia atrás y comprendes que algo cambió.

Creo que contigo me pasó eso.

No sé cuál fue el instante exacto en el que dejaste de ser simplemente una persona importante y empezaste a convertirte en alguien que realmente quería tener en mi vida.

No hubo una señal.

No hubo una canción de fondo ni una escena perfecta.

Simplemente ocurrió mientras te conocía.

Fue en las conversaciones, en los momentos que compartíamos, en la forma en que poco a poco empecé a acostumbrarme a tu presencia.

Hasta que llegó un punto en el que ya no imaginaba mis días exactamente igual sin ti.

Y creo que ahí empecé a entenderlo.

Me estaba enamorando de ti.

No solamente de tu forma de ser cuando todo estaba bien.

También de tus rarezas, de tu manera de pensar, de esa personalidad que nunca ha sido completamente fácil de explicar.

Me enamoré de la persona que eras cuando nadie te estaba pidiendo que fueras de determinada manera.

Y quizá eso sea lo más bonito.

Que no tuve que encontrar una versión perfecta de ti para quererte.

Me bastó con conocerte.

Y cuanto más te conocía, más razones encontraba para quedarme.

Jesús Manuel"""
    },

    {
        "titulo": "Los pequeños momentos",
        "texto": """Cuando uno piensa en una historia de amor, suele imaginar los grandes momentos.

El primer beso.

El primer “te amo”.

Una fecha importante.

Una fotografía que termina guardándose durante años.

Pero cuando pienso en nosotros, también pienso en todo aquello que parecía pequeño.

Las conversaciones que probablemente ninguno de los dos consideraría importantes si las viéramos por separado.

Las veces que simplemente estuvimos juntos.

Las palabras que dijimos sin pensar demasiado.

Las risas.

Los silencios.

Las cosas que solamente nosotros entendíamos.

Porque al final una relación no se construye únicamente con grandes acontecimientos.

Se construye con cientos de momentos pequeños que, juntos, terminan convirtiéndose en una historia enorme.

Y eso es algo que me gusta de nosotros.

Que no necesito recordar solamente un día extraordinario para saber lo mucho que significas para mí.

Tengo muchos pequeños recuerdos.

Y cada uno guarda una parte de lo que hemos sido.

Quizá algún día olvidemos exactamente qué dijimos en una conversación cualquiera.

Quizá olvidemos algunos detalles.

Pero espero que nunca olvidemos cómo nos hacíamos sentir.

Porque ahí está una parte de nuestra historia que ningún calendario puede guardar.

Y si algún día vuelvo a mirar hacia atrás, quiero recordar precisamente eso:

que fuimos felices en muchos momentos que, en aquel instante, parecían simplemente momentos normales.

Jesús Manuel"""
    },

    {
        "titulo": "Lo que descubrí de ti",
        "texto": """Al principio pensé que podía conocerte.

Después entendí que conocer a una persona nunca es tan sencillo.

Cada vez que creía haber descubierto una parte de ti, aparecía otra.

Descubrí tu forma de querer.

Tu manera de reaccionar.

Tu forma de reír.

Tus pensamientos.

Tus rarezas.

Esa locura tan tuya que, con el tiempo, terminó siendo una de las cosas que más me gustan de ti.

Y también descubrí algo que ya había comenzado a ver desde el principio:

que eres mucho más de lo que aparentas.

Hay una parte de ti que quizá no siempre ves.

Una parte fuerte.

Una parte sensible.

Una parte que ha tenido que aprender a seguir adelante incluso cuando las cosas no han sido fáciles.

Y mientras más te conocía, más entendía que no quería quedarme únicamente con la versión superficial de ti.

Quería conocerte completa.

Con tus días buenos y tus días malos.

Con tus momentos de tranquilidad y tus momentos de locura.

Con tus virtudes y tus defectos.

Porque quererte nunca ha significado pensar que eres perfecta.

Ha significado conocerte y, aun así, seguir encontrando razones para admirarte.

Y después de todo este tiempo, todavía hay cosas de ti que sigo descubriendo.

Creo que esa es una de las razones por las que nunca me aburriría de conocerte.

Porque eres tú.

Y tú nunca has sido una persona que pueda explicarse en unas pocas palabras.

Jesús Manuel"""
    },

    {
        "titulo": "Nosotros",
        "texto": """Hubo un momento en el que dejamos de ser simplemente tú y yo.

No sé exactamente cuándo ocurrió.

Quizá fue poco a poco.

Quizá comenzó aquel 27 de octubre.

Quizá comenzó con aquella mano.

Quizá comenzó incluso antes.

Pero en algún punto apareció una palabra que empezó a tener sentido:

“nosotros”.

Y esa palabra terminó significando muchísimo.

Porque “nosotros” no significa solamente estar juntos.

Significa compartir.

Significa tener recuerdos que solamente nosotros conocemos.

Significa saber cosas del otro que nadie más sabe.

Significa aprender a entenderse.

Significa poder mirar hacia atrás y reconocer un camino que recorrimos juntos.

Me gusta pensar que nuestro “nosotros” no nació de un momento perfecto.

Nació de muchos momentos imperfectos.

De dos personas que no sabían exactamente qué estaban haciendo.

De dos personas que se encontraron, se alejaron, volvieron a encontrarse y terminaron eligiéndose.

Y quizá por eso tiene tanto valor.

Porque no fue algo que simplemente apareció.

Lo fuimos construyendo.

Día después de día.

Momento después de momento.

Y si tuviera que explicar qué significa para mí la palabra “nosotros”, probablemente no buscaría una definición.

Simplemente pensaría en ti.

Porque cuando pienso en nosotros, pienso en todo lo que hemos llegado a ser.

Y me gusta.

Me gusta muchísimo.

Jesús Manuel"""
    },

    {
        "titulo": "Cuando no todo fue fácil",
        "texto": """No quiero que estas cartas cuenten una historia perfecta.

Porque la nuestra nunca necesitó ser perfecta para ser importante.

Hemos tenido momentos bonitos.

Pero también hemos tenido momentos complicados.

Momentos en los que quizá fue más difícil entendernos.

Momentos en los que las emociones pesaron más que las palabras.

Y creo que eso también forma parte de amar a alguien.

Porque querer a una persona cuando todo está bien es sencillo.

Lo verdaderamente importante aparece cuando las cosas dejan de ser tan sencillas.

Ahí es donde uno descubre cuánto está dispuesto a comprender.

A escuchar.

A tener paciencia.

A quedarse.

No quiero recordar las dificultades para quedarme en ellas.

Quiero recordarlas porque, a pesar de ellas, seguimos teniendo una historia que contar.

Y quizá eso sea una de las cosas que más valoro.

Que nuestra relación no está hecha solamente de momentos bonitos.

También está hecha de aprendizaje.

De crecer.

De equivocarnos.

De entendernos nuevamente.

De descubrir que amar a alguien también significa aprender cómo acompañarlo.

No sé qué nos traerá la vida.

Pero sí sé algo:

todo lo que hemos vivido, incluso aquello que no fue fácil, forma parte de nosotros.

Y no cambiaría nuestra historia por una historia perfecta.

Prefiero la nuestra.

Jesús Manuel"""
    },

    {
        "titulo": "Tu resiliencia",
        "texto": """Hay algo de ti que siempre he admirado.

Tu capacidad de seguir.

Has tenido que enfrentarte a cosas que no siempre fueron sencillas.

Y aun así, sigues siendo tú.

Sigues riendo.

Sigues queriendo.

Sigues teniendo esa manera tan particular de hacer las cosas.

Y quizá no siempre te das cuenta de lo fuerte que eres.

Tal vez porque cuando uno vive sus propias dificultades, deja de notar la fuerza que necesita para atravesarlas.

Pero yo la he visto.

La vi cuando apenas comenzaba a conocerte.

Y con el tiempo la he entendido mucho más.

Tu resiliencia no significa que nunca te duela nada.

Significa que, incluso cuando algo duele, encuentras una manera de seguir adelante.

Y eso es algo que admiro profundamente.

No quiero que pienses que tienes que ser fuerte todo el tiempo.

No tienes que demostrarle nada a nadie.

También tienes derecho a cansarte.

A llorar.

A sentir.

A necesitar que alguien te acompañe.

Y si algún día necesitas recordar que eres capaz de seguir adelante, quiero que recuerdes que hay alguien que lo ha visto en ti desde hace mucho tiempo.

Yo.

La chica tranquila de aquella primera carta terminó enseñándome que detrás de la tranquilidad podía existir una fuerza enorme.

Y esa chica eres tú.

Jesús Manuel"""
    },

    {
        "titulo": "Nuestra locura",
        "texto": """Si todas nuestras cartas fueran serias, probablemente no estaríamos contando nuestra verdadera historia.

Porque también existe esa parte de nosotros que no tiene demasiado sentido.

Nuestra locura.

Las cosas que hacemos.

Las conversaciones que probablemente nadie más entendería.

Las risas por cualquier tontería.

Los momentos en los que simplemente somos nosotros sin preocuparnos demasiado por cómo nos vemos desde afuera.

Y, sinceramente, me encanta.

Me encanta que contigo pueda existir esa versión de mí.

La que se ríe por cualquier cosa.

La que puede hablar de algo completamente absurdo.

La que no necesita estar buscando constantemente el momento perfecto.

Porque contigo aprendí que una relación también está hecha de eso.

De poder ser uno mismo.

De sentirse cómodo.

De poder hacer el ridículo y aun así saber que la otra persona se queda.

Tú tienes una forma muy particular de ser.

Una mezcla de tranquilidad y locura.

De ternura y carácter.

De cosas que a veces ni siquiera sé cómo explicar.

Y creo que precisamente por eso eres tú.

No quiero una versión diferente.

No quiero que pierdas esa forma tan única de existir.

Porque si tuviera que elegir una sola cosa para cambiar de nuestra historia, probablemente no cambiaría esa parte.

Quiero seguir teniendo recuerdos que, cuando los recordemos dentro de muchos años, nos hagan mirarnos y pensar:

“¿Cómo se nos ocurrió hacer eso?”

Y después reírnos.

Porque también eso somos.

Nosotros.

Jesús Manuel"""
    },

    {
        "titulo": "Todo lo que hemos vivido",
        "texto": """Si pudiera colocar nuestra historia delante de mí como fotografías, probablemente necesitaría muchísimo espacio.

Estaría aquella primera vez que te conocí.

Estaría la chica tranquila que todavía no sabía todo lo que iba a significar para mí.

Estarían los seis meses.

Estaría el 27 de octubre.

Estaría tu mano junto a la mía.

Estaría aquel momento en el que descubrimos que ya éramos algo, incluso antes de preguntarlo.

Y después vendrían todos los demás recuerdos.

Los que todavía puedo recordar perfectamente.

Los que quizá algún día se vuelvan borrosos.

Los que solamente nosotros conocemos.

Y al mirar todo eso junto, hay algo que me sorprende.

Cuánto puede cambiar una vida cuando aparece una persona.

Porque aquel día en que te conocí no tenía forma de saber que terminaría escribiendo diecisiete cartas para celebrar tus diecisiete años.

No podía saberlo.

Tú tampoco.

Y quizá esa sea precisamente la magia.

No sabíamos el final.

Simplemente empezamos.

Y seguimos.

Hasta llegar aquí.

Hoy puedo mirar hacia atrás y entender que cada pequeño momento tenía un lugar dentro de la historia.

Incluso aquellos que parecían insignificantes.

Todo nos trajo hasta este punto.

Hasta estas cartas.

Hasta tus diecisiete años.

Hasta nosotros.

Y si tuviera que resumir todo lo que hemos vivido en una sola frase, sería esta:

Qué bonito que aquella coincidencia terminara convirtiéndose en nuestra historia.

Jesús Manuel"""
    },

    {
        "titulo": "17",
        "texto": """Hoy cumples 17.

Y mientras escribo esta última carta, no puedo evitar pensar en la primera.

Una chica de 14 años.

Un chico que todavía no sabía lo que estaba a punto de ocurrir.

Dos personas que coincidieron sin saber que algún día esa coincidencia tendría un significado enorme.

Después vinieron los seis meses.

El 27 de octubre.

Tu mano.

La ventana.

Tu primer paso en aquel primer beso.

Tu primera carta.

Mi primera carta para ti.

El momento en que empezamos a ser nosotros.

Y después, todo lo demás.

No sé si alguna vez podremos recordar absolutamente cada detalle.

Probablemente no.

El tiempo va a borrar algunas fechas.

Algunos mensajes desaparecerán.

Algunas conversaciones quedarán solamente en nuestra memoria.

Pero espero que haya algo que nunca se borre:

la sensación de haber vivido todo esto juntos.

Hoy quiero celebrar tus 17 años.

Pero también quiero celebrar a la persona que eres.

Tu resiliencia.

Tu forma de querer.

Tu locura.

Tu manera única de ser.

Esa combinación que hace que seas simplemente tú.

No quiero decirte que sé exactamente qué ocurrirá en el futuro.

Nadie puede saberlo.

Pero sí puedo decirte algo sobre el presente.

Hoy estoy aquí.

Hoy te miro y sigo pensando que tuve muchísima suerte aquel día en que apareciste en mi vida.

Y entre todas las cosas que podrían haber sucedido, sucedió algo que todavía me parece increíble:

te encontré.

Así que estas 17 cartas no son solamente 17 textos.

Son 17 pequeñas partes de una historia.

Una historia que comenzó antes de que nosotros supiéramos que existía.

Y si algún día vuelves a leerlas cuando tengas 18, 20, 30 o muchos más años, quiero que recuerdes a aquella chica de 14 años que todavía no sabía lo que iba a vivir.

Y quiero que recuerdes que alguien la conoció.

La miró.

La admiró.

Se enamoró de ella.

Y tuvo la suerte de llamarla:

mi amor.

Feliz cumpleaños número 17, Marlys Julieth.

Gracias por haber aparecido en mi vida.

Gracias por cada recuerdo.

Gracias por ser tú.

Y gracias por convertir un simple “tú y yo” en algo que para mí siempre significará mucho más:

nosotros.

Con todo mi amor,

Jesús Manuel"""
    }
]


# ============================================================
# DATOS
# ============================================================

class Datos:

    def __init__(self, app):

        self.app = app

        self.ruta = os.path.join(
            app.user_data_dir,
            "recuerdos.json"
        )

        self.data = {
            "canciones": [],
            "fotos": [],
            "momentos": []
        }

        self.cargar()

    def cargar(self):

        try:

            if os.path.exists(self.ruta):

                with open(
                    self.ruta,
                    "r",
                    encoding="utf-8"
                ) as archivo:

                    datos = json.load(archivo)

                    if isinstance(datos, dict):

                        self.data["canciones"] = datos.get(
                            "canciones",
                            []
                        )

                        self.data["fotos"] = datos.get(
                            "fotos",
                            []
                        )

                        self.data["momentos"] = datos.get(
                            "momentos",
                            []
                        )

        except Exception:

            pass

    def guardar(self):

        try:

            with open(
                self.ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    self.data,
                    archivo,
                    ensure_ascii=False,
                    indent=2
                )

        except Exception:

            pass


# ============================================================
# FONDO ROMÁNTICO ANIMADO
# ============================================================

class FondoRomantico(FloatLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        with self.canvas.before:

            Color(*FONDO)

            self.rect = Rectangle(
                pos=self.pos,
                size=self.size
            )

            Color(
                0.35,
                0.02,
                0.50,
                0.10
            )

            self.glow1 = Ellipse(
                size=(
                    dp(300),
                    dp(300)
                )
            )

            Color(
                1,
                0.02,
                0.45,
                0.06
            )

            self.glow2 = Ellipse(
                size=(
                    dp(250),
                    dp(250)
                )
            )

        self.bind(
            pos=self.actualizar_fondo,
            size=self.actualizar_fondo
        )

        self.particulas = []

        for _ in range(60):

            with self.canvas:

                Color(
                    random.choice([
                        1,
                        0.8,
                        0.5,
                        0.2,
                        0.05
                    ]),
                    random.choice([
                        0.05,
                        0.2,
                        0.7,
                        0.95
                    ]),
                    1,
                    random.uniform(
                        0.25,
                        0.85
                    )
                )

                punto = Ellipse(
                    size=(
                        dp(random.uniform(1, 3)),
                        dp(random.uniform(1, 3))
                    )
                )

            self.particulas.append({
                "obj": punto,
                "x": random.random(),
                "y": random.random(),
                "vel": random.uniform(
                    0.0005,
                    0.002
                )
            })

        self.corazones = []

        for _ in range(12):

            corazon = Label(
                text=random.choice([
                    "♥",
                    "✦",
                    "★",
                    "•"
                ]),
                font_size=dp(
                    random.randint(11, 23)
                ),
                color=(
                    1,
                    random.uniform(
                        0.1,
                        0.7
                    ),
                    random.uniform(
                        0.45,
                        0.9
                    ),
                    random.uniform(
                        0.15,
                        0.55
                    )
                ),
                size_hint=(None, None),
                size=(
                    dp(35),
                    dp(35)
                )
            )

            corazon.x = random.uniform(
                0,
                max(1, Window.width)
            )

            corazon.y = random.uniform(
                0,
                max(1, Window.height)
            )

            self.add_widget(corazon)

            self.corazones.append({
                "obj": corazon,
                "vel": random.uniform(
                    0.3,
                    1.0
                )
            })

        Clock.schedule_interval(
            self.animar,
            1 / 30
        )

    def actualizar_fondo(self, *args):

        self.rect.pos = self.pos
        self.rect.size = self.size

        self.glow1.pos = (
            self.width * 0.60,
            self.height * 0.60
        )

        self.glow2.pos = (
            self.width * 0.02,
            self.height * 0.20
        )

    def animar(self, dt):

        w = max(
            self.width,
            1
        )

        h = max(
            self.height,
            1
        )

        for particula in self.particulas:

            x = particula["x"]
            y = particula["y"]

            y += particula["vel"]

            if y > 1:
                y = 0

            particula["y"] = y

            particula["obj"].pos = (
                x * w,
                y * h
            )

        for corazon in self.corazones:

            obj = corazon["obj"]

            obj.y += corazon["vel"]

            if obj.y > h + dp(30):

                obj.y = -dp(30)


# ============================================================
# BOTÓN
# ============================================================

class BotonRomantico(Button):

    def __init__(
        self,
        color_borde=ROSA,
        **kwargs
    ):

        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""

        self.background_color = (
            0,
            0,
            0,
            0
        )

        self.color = BLANCO
        self.font_size = dp(15)
        self.bold = True

        self.size_hint_y = None
        self.height = dp(58)

        if FUENTE:

            self.font_name = FUENTE

        with self.canvas.before:

            Color(
                PANEL[0],
                PANEL[1],
                PANEL[2],
                0.96
            )

            self.fondo = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[
                    dp(18)
                ]
            )

            Color(*color_borde)

            self.borde = Line(
                rounded_rectangle=(
                    self.x,
                    self.y,
                    self.width,
                    self.height,
                    dp(18)
                ),
                width=1.3
            )

        self.bind(
            pos=self.actualizar,
            size=self.actualizar
        )

        self.bind(
            state=self.estado
        )

    def actualizar(self, *args):

        self.fondo.pos = self.pos
        self.fondo.size = self.size

        self.borde.rounded_rectangle = (
            self.x,
            self.y,
            self.width,
            self.height,
            dp(18)
        )

    def estado(self, *args):

        if self.state == "down":

            self.fondo.pos = (
                self.x + dp(2),
                self.y + dp(2)
            )

            self.fondo.size = (
                self.width - dp(4),
                self.height - dp(4)
            )

        else:

            self.actualizar()


# ============================================================
# ETIQUETA
# ============================================================

def etiqueta(
    texto,
    tam=18,
    color=BLANCO,
    negrita=False
):

    lbl = Label(
        text=texto,
        color=color,
        font_size=dp(tam),
        bold=negrita,
        halign="center",
        valign="middle"
    )

    if FUENTE:

        lbl.font_name = FUENTE

    lbl.bind(
        size=lambda obj, value:
        setattr(
            obj,
            "text_size",
            (
                obj.width,
                None
            )
        )
    )

    return lbl


# ============================================================
# TEXTO DE LAS CARTAS
# ============================================================

class TextoCarta(Label):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.color = BLANCO
        self.font_size = dp(18)

        self.halign = "left"
        self.valign = "top"

        self.padding = (
            dp(16),
            dp(18)
        )

        self.size_hint_y = None

        if FUENTE:

            self.font_name = FUENTE

        self.bind(
            width=self.actualizar_texto
        )

        self.bind(
            texture_size=self.actualizar_altura
        )

    def actualizar_texto(self, *args):

        self.text_size = (
            max(
                dp(10),
                self.width - dp(32)
            ),
            None
        )

    def actualizar_altura(self, *args):

        self.height = (
            self.texture_size[1]
            + dp(36)
        )


# ============================================================
# PANTALLA BASE
# ============================================================

class PantallaBase(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.fondo = FondoRomantico()

        self.add_widget(
            self.fondo
        )


# ============================================================
# INICIO
# ============================================================

class InicioScreen(PantallaBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        caja = BoxLayout(
            orientation="vertical",
            padding=(
                dp(28),
                dp(60)
            ),
            spacing=dp(15)
        )

        caja.add_widget(
            Label(
                text="17",
                font_size=dp(82),
                color=ORO,
                bold=True,
                size_hint_y=None,
                height=dp(105)
            )
        )

        caja.add_widget(
            etiqueta(
                "CARTAS PARA TI",
                30,
                ROSA_CLARO,
                True
            )
        )

        caja.add_widget(
            etiqueta(
                "Marlys Julieth",
                25,
                BLANCO,
                True
            )
        )

        caja.add_widget(
            etiqueta(
                "Una historia escrita con amor",
                15,
                GRIS
            )
        )

        caja.add_widget(
            Label()
        )

        caja.add_widget(
            etiqueta(
                "27 • 10 • 2024",
                19,
                ROSA_CLARO,
                True
            )
        )

        entrar = BotonRomantico(
            ROSA
        )

        entrar.text = (
            "ABRIR NUESTRA HISTORIA"
        )

        entrar.bind(
            on_release=self.pedir_contrasena
        )

        caja.add_widget(
            entrar
        )

        self.add_widget(caja)

    def pedir_contrasena(self, *args):

        caja = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            padding=dp(18)
        )

        caja.add_widget(
            etiqueta(
                "Esta historia es solo para ti ♥",
                18,
                ROSA_CLARO,
                True
            )
        )

        campo = TextInput(
            hint_text="Contraseña",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=dp(52),
            font_size=dp(18),
            halign="center",
            background_color=(
                0.12,
                0.03,
                0.18,
                1
            ),
            foreground_color=BLANCO,
            cursor_color=ROSA
        )

        caja.add_widget(campo)

        botones = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(8)
        )

        cancelar = BotonRomantico(
            VIOLETA
        )

        cancelar.text = "CERRAR"

        entrar = BotonRomantico(
            ROSA
        )

        entrar.text = "ENTRAR"

        botones.add_widget(
            cancelar
        )

        botones.add_widget(
            entrar
        )

        caja.add_widget(
            botones
        )

        popup = Popup(
            title="♥",
            content=caja,
            size_hint=(
                0.9,
                None
            ),
            height=dp(260),
            separator_color=ROSA
        )

        cancelar.bind(
            on_release=popup.dismiss
        )

        def verificar(*_):

            if campo.text == CONTRASENA:

                popup.dismiss()

                self.manager.transition = FadeTransition(
                    duration=0.3
                )

                self.manager.current = "cartas"

            else:

                campo.text = ""

                campo.hint_text = (
                    "Contraseña incorrecta"
                )

        entrar.bind(
            on_release=verificar
        )

        campo.bind(
            on_text_validate=verificar
        )

        popup.open()


# ============================================================
# LISTA DE CARTAS
# ============================================================

class CartasScreen(PantallaBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        caja = BoxLayout(
            orientation="vertical",
            padding=(
                dp(15),
                dp(25)
            ),
            spacing=dp(10)
        )

        caja.add_widget(
            etiqueta(
                "♥ 17 CARTAS PARA TI ♥",
                24,
                ROSA_CLARO,
                True
            )
        )

        caja.add_widget(
            etiqueta(
                "Marlys Julieth • 17 años",
                15,
                GRIS
            )
        )

        scroll = ScrollView(
            do_scroll_x=False,
            bar_width=dp(3)
        )

        lista = GridLayout(
            cols=1,
            spacing=dp(10),
            padding=dp(5),
            size_hint_y=None
        )

        lista.bind(
            minimum_height=lista.setter(
                "height"
            )
        )

        colores = [
            ROSA,
            MAGENTA,
            VIOLETA,
            AZUL,
            CIAN,
            VERDE,
            ORO,
            ROSA,
            MAGENTA,
            VIOLETA,
            AZUL,
            CIAN,
            VERDE,
            ORO,
            ROSA,
            MAGENTA,
            VIOLETA
        ]

        for i, carta in enumerate(CARTAS):

            boton = BotonRomantico(
                colores[i]
            )

            boton.text = (
                f"{i + 1:02d}   ♥   "
                f"{carta['titulo']}"
            )

            boton.font_size = dp(14)

            boton.bind(
                on_release=lambda btn, indice=i:
                self.abrir_carta(indice)
            )

            lista.add_widget(
                boton
            )

        recuerdos = BotonRomantico(
            ORO
        )

        recuerdos.text = (
            "✦ NUESTROS RECUERDOS ✦"
        )

        recuerdos.bind(
            on_release=lambda *_:
            self.ir("recuerdos")
        )

        lista.add_widget(
            recuerdos
        )

        scroll.add_widget(
            lista
        )

        caja.add_widget(
            scroll
        )

        volver = BotonRomantico(
            VIOLETA
        )

        volver.text = "VOLVER AL INICIO"

        volver.bind(
            on_release=lambda *_:
            self.ir("inicio")
        )

        caja.add_widget(
            volver
        )

        self.add_widget(caja)

    def abrir_carta(self, indice):

        CartaScreen.indice_actual = indice

        self.manager.transition = SlideTransition(
            direction="left",
            duration=0.25
        )

        self.manager.current = "carta"

    def ir(self, pantalla):

        self.manager.transition = FadeTransition(
            duration=0.25
        )

        self.manager.current = pantalla


# ============================================================
# CARTA INDIVIDUAL
# ============================================================

class CartaScreen(PantallaBase):

    indice_actual = 0

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        caja = BoxLayout(
            orientation="vertical",
            padding=(
                dp(12),
                dp(18)
            ),
            spacing=dp(8)
        )

        self.titulo = etiqueta(
            "",
            23,
            ROSA_CLARO,
            True
        )

        self.titulo.size_hint_y = None
        self.titulo.height = dp(65)

        caja.add_widget(
            self.titulo
        )

        self.scroll_carta = ScrollView(
            do_scroll_x=False,
            bar_width=dp(4),
            scroll_type=[
                "bars",
                "content"
            ]
        )

        self.texto = TextoCarta()

        self.scroll_carta.add_widget(
            self.texto
        )

        caja.add_widget(
            self.scroll_carta
        )

        controles = BoxLayout(
            size_hint_y=None,
            height=dp(56),
            spacing=dp(6)
        )

        self.anterior = BotonRomantico(
            VIOLETA
        )

        self.anterior.text = "‹"

        centro = BotonRomantico(
            ROSA
        )

        centro.text = "CARTAS"

        siguiente = BotonRomantico(
            MAGENTA
        )

        siguiente.text = "›"

        self.anterior.bind(
            on_release=lambda *_:
            self.cambiar(-1)
        )

        centro.bind(
            on_release=lambda *_:
            self.volver()
        )

        siguiente.bind(
            on_release=lambda *_:
            self.cambiar(1)
        )

        controles.add_widget(
            self.anterior
        )

        controles.add_widget(
            centro
        )

        controles.add_widget(
            siguiente
        )

        caja.add_widget(
            controles
        )

        self.add_widget(caja)

        self.bind(
            on_pre_enter=self.actualizar_carta
        )

    def actualizar_carta(self, *args):

        indice = max(
            0,
            min(
                CartaScreen.indice_actual,
                len(CARTAS) - 1
            )
        )

        carta = CARTAS[indice]

        self.titulo.text = (
            f"{indice + 1:02d}  •  "
            f"{carta['titulo']}"
        )

        self.texto.text = carta["texto"]

        self.texto.color = BLANCO

        self.texto.texture_update()

        self.texto.actualizar_texto()

        self.texto.texture_update()

        Clock.schedule_once(
            lambda dt:
            setattr(
                self.scroll_carta,
                "scroll_y",
                1
            ),
            0.08
        )

        self.anterior.disabled = (
            indice == 0
        )

    def cambiar(self, paso):

        nuevo = (
            CartaScreen.indice_actual
            + paso
        )

        if 0 <= nuevo < len(CARTAS):

            CartaScreen.indice_actual = nuevo

            self.actualizar_carta()

    def volver(self):

        self.manager.transition = SlideTransition(
            direction="right",
            duration=0.25
        )

        self.manager.current = "cartas"


# ============================================================
# RECUERDOS
# ============================================================

class RecuerdosScreen(PantallaBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        caja = BoxLayout(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(14)
        )

        caja.add_widget(
            etiqueta(
                "✦ NUESTROS RECUERDOS ✦",
                26,
                ROSA_CLARO,
                True
            )
        )

        caja.add_widget(
            etiqueta(
                "Guarda fotografías, canciones y momentos.",
                15,
                GRIS
            )
        )

        caja.add_widget(
            Label()
        )

        fotos = BotonRomantico(
            ROSA
        )

        fotos.text = (
            "♥  ÁLBUM DE FOTOS"
        )

        fotos.bind(
            on_release=lambda *_:
            self.ir("fotos")
        )

        caja.add_widget(
            fotos
        )

        canciones = BotonRomantico(
            CIAN
        )

        canciones.text = (
            "♫  NUESTRAS CANCIONES"
        )

        canciones.bind(
            on_release=lambda *_:
            self.ir("canciones")
        )

        caja.add_widget(
            canciones
        )

        momentos = BotonRomantico(
            ORO
        )

        momentos.text = (
            "★  MOMENTOS ESPECIALES"
        )

        momentos.bind(
            on_release=lambda *_:
            self.ir("momentos")
        )

        caja.add_widget(
            momentos
        )

        caja.add_widget(
            Label()
        )

        volver = BotonRomantico(
            VIOLETA
        )

        volver.text = "VOLVER A LAS CARTAS"

        volver.bind(
            on_release=lambda *_:
            self.ir("cartas")
        )

        caja.add_widget(
            volver
        )

        self.add_widget(caja)

    def ir(self, pantalla):

        self.manager.transition = FadeTransition(
            duration=0.25
        )

        self.manager.current = pantalla


# ============================================================
# MOMENTOS
# ============================================================

class MomentosScreen(PantallaBase):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        caja = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        caja.add_widget(
            etiqueta(
                "★ MOMENTOS ESPECIALES ★",
                24,
                ORO,
                True
            )
        )

        self.entrada = TextInput(
            hint_text="Escribe aquí un recuerdo...",
            multiline=True,
            font_size=dp(17),
            background_color=(
                0.08,
                0.02,
                0.13,
                1
            ),
            foreground_color=BLANCO,
            cursor_color=ROSA,
            padding=dp(15)
        )

        caja.add_widget(
            self.entrada
        )

        guardar = BotonRomantico(
            ORO
        )

        guardar.text = "GUARDAR MOMENTO"

        guardar.bind(
            on_release=self.guardar
        )

        caja.add_widget(
            guardar
        )

        scroll = ScrollView(
            do_scroll_x=False
        )

        self.lista = GridLayout(
            cols=1,
            spacing=dp(8),
            size_hint_y=None
        )

        self.lista.bind(
            minimum_height=self.lista.setter(
                "height"
            )
        )

        scroll.add_widget(
            self.lista
        )

        caja.add_widget(
            scroll
        )

        volver = BotonRomantico(
            VIOLETA
        )

        volver.text = "VOLVER"

        volver.bind(
            on_release=lambda *_:
            self.volver()
        )

        caja.add_widget(
            volver
        )

        self.add_widget(caja)

        self.bind(
            on_pre_enter=self.cargar
        )

    def datos(self):

        return App.get_running_app().datos

    def guardar(self, *args):

        texto = self.entrada.text.strip()

        if not texto:
            return

        self.datos().data[
            "momentos"
        ].append(texto)

        self.datos().guardar()

        self.entrada.text = ""

        self.cargar()

    def cargar(self, *args):

        self.lista.clear_widgets()

        momentos = self.datos().data.get(
            "momentos",
            []
        )

        if not momentos:

            aviso = etiqueta(
                "Todavía no hay momentos guardados ♥",
                15,
                GRIS
            )

            aviso.size_hint_y = None
            aviso.height = dp(55)

            self.lista.add_widget(
                aviso
            )

            return

        for momento in momentos:

            lbl = etiqueta(
                "♥  " + momento,
                15,
                BLANCO
            )

            lbl.halign = "left"

            lbl.size_hint_y = None
            lbl.height = dp(90)

            self.lista.add_widget(
                lbl
            )

    def volver(self):

        self.manager.transition = SlideTransition(
            direction="right",
            duration=0.25
        )

        self.manager.current = "recuerdos"


# ============================================================
# FOTOS
# ============================================================

class FotoArrastrable(Image):

    def __init__(
        self,
        ruta,
        pantalla,
        **kwargs
    ):

        super().__init__(**kwargs)

        self.ruta = ruta
        self.pantalla = pantalla

        self.keep_ratio = True
        self.allow_stretch = True

        self.inicio = None
        self.arrastrando = False

    def on_touch_down(self, touch):

        if self.collide_point(
            *touch.pos
        ):

            self.inicio = touch.pos

            Clock.schedule_once(
                self.activar_arrastre,
                0.45
            )

            return True

        return super().on_touch_down(
            touch
        )

    def activar_arrastre(self, dt):

        if self.inicio is not None:

            self.arrastrando = True

    def on_touch_move(self, touch):

        if self.inicio is None:

            return super().on_touch_move(
                touch
            )

        if self.arrastrando:

            dx = (
                touch.pos[0]
                - self.inicio[0]
            )

            dy = (
                touch.pos[1]
                - self.inicio[1]
            )

            self.x += dx
            self.y += dy

            self.inicio = touch.pos

            return True

        return super().on_touch_move(
            touch
        )

    def on_touch_up(self, touch):

        if self.inicio is None:

            return super().on_touch_up(
                touch
            )

        inicio = self.inicio

        self.inicio = None

        if self.arrastrando:

            self.arrastrando = False

            self.pantalla.finalizar_arrastre(
                self
            )

            return True

        dx = abs(
            touch.pos[0]
            - inicio[0]
        )

        dy = abs(
            touch.pos[1]
            - inicio[1]
        )

        if dx < dp(15) and dy < dp(15):

            self.pantalla.mostrar_foto(
                self.ruta
            )

        return True


class FotosScreen(PantallaBase):

    EXTENSIONES = (
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".gif",
        ".bmp"
    )

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        caja = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(8)
        )

        caja.add_widget(
            etiqueta(
                "♥  ÁLBUM DE FOTOS  ♥",
                24,
                ROSA_CLARO,
                True
            )
        )

        caja.add_widget(
            etiqueta(
                "Toca una foto para verla • "
                "Mantén pulsada para moverla",
                12,
                GRIS
            )
        )

        self.scroll = ScrollView(
            do_scroll_x=False,
            bar_width=dp(3)
        )

        self.grid = GridLayout(
            cols=2,
            spacing=dp(10),
            padding=dp(6),
            size_hint_y=None
        )

        self.grid.bind(
            minimum_height=self.grid.setter(
                "height"
            )
        )

        self.scroll.add_widget(
            self.grid
        )

        caja.add_widget(
            self.scroll
        )

        agregar = BotonRomantico(
            ROSA
        )

        agregar.text = "＋  AGREGAR FOTO"

        agregar.bind(
            on_release=self.abrir_selector
        )

        caja.add_widget(
            agregar
        )

        volver = BotonRomantico(
            VIOLETA
        )

        volver.text = "VOLVER"

        volver.bind(
            on_release=lambda *_:
            self.volver()
        )

        caja.add_widget(
            volver
        )

        self.add_widget(caja)

        self.bind(
            on_pre_enter=self.cargar
        )

    def datos(self):

        return App.get_running_app().datos

    def cargar(self, *args):

        self.grid.clear_widgets()

        datos_fotos = self.datos().data.get(
            "fotos",
            []
        )

        fotos = []

        for item in datos_fotos:

            if isinstance(
                item,
                str
            ):

                ruta = item

            elif isinstance(
                item,
                dict
            ):

                ruta = item.get(
                    "ruta",
                    ""
                )

            else:

                continue

            if (
                isinstance(ruta, str)
                and os.path.isfile(ruta)
            ):

                fotos.append(ruta)

        self.datos().data[
            "fotos"
        ] = fotos

        self.datos().guardar()

        if not fotos:

            aviso = etiqueta(
                "Aún no hay fotografías.\n\n"
                "Agrega aquí tus recuerdos ♥",
                16,
                GRIS
            )

            aviso.size_hint_y = None
            aviso.height = dp(140)

            self.grid.add_widget(
                aviso
            )

            return

        for ruta in fotos:

            imagen = FotoArrastrable(
                ruta,
                self,
                source=ruta,
                size_hint=(1, None),
                height=dp(180)
            )

            self.grid.add_widget(
                imagen
            )

    # --------------------------------------------------------
    # MISMO SELECTOR QUE CANCIONES
    # --------------------------------------------------------

    def abrir_selector(self, *args):

        caja = BoxLayout(
            orientation="vertical"
        )

        chooser = FileChooserListView(
            path="/storage/emulated/0",
            filters=[
                "*.jpg",
                "*.jpeg",
                "*.png",
                "*.webp",
                "*.gif",
                "*.bmp"
            ],
            multiselect=False
        )

        caja.add_widget(
            chooser
        )

        botones = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(8)
        )

        cancelar = BotonRomantico(
            VIOLETA
        )

        cancelar.text = "CANCELAR"

        aceptar = BotonRomantico(
            ROSA
        )

        aceptar.text = "SELECCIONAR"

        botones.add_widget(
            cancelar
        )

        botones.add_widget(
            aceptar
        )

        caja.add_widget(
            botones
        )

        popup = Popup(
            title="Seleccionar fotografía",
            content=caja,
            size_hint=(
                0.98,
                0.92
            ),
            separator_color=ROSA
        )

        cancelar.bind(
            on_release=popup.dismiss
        )

        def aceptar_foto(*_):

            if not chooser.selection:
                return

            origen = chooser.selection[0]

            if not origen.lower().endswith(
                self.EXTENSIONES
            ):
                return

            carpeta = os.path.join(
                App.get_running_app().user_data_dir,
                "fotos"
            )

            os.makedirs(
                carpeta,
                exist_ok=True
            )

            nombre = os.path.basename(
                origen
            )

            destino = os.path.join(
                carpeta,
                nombre
            )

            base, extension = os.path.splitext(
                destino
            )

            contador = 1

            while os.path.exists(
                destino
            ):

                destino = (
                    f"{base}_{contador}"
                    f"{extension}"
                )

                contador += 1

            try:

                shutil.copy2(
                    origen,
                    destino
                )

                self.datos().data[
                    "fotos"
                ].append(
                    destino
                )

                self.datos().guardar()

                popup.dismiss()

                self.cargar()

            except Exception as error:

                popup.dismiss()

                self.mensaje(
                    "No se pudo agregar la foto:\n\n"
                    + str(error)
                )

        aceptar.bind(
            on_release=aceptar_foto
        )

        popup.open()

    def mostrar_foto(self, ruta):

        caja = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=dp(8)
        )

        imagen = Image(
            source=ruta,
            allow_stretch=True,
            keep_ratio=True
        )

        caja.add_widget(
            imagen
        )

        botones = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(8)
        )

        eliminar = BotonRomantico(
            MAGENTA
        )

        eliminar.text = "ELIMINAR FOTO"

        cerrar = BotonRomantico(
            VIOLETA
        )

        cerrar.text = "CERRAR"

        botones.add_widget(
            eliminar
        )

        botones.add_widget(
            cerrar
        )

        caja.add_widget(
            botones
        )

        popup = Popup(
            title="♥",
            content=caja,
            size_hint=(
                0.98,
                0.92
            ),
            separator_color=ROSA
        )

        cerrar.bind(
            on_release=popup.dismiss
        )

        eliminar.bind(
            on_release=lambda *_:
            self.confirmar_eliminacion(
                ruta,
                popup
            )
        )

        popup.open()

    def confirmar_eliminacion(
        self,
        ruta,
        popup_anterior
    ):

        popup_anterior.dismiss()

        caja = BoxLayout(
            orientation="vertical",
            spacing=dp(15),
            padding=dp(18)
        )

        caja.add_widget(
            etiqueta(
                "¿Eliminar esta fotografía?",
                18,
                BLANCO,
                True
            )
        )

        botones = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(8)
        )

        cancelar = BotonRomantico(
            VIOLETA
        )

        cancelar.text = "CANCELAR"

        eliminar = BotonRomantico(
            MAGENTA
        )

        eliminar.text = "ELIMINAR"

        botones.add_widget(
            cancelar
        )

        botones.add_widget(
            eliminar
        )

        caja.add_widget(
            botones
        )

        popup = Popup(
            title="Confirmar",
            content=caja,
            size_hint=(
                0.88,
                None
            ),
            height=dp(210),
            separator_color=MAGENTA
        )

        cancelar.bind(
            on_release=popup.dismiss
        )

        def borrar(*_):

            datos = self.datos()

            if ruta in datos.data[
                "fotos"
            ]:

                datos.data[
                    "fotos"
                ].remove(ruta)

            try:

                if os.path.exists(ruta):

                    os.remove(ruta)

            except Exception:

                pass

            datos.guardar()

            popup.dismiss()

            self.cargar()

        eliminar.bind(
            on_release=borrar
        )

        popup.open()

    def finalizar_arrastre(
        self,
        imagen
    ):

       
