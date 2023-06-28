import numpy as np

def calculate(list):
   calculations=0
   if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
   else:
      arr=[]
      arr=np.array(list)
      arr=arr.reshape(3,3)

      mean1 = arr.mean(axis=0).reshape(1, 3).tolist()
      mean2 = arr.mean(axis=1).reshape(1, 3).tolist()
      mean3 = arr.mean().tolist()
      mean = mean1 + mean2 + [mean3]

      var1=arr.var(axis=0).reshape(1,3).tolist()
      var2=arr.var(axis=1).reshape(1,3).tolist()
      var3=arr.var().tolist()
      variance=var1+var2+[var3]

      std1=arr.std(axis=0).reshape(1,3).tolist()
      std2=arr.std(axis=1).reshape(1,3).tolist()
      std3=arr.std().tolist()
      standard=std1+std2+[std3]

      maxi1=arr.max(axis=0).reshape(1,3).tolist()
      maxi2=arr.max(axis=1).reshape(1,3).tolist()
      maxi3=arr.max().tolist()
      maximum=maxi1+maxi2+[maxi3]

      mini1=arr.min(axis=0).reshape(1,3).tolist()
      mini2=arr.min(axis=1).reshape(1,3).tolist()
      mini3=arr.min().tolist()
      mini=mini1+mini2+[mini3]

      sum1=arr.sum(axis=0).reshape(1,3).tolist()
      sum2=arr.sum(axis=1).reshape(1,3).tolist()
      sum3=arr.sum().tolist()
      sum_all=sum1+sum2+[sum3]

   calculations={
         'mean':mean,
         'variance':variance,
         'standard deviation':standard,
         'max':maximum,
         'min':mini,
         'sum':sum_all
   }
   
   return calculations