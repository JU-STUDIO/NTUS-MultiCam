import math

def main():
    angle = float(input('Launch angle (in degrees): '))
    v = float(input('Initial velocity (in meters/second): '))
    py = float(input('Initial height (in meters): '))
    interval = float(input('Time interval (in seconds): '))

    # Convert angle to radians
    theta = math.radians(angle)
    vx = v * math.cos(theta)
    vy = v * math.sin(theta)

    print('\nThe trajectory:')
    print('    x       y')
    print('--------------')
        
    # Loop until the cannonball hits the ground
    px = 0.0
    while py >= 0.0:
        # Calculate position and velocity in interval seconds
        px += interval*vx
        vy2 = vy - interval*9.8
        py += interval*(vy+vy2)/2.0
        vy = vy2
        print(f'{px:>5.1f}\t{py:>5.1f}')    # Print the trajectory of the cannonball

    print(f'\nDistance traveled: {px:.1f} meters.')


if __name__ == '__main__':
    main()