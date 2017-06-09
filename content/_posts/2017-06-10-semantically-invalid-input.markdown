Title: Semantically Invalid Input
Headline: with Sudoku examples
date: 2017-06-10 22:00
comments: true
Tags: QA, fedora.planet
og_image: images/sudoku_invalid.jpg
twitter_image: images/sudoku_invalid.jpg

    :::python Unsolvable Square example
    . . 9 | . 2 8 | 7 . .
    8 . 6 | . . 4 | . . 5
    . . 3 | . . . | . . 4
    ------+-------+------
    6 . . | . . . | . . .
    ? 2 . | 7 1 3 | 4 5 .
    . . . | . . . | . . 2
    ------+-------+------
    3 . . | . . . | 5 . .
    9 . . | 4 . . | 8 . 7
    . . 1 | 2 5 . | 3 . .


In a comment to a
[previous post]({filename}2016-04-16-hiring-qa-sudoku.markdown)
*Flavio Poletti* proposed a very interesting test case for a function which solves
the Sudoku game - *semantically invalid input, i.e. an input that passes intermediate
validation checks (no duplicates in any row/col/9-square) but that cannot possibly
have a solution*.


Until then I thought that Sudoku was a completely deterministic game and if input
followed all validation checks then we always have a solution. Apparently I was wrong!
Reading more on the topic I discovered these
[Sudoku test cases from Sudopedia](http://sudopedia.enjoysudoku.com/Test_Cases.html).
Their [Invalid Test Cases](http://sudopedia.enjoysudoku.com/Invalid_Test_Cases.html)
section lists several examples of semantically invalid input in Sudoku:

* Unsolvable Square;
* Unsolvable Box;
* Unsolvable Column;
* Unsolvable Row;
* Not Unique with examples having 2, 3, 4, 10 and 125 solutions

The example above cannot be solved because the left-most
square of the middle row (r5c1) has no possible candidates.


Following the rule *non-repeating numbers from 1 to 9 in each row* for row 5 we're
left with numbers: 6, 8 and 9. For (r5c1) 6 is a no-go because it is already present
in the same square. Then 9 is a no-go because it is present in column 1. Which leaves
us with 8, which is also present in column 1! Pretty awesome, isn't it?

Also check the
[Valid Test Cases](http://sudopedia.enjoysudoku.com/Valid_Test_Cases.html) section
which includes other interesting examples and definitely not ones which I have considered
previously when [testing Sudoku]({filename}2016-04-16-hiring-qa-sudoku.markdown).


On a more practical note I have been trying to remember a case from my QA practice
where we had input data that matched all conditions but is semantically invalid. I
can't remember of such a case. If you do have examples about semantically invalid
data in real software please let me know in the comments below!


Thanks for reading and happy testing!
