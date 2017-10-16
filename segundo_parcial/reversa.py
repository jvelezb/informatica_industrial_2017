class reversa:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(reversa().reverse_words('Ya casi se aproxima el segundo parcial'))