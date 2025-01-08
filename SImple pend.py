import numpy as np
import matplotlib.pyplot as plt

def pendulum_motion(theta0, L, g, t_max, dt):
    t = np.arange(0, t_max, dt)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    energy = np.zeros(len(t))

    theta[0] = np.radians(theta0)

    for i in range(1, len(t)):
        omega[i] = omega[i - 1] - (g / L) * np.sin(theta[i - 1]) * dt
        theta[i] = theta[i - 1] + omega[i] * dt
        energy[i] = 0.5 * (L * omega[i])**2 + g * L * (1 - np.cos(theta[i]))

    return t, theta, energy

def plot_motion(t, theta, energy):
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t, np.degrees(theta), color='blue')
    plt.title("Pendulum Motion")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (degrees)")

    plt.subplot(1, 2, 2)
    plt.plot(t, energy, color='red')
    plt.title("Energy of the Pendulum")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")

    plt.tight_layout()
    plt.show()

def main():
    print("Welcome to the Pendulum Motion Simulator!")
    try:
        theta0 = float(input("Enter the initial angle (deg): "))
        L = float(input("Enter the length of the pendulum (m): "))
        g = 9.81
        t_max = float(input("Enter the simulation duration (s): "))
        dt = float(input("Enter the time step for the simulation (s): "))

        print("\nSimulating pendulum motion... Please wait!")
        t, theta, energy = pendulum_motion(theta0, L, g, t_max, dt)
        plot_motion(t, theta, energy)

    except ValueError:
        print("Invalid input! .")

if __name__ == "__main__":
    main()
