# Programming Assignment 02 from Universitas Indonesia [KI]

For future references and education purposes only.
Use wisely.

# Task Description
Write a Python program that can also be run outside of IDE (Spyder, IDLE, etc): by double-clicking on the program file icon or from the terminal (command prompt). The program draws two groups of colorful shapes. THe first group consists of 72 squares, varying in size, color and orientation. The second group consists of 36 disks, varying in size, color and positions.

The algorithm:
1. Your program has to interact with the user to ask for the side-length of the first square (an int), limited to between 20 and 60 (default 40). You can use the function numinput() from the turtle module.
2. Move the turtle some suitable distance to the left.
3. Draws 72 squares with random color. A square is rotated right 5 degrees relative to the previous square and its side-length is incremented by 2 units relative to the side-length of the previous square.
4. Move the turtle some suitable distance to the right.
5. Draws 36 disks (filled circles) with random colors. The radius of the first circle is one half of the sidelength of the last square. A circle position or orientation is rotated left 10 degrees relative to the previous circle and its radius is decremented by 2 units relative to the radius of the previous circle.
