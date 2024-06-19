#Imports
from json import dumps
from functions import itemFromName, itemFromID, generateOutsideItem
from variables import ViewMultipliers






#Save Handling Class
class SaveFileHandler:
    def __init__(self, mainInformation):
        self.saveslot = mainInformation['SaveIndex']
        self.id = mainInformation['SaveID']
        self.seed = mainInformation['MatchSeed']


        self.day = mainInformation['CurrentQuotaDay']
        self.week = int((mainInformation['CurrentDay'] - self.day) / 3 + 1)
        self.time = mainInformation['TimeOfDay']

        self.money = mainInformation['Money']
        self.views = mainInformation['CurrentQuota']

        self.map = mainInformation['LastPlayedLevel']

        self.houseItems = mainInformation['InventoryItems']
        self.outsideItems = mainInformation['SurfaceItems']

        self.networkDeals = mainInformation['PickableNetworkDeals']
    


    def UncompressViews(self) -> None:
        global ViewMultipliers
        self.views *= ViewMultipliers[self.week]
        self.views = int(self.views)
    


    def CompressViews(self) -> None:
        global ViewMultipliers
        self.views /= ViewMultipliers[self.week]
        self.views = int(self.views)
    

    #Have this here for future.
    def listNetworkDeal(self, deal: dict) -> list:
        global NetworkDeals

        name = NetworkDeals['ID'][deal['dealType'].split(',')[0]]
        reward = {'DealRewardMeta_2' : 'Meta Coins', 'NetworkRewardMoney' : 'Money'}[deal['rewardType'].split(',')[0]]
        difficulty = {10 : 'Very Easy', 50 : 'Easy', 100 : 'Medium', 150 : 'Hard', 200 : 'Very Hard'}[deal['difficulty']]

        return [name, difficulty, reward]
    

    #Have this here for future.
    def compressedNetworkDeal(self, deal: dict) -> str:
        name, difficulty, reward = self.listNetworkDeal(deal)
        return f'{name} ({difficulty}) [{reward}]'
    


    def AddItem(self, item: str, location: str) -> bool:
        try:
            if location == 'house': self.houseItems.append({'persistentID' : itemFromName(item)})
            else: self.outsideItems.append(generateOutsideItem(itemFromName(item)))
        except: return False
        return True
    


    def RemoveItem(self, index: int, location: str) -> bool:
        try:
            if location == 'house': self.houseItems.pop(index)
            else: self.outsideItems.pop(index)
        except: return False
        return True
    


    def RemoveAllItems(self, location: str) -> bool:
        try:
            if location == 'house': self.houseItems = []
            else: self.outsideItems = []
        except: return False
        return True
    


    def UpdateViews(self, value: int) -> None:
        self.views = int(value)
        self.CompressViews()
    


    def UpdateValue(self, name: str, value):
        match name:
            case 'Index': self.saveslot = int(value)          
            case 'Time': self.time = {'Morning' : 0, 'Evening' : 1}[value]
            case 'Map': self.map = {'Factory' : 0, 'Mines' : 1, 'Ship' : 2}[value]
            case 'Seed': self.seed = int(value)            
            case 'Money': self.money = int(value)                    
            case 'Week': self.week = int(value)            
            case 'Day': self.day = int(value)
            case 'Views': self.UpdateViews(int(value))
    


    #Have this here for future.
    def UpdateNetworkDeal(self, dealID: int, name: str, value: str):
        dealType, dealDifficulty, dealReward = self.listNetworkDeal(self.networkDeals[dealID])

        match name:
            case 'type' : dealType = value
            case 'difficulty' : dealDifficulty = value
            case 'reward' : dealReward = value

        dealType = NetworkDeals['NAME'][dealType]

        dealDifficulty = {
            'Very Easy' : 10,
            'Easy' : 50,
            'Medium' : 100,
            'Hard' : 150,
            'Very Hard' : 200
        }[dealDifficulty]

        dealReward = {
            'Meta Coins' : 'DealRewardMeta_2',
            'Money' : 'NetworkRewardMoney'
        }[dealReward]

        deal = {
            'difficulty' : dealDifficulty,
            'rewardType' : f'{dealReward}, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null',
            'dealType' : f'{dealType}, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null'
        }

        self.networkDeals[dealID] = deal


    @property
    def display_time(self): return {0 : 'Morning', 1 : 'Evening'}[self.time]



    @property
    def display_views(self): 
        self.UncompressViews()
        views = self.views
        self.CompressViews()
        return views


    @property
    def display_map(self): return {0 : 'Factory', 1 : 'Mines', 2 : 'Ship'}[self.map]


    @property
    def display_houseItems(self): return [itemFromID(item['persistentID']) for item in self.houseItems]


    @property
    def display_outsideItems(self): return [itemFromID(item['persistentID']) for item in self.outsideItems]

    #Have this here for future.
    @property
    def display_networkDeals(self): return [self.compressedNetworkDeal(deal) for deal in self.networkDeals]


    @property
    def formatDetails(self):
        save = ['version:2\nSerializedSave, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null']

        details = {
            'SaveIndex' : self.saveslot,
            'SaveID' : self.id,
            'MatchSeed' : self.seed,
            'CurrentDay' : (self.week - 1) * 3 + self.day,
            'CurrentQuotaDay': self.day,
            'TimeOfDay' : self.time,
            'Money' : self.money,
            'CurrentQuota' : self.views,
            'LastPlayedLevel' : self.map,
            'InventoryItems' : self.houseItems,
            'SurfaceItems' : self.outsideItems,
            'PickableNetworkDeals' : self.networkDeals
        }

        save.append(dumps(details))
        return '|'.join(save)