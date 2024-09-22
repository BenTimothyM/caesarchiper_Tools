print("--------------------------")
print("|CAESAR CHIPER DECRYPTION|")
print("--------------------------")
print("Write the message you want to decrypt! (lowercase)")
message = input("> ")
print("--------------------------------")
Letters = 'abcdefghijklmnopqrstuvwxyz'

for key in range(len(Letters)):
   translated = ''
   for ch in message:
      if ch in Letters:
         num = Letters.find(ch)
         num = num - key
         if num < 0:
            num = num + len(Letters)
         translated = translated + Letters[num]
      else:
         translated = translated + ch
   print('Trial to %s: %s' % (key, translated))

print("--------------------------------")