#include <stdio.h>

int main()
{
	int arr[30] = {0, };
	int n, i = 0;
	
	for(i = 0; i < 28; i++)
	{
		scanf("%d", &n);
		arr[n] = 1;
	}
	for(i = 1; i <= 30; i++)
	{
		if(arr[i] != 1)
		{
			printf("%d\n", i);
		}
	}
}