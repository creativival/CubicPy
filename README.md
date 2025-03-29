# CubicPy

*[日本語](https://creativival.github.io/CubicPy/README.ja.html) | English*

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

CubicPy - A 3D programming learning app for placing and building physics objects with code

Call it "CubicPy" - or simply "CuPy" for short!

## Application Description

CubicPy is an application that allows you to place objects in 3D space using Python code and build worlds that operate with realistic physics simulations. You can freely place boxes, spheres, and other objects to create structures and learn programming while experiencing physical laws such as gravity and collisions.

![CubicPy Sample Animation Gif](https://creativival.github.io/CubicPy/assets/cubicpy_sample.gif)

The constructed objects and structures can be observed undergoing realistic collapse processes by tilting the ground or removing objects using physics simulations. You can also change the gravity factor to observe physical behavior under different gravitational environments. Additionally, you can set initial velocity vectors for objects and launch them.

## Installation

```
pip install cubicpy
```

## Using the cubicpy Command

After installation, you can easily run from the command line:

```
# Run a randomly selected sample code
cubicpy

# Display help
cubicpy --help
cubicpy -h

# Display sample list
cubicpy --list
cubicpy -l

# Run a specific sample
cubicpy --example cube_tower_sample
cubicpy -e cube_tower_sample

# Run your own Python file
cubicpy your_body_data_script.py

# Run with modified gravity factor (specifies the power of 10 to multiply gravity by)
cubicpy --gravity 0.01 --example cube_tower_sample
cubicpy -g 0.01 -e cube_tower_sample

# Run with custom window size (1280x720)
cubicpy -e cube_tower_sample -w 1280,720
cubicpy --window-size 1280,720 -e cube_tower_sample

# Run with specific camera lens type (perspective or orthographic)
cubicpy -e cube_tower_sample -c orthographic
cubicpy --camera-lens orthographic -e cube_tower_sample
```

## Sample Code Examples

### Creating a Tower of Boxes (cube_tower_sample.py)

![Sample cube tower](https://creativival.github.io/CubicPy/assets/cube_tower.png)

```python
# Create an array of object data
body_data = []

# Stack 10 levels of cubes
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (0, 0, i),  # Position: x, y, z
        'scale': (1, 1, 1),  # Size: width, depth, height
        'color': (i/10, 0, 1-i/10),  # Color: red, green, blue (0-1)
        'mass': 1  # Mass (optional)
    })
```

### Launching Objects with Initial Velocity Vectors

```python
# Create a projectile
body_data.append({
    'type': 'sphere',
    'pos': (5, 5, 2),  # Position: x, y, z
    'scale': (1, 1, 1),  # Size
    'color': (1, 0, 0),  # Red color
    'mass': 5,  # Mass
    'vec': (10, -5, 3)  # Initial velocity vector: x, y, z direction
})
```

## Object Definition Details (for cubicpy command)

Details of object definitions to add to the `body_data` list:

| Parameter    | Description                                   | Required | Default Value     |
|--------------|-----------------------------------------------|----------|-------------------|
| `type`       | Object type: 'cube', 'sphere', 'cylinder'     | Required | -                 |
| `pos`        | Position coordinates (x, y, z)                | Required | -                 |
| `scale`      | Size (width, depth, height)                   | Optional | (1, 1, 1)         |
| `color`      | Color (red, green, blue) - values from 0 to 1 | Optional | (0.5, 0.5, 0.5)   |
| `mass`       | Mass (0: fixed object)                        | Optional | 1                 |
| `color_alpha`| Transparency (0: transparent to 1: opaque)    | Optional | 1                 |
| `hpr`        | Rotation degree angles (heading, pitch, roll) | Optional | (0, 0, 0)         |
| `base_point` | Position reference point                      | Optional | 0                 |
| `remove`     | Removed Object                                | Optional | False             |
| `vec`        | Initial velocity vector (x, y, z)             | Optional | (0, 0, 0)         |

※ `base_point` can be set to the following values:
- `0`: The corner nearest to the origin is the reference
- `1`: The center of the bottom surface is the reference
- `2`: The center of gravity is the reference

## Building Worlds with the cubicpy Command

1. Create a Python file in the format of the sample
2. Run it with the `cubicpy your_file.py` command

## Sample Code for API Mode

![Sample api mode](https://creativival.github.io/CubicPy/assets/sample_api_mode.png)

```python
from cubicpy import CubicPyApp

# Instantiate
app = CubicPyApp(gravity_factor=0.01)

# Adding individual objects
# Add objects using API
app.add_cube(position=(0, 0, 0), scale=(1, 1, 1), color=(1, 0, 0))
app.add_sphere(position=(2, 0, 0),  scale=(1, 1, 1), color=(0, 1, 0))
app.add_cylinder(position=(4, 0, 0),  scale=(1, 1, 1), color=(0, 0, 1))

# Add an object with initial velocity vector
app.add_sphere(
    position=(5, 5, 2),
    scale=(1, 1, 1),
    color=(1, 0, 0),
    mass=5,
    vec=(10, -5, 3)  # Will be launched when space key is pressed
)

# Adding multiple objects (loop)
for i in range(10):
    app.add_cube(
        position=(0, 5, i),
        color=(i/10, 0, 1-i/10)
    )

# Adding body_data for compatibility with cubicpy command
body_data = []
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (0, 10, i),
        'scale': (1, 1, 1),
        'color': (i / 10, 0, 1 - i / 10),
        'mass': 1,
        'color_alpha': 1,
    })

app.from_body_data(body_data)

# Run simulation
app.run()
```

## API Mode Method Details

### CubicPyApp Class

```python
CubicPyApp(code_file=None, gravity_factor=1, window_size=(900, 600), camera_lens='perspective')
```
- `code_file`: Path to Python file to execute (optional)
- `gravity_factor`: Gravity factor (optional, default: 1)
- `window_size`: Window size (optional, default: (900, 600))
- `camera_lens`: Camera lens type ('perspective' or 'orthographic', optional, default: 'perspective')

### Object Addition Methods

#### Adding a Box
```python
add_cube(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1, hpr=(0, 0, 0), base_point=0, remove=False, vec=(0, 0, 0))
```
- `position`: Position coordinates (x, y, z)
- `scale`: Size (width, depth, height)
- `color`: Color (red, green, blue) - values from 0 to 1
- `mass`: Mass (0: fixed object)
- `color_alpha`: Transparency (0: transparent to 1: opaque)
- `hpr`: Rotation degree angles (heading, pitch, roll)
- `base_point`: Position reference point
- `remove`: Removed object (Boolean)
- `vec`: Initial velocity vector (x, y, z) - applied when space key is pressed

#### Adding a Sphere
```python
add_sphere(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1, hpr=(0, 0, 0), base_point=0, remove=False, vec=(0, 0, 0))
```
- Parameters are the same as `add_cube`

#### Adding a Cylinder
```python
add_cylinder(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1, hpr=(0, 0, 0), base_point=0, remove=False, vec=(0, 0, 0))
```
- Parameters are the same as `add_cube`

### Generic Object Addition

```python
add(obj_type, **kwargs)
```

- obj_type: Type of object ('cube', 'sphere', 'cylinder')
- **kwargs: Object parameters (the following keyword arguments can be used)
  - position or pos: Position coordinates
  - scale: Size
  - color: Color
  - mass: Mass
  - color_alpha: Transparency
  - hpr: Rotation degree angles (heading, pitch, roll)
  - base_point: Position reference
  - remove: Removed Object - can be deleted with the X key
  - vec: Initial velocity vector - applied when space key is pressed

#### Building Objects from body_data List
```python
from_body_data(body_data) 
```
- `body_data`: List of object definitions (dictionaries) as used by the cubicpy command

### World Operation Methods

```python
run()  # Build and run the world
reset()  # Reset the world
launch_objects()  # Launch objects with initial velocity vectors (also triggered by space key)
```

## Building Worlds with API Mode

1. Create a CubicPyApp instance in your Python script
2. Add objects using methods like `add_cube()`, `add_sphere()`, etc.
3. Call the `run()` method to build and run the world
4. If needed, use the `reset()` method to rebuild
5. Run with `python your_script.py`

## Application Controls

- **Arrow keys**: Change camera angle
- **SHIFT + Arrow keys**: Move camera target point
- **SHIFT + Page Up/Down**: Move camera target point forward/backward
- **Mouse wheel**: Zoom in/out (perspective mode) or change display range (orthographic mode)
- **W/S/A/D**: Tilt the ground
- **F/G**: Change gravity strength
- **R**: Reset (also resets camera position and target point)
- **Z**: Toggle debug display
- **X**: Remove selected objects one by one
- **Space key**: Launch objects with velocity vectors (`vec`)
- **ESC**: Exit

## Requirements

- Python 3.9 or higher
- Panda3D
- NumPy

These dependencies are automatically installed with `pip install cubicpy`.

## Copyright

Released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution

Bug reports and feature improvement suggestions are welcome via GitHub Issues or Pull Requests. New sample creation and documentation improvements are also welcome.

---

Have fun learning programming with CubicPy!