#Single Responsibility Principle
#Uma classe só deve ter um motivo para mudar e o motivo deve estar relacionado com sua responsabilidade principal.


class journal:
    def __init__(self) -> None:
        self.entries = []
        self.entriesCount = 0

    def add_entry(self, text):
        self.entriesCount += 1
        self.entries.append(f'Registro {self.entriesCount}: {text}')
    
    def get_entry(self):        
        return '\n'.join(self.entries)
    
    def __str__(self) -> str:
        return self.get_entry()
    
    #Um cenário que seria uma violação desse principio por exemplo, seria adicionar metódos que atuam na persistencia das informações gerando arquivos.
    #generate_file()
    #    pass
    #
#Para esse caso foi criado uma classe especifica para o manuseio de arquivos.
class PersistenceMannager:
    
    @staticmethod
    def generate_file(fileName, string):
        with open(fileName, 'w') as file:
            file.write(string)
            file.close()
    @staticmethod
    def read_file(fileName):
        with open(fileName, 'r') as file:
            return file.read()



j = journal()
j.add_entry('Hoje eu acordei')
j.add_entry('Entrada aleatória')

fileMannager = PersistenceMannager()
fileMannager.generate_file('registro', j.get_entry())
print(fileMannager.read_file('registro'))



