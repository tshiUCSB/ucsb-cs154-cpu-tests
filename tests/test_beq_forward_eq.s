#eyIwIjogODcyNjc3Mzc3LCAiMSI6IDI2ODQzNTQ1NywgIjIiOiA4NzI2NzczNzgsICIzIjogODcyNzQyOTE0LCAiNCI6IDI2ODUwMDk5MH0=

# DO NOT DELETE THE ABOVE BASE64 LINE. IT IS USED TO LOAD INSTRUCTIONS

.text

main:
    ori $a0, $zero, 1
    beq $zero, $zero, skip
    ori $a0, $zero, 2

skip:
    ori $a1, $zero, 2
    beq $zero, $zero, skip