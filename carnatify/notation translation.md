# Basic notation

## Individual notes
The notes are based on the Carnatic solfege system. We will specify the starting note to which the middle "sa" is mapped. Unless otherwise specified, by default assume it is middle C (C4) which is MIDI note 60.

Middle octave: sa, ri, ga, ma, pa, da, ni
Higher octave: Sa, Ri, Ga, Ma, Pa, Da, Ni
Lower octave: sA, rI, gA, mA, pA, dA, nI

## Time
Individual notes are one time unit. E.g. `Sa` is one time unit. `Sa Ri` is two time units. `Sa - Ri` is two time unites.

Parantheses indicate the time is halved within the parantheses. E.g. `(Sa Ri)` is one time unit. `(Sa Ri Sa Ri)` is two time units. `((Sa Ri Sa Ri))` is one time unit.

A comma ',' indicates either a silence of one note duration(when used at the beginning of a phrase) or extending the previous note by one unit of duration when used after a note without '-'

A semicolon ';' is similar but indicates 2 notes' duration
(Comma and semicolon are used in the existing conventions but whether they indicate a silence or extend the previous note has to be guessed from the context since there is no accepted convention for grouping notes into phrases.)

## Pitch modifiers
A '<' symbol increases the pitch of the note by a fraction of 81/80 and may be repeated for further increase.

A '>' symbol decreases the pitch of the note by a fraction of 80/81 and may be repeated for further decrease.


## Slides
Dash indicates that the notes have a stop (i.e. note off event) between them, e.g. `Sa - Ri` means Sa note on, Sa note off, Ri note on, then Ri note off. Lack of dash indicates a slide between notes without any note off event between them, e.g. `Sa Ri`.

A '/' or '\' increases the transit duration between two notes by .05 seconds. May be repeated to further increase the duration and thus provide slide or portamento or slur - a very important aspect of Carnatic Music. The transit time is taken off the subsequent note. This symbol is sometimes used in the existing convention for a slide but without any quantitative significance.

