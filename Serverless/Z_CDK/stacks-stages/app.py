#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stages.my_stage import MyAppStage

#  Create a CDK app
app = cdk.App()

# Create the development stage
MyAppStage(app, 'Dev',
           env=cdk.Environment(account='123456789012', region='us-east-1'),
           )

# Create the production stage 
MyAppStage(app, 'Prod',
           env=cdk.Environment(account='098765432109', region='us-east-1'),
           )

app.synth()

"""
after cdk synth->
cdk-demo-app
├── app.py
├── cdk.out
│   ├── assembly-Dev
│   │   ├── DevAppStackunique-hash.assets.json
│   │   ├── DevAppStackunique-hash.template.json
│   │   ├── DevDatabaseStackunique-hash.assets.json
│   │   ├── DevDatabaseStackunique-hash.template.json
│   │   ├── cdk.out
│   │   └── manifest.json
│   ├── assembly-Prod
│   │   ├── ProdAppStackunique-hash.assets.json
│   │   ├── ProdAppStackunique-hash.template.json
│   │   ├── ProdDatabaseStackunique-hash.assets.json
│   │   ├── ProdDatabaseStackunique-hash.template.json
│   │   ├── cdk.out
│   │   └── manifest.json
│   ├── cdk.out
│   ├── manifest.json
│   └── tree.json
└── cdk_demo_app
    ├── __init__.py
    ├── app_stack.py
    ├── database_stack.py
    └── my_stage.py

"""