class reverse:
    def reverse_words(self, st):
        return ' '.join(reversed(st.split()))
print(reverse().reverse_words(input("Please enter your sentence : "))) 