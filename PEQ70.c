#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int totient(int n)
{
    int result = n;
    int flag;
    int is_even = 0;

    while(n%2==0)
    {
        n = n/2;
        is_even = 1;
    }

    if (is_even==1)
    {
        result = result/2;
    }

    for(int i=3; i <= sqrt(n);i+=2)
    {
        flag = 0;
        while (n%i==0)
        {
            n = n/i;
            flag = 1;
        }
        if (flag==1)
        {
            result = (result * (i-1))/i;
        }
    }

    if (n > 2)
        result = (result * (n-1))/n;

    return result;
}

int is_permutation(int a, int b)
{
    int arr1[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int arr2[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    while (1)
    {
        arr1[a%10]++;
        a /= 10;
        arr2[b%10]++;
        b /= 10;

        if (a==0 || b==0)
            break;
    }

    for (int i = 0; i < 10; i++)
        if (arr1[i] != arr2[i])
            return 0;

    return 1;
}

void solve()
{
    long answer;
    double temp=3;
    double totient_value;
    for(long n=1000;n<pow(10,7);n++)
    {
        totient_value = totient(n);
        if ( n / (double) totient_value < temp)
        {
            if (is_permutation(n,totient_value)==1)
            {
                answer = n;
                temp = n/totient_value;
                printf("%ld %lf\n", answer,temp);
            }
        }
    }
}

int main()
{
    //printf("%d",totient(291));
    solve();
    return 0;
}
