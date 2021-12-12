//snippet-sourcedescription:[DynamoDBScanItems.kt demonstrates how to return items from an Amazon DynamoDB table.]
//snippet-keyword:[AWS SDK for Kotlin]
//snippet-keyword:[Code Sample]
//snippet-service:[Amazon DynamoDB]
//snippet-sourcetype:[full-example]
//snippet-sourcedate:[11/04/2021]
//snippet-sourceauthor:[scmacdon-aws]

/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/


package com.kotlin.dynamodb

// snippet-start:[dynamodb.kotlin.scan_items.import]
import aws.sdk.kotlin.services.dynamodb.DynamoDbClient
import aws.sdk.kotlin.services.dynamodb.model.ScanRequest
import kotlin.system.exitProcess
// snippet-end:[dynamodb.kotlin.scan_items.import]

/**
To run this Kotlin code example, ensure that you have setup your development environment,
including your credentials.

For information, see this documentation topic:
https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html
 */
suspend fun main(args: Array<String>) {

    val usage = """
    Usage:
        <tableName>

    Where:
        tableName - the Amazon DynamoDB table to scan (for example, Music3).
    """

     if (args.size != 1) {
           println(usage)
           exitProcess(0)
       }

    val tableName = args[0]
    scanItems(tableName)
}

// snippet-start:[dynamodb.kotlin.scan_items.main]
suspend fun scanItems(tableNameVal: String) {

    val request = ScanRequest {
        tableName = tableNameVal
    }

    DynamoDbClient { region = "us-east-1" }.use { ddb ->
            val response = ddb.scan(request)
            response.items?.forEach { item ->
                 item.keys.forEach { key ->
                     println("The key name is $key\n")
                     println("The value is ${item[key]}")
                }
            }
        }
 }
// snippet-end:[dynamodb.kotlin.scan_items.main]