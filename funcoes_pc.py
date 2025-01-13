import os
import pyttsx3
import datetime
import webbrowser
import psutil




#Abrir Funções da Nova
def welcome():
    responder = 'Olá, me chamo Nova, sou sua assistente virtual e vim aqui para deixar sua vida um pouquinho mais fácil!'
    speak(responder)

    print("\n")

def gettime():
    now = datetime.datetime.now()
    responder = f'São {now.hour} horas e {now.minute} minutos.'
    print(responder)
    speak(responder)

    print("\n")

def desligar_pc():
    speak("até a próxima")
    print("desligando o computador...")
    os.system("shutdown /s /t 0")

    print("\n")

def reiciniar_pc():
    speak("reiniciando")
    print("Reiniciando o computador...");
    os.system("shutdown /r /t 0")

    print("\n")
 
def getData():
    hoje = datetime.datetime.now().strftime("%d/%m/%Y")
    responder = f'Hoje é dia {hoje}'
    print(responder)
    speak(responder)

    print("\n")


def ausentar():
    speak("Até mais tarde!")
    exit();

    print("\n")

def pedro():
    print("Vai tomar no cu Pedro seu bosta");
    speak("Vai tomar no cu Pedro seu bosta")


def lista_comandos():
    print("\n\n\n")

    print("Lista de comandos:")

    print("\n\n\n")

    print("1 - Apresentação: Quem é você? ou Me fale sobre você\n");

    print("2 - Horas: Me diga as horas ou Que horas são?\n");

    print("3 - Desligar: Desligar ou Adeus\n");

    print("4 - Reiniciar: Reiniciar\n");

    print("5 - Fechar opera: Fechar Opera\n")

    print("6 - Ausentar: ausentar\n")

    print("7 - Data: que dia é hoje ou dia\n")

    print("8 - Aumentar Volume: aumentar volume\n");

    print("9 - Diminuir Volume: diminuir volume\n");

    print("10 - Abrir Google: abrir google ou google\n")

    print("11 - Pesquisar Google: pesquisar google ou pesquisar\n")
    
    print("12 - Abrir Youtube: abrir youtube ou youtube\n");

    print("13 - Pesquisar Youtube: pesquisar youtube ou tocar\n")

    print("14 - Abrir ChatGpt: abrir chat ou abrir chat gpt ou chat\n")

    print("15 - Abrir Trello Aruda: abrir trabalho ou trabalho\n")

    print("16 - Abrir Whatsapp: abrir whatsapp ou abrir conversa ou whatsapp\n")

    print("17 - Abrir Instagram: abrir instagram ou abrir insta ou instagram\n")

    print("18 - Abrir E-mail: abrir envelope ou abrir e-mail ou envelope\n");

    print("19 - Abrir Hostinger: abrir host ou site\n")

    print("20 - Abrir Netflix: hora h ou abrir netflix ou netflix ou net\n")

    print("21 - Abrir Ifood: abrir ifood ou tô com fome ou fome\n");

    print("22 - Nicole Chegou: nicoele chegou ou nicole tá aqui\n");

    print("23 - Abrir Visual Studio Code: abrir vs ou abrir code ou vs\n");

    print("24 - Abrir Opera: abrir opera ou opera ou abrir navegador\n");

    print("25 - Abrir Controlador de Gastos: abrir controlador de gastos ou abrir gastos ou gastos ou gasto\n")

    print("26 - Abrir Steam: abrir steam ou abrir azul\n")

    print("27 - Abrir Xbox: abrir xbox ou verde\n");

    print("28 - Abrir Valorant: abrir jogo de tiro de fadinha ou abrir valorant ou jogo");

    print("29 - Xingar Pedro - Pedro está aqui ou Pedro")


    print("\n\n\n")


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-2].id)
    engine.setProperty('rate',200)
    engine.say(text)
    engine.runAndWait()







#Abrir Sites
def abrir_google():
    print("Abrindo Google")
    webbrowser.open("https://www.google.com")

    print("\n")

def abrir_youtube():
    print("Abrindo Youtube")
    webbrowser.open("https://www.youtube.com")

    print("\n")

def abrir_chatgpt():
    print("Abrindo ChatGPT")
    webbrowser.open("https://chatgpt.com");

    print("\n")

def abrir_whatsapp():
    print("Abrindo Whatsapp")
    webbrowser.open("https://web.whatsapp.com")

    print("\n")

def abrir_instagram():
    print("Abrindo Instagram")
    webbrowser.open("https://www.instagram.com")

    print("\n")

def abrir_hostinger():
    print("Abrindo Hostinger")
    webbrowser.open("https://hpanel.hostinger.com/?redirect_back_url=https%3A%2F%2Fauth.hostinger.com%2Fbr%2Flogin&_ga=GA1.2.GA1.1.1064882336.1715141620&_gl=1*bngghs*_ga*R0ExLjEuMTA2NDg4MjMzNi4xNzE1MTQxNjIw*_ga_73N1QWLEMH*R1MxLjEuMTczNjI4NjUyMC4yOS4wLjE3MzYyODY1MjIuNTguMC4xNjgyNjc5NDcy")

    print("\n")

def abrir_gmail():
    print("Abrindo Gmail")
    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

    print("\n")

def abrir_netflix():
    print("Abrindo Netflix")
    webbrowser.open('https://www.netflix.com/browse');

    print("\n") 

def abrir_ifood():
    print("Abrindo Ifood")
    webbrowser.open('https://www.ifood.com.br/mercados')

    print("\n")

def abrir_trello():
    print("Abrindo Trello Aruda")
    webbrowser.open("https://trello.com/b/821ViYga/aruda-web")

    print("\n")
    
def nicole_chegou():
    speak("seja bem vinda nicole.")
    webbrowser.open('https://www.youtube.com/watch?v=JqIHlDVqUTw')

    print("\n")








#Abrir programas
def abrir_opera():
    print("Abrindo Opera")
    caminho_opera = '"C:/Users/Pichau/AppData/Local/Programs/Opera GX/opera.exe"'

    os.startfile(caminho_opera)

    print("\n")

def auto_destruir():
    nome_processo = 'opera.exe'

    
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            
            if process.info['name'].lower() == nome_processo:
                print(f"Fechando o Opera (PID: {process.info['pid']})...")
                print("\n")
                process.terminate()  
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def abrir_vs():
    print("Abrindo Visual Studio Code")
    caminho_vs = 'C:/Users/Pichau/AppData/Local/Programs/Microsoft VS Code/Code.exe'

    os.startfile(caminho_vs)

    print("\n")

def abrir_controlador_de_gastos():
    print("Abrindo Controlador de Gastos")
    caminho_controlador_de_gastos = 'C:/Users/Pichau/Desktop/Igor/gasto_mensais'
    os.startfile(caminho_controlador_de_gastos)

    print("\n")

def abrir_valorant():
    print("Abrindo Valorant")
    caminho_valorant = "C:/Users/Pichau/Desktop/Jogo/valorant"
    os.startfile(caminho_valorant)

    print("\n")

def abrir_steam():
    print("Abrindo Steam")
    caminho_steam = "C:/Users/Pichau/Desktop/Jogo/steam"
    os.startfile(caminho_steam)

    print("\n")

def abrir_xbox():
    print("Abrindo Xbox")
    caminho_xbox = ""
    os.startfile(caminho_xbox)

    print("\n")