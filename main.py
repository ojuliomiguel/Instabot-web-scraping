from instabot import InstaBot 

if __name__ == "__main__":
    instaBot = InstaBot('@username','senha')
    instaBot.login()
    instaBot.curtirFotos('tiringa')
    #instaBot.unfollow()
