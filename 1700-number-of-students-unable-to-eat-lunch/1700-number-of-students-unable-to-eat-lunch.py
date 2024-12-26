class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        attempts = 0 
        # Tracks consecutive unsuccessful attempts to match the top sandwich
        while students and attempts < len(students):
            if students[0] == sandwiches[0]:
                # If the current student's preference matches the top sandwich
                students.pop(0)
                # Remove the student from the queue
                sandwiches.pop(0) 
                # Remove the sandwich from the stack
                attempts = 0 
                # Reset attempts since a match was made
            else:
                # If no match, move the student to the end of the queue
                students.append(students.pop(0))
                attempts += 1
                # Increment attempts as no sandwich was taken

        # Return the number of students left in the queue who couldn't eat
        return len(students)
