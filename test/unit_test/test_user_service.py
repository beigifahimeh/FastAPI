
def test_delete_user(user_service):
    user_to_delete = 0
    user_service.delete_user(user_to_delete) 
    assert user_to_delete not in user_service.profile_info
    assert user_to_delete not in user_service.content
