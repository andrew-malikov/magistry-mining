from data import students, Profile

from queries import unique_students, students_with_one_profile
from queries import students_with_fiit_profile, unique_students_by_profiles

import pprint

pretifier = pprint.PrettyPrinter(indent=4)


def pretify(data):
    pretifier.pprint(data)


def print_unique_students():
    print("unique students", end="\n")

    pretify(len(unique_students(students)))


def print_students_with_one_profile():
    print("danger students", end="\n")

    found_students = list(students_with_one_profile(students))

    print("count: ", len(found_students), end="\n")
    pretify(found_students)


def print_students_with_fiit_profile():
    print("Relations of [ФИИТ] students:", end="\n")

    found_students = list(students_with_fiit_profile(students))

    print("count: ", len(found_students), end="\n")
    pretify(found_students)


def print_students_with_fiit_ict_2_pi_profiles():
    print("unique students by [ФИИТ, ИВТ-2, ПИ] profiles", end="\n")

    profiles = [Profile.FIIT, Profile.ICT_2, Profile.PI]
    found_students = unique_students_by_profiles(students, profiles)

    print("count: ", len(found_students), end="\n")
    pretify(found_students)


def print_students_with_fiit_ist_pmi_profiles():
    print("unique students by [ФИИТ, ПМИ, ИСТ] profiles", end="\n")

    profiles = [Profile.FIIT, Profile.PMI, Profile.IST]
    found_students = unique_students_by_profiles(students, profiles)

    print("count: ", len(found_students), end="\n")
    pretify(found_students)


def print_students_with_ict_1_ict_2_pi_profiles():
    print("unique students by [ИВТ-1, ИВТ-2, ПИ] profiles", end="\n")

    profiles = [Profile.ICT_1, Profile.ICT_2, Profile.PI]
    found_students = unique_students_by_profiles(students, profiles)

    print("count: ", len(found_students), end="\n")
    pretify(found_students)


if __name__ == "__main__":
    print_unique_students()
    print_students_with_one_profile()
    print_students_with_fiit_profile()
    print_students_with_fiit_ict_2_pi_profiles()
    print_students_with_fiit_ist_pmi_profiles()
    print_students_with_ict_1_ict_2_pi_profiles()
