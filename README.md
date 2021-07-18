# cellSorter
python program to sort battery Cells into pairs, then into groups

### Introduction

As part of the Solar Ute project, the conversion of a diesel Bravo ute to Battery Electric.  300 30Ah LTO (Lithium Titanate) cells were purchased which are to be configured into a string of 150 by 2 paralled cells.  My BMS monitor-balancing (Active) boards will connect to 12  cells each.

### Why I Match

So the question is how to best select which cells to pair up and to how best to group the batteries for the balancing boards.

I have the Ah data for each cell, which ranged from 30Ah to 35.xAh.  
If we just randomly paired each cell up we would get a possible range of 10Ah in a average 65Ah pair.  This would lead to some inbalance when charging the battery.

Using this program I acheived a Standard Deviation of only 435mAh in the 65Ah pairs.

### Why I Group

I am being indulgent, implementing a form of active balancing in my 12 cell BMS balancing boards.
The energy is distributed amongst the 12 cells (and the first cell of the next board) - so it is useful if the distrubution of pairs are somewhat uniform for each balancer.

The result is pleasing.  The variation of the Average Paired Ah from one group to another was only 100mAh with many being within 10mAh.


![300 LTO Cells](https://github.com/mackelec/cellSorter/blob/main/P1080219.jpg)


### Brute Force won't work

I quickly realized that brute force algoithm will not work

Npairings = n! / (m!*2^m)

where n=300 and m=150

This results in a very large number of iterations !!!

### Method

##### Match Pairs
I used a simple method of pairing the cells.  I matched the smallest cell with the largest Cell, then the next and so on.  It's not perfect but it's very close.

##### Grouping 
This is a little bit more interesting.  I calculate the Standard Deviation of each pair, sort the pairs from highest to lowest SD.  I then in a serpintine pattern, sequentially allocated the pair to each group, thus getting a some what approximate spread of pairs into each group.  Again not perfect - but pretty close.

### Why python

Why not :-)
Well, I proved it in Open office Calc first, but this proved to be a lot of work for each group.

I have never written a program in Python before so I thought this was an ideal little project.   I still prefer C but Python presented no problem and I enjoyed useing the light-weight IDE.


