import pyttsx3
import speech_recognition as sr
from funcoes_pc import welcome, gettime, getData, abrir_google, abrir_youtube, abrir_chatgpt, abrir_whatsapp, abrir_hostinger, abrir_netflix, abrir_gmail, abrir_steam, abrir_xbox, abrir_valorant, desligar_pc, abrir_controlador_de_gastos, abrir_ifood, nicole_chegou, abrir_instagram, auto_destruir, reiciniar_pc, abrir_opera, ausentar, abrir_vs, abrir_trello, lista_comandos,speak, pedro
import webbrowser


engine = pyttsx3.init()

recognizer = sr.Recognizer()


def iniciar_comandos():
    speak("Me chamo Nova, em que posso ajudar?");
    while True:
            print("Aguardando comando...")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                try:

                    comando = recognizer.recognize_google(audio, language="pt-BR")
                    comando = comando.lower()

                    print(f"Você disse: {comando}")
                    if comando == 'quem é você' or comando == 'me fale sobre você':
                        welcome()

                    elif comando == 'me diga as horas' or comando == 'que horas são' or comando == 'horas':
                        gettime()

                    elif comando == 'que dia é hoje' or comando == 'dia':
                        getData()

                    elif comando == 'desligar' or comando == 'adeus':
                        desligar_pc()

                    elif comando == 'reiniciar':
                        reiciniar_pc()


                    elif comando == 'ausentar':
                        ausentar()

                    elif comando == 'lista de comandos' or comando == 'lista' or comando == 'lista de comando':
                        lista_comandos()

                    elif comando == 'pedro está aqui' or comando == 'pedro':
                        pedro()






                    elif comando == 'aumentar volume':
                        speak('Aumentando o volume.')
                        print("Aumentando o volume...")
                        try:
                            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                            from comtypes import CLSCTX_ALL

                            devices = AudioUtilities.GetSpeakers()
                            interface = devices.Activate(
                                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                            volume = interface.QueryInterface(IAudioEndpointVolume)

                            volume_atual = volume.GetMasterVolumeLevelScalar()
                            novo_volume = min(volume_atual + 0.2, 1.0)
                            volume.SetMasterVolumeLevelScalar(novo_volume, None)
                            print(f"Volume aumentado para {int(novo_volume * 100)}%")
                            speak(f"Volume aumentado para {int(novo_volume * 100)} por cento.")
                        except Exception as e:
                            print(f"Erro ao ajustar o volume: {e}")
                            speak("Não foi possível ajustar o volume.")

                    elif comando == 'diminuir volume':
                        speak('Diminuindo o volume.')
                        print("Diminuindo o volume...")
                        try:
                            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                            from comtypes import CLSCTX_ALL

                            devices = AudioUtilities.GetSpeakers()
                            interface = devices.Activate(
                                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                            volume = interface.QueryInterface(IAudioEndpointVolume)

                            volume_atual = volume.GetMasterVolumeLevelScalar()
                            novo_volume = max(volume_atual - 0.2, 0.0)
                            volume.SetMasterVolumeLevelScalar(novo_volume, None)
                            print(f"Volume diminuído para {int(novo_volume * 100)}%")
                            speak(f"Volume diminuído para {int(novo_volume * 100)} por cento.")
                        except Exception as e:
                            print(f"Erro ao ajustar o volume: {e}")
                            speak("Não foi possível ajustar o volume.")

                    elif comando == 'abrir google' or comando == 'google':
                        abrir_google()

                    elif comando == 'pesquisar google' or comando == 'pesquisar':

                        print("O que deseja pesquisar?")
                        speak("O que deseja pesquisar?");

                        try:
                            audio = recognizer.listen(source)
                            consulta = recognizer.recognize_google(audio, language="pt-BR")
                            consulta = consulta.lower()

                            webbrowser.open(f"https://www.google.com/search?q={consulta}")

                            print(f"Resultados da pesquisa no Google: {consulta}");
                            speak(f"Resultados da pesquisa no Google: {consulta}");

                           
                        
                        except sr.UnknownValueError:
                            print("Não consegui entender a consulta. Tente novamente.")
                            speak("Não consegui entender a consulta.")


                    elif comando == 'abrir youtube' or comando == 'youtube':
                        abrir_youtube()

                    elif comando == 'pesquisar youtube' or comando == 'tocar':
                        print("O que deseja pesquisar no Youtube?")
                        speak("O que deseja pesquisar no Youtube?");

                        try:
                            audio = recognizer.listen(source)
                            consulta = recognizer.recognize_google(audio, language="pt-BR")
                            consulta = consulta.lower()

                            webbrowser.open(f"https://www.youtube.com/search?q={consulta}")

                            print(f"Resultados da pesquisar no Youtube: {consulta}");
                            speak(f"Resultados da pesquisar no Youtube: {consulta}");


                        
                        except sr.UnknownValueError:
                            print("Não consegui entender a consulta. Tente novamente.")
                            speak("Não consegui entender a consulta.")


                    elif comando == 'abrir chat' or comando == 'abrir chat gpt' or comando == 'chat':
                        abrir_chatgpt()

                    elif comando == 'abrir trabalho' or comando == 'trabalho':
                        abrir_trello()

                    elif comando == 'abrir whatsapp' or comando == 'abrir conversa' or comando == 'whatsapp':
                        abrir_whatsapp()

                    elif comando == 'abrir instagram' or comando == 'abrir insta' or comando == 'instagram':
                        abrir_instagram()

                    elif comando == 'abrir envelope' or comando == 'abrir e-mail' or comando == 'envelope':
                        abrir_gmail()

                    elif comando == 'abrir host' or comando == 'site':
                        abrir_hostinger()

                    elif comando == 'hora h' or comando == 'abrir netflix' or comando == 'netflix' or comando == 'net':
                        abrir_netflix()

                    elif comando == 'abrir ifood' or comando == 'tô com fome' or comando == 'fome':
                        abrir_ifood()

                    elif comando == 'nicole chegou' or comando == 'nicole tá aqui':
                        nicole_chegou()

                    elif comando == 'abrir vs' or comando == 'abrir code' or comando == 'vs':
                        abrir_vs()

                    elif comando == 'abrir opera' or comando == 'opera' or comando == 'abrir navegador':
                        abrir_opera()
                        
                    elif comando == 'fechar opera':
                        auto_destruir()

                    elif comando == 'abrir controlador de gastos' or comando == 'abrir gastos' or comando == 'gastos' or comando == 'gasto':
                        abrir_controlador_de_gastos()

                    elif comando == 'abrir steam' or comando == 'abrir azul':
                        abrir_steam()

                    elif comando == 'abrir xbox' or comando == 'verde':
                        abrir_xbox()

                    elif comando == 'abrir jogo de tiro de fadinha' or comando == 'abrir valorant' or comando == 'jogo':
                        abrir_valorant()

                except sr.UnknownValueError:
                    print("Não entendi o que você disse. Tente novamente.")

                    print("\n")

iniciar_comandos()
