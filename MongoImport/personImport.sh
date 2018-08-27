#!/bin/bash

echo "====== + start + ======";
for ((i=1; i<13; i++));
do
    cd $i
    echo "start ====> $i";
    for file in *
    do
        mongoimport --db map --collection D$i  --file $file --jsonArray
    done
    cd ..
    echo "start ====> $i ====> end";
done
echo "====== +  end  + ======";