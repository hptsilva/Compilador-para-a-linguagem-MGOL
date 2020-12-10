#include <stdio.h>
#include <stdlib.h>

typedef char literal[256];
void main()
{
	literal A;
	int B;
	int D;
	float C;



	printf("Digite B:");
	scanf("%d", &B);
	printf("Digite A:");
	scanf("%s", &A);
	int T0 = B > 2;
	if(T0)
	{
	int T1 = B <= 4;
	if(T1)
	{
	printf("B esta entre 2 e 4");
	}
	}
	int T2 = B + 1;
	B = T2;
	int T3 = B + 2;
	B = T3;
	int T4 = B + 3;
	B = T4;
	D = B;
	C = 5.0;
	printf("\nB=\n");
	printf("%d", D);
	printf("\n");
	printf("%lf", C);
	printf("\n");
	printf("%s", A);
	system("PAUSE");
}