# controllers/users.py
class UserController:
    @staticmethod
    async def get_users():
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    @staticmethod
    async def create_user(user: dict):
        return {"message": "User created", "user": user}
