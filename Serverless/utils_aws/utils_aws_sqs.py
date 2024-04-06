
import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='test')
response = queue.send_message(MessageBody='world')

# queue.send_message(MessageBody='boto3', MessageAttributes={#     'Author': {
#         'StringValue': 'Daniel',
#         'DataType': 'String'
#     }
# })
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

# Batch send
# response = queue.send_messages(Entries=[
#     {
#         'Id': '1',
#         'MessageBody': 'world'
#     },
#     {
#         'Id': '2',
#         'MessageBody': 'boto3',
#         'MessageAttributes': {
#             'Author': {
#                 'StringValue': 'Daniel',
#                 'DataType': 'String'
#             }
#         }
#     }
# ])

# # Print out any failures - partial failures
# print(response.get('Failed'))

# Process messages
# Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))

    # Let the queue know that the message is processed
    message.delete()