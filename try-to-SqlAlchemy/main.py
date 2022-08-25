from connection.repositories.OperateUserRepository import OperateUserRepository


if __name__ == "__main__":
    users = OperateUserRepository()
    user_select_result = users.select_Users()
    print(user_select_result[0].first_name)
