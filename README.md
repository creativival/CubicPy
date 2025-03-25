# CubicPy

*[日本語](https://creativival.github.io/CubicPy/README.ja.html) | English*

![CubicPy Logo](https://creativival.github.io/CubicPy/assets/cubicpy_logo.png)

CubicPy - A 3D programming learning app for placing and building physics objects with code

Call it "CubicPy" - or simply "CuPy" for short!

## Application Description

CubicPy is an application that allows you to place objects in 3D space using Python code and build worlds that operate with realistic physics simulations. You can freely place boxes, spheres, and other objects to create structures and learn programming while experiencing physical laws such as gravity and collisions.

![CubicPy Sample Animation Gif](https://creativival.github.io/CubicPy/assets/cubicpy_sample.gif)

The constructed objects and structures can be observed undergoing realistic collapse processes by tilting the ground using physics simulations. You can also change the gravity factor to observe physical behavior under different gravitational environments.

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
cubicpy --example box_tower_sample
cubicpy -e box_tower_sample

# Run your own Python file
cubicpy my_script.py

# Run with modified gravity factor (specifies the power of 10 to multiply gravity by)
cubicpy --gravity 0.01 --example box_tower_sample
cubicpy -g 0.01 -e box_tower_sample

# Run with custom window size (1280x720)
cubicpy -e box_tower_sample -w 1280,720
cubicpy --window-size 1280,720 -e box_tower_sample
```

## Sample Code Examples

### Creating a Tower of Boxes (box_tower_sample.py)

![Sample box tower](https://creativival.github.io/CubicPy/assets/box_tower.png)


```python
# Create an array of object data
body_data = []

# Stack 10 levels of boxes
for i in range(10):
    body_data.append({
        'type': 'box',
        'pos': (0, 0, i),  # Position: x, y, z
        'scale': (1, 1, 1),  # Size: width, depth, height
        'color': (i/10, 0, 1-i/10),  # Color: red, green, blue (0-1)
        'mass': 1  # Mass (optional)
    })
```

## Object Definition Details (for cubicpy command)

Details of object definitions to add to the `body_data` list:

| Parameter | Description | Required | Default Value |
|------------|------|------|--------|
| `type` | Object type: 'box', 'sphere', 'cylinder' | Required | - |
| `pos` | Position coordinates (x, y, z) | Required | - |
| `scale` | Size (width, depth, height) | Optional | (1, 1, 1) |
| `color` | Color (red, green, blue) - values from 0 to 1 | Optional | (0.5, 0.5, 0.5) |
| `mass` | Mass (0: fixed object) | Optional | 1 |
| `color_alpha` | Transparency (0: transparent to 1: opaque) | Optional | 1 |
| `hpr` | Rotation angles (heading, pitch, roll) | Optional | (0, 0, 0) |
| `position_mode` | Position reference | Optional | 'corner_near_origin' |

※ `position_mode` can be set to the following values:
- `'corner_near_origin'`: The corner nearest to the origin is the reference
- `'bottom_center'`: The center of the bottom surface is the reference
- `'gravity_center'`: The center of gravity is the reference

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
app.add_box(position=(0, 0, 0), scale=(1, 1, 1), color=(1, 0, 0))
app.add_sphere(position=(2, 0, 0),  scale=(1, 1, 1), color=(0, 1, 0))
app.add_cylinder(position=(4, 0, 0),  scale=(1, 1, 1), color=(0, 0, 1))

# Adding multiple objects (loop)
for i in range(10):
    app.add_box(
        position=(0, 5, i),
        color=(i/10, 0, 1-i/10)
    )

# Adding body_data for compatibility with cubicpy command
body_data = []
for i in range(10):
    body_data.append({
        'type': 'box',
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
CubicPyApp(code_file=None, gravity_factor=0.01)
```
- `code_file`: Path to Python file to execute (optional)
- `gravity_factor`: Gravity factor (optional, default: 1)

### Object Addition Methods

#### Adding a Box
```python
add_box(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1)
```
- `position`: Position coordinates (x, y, z)
- `scale`: Size (width, depth, height)
- `color`: Color (red, green, blue) - values from 0 to 1
- `mass`: Mass (0: fixed object)
- `color_alpha`: Transparency (0: transparent to 1: opaque)

#### Adding a Sphere
```python
add_sphere(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1)
```
- Parameters are the same as `add_box`

#### Adding a Cylinder
```python
add_cylinder(position=(0, 0, 0), scale=(1, 1, 1), color=(0.5, 0.5, 0.5), mass=1, color_alpha=1)
```
- Parameters are the same as `add_box`

### Generic Object Addition

```python
add(obj_type, **kwargs)
```

- obj_type: Type of object ('box', 'sphere', 'cylinder')
- **kwargs: Object parameters (the following keyword arguments can be used)
  - position or pos: Position coordinates
  - scale: Size
  - color: Color
  - mass: Mass
  - color_alpha: Transparency

#### Building Objects from body_data List
```python
from_body_data(body_data) 
```
- `body_data`: List of object definitions (dictionaries) as used by the cubicpy command

### World Operation Methods

```python
run()  # Build and run the world
reset()  # Reset the world
```

## Building Worlds with API Mode

1. Create a CubicPyApp instance in your Python script
2. Add objects using methods like `add_box()`, `add_sphere()`, etc.
3. Call the `run()` method to build and run the world
4. If needed, use the `reset()` method to rebuild
5. Run with `python your_script.py`

## Application Controls

- **Arrow keys**: Change camera angle
- **Mouse wheel**: Zoom in/out
- **W/S/A/D**: Tilt the ground
- **F/G**: Change gravity strength
- **R**: Reset
- **Z**: Toggle debug display
- **ESC**: Exit

## Requirements

- Python 3.9 or higher
- Panda3D
- Panda3D-Bullet physics engine
- NumPy

These dependencies are automatically installed with `pip install cubicpy`.

## Copyright

Released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution

Bug reports and feature improvement suggestions are welcome via GitHub Issues or Pull Requests. New sample creation and documentation improvements are also welcome.

---

Have fun learning programming with CubicPy!
