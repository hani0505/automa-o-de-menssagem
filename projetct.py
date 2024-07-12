import pywhatkit
phone = ""
# numero que você quer automatizar menssagens
msg = "oii"
time = 13
timeMinute = 20

close = False
closeTime = 5

pywhatkit.sendwhatmsg_instantly(phone, msg, time, timeMinute, True)

print("menssagem enviada")
# para confirmação de menssagem
