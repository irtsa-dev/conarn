#Imports
from os import environ






#Global Variables
animationFolder = 'assets/animations'

saveFolder = f'C:\\Users\\{environ['USERNAME']}\\AppData\\LocalLow\\Landfall Games\\Content Warning\\Saves'

Items = {
    'ID' : {
        "fd581672-b8a9-408b-8c3e-75c84f21bdbc" : "apple",
        "f3878af1-a47d-42d9-9458-3fcbe1427fd1" : "flare",
        "fa3ef47d-320b-40f0-b6b6-b406552d7de2" : "flashlightOld",
        "03b445ad-56cb-4549-ad03-9ae1538c8ac3" : "flashlightModern",
        "ec3f00e6-82a8-4333-acb5-6bb8776ac28c" : "flashlightModernPro",
        "e873cd77-de94-436f-91d5-c98675088a95" : "flashlightLong",
        "88dbcae0-7dde-4df3-8030-e6fbc1cddc3b" : "flashlightLongPro",
        "54bdd6a9-8fd6-492f-a970-9a71e5b889ff" : "boomMic",
        "e4a1770e-12a8-4676-98f7-9a55da51694d" : "soundPlayer",
        "cfdeedb1-994d-4423-8ec1-2fb46da086f0" : "clapper",
        "279edcd0-2286-4d55-a0fa-3936c203416a" : "rescueHook",
        "1ddde64a-e09d-46c8-b06b-edbaf6966e19" : "partyPopper",
        "259df225-0afb-47fa-840f-19aca2f08cdc" : "reporterMic",
        "439eb5c0-dec5-43dd-b678-dc2af324d185" : "gooBall",
        "5f2b203b-7437-4691-9975-99882ab3e00c" : "shockStick",
        "0801e048-8c94-444b-b3dd-de331765ad6b" : "hug",
        "c359f474-1eb6-4b2c-b62e-88fa14cc6a8e" : "defibrillator",
        "d4480b01-fc38-4112-82ce-c598917b2a1d" : "workout2",
        "1f6e51e7-af30-45af-a3e6-9ace370ad8ad" : "thumbnail2",
        "a4da2558-d060-4c0d-bac9-05d7d8ed59c1" : "ancientGestures3",
        "16ea236c-a348-4cd8-93d2-755d236d2ed2" : "caring",
        "ec3acf99-c659-400a-83e4-544deb17eba6" : "ancientGestures2",
        "87482137-a844-4d5e-9692-a4c391f4f998" : "thumbnail1",
        "c48eda8b-cbb0-4798-b94a-b966d5004f5f" : "ancientGestures1",
        "a7e48161-7cc8-41dd-adb6-d9dae3734880" : "applause",
        "f2f236a9-9e4d-4fde-90df-e9031f3a869d" : "workout1",
        "f50ea940-fdda-4f19-9e67-63a6f921226c" : "dance103",
        "233b951f-4f6d-44f7-9b03-8a115b8bcaba" : "confused",
        "c3d6b0b1-cb81-462f-bf26-c61bd3a64908" : "dance102",
        "3fc4e653-529e-495b-a6f9-07a06074a60c" : "dance101",
        "497582d8-c0be-462b-97db-a72e6538aaed" : "gymnastics",
        "c8edb58c-1e9d-40f9-a4b3-8b3cf396b2dc" : "backflip",
        "aea4d548-edd4-4b06-92e7-5e8bd8104e4a" : "yoga"
    }
}
Items['NAME'] = {Items['ID'][item] : item for item in Items['ID']}

#Have this here for future.
NetworkDeals = {
    'ID' : {
        'NetworkHoldTheBombo_9' : 'Hold the Bomb',
        'NetworkInterviewer_2' : 'Interviews',
        'NetworkJackass_4' : 'Jackass',
        'NetworkMultiMonsterInFrameAtOnce_5' : 'Monsters in Frame',
        'NetworkTaunting_3' : 'Taunting',
        'NetworkWalletMoney_1' : 'Rich Streamers'
    }
}
NetworkDeals['NAME'] = {NetworkDeals['ID'][deal] : deal for deal in NetworkDeals['ID']}

#Have this here for future.
NetworkAllowedDifficulties = {
    'NetworkHoldTheBombo_9' : ['Hard'],
    'NetworkInterviewer_2' : ['Easy', 'Medium', 'Hard', 'Very Hard'],
    'NetworkJackass_4' : ['Easy', 'Medium', 'Hard', 'Very Hard'],
    'NetworkMultiMonsterInFrameAtOnce_5' : ['Easy', 'Hard'],
    'NetworkTaunting_3' : ['Easy', 'Medium', 'Hard', 'Very Hard'],
    'NetworkWalletMoney_1' : ['Easy', 'Medium', 'Hard', 'Very Hard']
}

ViewMultipliers = {
    1 : 10,
    2 : 114,
    3 : 302,
    4 : 665,
    5 : 1100,
    6 : 1900,
    7 : 3000,
    8 : 3000,
    9 : 3000,
    10 : 3000
}

themeColors = {
    'fg' : "#fafafa",
    'bg' : "#1c1c1c",
    'disfg' : "#595959",
    'selfg' : "#ffffff",
    'selbg' : "#2f60d8",
    'accent' : "#57c8ff",
    'additional' : "#101010"
}

itemGridSize = 4