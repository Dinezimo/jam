import speech_recognition as sr
import subprocess
import facebook

recognizer = sr.Recognizer()

access_token = 'EAAPTEGWZCoNYBO7lt14KdUD0ezryQ0MxtZBdSEOHX0drWKZBjvs00wtTcHqUiDCuULwTqPWbD7ZAGtGcCQd1kMTGkO6fALIhNHXrRHICaZCmRZCmrnragKJdhhP09QXchQVtr7gLWfZBR2xuzZA5yQqrsF024Tzq3Gz0lI5ZBLWnbRLDGXZCYmzactdUD01satJ6zrZA7PsjDo6H0MwQfMgrHmTCkKlWWR33010oHhdVeLQZA7SC8VZCUqPhvydVzD5NHzFMZD'

def record_audio():
    print("Quelle commande dois je exécuter ???\n\n");
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            return audio
        except sr.RequestError:
            print("Erreur : Impossible de récupérer l'audio. Veuillez vérifier votre connexion Internet.")
            return None
        except sr.UnknownValueError:
            print("Erreur : Impossible de comprendre l'audio. Veuillez réessayer.")
            return None

def recognize_speech(audio):
    text = recognizer.recognize_google(audio)
    print(text)
    if (text == "Ellis" or text == "Alice" or text == "hello"):
        cmd = "/bin/ls"
        return cmd
    if (text == "CD" or text == "Sydney"):
        print("quelle est votre path ?")
        dest = recognizer.recognize_google(record_audio())
        print("\n\n-----------------------------------------------------PATH CHOISE-------------------------------------------------------------------\n");
        cmd = "cd " + dest
        return cmd
    if (text == "push in GitHub" or text == "search in YouTub.e" or text == "push in Gita" or text == "best in YouTube" or text == "push in YouTube" or text == "push in guitar" or text == "Porsche in YouTube"
        or text == "best guitar" or text == "best in GitHub"):
        print("\n\nquelle commit souhaitez-vous utiliser ?")
        commit = recognizer.recognize_google(record_audio())
        cmd = "git add . ; git commit -m \" " + commit + "\" ; git push; clear"
        return cmd
    if (text == "compile" or text == "open" or text == "compare" or text == "Kapil" or text == "compel" or text == "call Bill"):
        cmd = "gcc -o prog *.c ; clear; ./prog"
        return cmd
    if (text == "exit"):
        cmd = "echo \"Sortie en cours ... .... ... ... ... ... ..\n\n exit successifully\n\n"
        return cmd
    if (text == "share" or text == "sure" or text == "Shaw" or text == "shower" or text == "show"):
        cmd = "echo \"\n..............OK cool..........\n\""
        return cmd
    else:
        cmd = ""
    return cmd

def publish_to_facebook(message, access_token):
    graph = facebook.GraphAPI(access_token)
    try:
        graph.put_object("me", "feed", message=message)
        print("Message publié avec succès sur Facebook.")
    except facebook.GraphAPIError as e:
        print("Erreur lors de la publication sur Facebook")

def share_face(cmd):
    if (cmd == "echo \"\n..............OK cool..........\n\""):
        print("Avez vous envie de partager l'expérience sur la page officielle de Vocal-compilator Jam epitech ?")
        x = input().lower()
        if (x == "oui"):
            print("-------------------------------------------------que pensez vous de l'appli ???------------------------------------------------------------\n\n");
            post = recognizer.recognize_google(record_audio())
            print("\n\n . . . . . . .  . . . Tentative de connection .  .  . .  . . .  . .\n")
            publish_to_facebook(post, access_token)
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_Connection Succès_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")
            print("\nthank you dear user\n")
        else:
            print("---___---___---___---___----___Ce fut un grand honneur d'être à vos côté. Bonne journée ---___---___---___---___---___---___---___---___\n")

def run_command(command):
    print("vocal_minishell2-> " + command);
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        print(output.decode("utf-8"))
    if error:
        print(error.decode("utf-8"))
    share_face(cmd)
    print("\nCommande exécuté avec succès. voulez vous en exécuter une autre ? ? ?\n")
cmd = "begin"
if __name__ == "__main__":
    print(". . . . . . . . . . . . . . .. . . . . . . .. . . . . . . . Lancemant en cours .. . . . . . . . . . . . . . .  . . . . . . . . . . .  . . . .. . . .. . . . . \n\n")
    while (cmd != "echo \"Sortie en cours ... .... ... ... ... ... ..\n\n exit successifully\n\n"):
        audio = record_audio()
        if (audio == None):
            continue
        print(". . . . . .  . .  . .  . . . ..  . .. . . . .  . . . . . Audio récupéré.. . . . . . . . . Début de l'analyse . . . . . . . . . . . . .\n");
        cmd = recognize_speech(audio)
        print("\n\n----------------------------------------------------COMMAND EXECUTION RESULT-------------------------------------------------------------------\n");
        if (cmd != ""):
            run_command(cmd)
        else:
            print("excuse us, this cmmand had not been manage... Try to une another the next time");
