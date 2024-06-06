import unittest

# import main
import particle
import pygame as pyg
from pygame import *


class MatrixTest(unittest.TestCase):
    def test_velocity_half_life(self):
        p1 = particle.Particle(2, 1, 0)
        # p2 = particle.Particle(2, 0, 0)
        p1.update()
        self.assertEqual(p1.applied_force, p1.velocity)

    def test_particle_nearby(self):
        p1 = particle.Particle(2, 0, 0)
        p2 = particle.Particle(2, 0.5, 0)
        p3 = particle.Particle(2, 4, 0)
        p4 = particle.Particle(2, 6, 0)
        particles = [p1, p2, p3, p4]
        nearby_particles = p1.find_nearby_particles(particles, 5)
        self.assertIn(p2, nearby_particles[0], "to_Close")
        self.assertIn(p3, nearby_particles[1], "in_radius")
        self.assertNotIn(p4, nearby_particles[0] and nearby_particles[1], "not there")

    def test_0_nearby_particles(self):
        p1 = particle.Particle(1, 0, 0)
        n = p1.find_nearby_particles([p1], 5)
        p1.resulting_calculated_forces(n)
        self.assertEqual(p1.applied_force, Vector2(0, 0))


if __name__ == "__main__":
    unittest.main()
