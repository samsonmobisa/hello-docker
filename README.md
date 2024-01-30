# Hello, Docker!

This is a simple Python program that prompts the user for their name and prints a personalized greeting. The project is containerized using Docker, allowing for easy deployment.

## Requirements

- [Docker](https://www.docker.com/get-started)

## Usage

1. Clone the repository:

   ```bash
  https://github.com/samsonmobisa/hello-docker.git
  
   cd hello-docker
   docker build -t hello-docker-app .
   docker run -it hello-docker-app YourName

Replace hello-docker-app with YourAppName

