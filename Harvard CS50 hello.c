// This was my first lab assignment from the Harvard CS50 course and helped me to also  understand using Git Hub
// This program outputs the phrase hello and the entered name variable
// This program is written in c

#include <cs50.h>
#include <stdio.h>

int main(void)

{
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}
