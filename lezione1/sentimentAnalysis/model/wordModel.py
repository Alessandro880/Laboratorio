from .model import Model

class WordModel(Model):
    def __init__(self, name):
        super().__init__(name)
        self.felici = ["loved","Loved", "Love", "love","excellent", "Excellent","happy","Happy", "good","Good","Fantastic","wonderful", "Wonderful", "fantastic","Great", "great"]
        self.tristi = ["awful", "Awful","Bad", "bad", "Sad", "sad", "terrible", "Terrible", "poor", "Poor", "Hate", "hate", "Hated", "hated"]

    def studia(self):
        lista = self.righe[:(len(self.righe)//2)]
        for l in lista:
            x = l[0].split(" ")
            count:int=0
            for el in x:
                if(el[-1]==',' or el[-1]=='.'):
                    if(el[:-1] in self.felici):
                        count+=1
                    elif(el[:-1] in self.tristi): count-=1
                elif(el in self.felici) :count+=1
                elif(el in self.tristi) : count-=1

            if(count>=0) : self.positive+=1
        self.percentuale = (self.positive*100)/len(lista)

    def analizza(self):
        self.percentuale=0
        self.positive=0
        lista = self.righe[(len(self.righe)//2)+1:]
        for l in lista:
            x = l[0].split(" ")
            count:int=0
            for el in x:
                if(el[-1]==',' or el[-1]=='.'):
                    if(el[:-1] in self.felici):
                        count+=1
                    elif(el[:-1] in self.tristi): count-=1
                elif(el in self.felici) :count+=1
                elif(el in self.tristi) : count-=1

            if(count>=0 and l[1]=='positiva') : self.positive+=1
            elif(count<0 and l[1]=='negativa') : self.positive+=1
        self.percentuale = (self.positive*100)/len(lista)
        