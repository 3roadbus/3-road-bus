from pycat.core import Window,Sprite,Label,Color
window = Window()

class Path:
    def __init__(self,start,end,description):
        self.start = start
        self.end = end
        self.description = description

class Level:
    def __init__(self):
        self.stations ={}
        self.paths=[]

    def add_station(self, station):
        self.stations[station.name] = station

    def add_paths(self, path):
        self.paths.append(path)

class nextroombutton(Sprite):
    def on_create(self):
        self.color = Color.GREEN
        self.scale = 30
    
    def on_left_click(self):
        window.delete_all_labels()
        window.delete_all_sprites()

        next_sta_object = level.stations[self.next_sta_str]
        next_sta_object.showing()

class station:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def get_paths(self):
        path_for_room =[]
        for path in level.paths:
            if path.start == self.name:
                path_for_room.append(path)
        return path_for_room
    
    def showing(self):
        window.create_label(text=self.name,y=150)
        window.create_label(text=self.description, y=50)
        path_for_room = self.get_paths()
        YY=500
        for path in path_for_room:
            pl = window.create_label(text = path.description, y=YY)
            button=window.create_sprite(nextroombutton, x = pl.x, y=YY)    
            button.next_sta_str = path.end
            YY-=50

level=Level()

Central= station('Central station','You need to escape from Hong kong because a ghost is chasing you. leave here ASAP.', )
Hong_kong= station('Hong kong','You run to here to take a metro and leave, but you only find a metro to Airport, so you walk into the metro.')
hku= station('HKU','You decided to learn the knowledge, and the ghost hate smart people so it ran away.(HKU ending)')
aDMirAlTy= station('Admiralty','You got squeezed off the train, so what you gonna do now?')
lowu= station('Lo wu','Congratulations, you escaped Hong Kong and unlock the Good ending 1')
tsuenwan= station('Tsuen Wan','You have got saved by some bad guys, so you decided to join them.(Good ending 2)')
fly= station('Airport','Congratulations, you escaped Hong Kong and unlock the Good ending 3')
disney= station('Disneyland resort','You come here and have fun, but the ghost hate joy so it left.(Disney ending)')
tst= station('Tsim Sha Tsui','You just arrived and heard that can transfer to the brown line, what should you do?')
jd= station('Jordan','You got squeezed off the train, so the only way for now is take the HSR.')
kowloooooooooon=station('Kowloon','You heard that this station can transfer to the HSR, wanna transfer?')
sunny= station('Sunny Bay','You felt quite depressed, but you heard this station can transfer to the Disney, wanna transfer?')
hsr= station('HSR west Kowloon','Congratulations, you escaped Hong Kong and unlock the Good ending 4')
dongchong= station('Tung Chung','Huh, what is this place? I am missing the way out...')

level.add_paths(Path('Central station','Hong kong','Walking to Hong Kong station'))
level.add_paths(Path('Central station','Admiralty','Take island line to Admiralty station'))
level.add_paths(Path('Central station','HKU','Take island line to HKU'))
level.add_paths(Path('Hong kong','Kowloon','Continue the journey'))
level.add_paths(Path('Kowloon','Sunny Bay','leave the train and transfer into Tung Chung line'))
level.add_paths(Path('Kowloon','HSR west Kowloon','leave the train and transfer into HSR'))
level.add_paths(Path('Kowloon','HSR west Kowloon','Continue the journey'))
level.add_paths(Path('Sunny Bay','Disneyland resort','leave the train and transfer into Disney line'))
level.add_paths(Path('Sunny Bay','Tung Chung','Continue the journey'))
level.add_paths(Path('Admiralty','Tsim Sha Tsui','leave the train and transfer into Tsuen Wan line'))
level.add_paths(Path('Admiralty','Lo wu','leave the train and transfer into East rail line'))


level.add_station(Central)
level.add_station(Hong_kong)
level.add_station(hku)
level.add_station(aDMirAlTy)
level.add_station(lowu)
level.add_station(tsuenwan)
level.add_station(fly)
level.add_station(disney)
level.add_station(tst)
level.add_station(jd)
level.add_station(kowloooooooooon)
level.add_station(sunny)
level.add_station(hsr)
level.add_station(dongchong)

Central.showing()

window.run()