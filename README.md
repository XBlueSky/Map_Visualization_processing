# Map_Visualization_processing

> Before using this raw data, we have to do some processing with this huge unoptimized data.

## Structure

    Map_Visualization_processing/
        ├── merge/              # merge action file
        ├── split/              # count and classify action file
        ├── mongoImports/       # import to mongodb action file
        └── README.md           

## Flow_Chart 
![Flow Chart](/img/Flow_Chart.png)

### Merge

- #### Directory Structure

        merge/
            ├── merge.sh   
            └── split.py

- #### Command

    ```console
    sh merge.sh
    ```
    
- #### Description

        At first, this file(merge.sh) would zcat file and only get ID, start_time, end_time, latitude, longitude to reduce data.
        
        After previous step it will automatically run merge.py that is using the same location in continuous time to merge data by identical ID. 
        In this step, all of data we want must be lossless and reduced.
    
### Split

- #### Directory Structure

        split/
            ├── split.sh  
            ├── count.py     
            ├── countByTenMin.py   
            ├── districtTW.csv
            ├── KDpreson.py   
            └── personByDistrict.py

- #### Command

    ```console
    sh split.sh
    ```
    
- #### Description

        At first, this file(split.sh) would call two part process to deal with data.
        
        One is for population moving, so it would call for count.py(by hour) and countByTenMin.py(by ten minutes) to count the population in each location.
        
        Another is for resolving the problem that data is too big to visualize on web.
        So In the beginning we build KD-tree from districtTW.csv by KDpreson.py.
        And the we run personByDistrict.py to classify people by district and finally output json file format that can be imported to database.
        
### Mongo_Import

- #### Directory Structure

        MongoImport/
            ├── mongoImport.sh   
            └── personImport.py

- #### Command

    ```console
    sh mongoImport.sh  | sh personImport.sh
    ```
    
- #### Description

        When all data are done, the final step is import data to your database. 
        
        Because of this step is different from person to person.
        This import section is reference for you to make you quickly write your own shell script.
        
        