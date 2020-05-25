#eyIwIjogODc0MzgxMzExLCAiMSI6IDMyODA0LCAiMiI6IDg3MzUyOTM0NSwgIjMiOiA5MDYyMzE4MDgsICI0IjogOTA4Mzk0NDk2LCAiNSI6IDg3MjgwODQ2NCwgIjYiOiAxMDA3MjIyNzgzLCAiNyI6IDg4OTc4MjI2OSwgIjgiOiA2MTQwMTEyMCwgIjkiOiAyOTQ3NTQ3MTM2LCAiMTAiOiAyOTQ3NjEyNjczLCAiMTEiOiAyOTQ3Njc4MjEwLCAiMTIiOiA4ODE4NTI0MTYsICIxMyI6IDg4NDAxNTEwNCwgIjE0IjogNTUwNjk5MDA3LCAiMTUiOiAxMTk4MTIyLCAiMTYiOiAyODczMDk4NDMsICIxNyI6IDkwNjIzMTgwOCwgIjE4IjogOTA4Mzk0NDk2LCAiMTkiOiAyNjg0MzU0NjAsICIyMCI6IDkwOTExNTM5MiwgIjIxIjogODc3NzIzNjQ4LCAiMjIiOiA1NzU4NjQ4MzEsICIyMyI6IDI2ODUwMDk4MywgIjI0IjogMTAwNzIyMjc4MywgIjI1IjogODg5NzgyMjcwLCAiMjYiOiA2MTQwMTEyMCwgIjI3IjogMjk0NzU0NzEzNiwgIjI4IjogMjk0NzYxMjY3MywgIjI5IjogODgxODUyNDE2LCAiMzAiOiA4ODQwMTUxMDQsICIzMSI6IDM0NjcyNjcyLCAiMzIiOiAyNDEwNjc2MjI0LCAiMzMiOiAyNDEwNzQxNzYxLCAiMzQiOiA1OTk1ODg4NjYsICIzNSI6IDI2ODUwMDk3NiwgIjM2IjogOTA4MTk3ODg4LCAiMzciOiAyNDEwNjc2MjI0LCAiMzgiOiAyNDEwNzQxNzYxLCAiMzkiOiAyNDEwODA3Mjk4LCAiNDAiOiA1OTk1ODg4NjcsICI0MSI6IDg5NDA1MjUzMSwgIjQyIjogMjY4NTAwOTkwfQ==

# DO NOT DELETE THE ABOVE BASE64 LINE. IT IS USED TO LOAD INSTRUCTIONS

.text

main:
    ori $sp, $zero, -1
    and $s0, $zero, $zero
    ori $s1, $zero, 1
    ori $a0, $s0, 0
    ori $a1, $s1, 0
    ori $a2, $zero, 16

fib:
    lui $t0, -1
    ori $t0, $t0, -3
    add $sp, $sp, $t0
    sw $s0, 0($sp)
    sw $s1, 1($sp)
    sw $s2, 2($sp)
    ori $s0, $a0, 0
    ori $s1, $a1, 0
    addi $s2, $a2, -1

loop:
    slt $t1, $zero, $s2
    beq $t1, $zero, exit
    ori $a0, $s0, 0
    ori $a1, $s1, 0
    beq $zero, $zero, addnums

ret:
    ori $s0, $s1, 0
    ori $s1, $v0, 0
    addi $s2, $s2, -1
    beq $zero, $zero, loop

addnums:
    lui $t0, -1
    ori $t0, $t0, -2
    add $sp, $sp, $t0
    sw $s0, 0($sp)
    sw $s1, 1($sp)
    ori $s0, $a0, 0
    ori $s1, $a1, 0
    add $v0, $s0, $s1
    lw $s0, 0($sp)
    lw $s1, 1($sp)
    addi $sp, $sp, 2
    beq $zero, $zero, ret
    
exit:
    ori $v0, $s1, 0
    lw $s0, 0($sp)
    lw $s1, 1($sp)
    lw $s2, 2($sp)
    addi $sp, $sp, 3

trap:
    ori $t2, $t2, 10419
    beq $zero, $zero, trap