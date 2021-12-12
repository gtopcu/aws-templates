//snippet-sourcedescription:[CreateCustomerKey.kt demonstrates how to create an AWS Key Management Service (AWS KMS) key.]
//snippet-keyword:[AWS SDK for Kotlin]
//snippet-keyword:[Code Sample]
//snippet-service:[AWS Key Management Service]
//snippet-sourcetype:[full-example]
//snippet-sourcedate:[11/04/2021]
//snippet-sourceauthor:[scmacdon-aws]

/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/

package com.kotlin.kms

// snippet-start:[kms.kotlin_create_key.import]
import aws.sdk.kotlin.services.kms.KmsClient
import aws.sdk.kotlin.services.kms.model.CreateKeyRequest
import aws.sdk.kotlin.services.kms.model.CustomerMasterKeySpec
import aws.sdk.kotlin.services.kms.model.KeyUsageType
// snippet-end:[kms.kotlin_create_key.import]

/**
To run this Kotlin code example, ensure that you have setup your development environment,
including your credentials.

For information, see this documentation topic:
https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html
 */

suspend fun main() {

    val keyDes = "Created by the AWS KMS Kotlin API"
    val keyId = createKey(keyDes)
    println("The key id is $keyId")
    }

// snippet-start:[kms.kotlin_create_key.main]
suspend fun createKey(keyDesc: String?): String? {

    val request = CreateKeyRequest {
        description = keyDesc
        customerMasterKeySpec = CustomerMasterKeySpec.SymmetricDefault
        keyUsage = KeyUsageType.fromValue("ENCRYPT_DECRYPT")
    }

    KmsClient { region = "us-west-2" }.use { kmsClient ->
              val result = kmsClient.createKey(request)
              println("Created a customer key with id "+result.keyMetadata?.arn)
              return result.keyMetadata?.keyId
    }
 }
// snippet-end:[kms.kotlin_create_key.main]