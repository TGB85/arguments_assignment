# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line
def greet(name, greeting="Hello, <name>!"):
    greet_msg = greeting.replace("<name>", name)
    return greet_msg


# print(greet('Doc'))
# print(greet('Bob', "What's up, <name>!"))


def force(mass, body="earth"):
    bodies = {
        "sun": 274.0,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    return round(mass * bodies[body], 2)


# print(force(0.1))


def pull(m1, m2, d):
    grav_constant = 6.674 * 10**-11
    return grav_constant * ((m1 * m2) / d**2)


# print(pull(800, 1500, 3))
# print(pull(m1=0.1, m2=(5.972*10**24), d=(6.371*10**6)))
# moon and earth
# earth_mass = 5.972 * 10**24
# moon_mass = 7.342 * 10**22
# print(pull(m1=earth_mass, m2=moon_mass, d=3840000))
