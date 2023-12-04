def test_userdata_manager():
    from userdatamanager.manager import UserDataManager

    manager = UserDataManager()

    manager.create_userdata("yvesjordan06@gmail.com")


if __name__ == "__main__":
    test_userdata_manager()