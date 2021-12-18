## TLDR; how to run
- Clone/unzip repo.
- Run the command `docker-compose up -d` to bring up both the backend and the frontend.
- Open browser and open `http://localhost:8000/admin/` for the admin to create the words and defintions.
- Use default username and password of `admin` and `admin` to access the admin.
- Open `http://localhost:3000/` for the frontend application to start using the flashcard app.

### Some additional Details
- Backend built using Python, Django, PostgreSQL and docker.
- Docker spins up 3 containers - 1 app server, 1 db server and 1 frontend server
- Docker compose up takes care of running migrations to create the models, creating first superuser admin and starting the server.


#### Approach
1. Set up 3 docker containers as a database was required, 1 backend app with APIs to get and update the words for the flashcard app along with an admin to create words+definition and a frontend server for the user facing app.
2. Created the basic model for storing the words, definitions along with bin number, next available time and the incorrect counter to be the base of the application to serve the words for flashcards.
3. Created 2 APIViews using DRF - 1. To get a words which should show up for the flashcard app, 2. To update if the definition was right or wrong.
4. Added methods with logic to get next word, mark as correct and mark as wrong in the model and mapped it to the API.
5. Created a single page react app to use the get and put APIs to show the words and mark the definition as right or wrong. 
  
