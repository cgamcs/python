import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar nuestro microfono y devolver el audio comotexto
def transformar_audio_en_texto():
    # almacenar recognizer en variabale
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Iniciando...")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-mx")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("No comprendi el audio")

            # devolver error:
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("No comprendi el pedido")

            # devolver error:
            return "sigo esperando"

        # error inesperado
        except:
            # prueba de que no comprendio el audio
            print("Algo salio mal")

            # devolver error:
            return "sigo esperando"

# funcion para que el asistente pueda ser esuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# informar el dia de la semana
def pedir_dia():
    # variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    dias_de_la_semana = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miercoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sabado',
                  6: 'Domingo'}

    # diccionario con nombre del mes
    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }

    hablar(f'Hoy es {dias_de_la_semana[dia_semana]} {dia.day} de {meses[dia.month]}')

# informar la hora del dia
def pedir_hora():
    # crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento, son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)

    # decir la hora
    hablar(hora)

# funcion saludo inicial
def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    print(hora.hour)
    if hora.hour < 6 or hora.hour > 18:
        momento = 'Buenos noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenos tardes'

    # decir saludo
    hablar(f'{momento}, soy Helena, tu asistente personal. Por favor, dime en que te puedo ayudar')

# funcion central del asistent
def pedir_cosas():
    # activar el saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abre youtube' in pedido:
            hablar('Con gusto estoy abriendo YouTube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abre el navegador' in pedido:
            hablar('Con gusto estoy abriendo el navegador')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en google' in pedido:
            hablar('Estoy en eso')
            pedido = pedido.replace('busca en google', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que eh encontrado')
        elif 'reproduce' in pedido:
            hablar('Empezando a reproducir')
            pedido = pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke(language='es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion_nombre = pedido.split('de')[-1].strip().lower()

            cartera = {
                'apple': 'AAPL',
                'amazon': 'AMZN',
                'google': 'GOOGL',
                'palantir': 'PLTR',
            }

            try:
                # Check if the stock is in our dictionary
                if accion_nombre in cartera:
                    ticker_symbol = cartera[accion_nombre]
                    stock = yf.Ticker(ticker_symbol)

                    # 3. OPTIMIZATION: Use fast_info
                    # .info is very slow (web scraping). .fast_info is much faster for just price.
                    precio = stock.fast_info['last_price']

                    # Format price to 2 decimal places for better speech
                    hablar(f'El precio de las acciones de {accion_nombre} es {round(precio, 2)} dólares')
                else:
                    hablar(f'Lo siento, no tengo a {accion_nombre} en mi lista')

            except Exception as e:
                print(f"Error técnico: {e}")  # Print error to console for debugging
                hablar('Hubo un error al intentar obtener el precio')

            continue
        elif 'hasta pronto' in pedido:
            hablar('Hasta pronto')
            break

pedir_cosas()