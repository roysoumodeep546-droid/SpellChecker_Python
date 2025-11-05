from spellchecker import SpellChecker



class SpellCheckeApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self,text: str) -> str:
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word and corrected_word.lower() != word.lower():
                print(f'correcting "{word}" to "{corrected_word}"')
                corrected_words.append(corrected_word) 
            else:
                corrected_words.append(word) 


        return '  '.join(corrected_words)
    

    def run(self):
        print("\n---spell checker---")

        while True:
            text = input('Enter text to check (or type"exit" to quit): ')

            if text.lower()=='exit':
                print('Closing the proghram....')
                break


            corrected_text = self.correct_text(text)
            print(f'Corrected Text : {corrected_text}')


if __name__ == "__main__":
    SpellCheckeApp().run()






