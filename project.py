import math
file=open("f1.txt",'r')
x=file.read()
file=open("f2.txt",'r')
y=file.read()

class Plagarism(object):
        def frequencies(self,word):
            self.word=word
            dict={}
            word=word.split()
            for ch in word:
                    if ch not in dict:
                            dict[ch]=word.count(ch)
            print(dict)		
            return dict
        def numerator(self,v,u):
          l=[]
          for i in v:
            for j in u:
              if i==j:
                 l.append(v[i]*u[j])
        #print(l)
          s=0
          for k in l:
            s=s+k
          return s   
        def denominator(self,v,u):
          s=0
          s1=0
          for i in v:
            s=s+v[i]**2
        #print(s)
          for j in u:
            s1=s1+u[j]**2
        #print(s1)
          de=math.sqrt(s)*math.sqrt(s1)
          return de

        def final(self,n,d):
            result=(n/d)*100
            return result
        
p=Plagarism()
v=p.frequencies(x)
u=p.frequencies(y)
n=p.numerator(v,u)
d=p.denominator(v,u)
print(p.final(n,d))





  



    
    
    
           






