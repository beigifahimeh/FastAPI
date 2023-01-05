import pytest
from app.exceptions import UserNotFound


def test_delete_user(user_service, valid_user_delete_id):
    user_service.delete_user(valid_user_delete_id) 
    assert valid_user_delete_id not in user_service.profile_info
    assert valid_user_delete_id not in user_service.content


def test_delete_invalid_user_make_correct_exception(user_service, invalid_user_delete_id):
    pytest.raises(UserNotFound, user_service.delete_user, invalid_user_delete_id )
   