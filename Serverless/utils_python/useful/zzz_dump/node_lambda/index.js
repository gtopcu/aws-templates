const { CloudWatchLogsClient, FilterLogEventsCommand } = require('@aws-sdk/client-cloudwatch-logs');

const client = new CloudWatchLogsClient({ region: 'eu-west-2' });

exports.handler = async (event) => {
  // Extract arguments from the GraphQL query
  const {
    logGroupNames,
    logStreamName,
    startTime,
    endTime,
    filterPattern,
    limit,
    descending,
  } = event.arguments || {};

  // Validate logGroupNames
  if (!Array.isArray(logGroupNames) || logGroupNames.length === 0) {
    throw new Error('logGroupNames must be a non-empty array');
  }

  // Create an array of promises, one for each log group
  const promises = logGroupNames.map(async (logGroupName) => {
    try {
      // Build parameters for FilterLogEventsCommand
      const params = {
        logGroupName,
        logStreamNames: logStreamName ? [logStreamName] : undefined,
        startTime: startTime ? parseInt(startTime) : undefined,
        endTime: endTime ? parseInt(endTime) : undefined,
        filterPattern: filterPattern || undefined,
        limit: limit ? parseInt(limit) : undefined,
      };

      // Create and send the command to fetch logs from CloudWatch
      const command = new FilterLogEventsCommand(params);
      const data = await client.send(command);

      // Format log entries
      const logs = (data.events || []).map((event) => ({
        timestamp: new Date(event.timestamp).toISOString(),
        message: event.message ? event.message.trim() : '',
      }));

      // Sort logs if descending is true (newest first)
      if (descending) {
        logs.reverse();
      }

      // Return successful result
      return { logGroupName, logs };
    } catch (error) {
      // Return error result if the API call fails
      return { logGroupName, error: error.message || 'Unknown error' };
    }
  });

  // Wait for all promises to resolve
  const results = await Promise.all(promises);

  return results;
};