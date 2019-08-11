from data import Profile
from pipeline import Student, merge


def unique_students(students):
    return merge(students)


def students_with_one_profile(students):
    return filter(lambda student: len(student.profiles) == 1, merge(students))


def students_with_fiit_profile(students):
    return filter(lambda student: Profile.FIIT in student.profiles,
                  merge(students))


def unique_students_by_profiles(students, profiles):
    def has_all_profiles(student: Student):
        return len(
            list(filter(lambda profile: profile in profiles,
                        student.profiles))) > 0

    return set(
        filter(lambda student: has_all_profiles(student), merge(students)))
