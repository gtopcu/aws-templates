
# https://aws.github.io/chalice/index

# python3 -m venv venv
# pip install chalice -U
# chalice new helloworld
# chalice new helloworld --generate-only
# chalice new-project helloworld
# chalice deploy
# chalice local
# chalice invoke index --log-level debug --raw-json '{"hello": "world"}' --stage dev
# chalice delete
# chalice update-project-config --autogen-policy --no-autogen-policy --autogen-iam --no-autogen-iam
# chalice 


from chalice import Chalice, Rate, Cron, Response
# NotFoundError, BadRequestError, UnauthorizedError, ForbiddenError, ConflictError, UnprocessableEntityError, 
# TooManyRequestsError, RequestTimeoutError, InternalServerError, ChaliceViewError, ChaliceDeprecationWarning, 
# ChaliceUnhandledError, ChaliceViewWarning

app = Chalice(app_name="helloworld")

@app.route("/")
def index():
    return {"hello": "world"}

@app.schedule(Rate(5, unit=Rate.MINUTES))
def periodic_task(event):
    return {"hello": "world"}

@app.on_s3_event(bucket='mybucket')
def s3_handler(event):
    print(event.bucket, event.key)