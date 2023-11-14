import random
import matplotlib.pyplot as plt


class TowerCost:
    def __init__( self, name, radius, cost ):
        self.name = name
        self.radius = radius
        self.cost = cost


class CityGrid:
    def __init__( self, row, colums, block=30 ):
        self.row = row
        self.colums = colums
        self.grid = self.generate_grid( block )
        self.towers = []


    def generate_grid( self, block ):

        grid = [[0 for _ in range( self.colums )] for _ in range( self.row )]
        total = int( ( self.row * self.colums ) * ( block / 100 ) )

        for _ in range( total ):
            row = random.randint( 0, self.row - 1 )
            col = random.randint( 0, self.colums - 1 )
            grid[row][col] = 1 

        return grid


    def place_tower( self, row, colums, radius ):

        if row < 0 or row >= self.row or colums < 0 or colums >= self.colums:
            print( "За пределами" )
            return

        self.towers.append( ( row, colums, radius ) )


    def visualize_grid( self ):

        obstacles = []
        towers = []

        for i in range( self.row ):
            for j in range( self.colums ):
                if self.grid[i][j] == 1:
                    obstacles.append( ( j, self.row - i - 1 ) ) 
                elif self.grid[i][j] == 2:
                    towers.append( ( j, self.row - i - 1 ) )  

        plt.figure( figsize=( 8, 8 ) )

        for obstacle in obstacles:
            plt.scatter( obstacle[0], obstacle[1], color='black', marker='s', s=100 )

        for tower in towers:
            plt.scatter( tower[0], tower[1], color='red', marker='^', s=150 )

            for i in range( len( self.towers ) ):
                if self.towers[i][:2] == ( self.row - tower[1] - 1, tower[0] ):
                    krug = plt.Circle( ( tower[0], tower[1] ), self.towers[i][2], color='red', fill=False )
                    plt.gcf().gca().add_artist( krug )

        plt.xlim( -1, self.colums )
        plt.ylim( -1, self.row )
        plt.gca().set_aspect( 'equal', adjustable='box' )
        plt.title( 'CityGrid с препятствиями и башнями' )
        plt.xlabel( 'X-ось' )
        plt.ylabel( 'Y-ось' )
        plt.grid( visible=True )
        plt.show()


if __name__ == "__main__":
    
    city = CityGrid( 10, 10 )

    # Определение типов вышек с разной дальностью и стоимостью
    basic_tower = TowerCost( "Минимальный", 3, 10 )
    medium_tower = TowerCost( "Средний", 5, 20 )
    advanced_tower = TowerCost( "Продвинутый", 7, 30 )

    # Добавление вышек с учетом бюджета
    money = 50
    while money > 0:
        choice = random.choice( [basic_tower, medium_tower, advanced_tower] )
        if choice.cost <= money:
            row = random.randint( 0, city.row - 1 ) 
            col = random.randint( 0, city.colums - 1 )
            city.place_tower( row, col, choice.radius )
            money -= choice.cost

    city.visualize_grid()  # Визуализация сетки города с учетом различных типов вышек