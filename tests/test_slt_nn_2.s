#eyIwIjogMTAwNjk2MDYzOSwgIjEiOiA4ODExMzE1MTksICIyIjogMTAwNzAyNjE3NSwgIjMiOiA4ODMyOTQyMDYsICI0IjogMTA3NTIwNDJ9

# DO NOT DELETE THE ABOVE BASE64 LINE. IT IS USED TO LOAD INSTRUCTIONS

.text

main:
    lui $a0, -1 
    ori $a0, $a0, -1 
    lui $a1, -1
    ori $a1, $a1, -2
    slt $v0, $a1, $a0