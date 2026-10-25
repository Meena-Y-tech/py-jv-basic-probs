#WAP to identify if the character is vowel or consonant

c = input()

if c in 'aeiouAEIOU':
    print("vowel")
elif c.isalpha():
    print("consonant")
else:
    print("none")