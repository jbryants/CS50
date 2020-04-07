# import cs50

def main():
    while True:
        # cc_number = get_int("Number: ")
        cc_number = int(input("Number: "))
        if (cc_number > 0):
            break

    checkCC(cc_number)


def checkCC(cc_number):
    # int odds, evens, sum1, sum2, cc_length, tsum, r, no1, no2;
    odds = evens = sum1 = sum2 = cc_length = 0

    while (cc_number > 0):
        evens = cc_number % 10
        no1 = evens
        sum2 += evens
        cc_length += 1
        cc_number = cc_number // 10

        if (cc_number > 0):
            odds = cc_number % 10
            no2 = odds
            odds *= 2
            if (odds > 9):
                r = odds % 10
                odds = odds // 10
                odds += r

            sum1 += odds
            cc_length += 1
            cc_number = cc_number // 10

    tsum = sum1 + sum2

    if (cc_length % 2 == 0):
        no1 += no2
        no2 = no1 - no2
        no1 -= no2

    if (tsum % 10 == 0):
        if ((cc_length == 15) and (no1 == 3) and ((no2 == 4) or (no2 == 7))):
            print("AMEX")
        elif ((cc_length == 16) and (no1 == 5) and ((no2 == 1) or (no2 == 2) or (no2 == 3) or (no2 == 4) or (no2 == 5))):
            print("MASTERCARD")
        elif (((cc_length == 13) or (cc_length == 16)) and (no1 == 4)):
            print("VISA")
        elif cc_length == 16:
            print("MASTERCARD")
    else:
        print("INVALID")

if __name__ == '__main__':
    main()


'''
#include<stdio.h>
#include<cs50.h>

int checkCC(long long int cc_number);

int main(void)
{
    long long int cc_number;

    do
    {
        cc_number = get_long_long("Number: ");
    }
    while (cc_number < 0);

    checkCC(cc_number);

    return 0;
}

int checkCC(long long int cc_number)
{

    int odds, evens, sum1, sum2, cc_length, tsum, r, no1, no2;
    odds = evens = sum1 = sum2 = cc_length = 0;

    while (cc_number > 0)
    {

        evens = cc_number % 10;
        no1 = evens;
        sum2 = sum2 + evens;
        cc_length++;
        cc_number = cc_number / 10;

        if (cc_number > 0)
        {
            odds = cc_number % 10;
            no2 = odds;
            odds = odds * 2;
            if (odds > 9)
            {
                r = odds % 10;
                odds = odds / 10;
                odds = odds + r;
            }
            sum1 = sum1 + odds;
            cc_length++;
            cc_number = cc_number / 10;
        }
    }

    tsum = sum1 + sum2;

    if (cc_length % 2 == 0)
    {
        no1 = no1 + no2;
        no2 = no1 - no2;
        no1 = no1 - no2;
    }

    if (tsum % 10 == 0)
    {
        if ((cc_length == 15) && (no1 == 3) && ((no2 == 4) || (no2 == 7)))
        {
            printf("AMEX\n");
        }
        else if ((cc_length == 16) && (no1 == 5) && ((no2 == 1) || (no2 == 2) || (no2 == 3) || (no2 == 4) || (no2 == 5)))
        {
            printf("MASTERCARD\n");
        }
        else if (((cc_length == 13) || (cc_length == 16)) && (no1 == 4))
        {
            printf("VISA\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}
'''