#include<stdio.h>
#include<math.h>
#include <unistd.h>

void teste()
{
	printf("Ola LPD");
}

double mytan(double x, double y){
    return (sqrt(y/x));
}

int is_valid_ip(const char *ip_str)
{
	unsigned int n1,n2,n3,n4;

	if(sscanf(ip_str,"%u.%u.%u.%u", &n1, &n2, &n3, &n4) != 4) {
		return 0;
	}

	if((n1 != 0) && (n1 <= 255) && (n2 <= 255) && (n3 <= 255) && (n4 <= 255)) {
		char buf[64];
		sprintf(buf,"%u.%u.%u.%u",n1,n2,n3,n4);
		if(strcmp(buf,ip_str)){ 
			return 0;
		}
		else{
			return 1;
		}
	}
	return 0;
}