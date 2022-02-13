# factorial application

The application is returned using the Flask framework

It will calculate the facotorial of the number

Dockerfile included in the repo to make it convert into docker image.

Manual Commands used to build and push image:

1. aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 364485175950.dkr.ecr.ap-south-1.amazonaws.com
2. docker build -t factorial .
3. docker tag factorial:latest 364485175950.dkr.ecr.ap-south-1.amazonaws.com/factorial:latest
4. docker push 364485175950.dkr.ecr.ap-south-1.amazonaws.com/factorial:latest

The service is deployed in the ECS with ALB. The infrastructure is written using the terraform

Endpoint of the service: http://factorial-1242678218.ap-south-1.elb.amazonaws.com


