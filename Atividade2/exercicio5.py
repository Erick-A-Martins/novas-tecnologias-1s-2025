msg = input("Digite a mensagem: ")
msgCript = ""
for digito in msg:
    msgCript += str((int(digito) + 7) % 10)

msgCript = msgCript[2] + msgCript[3] + msgCript[0] +  msgCript[1]
print("Criptografada: " + msgCript)

msgDesCript= ""
for digito in msgCript:
    msgDesCript += str((int(digito) + 3) % 10)

msgDesCript = msgDesCript[2] + msgDesCript[3] + msgDesCript[0] +  msgDesCript[1]
print("Descriptografada: " + msgDesCript)
