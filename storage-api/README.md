## Usage

### Local dev

```sh
npm run dev
```

### Deploy

See package.json.

```sh
npm run sls:create_domain  # needed only for the first time
npm run sls:deploy
npm run sls:info
```

API gateway
https://ap-northeast-1.console.aws.amazon.com/apigateway/home?region=ap-northeast-1#/custom-domain-names

Lambda
https://ap-northeast-1.console.aws.amazon.com/lambda/home?region=ap-northeast-1#/functions

### Clean

```sh
npm sls:remove
npm sls:delete_domain
```


## Setup memo

1. Prepare

    ```sh
    mkdir -p infra/
    mkdir -p app/
    ```

2. Infra

    ```sh
    cd infra/
    touch main.tf
    touch terraform.tfvars
    ```
    `main.tf`
    ```sh
    # See the file
    ```
    `terraform.tfvars`
    ```sh
    # See the file
    ```
    ```sh
    tf init
    tf plan
    tf apply

    aws --version
    aws configure --profile scene-finder-storage
    # xxxxxxxx  # new IAM user's one
    # xxxxxxxxxxxxxxxx  # new IAM user's one
    # ap-northeast-1
    # txt
    less ~/.aws/credentials
    aws s3 ls --profile=scene-finder-storage

    cd ../
    ```

3. App

    ```
    cd app/
    npm init -y
    vim package.json  # edit scripts
    ```
    `package.json`
    ```json
    ...
      "scripts": {
        "dev": "npx serverless offline",
        "sls:create_domain": "npx serverless create_domain",
        "sls:delete_domain": "npx serverless delete_domain",
        "sls:package": "npx serverless package",
        "sls:deploy": "npx serverless deploy",
        "sls:remove": "npx serverless remove",
        "sls:info": "npx serverless info",
        "sls:log": "npx serverless logs -f fc-index"
      },
    ...
    ```
    ```sh
    npm i -D serverless serverless-domain-manager serverless-offline
    npm i -S aws-sdk aws-serverless-express express

    touch serverless.yml
    ```
    `serverless.yml`
    ```yml
    # See the file
    ```
