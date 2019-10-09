# Scene finder api

http://localhost:3000/health
http://localhost:3000/ytdl/download
http://localhost:3000/ytdl/download?url=https://www.youtube.com/watch?v=nRK81kMKXYw
http://localhost:3000/ytdl/download?url=https://www.youtube.com/watch?v=kjETQaKLDcA

### Dev on local

#### python env

See api/app/static/bin/opencv/setup.sh

#### run server

```sh
npm run dev
```

### deploy

```sh
# create the custom domain
sls create_domain

# Wait about 40 mins for its finish...
# + add an A record in Route53
```

```sh
# deploy to lambda with the custom domain
sls deploy

# Wait few mins.
```

```sh
# check
sls info
sls deploy list functions
#curl https://example.com/health

# invoke the lambda function
#serverless invoke -f fc-index -l  # it seems only for root path

# logs
sls logs -f fc-index
```

### Configure base mapping in the custom domain

https://ap-northeast-1.console.aws.amazon.com/apigateway/home?region=ap-northeast-1#/custom-domain-names

* '/{proxy+}' as API gateway path, and '/' as custom domain base mapping.
    * All works.
    * Only one api (other api will not be able to use custom domain)


### Thanks

https://github.com/yokrh/scene-finder_0/tree/master/app/scene-finder-api
