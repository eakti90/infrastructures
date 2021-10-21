# AWS CDK Infrastructure as Code Project for Container App
This project is an infrastructure as code (IaC) project for Container Application. Since load balancer, vpc, containerized(ECR,ECS) is required for this application, I found it appropriate to use Aws Cdk for IaC. Infrastructure was created with python, which is the application language.
you can find out how to meet the prerequisites from the [link](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_prerequisites).
## Steps Of Installation AWS CDK IaC

### Install CDK CLI tool

```
npm install -g aws-cdk
```

### How to create virtual environment for Python and install dependencies

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### How to run tests

```
pytest
```

### Show stacks

```
cdk ls
```

### How to deploy stack

```
cdk deploy --all --profile <AWS_PROFILE_NAME>
```
