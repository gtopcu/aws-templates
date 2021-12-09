#aws s3 sync D: s3://gokhantopcu-personal/PC --sse aws:kms --sse-kms-key-id arn:aws:kms:eu-west-1:066636589246:key/a0aa892d-6d79-4040-8d41-1ca72e1c89bb

#C:\Program Files\7-Zip
#7z a -tzip -mx1 D:/_Backup/S3/PC.zip D:/
#aws s3 sync D:/_Backup/S3/ s3://gokhantopcu-personal/PC --sse aws:kms --sse-kms-key-id arn:aws:kms:eu-west-1:066636589246:key/a0aa892d-6d79-4040-8d41-1ca72e1c89bb
#del /f D:/_Backup/S3/PC.zip
#cd D:\_Backup\S3
#cd D:/_Backup/S3
#del /f D:/PC.zip

#7z a -tzip -mx1 D:/_Backup/S3/PC.zip D:/ -spf -x!D:/System Volume Information
#aws s3 cp Notes.txt s3://gokhantopcu-backup --sse aws:kms --sse-kms-key-id arn:aws:kms:eu-west-1:066636589246:key/a0aa892d-6d79-4040-8d41-1ca72e1c89bb

#7z a -tzip -mx1 D:/_Backup/S3/PC.zip D:/ -spf x!D:/_Backup/S3 x!D:/IT/Java/eclipse -x!D:/IT/Java/Servers -x!D:/Programs/Developer Tools/DB/sqldeveloper
#aws s3 sync D:/_Backup/S3/ s3://gokhantopcu-backup/PC

aws s3 sync D:/ s3://gokhantopcu-backup/PC


