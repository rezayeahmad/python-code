from typing import Dict, Set, Union

# Defining the nested dictionary type hint
# Structure: { student_id: {"name": str, "courses": set_of_courses} }
StudentRecord = Dict[str, Union[str, Set[str]]]
registration_system: Dict[str, StudentRecord] = {
    "S101": {"name": "Alice", "courses": {"CS101", "MATH102"}},
    "S102": {"name": "Bob", "courses": {"CS101", "ENG201", "PHYS101"}},
    "S103": {"name": "Charlie", "courses": {"MATH102", "ENG201"}}
}

print("Initial Registration System:")
print(registration_system)


# --- Add a course ---
student_id = "S101"
new_course = "PHYS101"
registration_system[student_id]["courses"].add(new_course)
print(f"\nAdded {new_course} to {registration_system[student_id]['name']}'s courses.")

# --- Try to add a duplicate course (Step 4 requirement) ---
duplicate_course = "CS101"
registration_system[student_id]["courses"].add(duplicate_course)
print(f"Tried adding duplicate {duplicate_course}. Current courses: {registration_system[student_id]['courses']}")

# --- Drop a course ---
course_to_drop = "MATH102"
# .discard() is safer than .remove() because it won't crash if the course doesn't exist
registration_system[student_id]["courses"].discard(course_to_drop)
print(f"Dropped {course_to_drop} from {registration_system[student_id]['name']}'s courses.")


# Getting course sets for Alice (S101) and Bob (S102)
alice_courses: Set[str] = registration_system["S101"]["courses"]
bob_courses: Set[str] = registration_system["S102"]["courses"]

# Intersection using the & operator
common_courses: Set[str] = alice_courses & bob_courses

print(f"\nCommon courses between Alice and Bob: {common_courses}")


# Start with an empty set of strings
all_unique_courses: Set[str] = set()

# Loop through all student records and use union (|) to combine sets
for student_id, record in registration_system.items():
    all_unique_courses = all_unique_courses | record["courses"]

print(f"\nAll unique courses available in the system: {all_unique_courses}")
