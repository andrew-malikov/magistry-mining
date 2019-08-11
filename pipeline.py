class Student:
    def __init__(self, name, profile):
        self.name = name
        self.profiles = []

        self.profiles.append(profile)

    def _stringify_profiles(self):
        return list(map(lambda profile: profile.value, self.profiles))

    def __str__(self):
        return "{0} {1}".format(self.name, self._stringify_profiles())

    def __unicode__(self):
        return "{0} {1}".format(self.name, self._stringify_profiles())

    def __repr__(self):
        return "{0} {1}".format(self.name, self._stringify_profiles())

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.name == other.name)


def merge(RawStudents: list) -> list:
    merged = list()

    for rawStudent in RawStudents:
        maybe_student = list(
            filter(lambda x: x.name == rawStudent.name, merged))

        if len(maybe_student) > 0:
            maybe_student[0].profiles.append(rawStudent.profile)
        else:
            merged.append(Student(rawStudent.name, rawStudent.profile))

    return merged
