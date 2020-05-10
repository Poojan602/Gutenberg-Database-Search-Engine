# WebApp-using-docker-on-AWS
WebApplication to search books by author name or book name deployment in docker container on AWS EC2 instance

![Architecture](https://github.com/Poojan602/WebApp-using-docker-on-AWS/blob/master/Screen%20shots/Architecture.png)

## Architecture Explanation

- As show in the above image, user can perform 3 operations: search, note submission, and note retrieval.
- User can search by book name or author name through hosted webapplication.

## Search
- With the help of microservices, the search will be performed. 
- When user will search something, the searched keyword, time etc will be logged in log file which is text file.
- Catalog file keeps the record of searched keywords. So firstly, catalog file will be checked by the microservice. If the searched keyword is found then the result will be returned from the catalog file which is stored in MongoDB.
- If any keyword is searched for the first time, it will not be present in catalog file. So microservice will search for that keyword in MongoDB database.
- And for successful search (if result found for searched keyword) result will be stored in catalog file and result will be returned to user on webpage.

## Note Submission and Note retrieval
- User will be able to submit note on successful search(if result found for searched keyword).
- At the same time user can retrieve all the notes submitted for that keyword
- Notes are stored in text file


# Process

## Data extraction

- For this project, Gutenburg data were used where book and author list were downloaded for the year 1996 to 2020. 
- From those text files, author name and book names were extracted,cleaned and inserted into MongoDB database using python script named Scraping/scraping.py.

## Microservice

- Microservices were created for Log, Catalog, MainAPI and Notes and were dockerised using flask in python
- Microservices can be found in Containers folder
- All the interactions are made through Main API
- All the Dockerised microservices were deployed on AWS ec2 instance

## Webpage

- Webpage was created using standard HTML, CSS, and Bootstrap
- Backend for the webpage was also created in python flask which was responsible to call the microservice.
- Both Frontend and Backend code can be found under the folder Website

## Testing

- Testing for API were done using python unittest library
- Testing files can be found under the folder name Testing
- Though all the validations were taken into account, frontend testing was done manually. 






