#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("whats your name\n");
    printf("hello, %s\n",name );
    
    int i =get_int("How old are you: ");
    printf("Age:, %i\n",i);

    float f =get_float("Float: ");
    printf("hello ,%f\n",f) ;
}
