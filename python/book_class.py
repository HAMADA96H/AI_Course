class book :
    #global x,y
    def __init__(self,name,auther,num_pages,color = "black",typee=" techno",a=2 ,b=5 ):
        self.typee =typee
        self.name =name
        self.auther =auther
        self.num_pages =num_pages
        self.color =color
        self.a=a
        self.b=a
        #self.val=value
        
        
    def mul(self,a,b) :
        res = a*b
        #z = self.val
        return(res)
        
            
            
    def printvalue(self,v):
        print("result = ",v)
        
        
              
    def buy(self,price):
        print(self.name," the best book & price is ",price)
        
        
    def push(self,title):
        if title == "math" and self.auther == "raghad" :
            print (" thanke you : ",self.auther )
            

    

     