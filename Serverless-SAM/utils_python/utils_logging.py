"""
This library is provided to allow standard python logging
to output log data as JSON formatted strings
Source: https://github.com/madzak/python-json-logger
"""
import json
import logging
import re
import traceback
from collections import OrderedDict
from datetime import date, datetime, time, timezone
from inspect import istraceback
from typing import Dict, List, Tuple, Union

def set_basic_config() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="basic.log"   
    )
    #logger = logging.getLogger()

# skip natural LogRecord attributes
# http://docs.python.org/library/logging.html#logrecord-attributes
RESERVED_ATTRS: Tuple[str, ...] = (
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
)


def merge_record_extra(
    record: logging.LogRecord, target: Dict, reserved: Union[Dict, List]
) -> Dict:
    """
    Merges extra attributes from LogRecord object into target dictionary
    :param record: logging.LogRecord
    :param target: dict to update
    :param reserved: dict or list with reserved keys to skip
    """
    for key, value in record.__dict__.items():
        # this allows to have numeric keys
        if key not in reserved and not (
            hasattr(key, "startswith") and key.startswith("_")
        ):
            target[key] = value
    return target


class JsonEncoder(json.JSONEncoder):
    """
    A custom encoder extending the default JSONEncoder
    """

    def default(self, obj):
        if isinstance(obj, (date, datetime, time)):
            return self.format_datetime_obj(obj)

        elif istraceback(obj):
            return "".join(traceback.format_tb(obj)).strip()

        elif (
            type(obj) == Exception
            or isinstance(obj, Exception)
            or type(obj) == type
        ):
            return str(obj)

        try:
            return super(JsonEncoder, self).default(obj)

        except TypeError:
            try:
                return str(obj)

            except Exception:
                return None

    def format_datetime_obj(self, obj):
        return obj.isoformat()


class JsonFormatter(logging.Formatter):
    """
    A custom formatter to format logging records as json strings.
    Extra values will be formatted as str() if not supported by
    json default encoder
    """

    def __init__(self, *args, **kwargs):
        """
        :param rename_fields: an optional dict, used to rename field names
            in the output. Rename message to @message: {'message': '@message'}
        :param static_fields: an optional dict, used to add fields with static
            values to all logs
        :param reserved_attrs: an optional list of fields that will be skipped
            when
            outputting json log record. Defaults to all log record attributes:
            http://docs.python.org/library/logging.html#logrecord-attributes
        :param timestamp: an optional string/boolean field to add a timestamp
            when
            outputting the json log record. If string is passed, timestamp
            will be added to log record using string as key.
            If True boolean is passed, timestamp key will be "timestamp".
            Defaults to False/off.
        """

        self.json_encoder = JsonEncoder
        self.rename_fields = kwargs.pop("rename_fields", {})
        self.static_fields = kwargs.pop("static_fields", {})
        reserved_attrs = kwargs.pop("reserved_attrs", RESERVED_ATTRS)
        self.reserved_attrs = dict(zip(reserved_attrs, reserved_attrs))
        self.timestamp = kwargs.pop("timestamp", False)

        # super(JsonFormatter, self).__init__(*args, **kwargs)
        logging.Formatter.__init__(self, *args, **kwargs)

        self._required_fields = self.parse()
        self._skip_fields = dict(
            zip(self._required_fields, self._required_fields)
        )
        self._skip_fields.update(self.reserved_attrs)

    def parse(self) -> List[str]:
        """
        Parses format string looking for substitutions
        This method is responsible for returning a list of fields (as strings)
        to include in all log messages.
        """
        if isinstance(self._style, logging.StringTemplateStyle):
            formatter_style_pattern = re.compile(r"\$\{(.+?)\}", re.IGNORECASE)
        elif isinstance(self._style, logging.StrFormatStyle):
            formatter_style_pattern = re.compile(r"\{(.+?)\}", re.IGNORECASE)
        # PercentStyle is parent class of StringTemplateStyle and
        # StrFormatStyle, so it needs to be checked last.
        elif isinstance(self._style, logging.PercentStyle):
            formatter_style_pattern = re.compile(r"%\((.+?)\)s", re.IGNORECASE)
        else:
            raise ValueError("Invalid format: %s" % self._fmt)

        if self._fmt:
            return formatter_style_pattern.findall(self._fmt)
        else:
            return []

    def add_fields(self, log_record, record, message_dict):
        """
        Override this method to implement custom logic for adding fields.
        """
        for field in self._required_fields:
            if field in self.rename_fields:
                log_record[self.rename_fields[field]] = record.__dict__.get(
                    field
                )
            else:
                log_record[field] = record.__dict__.get(field)
        log_record.update(self.static_fields)
        log_record.update(message_dict)
        merge_record_extra(record, log_record, reserved=self._skip_fields)

        if self.timestamp:
            key = (
                self.timestamp if type(self.timestamp) == str else "timestamp"
            )
            log_record[key] = datetime.fromtimestamp(
                record.created, tz=timezone.utc
            )

    def format(self, record):
        """Formats a log record and serializes to json"""
        message_dict = {}
        if isinstance(record.msg, dict):
            message_dict = record.msg
            record.message = None
        else:
            record.message = record.getMessage()
        # only format time if needed
        if "asctime" in self._required_fields:
            record.asctime = self.formatTime(record, self.datefmt)

        # Display formatted exception, but allow overriding it in the
        # user-supplied dict.
        if record.exc_info and not message_dict.get("exc_info"):
            message_dict["exc_info"] = self.formatException(record.exc_info)
        if not message_dict.get("exc_info") and record.exc_text:
            message_dict["exc_info"] = record.exc_text
        # Display formatted record of stack frames
        # default format is a string returned from
        # :func:`traceback.print_stack`
        try:
            if record.stack_info and not message_dict.get("stack_info"):
                message_dict["stack_info"] = self.formatStack(
                    record.stack_info
                )
        except AttributeError:
            # Python2.7 doesn't have stack_info.
            pass

        log_record: Dict
        try:
            log_record = OrderedDict()
        except NameError:
            log_record = {}

        self.add_fields(log_record, record, message_dict)

        return json.dumps(log_record, cls=self.json_encoder)


class AdditionalFieldFilter(logging.Filter):
    def __init__(self, additional_field_map:Dict):
        super().__init__()
        self._additional_log_fields = additional_field_map

    def filter(self, log_record):
        for key, value in self._additional_log_fields.items():
            setattr(log_record, key, value)
        return True

    def set_fields(self, additional_fields:Dict):
        if not additional_fields:
            additional_fields = {}
        self._additional_log_fields = additional_fields

    def update_fields(self, update_dict:Dict):
        self._additional_log_fields.update(update_dict)
    
    def delete_fields(self, keys:List):
        for key in keys:
            self._additional_log_fields.pop(key, None)


def set_logger(logger: logging.Logger, additional_fields: Dict):
    """Sets up a logger with a dictionary as fields. These fields
    will be logged in all submodules too.

    Arguments:
    :param logger: logger to be set
    :param additional_fields: -- map of additional fields.
    """
    formatter = JsonFormatter(
        "%(levelname)s %(message)s %(pathname)s %(lineno)s"
    )
    filter = AdditionalFieldFilter(additional_fields)
    if len(logger.handlers) > 0:
        handler = logger.handlers[0]
    else:
        handler = logging.StreamHandler()
        logger.addHandler(handler)
    handler.setFormatter(formatter)
    handler.addFilter(filter)

def _get_filter(logger: logging.Logger):
    handler = logger.handlers[0]
    for filter in handler.filters:
        if isinstance(filter, AdditionalFieldFilter):
            return filter
    
    raise AttributeError

def add_fields(logger: logging.Logger, additional_fields: Dict):
    """Add fields to existing logger

    Arguments:
    :param logger: logger to be updated
    :param additional_fields: -- map of additional fields.
    """
    filter = _get_filter(logger)
    filter.update_fields(additional_fields)

def delete_fields(logger: logging.Logger, keys: List):
    """Delete fields from logger

    Arguments:
    :param logger: logger to be updated
    :param keys: -- list of keys.
    """
    filter = _get_filter(logger)
    filter.delete_fields(keys)

