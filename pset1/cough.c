#include <cs50.h>
#include <stdio.h>

int get_positive_int(string prompt);

void cough(int n)
{
    for(int i =0;i<3;i++)
    {
        printf("cough\n");
    }
   
}


int main (void)
{
    cough(3);

    int i=get_positive_int("Positive integer.\n");
    printf("%i\n",i);
}


int get_positive_int(string prompt)
{
    int n;
    do
    {
        n=get_int(prompt);
    }
    while(n<1);
    return n;
}
