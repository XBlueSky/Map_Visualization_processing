#!/bin/bash

cd /data/$1

# you can define what data prefix
prefix=LSR

for file in $prefix*
do
    echo "============== + start + ============== + ${file} + ==============";
    # change filename ex. LSR_20180630.csv.gz to LSR_20180630 
    name=$(echo $file | cut -d"." -f 1)
    
    echo "zcat ${file}"
    # zcat file.gz to ~/testlog/output and only get ID, start_time, end_time, latitude, longitude.
    cd /data/$1
    zcat ${file} | awk '{split($0,item,","); split(item[4],start," "); split(item[5],end," "); print item[1], start[2], end[2], item[6], item[7] }' > ~/testlog/LSR_$1/${name}
    echo "zcat ${file} ----> Sucess"
    
    cd ~/testlog/LSR_$1/
    echo "zcat ${file} ----> Sucess ----> merge $name"

    # use the same location in continuous time to merge data by identical ID. 
    # And it will generate a file named output.
    python merge.py $name
    echo "zcat ${file} ----> Sucess ----> merge $name ---->> Sucess"

    rm $name
    echo "============== +  end  + ============== + ${file} + ==============";
done

# zip -r $1.zip $1/