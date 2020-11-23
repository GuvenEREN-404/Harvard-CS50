#include <stdio.h>

#include <cs50.h>
#include <string.h>

int main(void)
{
 
 int sonrakam,sonuc=0;
 int grsayi=get_int("sayı gir");
while(grsayi>0){
  for(int i=0,n=strlen(grsayi); i<n; i++)
  {
   
   sonrakam=grsayi%10;
   int dizi[i]=sonrakam;
   sonrakam=grsayi/10;
   
  }
  printf("%d",dizi);
}
}
