# -*- coding: utf-8 -*-

from behave import given, when, then
from models.course import Course
from models.specialization import Specialization



@given('a set of specializations')
def step_impl(context):
    for row in context.table:
        Specialization.get(name=row['name'])

@given('a set of courses')
def step_impl(context):
    for row in context.table:
        Course.get_or_create(name=row['name'])

@when('we search for courses in "{name}"')
def step_impl(context, name):
    try:
        context.result = Specialization.select(name).join(Course, on=(Specialization.id == Course.sp_id)).where(Specialization.name == name)
    except Specialization.DoesNotExist:
        context.result = None
    assert context.result is not None

@then('we will find {count:d} Programming items')
def step_impl(context, count):
    assert context.result.count() == count
