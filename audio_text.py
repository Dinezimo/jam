import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    text = recognizer.recognize_google(audio)
    print(text)
    if (text == "Ellis" or text == "Alice"):
        #print("c'est ls")
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

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        print(output.decode("utf-8"))
    if error:
        print(error.decode("utf-8"))

if __name__ == "__main__":
    print("Que dois je exécuter ?")
    audio = record_audio()
    cmd = recognize_speech(audio)
    print("\n\n-----------------------------------------------------COMMAND EXECUTION RESULT-------------------------------------------------------------------\n");
    if (cmd != ""):
        run_command(cmd)
    else:
        print("excuse us, this cmmand had not been manage... Try to une another");
