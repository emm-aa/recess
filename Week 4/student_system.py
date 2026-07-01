"""
Student Records Management System
----------------------------------
A menu-driven CLI application that stores student records in CSV and JSON files.

Modules used:
  - csv      : read/write student core records
  - json     : read/write extended student details
  - logging  : log all actions and errors to student_system.log
  - os       : check if data files exist before reading
  - re       : validate contact numbers with a simple regex
"""

import csv
import json
import logging
import os
import re

# ──────────────────────────────────────────────
# File paths
# ──────────────────────────────────────────────
CSV_FILE  = "students.csv"       # stores reg_number, name, year_of_study
JSON_FILE = "students_details.json"  # stores address, contact, program keyed by reg_number
LOG_FILE  = "student_system.log"

# ──────────────────────────────────────────────
# Logging setup
# ──────────────────────────────────────────────
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def log(message: str, level: str = "info") -> None:
    """Write a message to the log file at the given level."""
    if level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)
    else:
        logging.info(message)


# ──────────────────────────────────────────────
# Custom exceptions
# ──────────────────────────────────────────────
class StudentNotFoundError(Exception):
    """Raised when a student with the given registration number does not exist."""
    pass

class DuplicateStudentError(Exception):
    """Raised when trying to add a student whose registration number already exists."""
    pass


# ──────────────────────────────────────────────
# CSV helpers  (core fields)
# ──────────────────────────────────────────────
CSV_FIELDS = ["reg_number", "name", "year_of_study"]

def _load_csv() -> list[dict]:
    """Return all rows from the CSV file as a list of dicts. Returns [] if file missing."""
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def _save_csv(records: list[dict]) -> None:
    """Write the full list of records back to the CSV file."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(records)


# ──────────────────────────────────────────────
# JSON helpers  (extended details)
# ──────────────────────────────────────────────
def _load_json() -> dict:
    """Return the JSON details dict. Returns {} if file missing or corrupt."""
    if not os.path.exists(JSON_FILE):
        return {}
    try:
        with open(JSON_FILE, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        log(f"{JSON_FILE} is corrupt – starting with empty details.", "warning")
        return {}

def _save_json(details: dict) -> None:
    """Write the details dict back to the JSON file."""
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(details, f, indent=4)


# ──────────────────────────────────────────────
# Input validation helpers
# ──────────────────────────────────────────────
def _validate_reg(reg: str) -> bool:
    """Registration number must be non-empty and contain only letters/digits/hyphens/slashes.
    Slashes are included to support formats like 22/U/0001/PS (common at Makerere)."""
    return bool(re.fullmatch(r"[A-Za-z0-9\-/]+", reg.strip()))

def _validate_contact(contact: str) -> bool:
    """Accept common phone formats: optional +, then 7-15 digits (spaces/dashes allowed)."""
    return bool(re.fullmatch(r"[\+]?[\d\s\-]{7,15}", contact.strip()))

def _validate_year(year: str) -> bool:
    """Year of study must be a positive integer (1-6 to cover most programmes)."""
    return year.strip().isdigit() and 1 <= int(year.strip()) <= 6

def _prompt(label: str, validator=None, hint: str = "") -> str:
    """Keep asking for input until the validator passes (or no validator given)."""
    while True:
        value = input(f"  {label}{' (' + hint + ')' if hint else ''}: ").strip()
        if not value:
            print("  ✖  This field cannot be empty. Please try again.")
            continue
        if validator and not validator(value):
            print(f"  ✖  Invalid input. {hint}. Please try again.")
            continue
        return value


# ──────────────────────────────────────────────
# Core operations
# ──────────────────────────────────────────────

def add_student() -> None:
    """Collect student info and save to both CSV and JSON."""
    print("\n── Add New Student ──")
    try:
        reg     = _prompt("Registration number", _validate_reg,
                          "letters, digits, hyphens only").upper()
        name    = _prompt("Full name")
        year    = _prompt("Year of study", _validate_year, "1 – 6")
        address = _prompt("Address")
        contact = _prompt("Contact number", _validate_contact, "7-15 digits")
        program = _prompt("Programme / course")

        records = _load_csv()
        # Check for duplicate
        if any(r["reg_number"] == reg for r in records):
            raise DuplicateStudentError(f"Student '{reg}' already exists.")

        # Save core record to CSV
        records.append({"reg_number": reg, "name": name, "year_of_study": year})
        _save_csv(records)

        # Save extended details to JSON
        details = _load_json()
        details[reg] = {"address": address, "contact": contact, "program": program}
        _save_json(details)

        print(f"\n  ✔  Student {name} ({reg}) added successfully.")
        log(f"ADD student: {reg} – {name}")

    except DuplicateStudentError as e:
        print(f"\n  ✖  Error: {e}")
        log(f"ADD failed – duplicate: {e}", "warning")
    except OSError as e:
        print(f"\n  ✖  File error: {e}")
        log(f"ADD file error: {e}", "error")
    finally:
        print()   # blank line for breathing room


def view_all_students() -> None:
    """Display every student record in a simple table."""
    print("\n── All Students ──")
    try:
        records = _load_csv()
        details = _load_json()

        if not records:
            print("  No student records found.")
            log("VIEW ALL – no records found")
            return

        # Print header
        print(f"  {'REG NO':<15} {'NAME':<25} {'YEAR':<6} {'PROGRAMME':<25} {'CONTACT'}")
        print("  " + "-" * 85)

        for r in records:
            reg  = r["reg_number"]
            det  = details.get(reg, {})
            prog = det.get("program", "N/A")
            cont = det.get("contact", "N/A")
            print(f"  {reg:<15} {r['name']:<25} {r['year_of_study']:<6} {prog:<25} {cont}")

        print(f"\n  Total: {len(records)} student(s)")
        log(f"VIEW ALL – {len(records)} records displayed")

    except OSError as e:
        print(f"\n  ✖  Could not read records: {e}")
        log(f"VIEW ALL file error: {e}", "error")
    finally:
        print()


def search_student() -> None:
    """Search for a student by registration number and show full details."""
    print("\n── Search Student ──")
    try:
        reg = input("  Enter registration number: ").strip().upper()
        if not reg:
            print("  ✖  Registration number cannot be empty.")
            return

        records = _load_csv()
        match = next((r for r in records if r["reg_number"] == reg), None)

        if match is None:
            raise StudentNotFoundError(f"No student found with reg number '{reg}'.")

        details = _load_json().get(reg, {})

        print(f"\n  Registration : {match['reg_number']}")
        print(f"  Name         : {match['name']}")
        print(f"  Year         : {match['year_of_study']}")
        print(f"  Programme    : {details.get('program', 'N/A')}")
        print(f"  Address      : {details.get('address', 'N/A')}")
        print(f"  Contact      : {details.get('contact', 'N/A')}")
        log(f"SEARCH – found student: {reg}")

    except StudentNotFoundError as e:
        print(f"\n  ✖  {e}")
        log(f"SEARCH – not found: {reg}", "warning")
    except OSError as e:
        print(f"\n  ✖  File error: {e}")
        log(f"SEARCH file error: {e}", "error")
    finally:
        print()


def update_student() -> None:
    """Update one or more fields for an existing student."""
    print("\n── Update Student ──")
    try:
        reg = input("  Enter registration number to update: ").strip().upper()
        if not reg:
            print("  ✖  Registration number cannot be empty.")
            return

        records = _load_csv()
        index   = next((i for i, r in enumerate(records) if r["reg_number"] == reg), None)

        if index is None:
            raise StudentNotFoundError(f"No student found with reg number '{reg}'.")

        details = _load_json()
        det     = details.get(reg, {})

        print("  Leave a field blank to keep its current value.\n")

        # ── CSV fields ──
        new_name = input(f"  Name [{records[index]['name']}]: ").strip()
        new_year = input(f"  Year of study [{records[index]['year_of_study']}]: ").strip()

        # ── JSON fields ──
        new_address = input(f"  Address [{det.get('address', '')}]: ").strip()
        new_contact = input(f"  Contact [{det.get('contact', '')}]: ").strip()
        new_program = input(f"  Programme [{det.get('program', '')}]: ").strip()

        # Validate only if the user actually typed something
        if new_year and not _validate_year(new_year):
            print("  ✖  Invalid year – must be 1 to 6. Update cancelled.")
            log(f"UPDATE failed – invalid year input for {reg}", "warning")
            return
        if new_contact and not _validate_contact(new_contact):
            print("  ✖  Invalid contact number. Update cancelled.")
            log(f"UPDATE failed – invalid contact for {reg}", "warning")
            return

        # Apply non-blank updates
        if new_name:    records[index]["name"]          = new_name
        if new_year:    records[index]["year_of_study"] = new_year
        if new_address: det["address"] = new_address
        if new_contact: det["contact"] = new_contact
        if new_program: det["program"] = new_program

        _save_csv(records)
        details[reg] = det
        _save_json(details)

        print(f"\n  ✔  Student {reg} updated successfully.")
        log(f"UPDATE student: {reg}")

    except StudentNotFoundError as e:
        print(f"\n  ✖  {e}")
        log(f"UPDATE – not found: {reg}", "warning")
    except OSError as e:
        print(f"\n  ✖  File error: {e}")
        log(f"UPDATE file error: {e}", "error")
    finally:
        print()


def delete_student() -> None:
    """Permanently remove a student from both CSV and JSON."""
    print("\n── Delete Student ──")
    try:
        reg = input("  Enter registration number to delete: ").strip().upper()
        if not reg:
            print("  ✖  Registration number cannot be empty.")
            return

        records = _load_csv()
        new_records = [r for r in records if r["reg_number"] != reg]

        if len(new_records) == len(records):
            raise StudentNotFoundError(f"No student found with reg number '{reg}'.")

        # Confirm before deleting
        confirm = input(f"  ⚠  Are you sure you want to delete student '{reg}'? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("  Deletion cancelled.")
            log(f"DELETE cancelled by user: {reg}")
            return

        _save_csv(new_records)

        details = _load_json()
        details.pop(reg, None)   # remove from JSON if present
        _save_json(details)

        print(f"\n  ✔  Student {reg} deleted successfully.")
        log(f"DELETE student: {reg}")

    except StudentNotFoundError as e:
        print(f"\n  ✖  {e}")
        log(f"DELETE – not found: {reg}", "warning")
    except OSError as e:
        print(f"\n  ✖  File error: {e}")
        log(f"DELETE file error: {e}", "error")
    finally:
        print()


# ──────────────────────────────────────────────
# Main menu
# ──────────────────────────────────────────────
MENU = """
╔══════════════════════════════════════╗
║    Student Records Management System  ║
╠══════════════════════════════════════╣
║  1. Add a new student                 ║
║  2. View all students                 ║
║  3. Search for a student              ║
║  4. Update student details            ║
║  5. Delete a student record           ║
║  0. Exit                              ║
╚══════════════════════════════════════╝
"""

ACTIONS = {
    "1": add_student,
    "2": view_all_students,
    "3": search_student,
    "4": update_student,
    "5": delete_student,
}

def main() -> None:
    """Entry point – display menu and dispatch to the chosen action."""
    log("=== Student System started ===")
    print("\nWelcome to the Student Records Management System!")

    while True:
        print(MENU)
        choice = input("  Enter your choice: ").strip()

        if choice == "0":
            print("\n  Goodbye! All actions have been logged to student_system.log\n")
            log("=== Student System exited ===")
            break
        elif choice in ACTIONS:
            ACTIONS[choice]()
        else:
            print("\n  ✖  Invalid choice. Please enter a number from the menu.\n")
            log(f"Invalid menu input: '{choice}'", "warning")


if __name__ == "__main__":
    main()
