#run all apps tests form here this folder

import pytest
from django.contrib.auth.models import User


def test_new_user1(new_user1):
    print(new_user1.first_name)
    assert new_user1.first_name =='rewan'


def test_new_user2(new_user2):
    print(new_user2.is_staff)
    assert new_user2.is_staff





'''
@pytest.mark.django_db   #that will give accsess to database
def test_user():
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password('4736')
    assert user_1.check_password('4736') is True

'''