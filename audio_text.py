import speech_recognition as sr
import subprocess
import facebook

recognizer = sr.Recognizer()

access_token = 'EAAPTEGWZCoNYBO7fkWqB71Xo0OV5l4OGFzkKwN1swo42M92zAQ7CjBGkVpW4qtZBlIYXJIRgSDZCgSDvHMhLAku4H14tqPjBLJV3grOYTwrgi0WocZAdOH6F64YdsSwS8FJdjgAv4nusnwFXC02XCDkHZBREkoKRx8y8n3GF7zL9Hg5JScc6iL4MI5GZB7U6ixqvIeeXQov9bcQxZA8fn7Q4w7AtVc7pyOKHZCQZD'

def record_audio():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    text = recognizer.recognize_google(audio)
    print(text)
    if (text == "Ellis" or text == "Alice"):
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
        print("test twiter")
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

def run_command(command):
    print("vocal_minishell2-> " + command);
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        print(output.decode("utf-8"))
    if error:
        print(error.decode("utf-8"))
    print("\nCommande exécuté avec succès. Avez vous envie de partager l'expérience sur la page officielle de Vocal-compilator Jam epitech ?")
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

if __name__ == "__main__":
    print("Que dois je exécuter ?")
    audio = record_audio()
    cmd = recognize_speech(audio)
    print("\n\n-----------------------------------------------------COMMAND EXECUTION RESULT-------------------------------------------------------------------\n");
    if (cmd != ""):
        run_command(cmd)
    else:
        print("excuse us, this cmmand had not been manage... Try to une another the next time");
