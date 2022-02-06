import os

from pathlib import Path
from enum import Enum

class AssetType(Enum):
    BACKGROUND_WHITE = 1
    BACKGROUND = 2
    ENTRY_BACKGROUND = 3
    
    BUTTON_HOME = 4
    BUTTON_USER = 5
    BUTTON_SETTINGS = 6
    BUTTON_GO = 7
    
    INSTAGRAM_CARD = 8
    WHATSAPP_CARD = 9
    FACEBOOK_CARD = 10
    TWITTER_CARD = 11

class AssetManager:
    def __init__(self):
        self.root_path = Path(__file__).absolute().parent.parent
        self.assets_path = Path(os.path.join(self.root_path, "assets"))

    def get_path(self, asset_type: AssetType):
        match asset_type:
            case AssetType.BACKGROUND_WHITE:
                return os.path.join(
                    self.assets_path,
                    "bg_white.png"
                )
                
            case AssetType.BACKGROUND:
                return os.path.join(
                    self.assets_path,
                    "bg.png"
                )
            
            case AssetType.ENTRY_BACKGROUND:
                return os.path.join(
                    self.assets_path,
                    "entry_bg.png"
                )
            
            case AssetType.BUTTON_HOME:
                return os.path.join(
                    self.assets_path,
                    "home_bt.png"
                )
            case AssetType.BUTTON_USER:
                return os.path.join(
                    self.assets_path,
                    "user_bt.png"
                )
            case AssetType.BUTTON_SETTINGS:
                return os.path.join(
                    self.assets_path,
                    "settings_bt.png"
                )
            case AssetType.BUTTON_GO:
                return os.path.join(
                    self.assets_path,
                    "bt_go.png"
                )
            case AssetType.INSTAGRAM_CARD:
                return os.path.join(
                    self.assets_path,
                    "instagram_card.png"
                )
                
            case AssetType.WHATSAPP_CARD:
                return os.path.join(
                    self.assets_path,
                    "whatsapp_card.png"
                )
            
            case AssetType.FACEBOOK_CARD:
                return os.path.join(
                    self.assets_path,
                    "facebook_card.png"
                )
            
            case AssetType.TWITTER_CARD:
                return os.path.join(
                    self.assets_path,
                    "twitter_card.png"
                )
