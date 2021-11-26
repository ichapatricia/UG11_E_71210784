def huruf_tengah(kalimat): 
    bagi= len(kalimat)//2

    if(len(kalimat)%2==0) and ((len(kalimat)/2)%2==0): 
        return kalimat [(bagi)//2 : ((bagi)//2)*-1]
   
    elif(len(kalimat)%2==0) and ((len(kalimat)/2)%2!=0): 
        return kalimat[((bagi)//2) +1 : (((bagi)//2)+1)*-1]
  
    else: 
        return kalimat[(((bagi)+1)//2) : (((bagi)+1)//2)*-1]
kalimat =str(input("Masukan kata: "))
print("Huruf tengah pada kata", kalimat , "adalah", huruf_tengah(kalimat))
