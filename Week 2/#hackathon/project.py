import re
import json


def read_file_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()


def count_lines(lines):
    total_lines = len(lines)
    blank_lines = 0
    comment_lines = 0
    code_lines = 0

    for line in lines:
        stripped = line.strip()
        if stripped == "":
            blank_lines += 1
        elif stripped.startswith("#"):
            comment_lines += 1
        else:
            code_lines += 1

    return {
        "total_lines": total_lines,
        "blank_lines": blank_lines,
        "comment_lines (#)": comment_lines,
        "code_lines": code_lines,
    }


def count_complexity(lines):
    complexity = {"if": 0, "elif": 0, "else": 0, "for": 0, "while": 0}

    for line in lines:

        stripped = line.strip()

        # Count statements
        if stripped.startswith("if "):
            complexity["if"] += 1

        elif stripped.startswith("elif "):
            complexity["elif"] += 1

        elif stripped.startswith("else:") or stripped.startswith("else "):
            complexity["else"] += 1

        elif stripped.startswith("for "):
            complexity["for"] += 1

        elif stripped.startswith("while "):
            complexity["while"] += 1

    return complexity


def count_comments(lines):
    comment_lines = 0
    inside_docstring = False

    for line in lines:

        stripped = line.strip()

        if '"""' in stripped or "'''" in stripped:

            comment_lines += 1

            if stripped.count('"""') == 1 or stripped.count("'''") == 1:
                inside_docstring = not inside_docstring

            continue

        if inside_docstring:
            comment_lines += 1
            continue

        if stripped.startswith("#"):
            comment_lines += 1

    total_lines = len(lines)

    if total_lines > 0:
        comment_ratio = (comment_lines / total_lines) * 100
    else:
        comment_ratio = 0

    return {"comment_lines": comment_lines, "comment_ratio": round(comment_ratio, 2)}


def check_snake_case(name):
    return bool(re.match(r"^[a-z_][a-z0-9_]*$", name))


def extract_variables(lines):
    violations = []
    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#") or not stripped:
            continue

        x = re.match(r"([a-zA-Z_]\w*)\s*=(?!=)", stripped)
        if x:
            var_name = x.group(1)
            if not check_snake_case(var_name):
                violations.append(var_name)
    return violations


def build_report(line_counts, complexity, comment_ratio, violations):
    return {
        "line_counts": line_counts,
        "complexity": complexity,
        "comment_ratio_percentage": round(comment_ratio, 2),
        "snake_case_violations": violations,
        "health_score": compute_score(
            line_counts, complexity, comment_ratio, violations
        ),
    }


def compute_score(lc, cx, cr, v):
    score = 100
    total = lc.get("total_lines", 1)
    complexity_total = sum(cx.values())
    if complexity_total / max(total, 1) > 0.2:
        score -= 20
    if cr < 5:
        score -= 15
    score -= len(v) * 5
    return max(0, score)


def print_report(report):
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    import sys

    filepath = sys.argv[1] if len(sys.argv) > 1 else "testfile.py"

    try:
        lines = read_file_lines(filepath)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

    line_counts = count_lines(lines)
    complexity = count_complexity(lines)
    comments = count_comments(lines)
    violations = extract_variables(lines)

    report = build_report(
        line_counts, complexity, comments.get("comment_ratio", 0), violations
    )

    report["comment_lines"] = comments.get("comment_lines", 0)

    print_report(report)
