// Helper functions for music

#include <cs50.h>
#include <math.h>
#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    switch (fraction[2])
    {
        case (50):
            return (fraction[0] - '0') * 4;
            break;
        case (52):
            return (fraction[0] - '0') * 2;
            break;
        case (56):
            return (fraction[0] - '0');
            break;
        default:
            return 0;
    }
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    double multiplier = 0;
    // note
    switch (note[0])
    {
        case (65):
            multiplier = 0;
            break;
        case (66):
            multiplier = 2;
            break;
        case (67):
            multiplier = -9;
            break;
        case (68):
            multiplier = -7;
            break;
        case (69):
            multiplier = -5;
            break;
        case (70):
            multiplier = -4;
            break;
        case (71):
            multiplier = -2;
            break;
        default:
            break;
    }


    // accidentals
    // set octave to second letter in string
    int octave = note[1];
    // look for accidentals in second letter of string
    if (note[1] == 'b')
    {
        multiplier -= 1;
        // if you find an accidental, the octave must be the third letter
        octave = note[2];
    }
    else if (note[1] == '#')
    {
        multiplier += 1;
        // if you find an accidental, the octave must be the third letter
        octave = note[2];
    }

    // octave
    if (octave != 52)
    {
        multiplier += 12 * (octave - '0' - 4);
    }

    // return
    double finalfreq = 440 * pow(2, multiplier / 12);
    return round(finalfreq);
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (s[0] == '\0')
    {
        return true;
    }
    else
    {
        return false;
    }
}
