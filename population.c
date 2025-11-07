#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("Enter starting population size: ");
    }
        while (start < 9);


    // TODO: Prompt for end size
 int end;
    do
    {
        end = get_int("Enter end population size: ");
    }
        while ( end < start);

    // TODO: Calculate number of years until we reach threshold
    int numy;
    numy = 0;
    do {
        end + (end/3) - (end/4);
        numy + 1;
    }
        while (end < start)
    // TODO: Print number of years
printf ("Years: %d", numy);

}
