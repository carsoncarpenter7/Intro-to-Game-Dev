#! /usr/bin/env python3
# Carson Carpenter
# CPSC 386-02
# 2022-04-24
# carson.carpenter7@csu.fullerton.edu
# @carsoncarpenter7
#
# Lab 05-00
#
# This my Pygame game program with of bouncing balls
#

"""A Ball class for the bouncing ball demo."""

import os.path
from random import randint
from math import isclose
import pygame
from game import rgbcolors

# python3 -m venv env
# source env/bin/activate
# pip install -r requirements.txt


def random_velocity(min_val=1, max_val=3):
    """Generate a random velocity in a plane, return it as a Vector2"""
    random_x = randint(min_val, max_val)
    random_y = randint(min_val, max_val)
    if randint(0, 1):
        random_x *= -1
    if randint(0, 1):
        random_y *= -1
    return pygame.Vector2(random_x, random_y)


def random_color():
    """Return a random color."""
    return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))


# This is the class we discussed in class. You can have this as a standalone
# definition of a circle's geometry or you can fold the Circle and Ball classes
# together into a single class definition. Your choice.
class Circle:
    """Class representing a circle with a bounding rect."""

    def __init__(self, center_x, center_y, radius):
        self._center = pygame.Vector2(center_x, center_y)
        self._radius = radius

    @property
    def radius(self):
        """Return the circle's radius"""
        return self._radius

    @property
    def center(self):
        """Return the circle's center."""
        return self._center

    @property
    def rect(self):
        """Return bounding Rect; calculate it and create a new Rect instance"""
        upper_left_x = self._center[0] - self._radius
        upper_left_y = self._center[1] - self._radius
        return pygame.Rect(upper_left_x, upper_left_y, self.width, self.height)

    @property
    def width(self):
        """Return the width of the bounding box the circle is in."""
        return 2 * self._radius

    @property
    def height(self):
        """Return the height of the bounding box the circle is in."""
        return 2 * self._radius

    def squared_distance_from(self, other_circle):
        """Squared distance from self to other circle."""
        return (other_circle._center - self._center).length_squared()

    def distance_from(self, other_circle):
        """Distance from self to other circle"""
        return (other_circle._center - self._center).length()

    def move_ip(self, x, y):
        """Move circle in place, update the circle's center"""
        self._center = self._center + pygame.Vector2(x, y)

    def move(self, x, y):
        """Move circle, return a new Circle instance"""
        new_center = self._center + pygame.Vector2(x, y)
        return Circle(new_center[0], new_center[1], self._radius)

    def stay_in_bounds(self, xmin, xmax, ymin, ymax):
        """Update the position of the circle so that it remains
        within the rectangle defined by xmin, xmax, ymin, ymax."""
        new_center = self._center + pygame.Vector2(xmin, ymin)
        new_center1 = self._center + pygame.Vector2(xmax, ymax)
        return new_center + new_center1


class Ball:
    """A class representing a moving ball."""

    default_radius = 25

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")
    # Feel free to change the sounds to something else.
    # Make sure you have permssion to use the sound effect file and document
    # where you retrieved this file, who is the author, and the terms of
    # the license.
    bounce_sound = os.path.join(data_dir, "Boing.aiff")
    reflect_sound = os.path.join(data_dir, "Monkey.aiff")

    def __init__(self, name, center_x, center_y, sound_on=True):
        """Initialize a bouncing ball."""
        # The name can be any string. The best choice is an integer.
        self._name = name
        # Yes, we could define the details about our geometry in the Ball
        # class or we can define the geometry in an instance variable.
        # It is up to you if you want to separate them out or integrate them
        # together.
        self._circle = Circle(center_x, center_y, Ball.default_radius)
        self._color = random_color()
        self._velocity = random_velocity()
        self._sound_on = sound_on
        self._bounce_count = randint(5, 10)
        self._is_alive = True
        self._draw_text = False
        font = pygame.font.SysFont(None, Ball.default_radius)
        self._name_text = font.render(str(self._name), True, rgbcolors.black)
        try:
            self._bounce_sound = pygame.mixer.Sound(Ball.bounce_sound)
            self._bounce_channel = pygame.mixer.Channel(2)
        except pygame.error as pygame_error:
            print(f"Cannot open {Ball.bounce_sound}")
            raise SystemExit(1) from pygame_error
        try:
            self._reflect_sound = pygame.mixer.Sound(Ball.reflect_sound)
            self._reflect_channel = pygame.mixer.Channel(3)
        except pygame.error as pygame_error:
            print(f"Cannot open {Ball.reflect_sound}")
            raise SystemExit(1) from pygame_error

    def toggle_draw_text(self):
        """Toggle the debugging text where each circle's name is drawn."""
        self._draw_text = not self._draw_text

    def draw(self, surface):
        """Draw the circle to the surface."""
        pygame.draw.circle(surface, self.color, self.center, self.radius)
        if self._draw_text:
            surface.blit(
                self._name_text, self._name_text.get_rect(center=self._circle.center)
            )

    def wall_reflect(self, xmin, xmax, ymin, ymax):
        """Reflect the ball off of a wall,
        play a sound if the sound flag is on."""
        if (
                self._circle.center.x >= xmax
                or (self._circle.center.x - self.radius) <= xmin
        ):
            print("\nHitting Right or Left Wall\n")
            self._velocity.x = self._velocity.x * -1

        if (
                self._circle.center.y >= ymax
                or (self._circle.center.y - self.radius) <= ymin
        ):
            print("\nHitting Top or Bottom Wall\n")
            self._velocity.y = self._velocity.y * -1
        # else:
        #     print("This is an error look at wall_reflect in Ball.py")
        #     exit(1)

    def bounce(self, other_ball):
        """Bounce the ball off of another ball,
        play a sound if the ball is no alive."""
        normal = self._circle.center - other_ball._circle.center
        # print(f'self = {self}')
        # print(f'normal = {normal}')
        self._velocity = self._velocity.reflect(normal)

    def collide_with(self, other_ball):
        """Return true if self collides with other_ball."""
        distance = self.circle.distance_from(other_ball.circle)
        return distance <= (self.radius + other_ball.radius)

    def separate_from(self, other_ball, rect):
        """Separate a ball from the other ball
        so they are no longer overlapping."""
        distance_between_centers = self._circle.distance_from(other_ball._circle)
        ideal_distance = self.radius + other_ball.radius
        move_distance = ideal_distance - distance_between_centers
        rect = move_distance / 2

        velocity = self._velocity * -1
        scaled_velocity = velocity * rect
        self._circle.move_ip(*scaled_velocity)

        velocity = other_ball._velocity * -1
        scaled_velocity = velocity * rect
        self._circle.move_ip(*scaled_velocity)

    @property
    def name(self):
        """Return the ball's name."""
        return self._name

    @property
    def rect(self):
        """Return the ball's rect."""
        return self._circle.rect

    @property
    def circle(self):
        """Return the ball's circle."""
        return self._circle

    @property
    def center(self):
        """Return the ball's center."""
        return self._circle.center

    @property
    def radius(self):
        """Return the ball's radius"""
        return self._circle.radius

    @property
    def color(self):
        """Return the color of the ball."""
        return self._color

    @property
    def velocity(self):
        """Return the velocity of the ball."""
        return self._velocity

    @property
    def is_alive(self):
        """Return true if the ball is still alive."""
        flag = True
        if self.is_alive == flag:
            return True
        return False

    def toggle_sound(self):
        """Turn off the sound effects."""
        self._sound_on = False

    def too_close(self, x_axis, y_axis, min_dist):
        """Is the ball too close to some point by some min_dist?"""
        if min_dist < self._circle:
            x_axis = self._circle
            y_axis = self._circle
            isclose(x_axis + y_axis)
            return True
        return False

    def stop(self):
        """Stop the ball from moving."""
        self._velocity = pygame.Vector2(0, 0)

    def set_velocity(self, x, y):
        """Set the ball's velocity."""
        self._velocity = pygame.Vector2(x, y)

    def update(self):
        """Update the ball's position"""
        self._circle.move_ip(*self._velocity)
        # print(str(self))

    def __str__(self):
        """Ball stringify."""
        return f"Ball name = {self.name}, \
            center = {self.circle.center}, \
                color = {self.color}, velocity = {self.velocity}"
