#include <pigpio.h>
#include <unistd.h>
#include "ssd.h"

void SSD::display()
{
    int i, j, k = 0;
    for (k = 0; k < 10; k++)
    {
        for (i = 0; i < 10; i++)
        {

            for (j = 0; j < 7; j++)
            {
                gpioWrite(SSD_PORT_2[j], ((numbers_array[k] >> j) & 1));

                gpioWrite(SSD_PORT_1[j], ((numbers_array[i] >> j) & 1));
            }

            usleep(500000);

        }

    }

}

SSD::SSD()
{

}
void SSD::initPins()
{
    int i;
    for (i = 0; i < 7; i++)
    {
        gpioSetMode(SSD_PORT_1[i], PI_OUTPUT);
        gpioSetMode(SSD_PORT_2[i], PI_OUTPUT);

    }
}