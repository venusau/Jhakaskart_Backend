from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Float,
    Boolean,
    JSON,
    ARRAY,
)
from sqlalchemy.orm import relationship, validates, declarative_base
from enum import Enum
from enums import PRTypeEnum, StatusEnum

Base = declarative_base()


# PRType Table for Product Categories
class PRType(Base):
    __tablename__ = "pr_type"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False, unique=True)

    @validates("type")
    def validate_type(self, key, value):
        """Validate that the type is in PRTypeEnum."""
        if value not in PRTypeEnum._value2member_map_:
            raise ValueError(
                f"Invalid type: {value}. Must be one of {list(PRTypeEnum._value2member_map_.keys())}."
            )
        return value

    # Relationships
    discounts = relationship("Discount", back_populates="pr_type")
    products = relationship("Product", back_populates="pr_type")


# Discount Table for Brand-Specific Discounts
class Discount(Base):
    __tablename__ = "discounts"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(
        Integer, ForeignKey("brands.id", ondelete="CASCADE"), nullable=False
    )
    pr_type_id = Column(
        Integer, ForeignKey("pr_type.id", ondelete="CASCADE"), nullable=False
    )
    discount = Column(Integer, nullable=False)  # Discount percentage (0-100)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    @validates("discount")
    def validate_discount(self, key, value):
        """Validate that discount is between 0 and 100."""
        if value < 0 or value > 100:
            raise ValueError(f"Discount must be between 0 and 100. Received: {value}")
        return value

    # Relationships
    pr_type = relationship("PRType", back_populates="discounts")
    brand = relationship("Brand", back_populates="discounts")


class Product(Base):
    def __init__(self, session):
        self.session = session

    __tablename__ = "products"

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    type = Column(Integer, ForeignKey("pr_type.id"), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=False)
    dimensions = Column(JSON, nullable=True)  # Corrected to use JSON column
    image_ids = Column(
        ARRAY(Integer, ForeignKey("imgages.id")), nullable=False
    )  # Store array of foreign keys
    vendor_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )  # Fixed reference to `users` table
    status = Column(
        String, nullable=False, default=StatusEnum.ACTIVE.value
    )  # Store status as a string

    # Relationships
    pr_type = relationship("PRType", back_populates="products")
    brand = relationship("Brand", back_populates="products")
    vendor = relationship("User", back_populates="products")

    @validates("status")
    def validate_status(self, key, value):
        """Validate that the status is in StatusEnum."""
        if value not in StatusEnum._value2member_map_:
            raise ValueError(
                f"Invalid status: {value}. Must be one of {list(StatusEnum._value2member_map_.keys())}."
            )
        return value


class Cart(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    qty = Column(Integer, nullable=False)
