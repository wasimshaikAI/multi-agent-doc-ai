import json

def process_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Example expected fields — customize as needed
        expected_fields = ['id', 'date', 'customer', 'total']

        extracted = {field: data.get(field) for field in expected_fields}
        missing = [k for k, v in extracted.items() if v is None]

        return extracted, missing

    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e}")
        return {}, ["invalid_json"]

    except FileNotFoundError:
        print("❌ File not found.")
        return {}, ["file_not_found"]

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return {}, ["unknown_error"]
