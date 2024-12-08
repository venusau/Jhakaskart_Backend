from datetime import datetime
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, declarative_base
from commons import Brand, Image

Base = declarative_base()


class User(Base):
    """User model representing application users."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(15), nullable=False, unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(15), nullable=False)
    brand_id = Column(
        Integer, ForeignKey("brands.id", ondelete="SET NULL"), nullable=True
    )  # Optional relationship
    password = Column(String, nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.now(datetime.UTC),
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(datetime.UTC),
        onupdate=datetime.now(datetime.UTC),
        nullable=False,
    )

    # Relationships
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    roles = relationship("Role", secondary="user_role_mappings", back_populates="users")
    brand = relationship("Brand", back_populates="users")  # Link to Brand


class Address(Base):
    """Address model for storing user addresses."""

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    address = Column(String(120), nullable=False)
    pincode = Column(String(6), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.now(datetime.UTC),
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(datetime.UTC),
        onupdate=datetime.now(datetime.UTC),
        nullable=False,
    )

    # Relationships
    user = relationship("User", back_populates="addresses")


class Role(Base):
    """Role model for user authorization."""

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now(datetime.UTC), nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.now(datetime.UTC),
        onupdate=datetime.now(datetime.UTC),
        nullable=False,
    )

    # Relationships
    users = relationship("User", secondary="user_role_mappings", back_populates="roles")


class UserRoleMapping(Base):
    """Mapping table for user-role many-to-many relationship."""

    __tablename__ = "user_role_mappings"

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    role_id = Column(
        Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    )
    created_at = Column(DateTime, default=datetime.now(datetime.UTC), nullable=False)

    __table_args__ = (UniqueConstraint("user_id", "role_id", name="unique_user_role"),)
