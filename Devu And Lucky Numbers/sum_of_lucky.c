#include<stdio.h>

#define IN_TABLE 99
#define min(a,b) (a < b? a : b)
unsigned long table_of_10s[] = {0, 1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 111111104, 111111034, 111110334, 111103334, 111033334, 110333334, 103333334, 33333334, 333333341, 333333390, 333333880, 333338780, 333387780, 333877780, 338777780, 387777780, 877777780, 777777745, 777777402, 777773972, 777739672, 777396672, 773966672, 739666672, 396666672, 966666700, 666666938, 666669339, 666693349, 666933449, 669334449, 693344449, 933444449, 334444428, 344444260, 444442580, 444425773, 444257703, 442577003, 425770003, 257700003, 577000017, 770000136, 700001312, 13072, 130721, 1307211, 13072111, 130721111, 307211104, 72111020, 721110201, 211101962, 111019607, 110196064, 101960634, 19606334, 196063341, 960633404, 606333978, 63339739, 633397391, 333973869, 339738670, 397386680, 973866780, 738667738, 386677332, 866773300, 667732945, 677329409, 773294049, 732940442, 329404372, 294043700, 940436987, 404369808, 43698053, 436980531, 369805283, 698052810, 980528059, 805280528, 52805225, 528052251, 280522476, 805224747, 52247415, 522474151, 224741476};

unsigned long mod_value = 1000000007;

unsigned long count_choices(unsigned int x, unsigned int y, unsigned int z, unsigned int k)
{
	if(k == 0)
		return 1;
	if( x==0 && y==0 && z==0)
		return 0;
	x = min(x,k);
	y = min(y,k);
	z = min(z,k);
	unsigned long count = 0;
	if(x > 0)
		count += count_choices(x-1,y,z,k-1);
	if(y > 0)
		count += count_choices(x,y-1,z,k-1);
	if(z > 0)
		count += count_choices(x,y,z-1,k-1);
	return count % mod_value;
}

int main()
{
	unsigned int x, y, z, max_digits, num_digits;
	unsigned long sum_value;
	scanf("%u %u %u", &x, &y, &z);
	max_digits = x + y + z;
	sum_value = 0;
	for(num_digits=1; num_digits < max_digits+1; num_digits ++)
	{
		//if(num_digits not in table_of_10s:
		//	table_of_10s[num_digits] = (table_of_10s[num_digits-1]*10 + 1) % mod_value
		if(x > 0)
			sum_value = (sum_value + 4*(table_of_10s[num_digits])*count_choices(x-1,y,z,num_digits-1)) % mod_value;
		if(y > 0)
			sum_value = (sum_value + 5*(table_of_10s[num_digits])*count_choices(x,y-1,z,num_digits-1)) % mod_value;
		if(z > 0)
			sum_value = (sum_value + 6*(table_of_10s[num_digits])*count_choices(x,y,z-1,num_digits-1)) % mod_value;
	}
	printf("%u\n", sum_value);
	return 0;
}