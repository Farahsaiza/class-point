
class Point ():
    def __init__(self, abscisse = 0   , ordonne =  0 ) :
        self.__abscisse = abscisse
        self.__ordonne = ordonne

    def getabscisse(self):
        return self.__abscisse
    
    def getordonne(self):
        return self.__ordonne
    
    def  setabscisse(self,abscisse):
        self.__abscisse=  abscisse
    
    def setordonne(self, ordonne)
        self.__ordonne   = ordonne
    
    def distance(self,p1):



        print("la distance entre 2 point est : {}".format(0.5**((p1.getabscisse())**2-(self.getabscisse()**2))+(p1.getordonne()**2-(self.getordonne()**2))))
    

    def norme(self): 
        
        print("la norme entre le point et  l'origine    est: {}".format(0.5**((self.getabscisse())**2)+(self.getordonne()**2)))




