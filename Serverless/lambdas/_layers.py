
# https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html

# Lambda extracts the layer contents into the /opt directory in your function’s execution environment. 
# All natively supported Lambda runtimes include paths to specific directories within the /opt directory. 
# This gives your function access to your layer content. 

# You can include up to five layers per function. Also, you can use layers only with Lambda functions deployed 
# as a .zip file archive. For functions defined as a container image, package your preferred runtime and all code 
# dependencies when you create the container image.

