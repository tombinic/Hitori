<h1 align="center">
Hitori</h1>
<h3 align="center"> Computer, Electronic and Telecommunications Engineering </h3>
<h5 align="center"> Project Assignment - Fundamentals Of Computer Science - <a href="https://www.unipr.it">University of Parma</a> (December 2019) </h5>
</hr>
  <h2 id="table-of-contents"> :book: Table of Contents</h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#intro"> ➤ Intro</a></li>
    <li><a href="#rules"> ➤ Rules</a></li>
    <li><a href="#solve"> ➤ Solving techniques</a></li>
    <li><a href="#preview"> ➤ Preview</a></li>
  </ol>
</details>
<h2 id="intro"> :bomb: Intro</h2>
Hitori is a logic puzzle that originated in Japan. The name “hitori” means “Alone” or “One person” (ひとりにしてくれ Hitori ni shite kure, literally "leave me alone") and the puzzle involves eliminating numbers from a grid so that no number appears more than once in any row or column.
<br/>


At the beginning of the puzzle, some numbers are already filled in, and the solver must use logic and deduction to determine which numbers to eliminate. The solved puzzle will have all remaining numbers arranged so that there are no duplicates in any row or column.

Hitori puzzles typically come in different sizes and difficulty levels, and they are often found in puzzle books or online puzzle websites.

<h2 id="rules"> :pencil: Rules</h2>
Hitori is played with a grid of squares or cells, with each cell initially containing a number. The game is played by eliminating squares/numbers and this is done by blacking them out. The objective is to transform the grid to a state wherein all three following rules are true:

* no row or column can have more than one occurrence of any given number
* black cells cannot be horizontally or vertically adjacent, although they can be diagonal to one another.
* the remaining numbered cells must be all connected to each other, horizontally or vertically.

<h2 id="solve"> :triangular_ruler: Solving techniques</h2>

* Once it is determined that a cell cannot be black, some players find it useful to circle the number, as it makes the puzzle easier to read as the solution progresses. Below we assume that this convention is followed.

* When it is determined that a cell must be black, all orthogonally adjacent cells cannot be black and so can be circled.

* If a cell has been circled to show that it cannot be black, any cells containing the same number in that row and column must be black.

* If blacking out a cell would cause a connected non-black area to become separated into several unconnected components, the cell cannot be black and so can be circled.

* In a sequence of three identical, adjacent numbers, the centre number cannot be black and the cells on either side must be black. The reason is that if one of the end numbers remains non-black this would result in either two adjacent black cells or two cells with the same number in the same row or column, neither of which are allowed. (This is a special case of the next item.)

* In case of two identical, adjacent numbers, if another cell occurs in the same row or column containing the same number, the latter cell must be black. Otherwise, if it remains non-black, this would result in either two cells with the same number in the same row or column, or two adjacent black cells, neither of which are allowed.

* Any number that has two identical numbers on opposite sides of itself cannot be black, because one of the two identical numbers must be black, and it cannot be adjacent to another black cell.

* When two pairs of identical numbers are in a two by two square on the grid, two of them must be black along a diagonal. There are only two possible combinations, and it is sometimes possible to decide which is correct by determining if one variation will cut non-black squares off from the remainder of the grid.

* When two pairs of identical numbers form a square in the corner of a grid, the corner square and the one diagonally opposite must be black. The alternative would leave the corner square isolated from the other non-black numbers.

<h2 id="preview"> :technologist: Preview</h2>
To run the script simply run the <b>main.py</b> with the command <b>python main.py</b> .
<br />
<br />

| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|<img src="preview/1.png " alt="Network Image"> |  <img src="preview/2.png" alt="Network Image"> |<img src="preview/3.png" alt="Network Image">|
