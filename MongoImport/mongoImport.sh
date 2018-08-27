#!/bin/bash

echo "============== + start + ============== + Count + ==============";
for countFile in C*
do
    echo "start ====> $countFile";
    mongoimport --db map --collection count  --file $countFile
    echo "start ====> $countFile ====> end";
done
echo "============== +  end  + ============== + Count + ==============";
echo "============== + start + ============== + Person + ==============";
for personFile in P*
do
    echo "start ====> $personFile";
    mongoimport --db map --collection person  --file $personFile --jsonArray
    echo "start ====> $personFile ====> end";
done
echo "============== +  end  + ============== + Person + ==============";