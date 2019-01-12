// Helper functions for music

#include <cs50.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int numer = atoi(&fraction[0]);
    int denom = atoi(&fraction[2]);

    int frac = (8/denom) * numer;
    return frac;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    double octave = 0.0;

    //check for accidentals; n is number of semitones
    double n = 0.0;

    //if length of the note is 3 for example: A#4
    if (strlen(note) == 3)
    {
        octave = atof(&note[2]);

        //if 2nd character is sharp '#' semitone increase by 1
        if (note[1] == '#')
        {
            n = n + 1.0;
        }
        //if 2nd character is flat 'b' semitone decrease by 1
        else if (note[1] == 'b')
        {
            n = n - 1.0;
        }
    }
    //if length of the note is 2 for example: A4
    else if (strlen(note) == 2)
    {
        octave = atof(&note[1]);
    }
    //finding semitones for all the notes away from 'A'
    switch (note[0])
    {
        case 'C':
            n = n - 9.0;
            break;
        case 'D':
            n = n - 7.0;
            break;
        case 'E':
            n = n - 5.0;
            break;
        case 'F':
            n = n - 4.0;
            break;
        case 'G':
            n = n - 2.0;
            break;
        case 'A':
            break;
        case 'B':
            n = n + 2.0;
            break;
        default :
            return 0.0;
    }
    //calculating octave
    n += (octave - 4.0) * 12.0;

    //finding frequency for notes C, D, E, F, G, A, B using 'n'
    double freq = 0.0;
    freq = 440.0 * (pow(2.0, (n / 12.0)));
    return round(freq);
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (strcmp(s, ""))
    {
        return false;
    }
    else
    {
        return true;
    }
}
