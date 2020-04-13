import random
"""
  This class will draw the night sky represented as a 2D array.
  For usage example see end of file

  In the constructor you specify 
  1) Height 
  2) Width 
  3) Start fill percentage (0<= perc <= 1),
  which shows how many of the cells are filled up with stars (see 'star_symbol' variable).
  
  All the other parts are filled in with 'empty_symbol' variable and indicate
  a clear sky
"""
class NightSky:

  empty_symbol='.'
  star_symbol='*'

  def __init__(self,h,w,star_fill_perc):
    self.w = w
    self.h = h
    self.grid = [[ self.empty_symbol for col in range(w)] for row in range(h)]
    self.add_stars(star_fill_perc)


  def __str__(self):
    return self.create_grid_str()

  def add_stars(self, perc):
    n_rows = len(self.grid)
    n_columns = len(self.grid[0])
    n_elem = n_rows*n_columns
    n_stars = int(n_elem*perc)

    free_pos_list = self.init_free_pos_list(n_rows, n_columns)
    for n_star in range(0, n_stars):
        rand_pos_idx = random.randint(0, len(free_pos_list)-1)
        free_pos = free_pos_list[rand_pos_idx]
        self.grid[free_pos[0]][free_pos[1]] = self.star_symbol
        free_pos_list.remove(free_pos)

    
  def init_free_pos_list(self,n_rows, n_columns):
    free_pos_list = []
    for row in range(0, n_rows):
        for column in range(0, n_columns):
            free_pos_list.append((row, column))
    return free_pos_list


  def create_grid_str(self):
    grid_str=""
    for row in self.grid:
        row_str = self.create_row_str(row)
        grid_str=grid_str+row_str+"\n"
    
    grid_str=grid_str[:-1]
    return grid_str

  def create_row_str(self,row):
    row_str = ""
    for col in row:
        row_str += str(col)
    return row_str


if __name__ == "__main__":
    sky = NightSky(20,20,0.3)
    print(sky)
