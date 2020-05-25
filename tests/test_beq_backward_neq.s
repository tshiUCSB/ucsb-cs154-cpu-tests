#eyIwIjogODcyNjc3NjMwLCAiMSI6IDI2ODc2MzEzNCwgIjIiOiA4NzI2Nzc1OTAsICIzIjogMjY4NTAwOTkwfQ==

# DO NOT DELETE THE ABOVE BASE64 LINE. IT IS USED TO LOAD INSTRUCTIONS

.text

main:
    ori $a0, $zero, 254
    beq $zero, $a0, main

exit:
    ori $a0, $zero, 214
    beq $zero, $zero, exit