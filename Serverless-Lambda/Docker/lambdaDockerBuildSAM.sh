
cd lambdas/resize
rm -rf libs lambda.zip
docker run --platform linux/x86_64 -v "$PWD":/var/task "public.ecr.aws/sam/build-python3.12" /bin/sh -c "pip install -r requirements.txt -t libs; exit"
cd libs && zip -r ../lambda.zip . && cd ..
zip lambda.zip handler.py
rm -rf libs
cd ../..