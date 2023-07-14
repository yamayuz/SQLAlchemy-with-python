from connection.repositories.UserRepository import UserRepository


if __name__ == "__main__":
    user_repo = UserRepository()
    users = user_repo.get_all_users()
    print(users[0].first_name)
