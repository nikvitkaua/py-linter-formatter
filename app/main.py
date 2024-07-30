def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                {
                    "line": err.get("line_number"),
                    "column": err.get("column_number"),
                    "message": err.get("text"),
                    "name": err.get("code"),
                    "source": "flake8"
                }
                for err in errors
            ],
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
