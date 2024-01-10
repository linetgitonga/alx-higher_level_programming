#!/usr/bin/python3

"""This module contains`Studen class"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Creates a new student.

        Args:
            first_name(string): The student name
            last_name(string): The student last name
            age(int): The student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Serialize `Student` object."""

        obj_attrs = None
        if type(attrs) is list:
            str_list = [d for d in attrs if type(d) is str]
            if len(str_list) == len(attrs):
                obj_attrs = attrs

        if obj_attrs is None:
            obj_attrs = [d for d in dir(self) if not d.startswith("__")]
        obj_dict = {}
        for attr in obj_attrs:
            try:
                data = getattr(self, attr)
                if type(data) in (list, dict, str, int, bool):
                    obj_dict[attr] = data
            except AttributeError:
                pass
        return obj_dict

    def reload_from_json(self, json):
        """replaces all attributes of the `Student` instance

        Args:
            json(str): The `JSON` doc.
        """

        for key in json:
            setattr(self, key, json[key])
