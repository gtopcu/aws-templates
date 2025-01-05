{
    "StartAt": "SubmitJob",
    "States": {
        "SubmitJob": {
            "Type": "Pass",
            "Parameters": {
                "jobId.$": "$$.Execution.Id",
                "input.$": "$.input"
            },
            "Next": "ProcessTask"
        },
        "ProcessTask": {
            "Type": "Task",
            "Resource": "process_lambda.function_arn",
            "Next": "CheckStatus"
        },
        "CheckStatus": {
            "Type": "Choice",
            "Choices": [
                {
                    "Variable": "$.status",
                    "StringEquals": "SUCCESS",
                    "Next": "JobSucceeded"
                },
                {
                    "Variable": "$.status",
                    "StringEquals": "FAILED",
                    "Next": "JobFailed"
                }
            ],
            "Default": "ProcessTask"
        },
        "JobSucceeded": {
            "Type": "Succeed"
        },
        "JobFailed": {
            "Type": "Fail",
            "Error": "ProcessingError",
            "Cause": "Job processing failed"
        }
    }
}
