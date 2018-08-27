#!/bin/bash

for file in 2*
do
    echo "============= + start + ============= + $file + =============";
    echo "count $file";
    # Will output json file containing population counting data
    # And it will generate a file prefix is "C".
    python count.py $file
    echo "count $file ----> Sucess";

    echo "KDtree map person to district for $file";
    # Will output table file containing every person mapping to corresponding district
    # And it will generate a file prefix is "T".
    python KDperson.py $file
    echo "map $file ----> Sucess";

    echo "map $file ----> Sucess ----> allocate $file";
    # Will output json file containing person information with time and location classified by district
    # And it will generate a file named itemKey+'d'+args.file.json.
    python personByDistrict.py $file -t T$file
    echo "map $file ----> Sucess ----> allocate $file ----> Sucess";

    rm $file
    rm T$file
    echo "============= +  end  + ============= + $file + =============";
done

# cd ..
# zip -r $1.zip $1/
# docker cp Person.json {containerID ex.795b39863127}:/openmap/