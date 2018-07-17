import sl4a
import time
droid = sl4a.Android()

data1 = open("storage/sdcard1/ques.txt", 'r+')
data2 = open("storage/sdcard1/ans.txt",'r+')

droid.ttsSpeak('Enter your name please')
time.sleep(0.5)
username = droid.recognizeSpeech()
droid.setClipboard(username.result)
uname = username.result
droid.ttsSpeak("hello " + uname)
print ("Hello " + uname)

def call():
    time.sleep(1)
    inputer = droid.recognizeSpeech()
    droid.setClipboard(inputer.result)
    inputer1 = inputer.result
    print (uname + ">> " + " " + inputer1)
    for i in predic:
        if inputer1+'\n'== i:
            index = predic.index(i)
            answer = answers[index]
            droid.ttsSpeak(answer)
            print ("Bot >> " + answer)
            call()
    call()
        
decide1=2
i = 0
predic = []
answers = []
if int(decide1)== 2:
    for u in data1:
        predic.append(u)
    for n in data2:
        answers.append(n)
    droid.ttsSpeak("All data loaded" )
    time.sleep(1)
    call()

data1.close()
data2.close()

