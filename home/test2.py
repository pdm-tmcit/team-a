import json

def main(myname, myrole, caracter1, text1, time1):
    jsondata ={
        "@context": [
            "https://werewolf.world/village/context/0.3/base.jsonld",
            "https://werewolf.world/village/context/0.3/chat.jsonld"
        ],
        "@id": "https://licos.online/state/0.3/village#3/chatMessage",
        "village": {
            "@context": "https://werewolf.world/village/context/0.3/village.jsonld",
            "@id": "https://licos.online/state/0.3/village",
            "id": 3,
            "name": "Fearwick",
            "totalNumberOfPlayers": 15,
            "language": "ja",
            "chatSettings": {
                "@context": "https://werewolf.world/village/context/0.3/chatSettings.jsonld",
                "@id": "https://licos.online/state/0.3/village#3/chatSettings",
                "maxNumberOfChatMessages": 10,
                "maxLengthOfUnicodeCodePoints": 140
            }
        },
        "token": "3F2504E0-4F89-11D3-9A0C-0305E82C3301",
        "phase": str(time1),
        "day": 1,
        "phaseTimeLimit": 600,
        "phaseStartTime": "2006-10-07T12:06:56.568+09:00",
        "serverTimestamp": "2006-10-07T12:06:56.568+09:00",
        "clientTimestamp": "2006-10-07T12:06:56.568+09:00",
        "directionality": "client to server",
        "intensionalDisclosureRange": "public",
        "extensionalDisclosureRange": [],
        "myCharacter": {
            "@context": "https://werewolf.world/village/context/0.3/character.jsonld",
            "@id": "https://licos.online/state/0.3/village#3/myCharacter",
            "id": 1,
            "name": {
                "en": "XXXX",
                "ja": str(myname)
            },
            "image": "https://werewolf.world/image/0.3/character_icons/50x50/a_50x50.png",
            "role": {
                "@context": "https://werewolf.world/village/context/0.3/role.jsonld",
                "@id": "https://licos.online/state/0.3/village#3/character#1/role",
                "name": {
                    "en": "Werewolf",
                    "ja": "人狼"
                },
                "image": "https://werewolf.world/image/0.3/role_icons/50x50withTI/werewolf_50x50.png"
            }
        },
        "character": {
            "@context": "https://werewolf.world/village/context/0.3/character.jsonld",
            "@id": "https://licos.online/state/0.3/village#3/character",
            "id": 1,
            "name": {
                "en": "XXX",
                "ja": str(caracter1)
            },
            "image": "https://werewolf.world/image/0.3/character_icons/50x50/a_50x50.png"
        },
        "isMine": True,
        "text": {
            "@value": str(text1),
            "@language": "ja"
        },
        "maxLengthOfUnicodeCodePoints": 140,
        "isOver": False
    }

    print(json.dumps(jsondata,ensure_ascii=False, indent=4))
    print(type(json.dumps(jsondata,ensure_ascii=False, indent=4)))

    file1 = open('test1.jsonld','w')
    json.dump(jsondata,file1,ensure_ascii=False,indent=4)
    file1.close()

if __name__ == '__main__':
    main()