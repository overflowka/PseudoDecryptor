#include <iostream>
typedef char _BYTE;

int main(void)
{
    int v297[13];
    int v51 = 0;

    v297[0] = -2096525854;
    v297[1] = -2028764687;
    v297[2] = -1154710047;
    v297[3] = -1077429967;
    v297[4] = -1289175762;
    v297[5] = -1222594269;
    v297[6] = -1412713175;
    v297[7] = -1355306692;
    v297[8] = -1557091009;
    v297[9] = -1489985072;
    v297[10] = -608328393;
    v297[11] = -548808259;
    v297[12] = -741155509;

    char buffer[1337];
    buffer[0] = '\0';

    for (int i = 0; i < sizeof(v297); ++i)
    {
        *((_BYTE *)v297 + v51) += v51 + 22 + 2 * (51 - (*((_BYTE *)v297 + v51) & (v51 + 22)));
        ++v51;
    }

    for (int i = 0; i < sizeof(v297); ++i)
    {
        char temp[2];
        sprintf_s(temp, "%c", *((char*)v297 + i));
        strcat_s(buffer, temp);
    }

    printf("%s", buffer);
    return 0;
}