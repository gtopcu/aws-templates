# https://aws.amazon.com/blogs/developer/testing-cdk-applications-in-any-language/

import aws_cdk as cdk
from aws_cdk import Stack
from aws_cdk.assertions import Template, Match, Capture

"""
Match.absent()
Match.any_value()
Match.array_equals()
Match.array_with()
Match.object_equals()
Match.object_like()
Match.string_like_regexp()
Match.serialized_json()
"""

my_stack: Stack = None
template: Template = Template.from_stack(my_stack)

template.has_resource_properties("AWS::CertificateManager::Certificate", {
    "DomainName": "test.example.com",
    "ShouldNotExist": Match.absent(),
})

template.has_resource_properties("AWS::S3::Bucket", {
    "BucketName": "XXXXXXXXXXX",
    "ShouldNotExist": Match.absent(),
})

template.has_resource_properties(
    "Find resource with property",
    Match.object_like({
        "Property": Match.any_value(),
    })
)

template.all_resources_properties(
    "Find all resources with property",
    Match.object_like({
        "Property": Match.any_value(),
    })
)

template.resource_count_is("AWS::S3::Bucket", 1)

template.resource_properties_count_is("AWS::S3::Bucket", {
    "BucketName": "XXXXXXXXXXX",
    "ShouldNotExist": Match.absent(),
}, 1)

template.find_outputs(  # returns a dict
    "Find CF outputs with export name & value",
    Match.object_like({
        "ExportName": Match.any_value(),
        "Value": Match.any_value(),
    })
)

template.has_output(  # returns a bool
    "Find CF outputs with export name & value",
    Match.object_like({
        "ExportName": Match.any_value(),
        "Value": Match.any_value(),
    })
)


