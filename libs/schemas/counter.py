schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "MetricItem",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "pattern": "^[a-z_][a-z0-9_]*$",
        },
        "date": {"type": "integer"},
        "value": {
            "type": "number",
            "minimum": 0,
        },
        "labels": {
            "type": "object",
            "minProperties": 1,
            "propertyNames": {
                "pattern": "^[a-z_][a-z0-9_]*$"
            },
            "additionalProperties": {
                "type": ["string", "null"]
            }
        }
    },
    "required": ["name", "value",]
}
