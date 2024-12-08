from pydantic import BaseModel, EmailStr, Field, field_validator
import bcrypt
import re


class UserSchema(BaseModel):
    username: str = Field(
        ..., max_length=15, description="Username must be 15 characters or fewer."
    )
    email: EmailStr
    first_name: str = Field(
        ..., max_length=50, description="First name must be 50 characters or fewer."
    )
    last_name: str = Field(
        ..., max_length=50, description="Last name must be 50 characters or fewer."
    )
    phone_number: str = Field(
        ..., max_length=10, description="Phone number must be 15 characters or fewer."
    )
    password: str = Field(
        ..., min_length=8, description="Password must be at least 8 characters long."
    )

    @field_validator("password", mode="before")
    @classmethod
    def validate_and_hash_password(cls, value: str) -> str:
        """Validate and hash the password."""
        if not value:
            raise ValueError("Password cannot be empty.")

        # Regular expression for validation
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must include at least one uppercase letter.")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must include at least one lowercase letter.")
        if not re.search(r"\d", value):
            raise ValueError("Password must include at least one numeric digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError("Password must include at least one special character.")

        # Hash the password
        return bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
