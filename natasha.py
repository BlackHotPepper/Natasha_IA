import pyttsx3
import speech_recognition as speaker
import pygame
import time
import requests
import webbrowser as web


pygame.init()
pygame.mixer.music.load("./intro_music.mp3")
pygame.mixer.music.play()
pygame.event.wait()

time.sleep(7)
robo = pyttsx3.init()
msg = 'Olá! Em que posso ajudar?'
robo.say(msg)
robo.runAndWait()

def Start():
    key = '102021'
    while key == '102021':
        def Begin():
            mic = speaker.Recognizer()
            with speaker.Microphone() as source:
                mic.adjust_for_ambient_noise(source)
                audio = mic.listen(source)
            try:
                voice_rec = mic.recognize_google(audio, language='pt-BR')
                print(voice_rec)
                
                if 'apresente-se' in voice_rec.lower() or 'se apresente' in voice_rec.lower() or 'quem é você' in voice_rec.lower() or 'apresenta' in voice_rec.lower() or 'se apresentar' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = 'Olá, é um prazer. Me chamo Natasha, e sou uma inteligência artificial criado com a linguagem paiton, com o objetivo em promover uma facilidade em tarefas diárias, e claro, ajudar no que for preciso. Enfim, essa sou eu.'
                    robo.say(msg)
                    robo.runAndWait()
                elif 'bom dia' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = 'Bom dia, como está se sentindo hoje?'
                    robo.say(msg)
                    robo.runAndWait()
                    
                    mic_bd = speaker.Recognizer()
                    with speaker.Microphone() as source:
                        mic_bd.adjust_for_ambient_noise(source)
                        audio_bd = mic_bd.listen(source)
                        mic.adjust_for_ambient_noise(source)
                        audio_bd = mic.listen(source)
                        
                        voice_rec_bd = mic.recognize_google(audio_bd, language='pt-BR')
                        if 'bem' in voice_rec_bd.lower() or 'bom' in voice_rec_bd.lower() or 'maravilhoso' in voice_rec_bd.lower() or 'tudo bem' in voice_rec_bd.lower() or 'melhor' in voice_rec_bd.lower():
                            robo = pyttsx3.init()
                            msg = 'Que bom saber disso, espero que continue assim.'
                            robo.say(msg)
                            robo.runAndWait()
                        elif 'cansado' in voice_rec_bd.lower() or 'mal' in voice_rec_bd.lower() or 'mau' in voice_rec_bd.lower() or 'triste' in voice_rec_bd.lower() or 'ruim' in voice_rec_bd.lower():
                            robo = pyttsx3.init()
                            msg = 'Espero que seu dia melhore, estou aqui caso precise.'
                            robo.say(msg)
                            robo.runAndWait()
                        else:
                            robo = pyttsx3.init()
                            msg = 'Espero que seu dia seja produtivo, estarei aqui qualquer coisa.'
                            robo.say(msg)
                            robo.runAndWait()
                elif 'boa tarde' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = 'Boa tarde, em que posso ajudá-lo?'
                    robo.say(msg)
                    robo.runAndWait()
                elif 'boa noite' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = 'Boa noite. Até outra hora.'
                    robo.say(msg)
                    robo.runAndWait()
                elif 'como está o clima' in voice_rec.lower() or 'clima' in voice_rec.lower() or 'como está a temperatura' in voice_rec.lower() or 'tempo' in voice_rec.lower() or 'como está o tempo hoje' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = "Para acessar a opção de clima e temperatura, você deve entrar no meu código fonte, informar sua cidade na função Clima, e em seguida chamar a função."
                    robo.say(msg)
                    robo.runAndWait()
                    def Clima():
                        key = "100e5db8f22f34f0b3d05c8de8882535"
                        city = "" #Digite sua cidade
                        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

                        req = requests.get(url)
                        req_dic = req.json()
                        sensação = req_dic['main']['feels_like'] - 273.15
                        press = req_dic['main']['pressure']
                        humidity = req_dic['main']['humidity']
                        temp = req_dic['main']['temp'] - 273.15

                        robo = pyttsx3.init()
                        msg = f'Na cidade de {city}, a temperatura está em cerca de {round(temp)} graus, com a sensação térmica de {round(sensação)}. A pressão atmosférica gira em torno de {press} pascal, com uma humidade de {humidity}%.'
                        robo.say(msg)
                        robo.runAndWait()
                    #Clima()
                elif 'facebook' in voice_rec.lower() or 'abra o facebook' in voice_rec.lower() or 'abrir facebook' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = 'Abrindo facebook, por favor aguarde.'
                    robo.say(msg)
                    robo.runAndWait()
                    
                    web.open('https://www.facebook.com/')
                elif 'youtube' in voice_rec.lower() or 'abra o youtube' in voice_rec.lower() or 'abrir youtube' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = 'Abrindo youtube, por favor aguarde.'
                    robo.say(msg)
                    robo.runAndWait()
                    
                    web.open('https://www.youtube.com/')
                elif 'whatsapp' in voice_rec.lower() or 'abra o whatsapp' in voice_rec.lower() or 'abrir whatsapp' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = 'Abrindo uatiszap, por favor aguarde.' #Escrito dessa forma por motivos de sotaque do módulo pyttsx3
                    robo.say(msg)
                    robo.runAndWait()
                    
                    web.open('https://web.whatsapp.com/')
                elif 'instagram' in voice_rec.lower() or 'abra o instagram' in voice_rec.lower() or 'abrir instagram' in voice_rec.lower() or 'insta' in voice_rec.lower():
                    robo = pyttsx3.init()
                    msg = 'Abrindo instagran, por favor aguarde.' #Escrito dessa forma por motivos de sotaque do módulo pyttsx3
                    robo.say(msg)
                    robo.runAndWait()
                    
                    web.open('https://www.instagram.com/')
                else:
                    robo = pyttsx3.init()
                    msg = "Desculpe-me, mas não pude entendê-lo corretamente. Talvez o seu comando não foi esclarecido no meu código fonte. Para isso, recomendo ir no meu código fonte e realizar uma atualização, colocando os devidos pedidos e efetuando tal comando."
                    robo.say(msg)
                    robo.runAndWait()
                    
                #Para adicionar uma nova funcionalidade, siga os comandos abaixo...
                #elif "frase" in voice_rec.lower():
                #    especifique seu comando
                    
            except speaker.UnknownValueError:
                print("Não entendi")
                Start()
        Begin()
Start()
    