from .model import Model

class WordModel(Model):
    def __init__(self, name):
        super().__init__(name)
        self.felici=set()
        self.tristi=set()

    def studia(self):
        lista = self.righe[:(len(self.righe)//2)]
        feliciTemp=set()
        tristiTemp=set()
        for l in lista:
            x = l[0].split(" ")
            for el in x:
                if(l[1]=='1'):
                    feliciTemp.add(el)
                else: tristiTemp.add(el)
        
        for x,y in zip(tristiTemp, feliciTemp):
            if(x not in feliciTemp):
                self.tristi.add(x)
            if(y not in tristiTemp):
                self.felici.add(y)
            

    def analizza(self):
        self.percentuale=0
        self.positive=0
        lista = self.righe[(len(self.righe)//2)+1:]
        #lista = self.righe
        for l in lista:
            x = l[0].split(" ")
            count:int=0
            for el in x:
                if(len(el)>0):
                    # if(el[-1]==',' or el[-1]=='.'):
                    #     if(el[-1] in self.felici):
                    #         count+=1
                    #     if(el[-1] in self.tristi): count-=1
                    if(el in self.felici) :
                        count+=1
                    elif(el in self.tristi) : count-=1

            if(count>=0 and l[1]=='1') : self.positive+=1
            elif(count<0 and l[1]=='0') : self.positive+=1
            else: self.positive-=1
        print(self.positive)

        self.percentuale = (self.positive*100)/((len(lista))/2)
        