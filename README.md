## Running project

1. Install [Docker](https://www.docker.com/)
2. Run `docker-compose up --build` in the source directory. Make
sure you have docker started. 
3. Frontend is at `http://localhost:80`
4. Backend is at `http://localhost:80/api/`

To generate qr code go to 
`http://localhost/api/generate_qr_code?data=YOUR_DATA_HERE`

## About the Project

1. Backend is in `backend` directory. It's using
    [FastAPI](https://fastapi.tiangolo.com/) as the web server.
    Only the `generate_qr_code` endpoint is implemented. Implement 
    the decode endpoint yourself. 
2. Frontend is in `frontend` directory. It's using 
    [React](https://reactjs.org/) as the frontend framework.
    I have not made the frontend for you. Implement it yourself.
    It exists just for the sake of hosting. 
3. Nginx is used as the reverse proxy. Look up what a reverse proxy is. 
   Read more about nginx [here](https://www.nginx.com/resources/wiki/).
4. Docker is used to containerize the project. You can then build the
   docker images and host it yourself on public or private cloud. 

## To host on public cloud (like AWS)

1. Build backend docker image
    ```bash
    cd backend
    docker build -t qr-coder-backend .
    ```
2. Build frontend docker image
    ```bash
    cd frontend
    docker build -t qr-coder-frontend .
    ```
3. Build the nginx docker image
    ```bash
    cd nginx
    docker build -t qr-coder-nginx .
    ```

4. Create an AWS account and login to the AWS console.
5. Setup ECR to push your docker images.
6. Push the docker images to ECR.
7. Run the docker images on ECS. Configure nginx as your ingress to route
   traffic to the frontend and backend.
8. You can also use AWS Fargate to run the docker images.
9. Get a domain name and point it to your Ingress.
   
   
    