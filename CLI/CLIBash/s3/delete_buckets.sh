#!/bin/bash

# chmod +x delete_buckets.sh

BUCKET_LIST=("bucket-name-1" "bucket-name-2" "bucket-name-3")

echo "Starting bucket cleanup process..."

for bucket in "${BUCKET_LIST[@]}"
do
    echo "Processing bucket: $bucket"
    
    # Check if bucket exists
    if aws s3 ls "s3://$bucket" >/dev/null 2>&1; then
        echo "Bucket exists. Proceeding with emptying..."
        
        # Check if bucket has versioning enabled
        versioning=$(aws s3api get-bucket-versioning --bucket $bucket --query 'Status' --output text)
        
        if [ "$versioning" == "Enabled" ] || [ "$versioning" == "Suspended" ]; then
            echo "Bucket has versioning. Removing all versions and delete markers..."
            
            # Delete all versions
            aws s3api list-object-versions --bucket $bucket --output json --query '{Objects: Versions[].{Key:Key,VersionId:VersionId}}' | \
            jq 'if .Objects != null then .Objects else [] end' | \
            jq -c '.[]' | \
            while read -r object; do
                key=$(echo $object | jq -r '.Key')
                version_id=$(echo $object | jq -r '.VersionId')
                aws s3api delete-object --bucket $bucket --key "$key" --version-id "$version_id"
                echo "Deleted object: $key (version $version_id)"
            done
            
            # Delete all delete markers
            aws s3api list-object-versions --bucket $bucket --output json --query '{Objects: DeleteMarkers[].{Key:Key,VersionId:VersionId}}' | \
            jq 'if .Objects != null then .Objects else [] end' | \
            jq -c '.[]' | \
            while read -r object; do
                key=$(echo $object | jq -r '.Key')
                version_id=$(echo $object | jq -r '.VersionId')
                aws s3api delete-object --bucket $bucket --key "$key" --version-id "$version_id"
                echo "Deleted marker: $key (version $version_id)"
            done
        else
            echo "Bucket does not have versioning or versioning is not enabled. Removing objects..."
            # Remove all objects from the bucket
            aws s3 rm "s3://$bucket" --recursive
        fi
        
        # Delete the empty bucket
        echo "Deleting bucket: $bucket"
        aws s3 rb "s3://$bucket"
        
        echo "Successfully deleted bucket: $bucket"
    else
        echo "Bucket $bucket does not exist. Skipping."
    fi
    
    echo "----------------------------------------"
done

echo "Bucket cleanup process completed."
