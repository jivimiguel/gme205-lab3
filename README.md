# Spatial Object Systems: Shapely, Inheritance, and Structured Data

## Overview
This laboratory focuses on turning basic Python classes into a more complete spatial object system by applying object‑oriented design concepts. I refactored my original Point class to use `Shapely` so that geometry handling and spatial computations are delegated to a proper geometry engine rather than manually implemented. After that, I introduced a shared abstraction through the `SpatialObject` base class, allowing different spatial entities like points and parcels to inherit common spatial behavior while adding their own meaning and attributes. The final part of the lab involved extending the system through structured data export `as_dict()`, dictionary‑based construction `from_dict()`, and shared spatial methods like `intersects()`, demonstrating how inheritance and encapsulation help create a scalable, maintainable spatial architecture.

---

## Environment Setup
- Python 3.14
- `pandas`, `matplotlib`, `shapely` 

---

## How to Run
1. Activate the virtual environment
2. Run `demo.py` to test the spatial classes
3. Run the final consolidated demo `run_lab3.py`. 

---

## Reflection
For the first part, I shifted the Point class from holding raw lon, lat numbers to encapsulating a Shapely geometry (`self.geometry`), so the object now carries both data and the spatial behavior that goes with it, not just coordinates. From the outside, nothing changed for users of the class, methods like `to_tuple()` and `distance_to()` still behave the same because this was a true refactoring, I changed how the class works internally without changing how it is used. Crucially, I moved spatial math out of my custom code and into the geometry engine like distances, coordinate access, and bounds come from Shapely now, which aligns with the lecture’s design idea to delegate geometry to a professional engine instead of reimplementing formulas in each class.

Moving to the next part, I realized how useful it is to have a shared base class like `SpatialObject`, because it captures the common idea that all spatial features simply exist in space and have geometry, without forcing each class to reimplement the same logic. By letting Point and Parcel inherit from it, I avoided repeating code and made the structure cleaner, since they both automatically gain behaviors like `bbox()` from a single definition. Storing parcel information in a dictionary also made sense because it keeps the attributes flexible and structured, while the class still controls how that information is used. What stood out most is how adding shared behavior in the base class immediately applies to all subclasses, which makes the system easier to scale. New spatial types can be added without rewriting geometry logic, just like the lecture emphasized about shared abstraction in spatial systems.

### Challenge 1: `from_dict()` Data to Object Boundary
`from_dict()` should stay thin and focus on translating structured input into constructor arguments, while all validation lives in `__init__` where class invariants are enforced in one place. This avoids duplicated rules, keeps behavior consistent as the class evolves, and matches the lab’s guidance that `from_dict()` must delegate to the constructor rather than reimplement checks.

### Challenge 2: `as_dict()` Structured Output
Exporting to a dictionary is part of the object’s responsibility boundary,  the class best understands which fields matter and how they should be presented. Keeping `as_dict()` inside the class preserves encapsulation, prevents scattered export logic in scripts, and ensures any structural change is defined once at the source. The output needs to be JSON‑ready and portable across files, tests, and APIs, so it must contain only primitives, lists or tuples, and dicts are not engine objects. If we return Shapely geometries, we leak how the class is built and create problems when saving to JSON. Converting geometry to a basic (x, y) tuple and the bounding box to a bounds tuple, keeps the representation simple and easy to use anywhere.

### Challenge 3: `intersects()` in `SpatialObject` Inheritance
Intersection is a shared spatial behavior that applies to any feature that exists in space, so it belongs in the shared abstraction which is the `SpatialObject` rather than being duplicated in each subclass. Centralizing it reduces repetition, guarantees consistent results, and reflects the lecture’s principle that common spatial capabilities should live in the common ancestor. Nothing beyond inheriting from `SpatialObject` and supplying a valid geometry. The subclass inherits `intersects()` automatically. This works because the method delegates to the geometry engine and relies only on the shared geometry attribute guaranteed by the base class.