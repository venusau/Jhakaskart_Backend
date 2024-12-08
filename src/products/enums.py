from enum import Enum

# Enum for Product Types


class PRTypeEnum(Enum):
    CLOTHING = "Clothing"
    ELECTRONICS = "Electronics"
    FURNITURE = "Furniture"
    BOOKS = "Books"
    GROCERIES = "Groceries"
    HYGIENE_PRODUCTS = "Hygiene Products"
    MEDICINES = "Medicines"
    FOOD_AND_BEVERAGES = "Food and Beverages"
    JEWELRY = "Jewelry"
    WATCHES = "Watches"
    HANDBAGS = "Handbags"
    VEHICLES = "Vehicles"
    SHELTER_RELATED_GOODS = "Shelter-related Goods"


class StatusEnum(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
