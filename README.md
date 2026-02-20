# Spatial Object Systems: Shapely, Inheritance, and Structured Data

---

## Environment Setup
- Python 3.14
- `pandas`, `matplotlib`, `shapely` 

---

## How to Run
1. Activate the virtual environment
2. Run `demo.py` to test the spatial classes

---

## Reflection
For the first part, I shifted the Point class from holding raw lon, lat numbers to encapsulating a Shapely geometry (`self.geometry`), so the object now carries both data and the spatial behavior that goes with it, not just coordinates. From the outside, nothing changed for users of the class, methods like `to_tuple()` and `distance_to()` still behave the same because this was a true refactoring, I changed how the class works internally without changing how it is used. Crucially, I moved spatial math out of my custom code and into the geometry engine like distances, coordinate access, and bounds come from Shapely now, which aligns with the lecture’s design idea to delegate geometry to a professional engine instead of reimplementing formulas in each class.

Moving to the next part, I realized how useful it is to have a shared base class like `SpatialObject`, because it captures the common idea that all spatial features simply exist in space and have geometry, without forcing each class to reimplement the same logic. By letting Point and Parcel inherit from it, I avoided repeating code and made the structure cleaner, since they both automatically gain behaviors like `bbox()` from a single definition. Storing parcel information in a dictionary also made sense because it keeps the attributes flexible and structured, while the class still controls how that information is used. What stood out most is how adding shared behavior in the base class immediately applies to all subclasses, which makes the system easier to scale. New spatial types can be added without rewriting geometry logic, just like the lecture emphasized about shared abstraction in spatial systems.