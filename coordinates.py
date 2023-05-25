import constants



def make_step_back_for_x_or_y(coord: float, dimention: int) -> float:
    result = coord - constants.STEP*constants.dt
    return result if result > dimention else coord



def make_step_forwafd_for_x_or_y(coord: float, dimention: int) -> float:
    result = coord + constants.STEP*constants.dt
    return result if result < dimention - 20 else coord


def make_wall_coordinates_list() -> list[list[int]]:
    x = 0
    y = 0
    wall_coordinates_list = []

    number_of_horisontal_blocks = constants.WIDTH // constants.WALL_SIZE
    number_of_vertical_blocks = constants.HEIGHT // constants.WALL_SIZE

    for _ in range(number_of_horisontal_blocks):
        wall_coordinates_list.append([x, 0])
        wall_coordinates_list.append([x, constants.HEIGHT - constants.WALL_SIZE])
        x+=constants.WALL_SIZE
       
    for _ in range(number_of_vertical_blocks - 2):
        y += 20
        wall_coordinates_list.append([0, y])
        wall_coordinates_list.append([constants.WIDTH - constants.WALL_SIZE, y])
                  
    return wall_coordinates_list
