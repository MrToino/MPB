import json
import jsonschema
from jsonschema.exceptions import ValidationError


requestSchema = {
  "type": "object",
  "properties": {
    "Filename": {"type": "string"},
    "ContentB64": {"type": "string"}
  },
  "required": ["Filename", "ContentB64"]
}


def validate_schema(request):
    """Validates request JSON schema"""
    try:
        jsonschema.validate(instance=request, schema=requestSchema)
        return True
    except ValidationError as err:
        print("Invalid request JSON schema.")
        exit()
        return False


def parse_json(request):
    """Validates and parse JSON request"""
    try:
        return json.loads(request)
    except ValueError:
        print("Invalid request: cannot parse JSON.")
        exit()


def validate_request(request):
    """Validates request json in format and schema"""
    parsed_response = parse_json(request)
    if validate_schema(parsed_response):
        return parsed_response
    else:
        print("Invalid request. Service was abandoned.")
        exit()