#!/bin/bash

echo -n "input : "
read semester

declare -a IPSmhs
i=0
let jumlah=$semester-1

    while [ $i -le $jumlah ];
    do
        let score=$i+1
        printf " " $score;
        read scoreIPS;
        IPSmhs[$i]=$scoreIPS;
        let total=total+$scoreIPS;
        let i=$i+1;
done

let IPK=$total/$semester
echo "IPS mhs = " $total "/" $semester
echo "IPK mhs = " $IPK
