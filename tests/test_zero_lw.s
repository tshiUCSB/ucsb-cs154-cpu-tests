#eyIwIjogNTQ1NTIxOTE4LCAiMSI6IDI4OTQzMzE5MDgsICIyIjogMjM1NzE5ODg1MiwgIjMiOiA0MTI4fQ==

# DO NOT DELETE THE ABOVE BASE64 LINE. IT IS USED TO LOAD INSTRUCTIONS

.text

main:
    addi $a0, $a0, 254
    sw $a0, 4($a0)
    lw $zero, 4($a0)
    add $v0, $zero, $zero