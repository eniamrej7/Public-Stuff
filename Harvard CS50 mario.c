#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int a;
    do
    {
        a = get_int("Height: ");
    }
    while (a < 1 || a > 8);

    for (int b = 0; b < a; b++)
    {
        for (int c = 0; c < a - b - 1; c++)
        {
            printf(" ");
        }
        for (int d = 0; d <= b; d++)
        {
            printf("#");
        }
        printf("\n");
    }
}
/*One variable for X and new line
One Variable for spacing out the Xs based on int x

Do Print Ys (space), then Print Xs (#), and while they are more than 0.*/

/*printf #
Printf # printf #



*/
